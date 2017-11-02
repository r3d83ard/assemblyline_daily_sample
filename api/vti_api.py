import os
import requests

class VTI_API:
    a_vti_api_key = ''

    a_api_scan_file = 'https://www.virustotal.com/vtapi/v2/file/scan'
    a_api_scan_large_file = 'https://www.virustotal.com/vtapi/v2/file/scan/upload_url'
    a_api_md5_report = 'https://www.virustotal.com/vtapi/v2/file/report'
    a_api_md5_behaviour = 'https://www.virustotal.com/vtapi/v2/file/behaviour'
    a_api_md5_pcap = 'https://www.virustotal.com/vtapi/v2/file/network-traffic'
    a_api_search = 'https://www.virustotal.com/vtapi/v2/file/search'
    a_api_clusters = 'https://www.virustotal.com/vtapi/v2/file/clusters'
    a_api_md5_download = 'https://www.virustotal.com/vtapi/v2/file/download'
    a_api_fp_report = 'https://www.virustotal.com/vtapi/v2/file/false-positives'

    def __init__(self):
        try:
            logger_util.setup_logger('master_logger', 'master.log', logging.INFO)
            logger_util.setup_logger('api_logger', 'api.log', logging.INFO)
            self.master_logger = logging.getLogger('master_logger')
            self.api_logger = logging.getLogger('api_logger')

            self.api_logger.debug('Getting environment variable $%s', 'MALSHR_API_KEY')
            self.a_vti_api_key = os.environ['VTI_API_KEY']
            self.api_logger.debug('Successfully found api key')
        except:
            self.master_logger.error('Environment variable $%s does not exist', 'MALSHR_API_KEY')
            self.api_logger.error('Environment variable $%s does not exist', 'MALSHR_API_KEY')
            raise

    def m_api_scan_file(self, file_location):
        """
        Description:
        ------------
        POST /vtapi/v2/file/scan. Upload a file for scanning with VirusTotal. File must be smaller than 32MB

        Parameters:
        -----------
        string : file_handle
            path to file to be uploaded

        Returns:
        --------
        json object
            response contains scan_id to access report and other info
        """
        try:
            params = {'apikey':self.a_malshare_api_key}
            files = {'file': (file_location, open(file_location, 'rb'))}
            response = requests.post(self.a_api_scan_file, files=files, params=params)
            return response.json()
        except requests.exceptions.RequestException as e:
            print "ERROR: VTI API call failed: m_api_scan_file. Got an error code:", e

    def m_api_scan_large_file(self, file_location):
        """
        Description:
        ------------
        GET /vtapi/v2/file/scan/upload_url. Get a special URL to upload files bigger than 32MB in size
        and upload file.

        Parameters:
        -----------
        string : file_location
            path to file to be uploaded

        Returns:
        --------
        json object
            response contains scan_id to access report and other info
        """
        try:
            params = {'apikey':self.a_malshare_api_key}

            # obtaining the upload URL
            response = requests.get(self.a_api_scan_large_file, params=params)
            json_response = response.json()
            upload_url = json_response['upload_url']

            # submitting the file to the upload URL
            files = {'file': (file_location.decode('utf-8'), open(file_location, 'rb'))}
            response = requests.post(upload_url, files=files)
            return response.json()
        except requests.exceptions.RequestException as e:
            print "ERROR: VTI API call failed: m_api_scan_file. Got an error code:", e

    def m_api_md5_report(self, md5):
        """
        Description:
        ------------
        GET /vtapi/v2/file/report	Get the scan results for a file

        Parameters:
        -----------
        string : md5
            hash value of file

        Returns:
        --------
        json object
            report detailing file
        """
        try:
            params = {'apikey':self.a_malshare_api_key,'resource':md5}
            headers = {
              "Accept-Encoding": "gzip, deflate",
              "User-Agent" : "gzip,  graywolf"
              }
            response = requests.get(self.a_api_md5_report, params=params, headers=headers)
            return response.json()
        except requests.exceptions.RequestException as e:
            print "ERROR: VTI API call failed: m_api_scan_file. Got an error code:", e

    def m_api_md5_behaviour(self, md5):
        """
        Description:
        ------------
        GET /vtapi/v2/file/behaviour. Get a report about the behaviour of the file when executed in a sandboxed environment.

        Parameters:
        -----------
        string : md5
            hash value of file

        Returns:
        --------
        json object
            report detailing file
        """
        try:
            params = {'apikey':self.a_malshare_api_key,'hash': md5}
            headers = {
                "Accept-Encoding": "gzip, deflate",
                "User-Agent" : "gzip,  graywolf"
            }
            response = requests.get(self.a_api_md5_behaviour, params=params, headers=headers)
            return response.json()
        except requests.exceptions.RequestException as e:
            print "ERROR: VTI API call failed: m_api_scan_file. Got an error code:", e

    #TODO: Broken, I/O issue
    def m_api_md5_pcap(self, md5, file_location):
        """
        Description:
        ------------
        GET /vtapi/v2/file/network-traffic	Get a dump of the network traffic generated by the file when executed.

        Parameters:
        -----------
        string : md5
            hash value of file
        string : file_location
            where to save the file

        Returns:
        --------
        none
        """
        try:
            params = {'apikey':self.a_malshare_api_key,'hash':md5}

            headers = {
                "Accept-Encoding": "gzip, deflate",
                "User-Agent" : "gzip,  graywolf"
            }

            first_bytes = None
            with open(file_location, 'wb') as handle:
                response = requests.get(self.a_api_md5_pcap, params=params, headers=headers, stream=True)

                if not response.ok:
                    print "something is wrong %s" % (response)
                    return

                for block in response.iter_content(4096):
                    handle.write(block)

                if not first_bytes:
                    first_bytes = str(block)[:4]

            valid_pcap_magics = [ '\xd4\xc3\xb2\xa1', '\xa1\xb2\xc3\xd4', '\x4d\x3c\xb2\xa1', '\xa1\xb2\x3c\x4d' ]

            if first_bytes in valid_pcap_magics:
                print "PCAP downloaded"
            elif first_bytes.startswith('{"'):
                print "NOT found"
            else:
                print "unknown file"
        except requests.exceptions.RequestException as e:
            print "ERROR: VTI API call failed: m_api_scan_file. Got an error code:", e

    def m_api_search(self, query_str):
        """
        Description:
        ------------
        POST /vtapi/v2/file/search	Search for samples that match certain binary/metadata/detection criteria.

        Parameters:
        -----------
        string : query_str
            hash value of file
            example: 'type:peexe size:90kb+ positives:5+ behaviour:"taskkill"'

        Returns:
        --------
        json object
            report detailing file
        """
        try:
            headers = {
                "Accept-Encoding": "gzip, deflate",
                "User-Agent" : "gzip,  graywolf"
            }
            params = {'apikey': self.a_malshare_api_key, 'query': query_str}
            response = requests.post(self.a_api_search, data=params, headers=headers)
            return response.json()
        except requests.exceptions.RequestException as e:
            print "ERROR: VTI API call failed: m_api_scan_file. Got an error code:", e

    def m_api_clusters(self, date):
        """
        Description:
        ------------
        GET /vtapi/v2/file/clusters	List file similarity clusters for a given time frame.

        Parameters:
        -----------
        string : date
            time frame for clusters

        Returns:
        --------
        json object
            report detailing cluster information
        """
        try:
            params = {'apikey': self.a_malshare_api_key, 'date': date}
            response = requests.get(self.a_api_clusters, params=params)
            return response.json()
        except requests.exceptions.RequestException as e:
            print "ERROR: VTI API call failed: m_api_scan_file. Got an error code:", e

    def m_api_md5_download(self, md5, file_location="./"):
        """
        Description:
        ------------
        GET /vtapi/v2/file/download	Download a file by its hash.

        Parameters:
        -----------
        string : md5
            hash value of file

        Returns:
        --------
        none
        """
        try:
            headers = {
                "Accept-Encoding": "gzip, deflate",
                "User-Agent" : "gzip,  graywolf"
            }
            params = {'apikey': self.a_malshare_api_key, 'hash': md5}
            response = requests.get(self.a_api_md5_download, params=params)
            new_file_byte_array = bytearray(response.content)
            new_file = open(file_location+md5, "w")
            new_file.write(new_file_byte_array)
            return True
        except requests.exceptions.RequestException as e:
            print "ERROR: VTI API call failed: m_api_scan_file. Got an error code:", e
            return False

    #TODO: Need to be granted access
    def m_api_fp_report(self):
        """
        Description:
        ------------
        GET /vtapi/v2/file/false-positives 	Consume file false positives from your notifications pipe

        Parameters:
        -----------
        none

        Returns:
        --------
        none
        """
        try:
            headers = {'User-Agent': 'gzip', 'Accept-Encoding': 'gzip'}
            params = {'apikey': self.a_malshare_api_key, 'limit': 500}
            response = requests.get(self.a_api_fp_report, params=params, headers=headers)
            return response.json()
        except requests.exceptions.RequestException as e:
            print "ERROR: VTI API call failed: m_api_scan_file. Got an error code:", e

def main():
    vti = VTI_API()

    # Small test file : WARNING: Malicious File
    md5 = '231a8de70336d7dbfff05de94d0c33a2'

    assert vti.m_api_md5_download(md5)
    print "PASS: m_api_md5_download"

    assert vti.m_api_scan_file("./"+md5)
    print "PASS: m_api_scan_file"
    os.remove("./"+md5)

    # Large test file : WARNING: Malicious File
    md5 = '4f5902bf3aef48a4b20b65fff434c98e'

    vti.m_api_md5_download(md5)

    assert vti.m_api_scan_large_file("./"+md5)
    print "PASS: m_api_scan_large_file"
    os.remove("./"+md5)

    assert vti.m_api_md5_report(md5)
    print "PASS: m_api_md5_report"

    assert vti.m_api_md5_behaviour(md5)
    print "PASS: m_api_md5_behaviour"

    #assert vti.m_api_md5_pcap(md5, "./"+md5)
    #print "PASS: m_api_md5_pcap"
    #os.remove("./"+md5)

    assert vti.m_api_search('type:peexe size:90kb+ positives:5+ behaviour:"taskkill"')
    print "PASS: m_api_search"

    #assert vti.m_api_fp_report()
    #print "PASS: m_api_fp_report"

if __name__ == "__main__":
    main()
