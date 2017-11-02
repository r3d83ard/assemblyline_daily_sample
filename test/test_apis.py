import unittest
import hashlib

from utilities import logger_util
from api import malshr_api

class TestMalshrAPI(unittest.TestCase):
    malshare = ''
    vti
    md5 = ''
    hash_md5 = ''

    def setUp(self):
        self.malshare = malshr_api.Malshare_API()
        self.md5 = 'b63bff90e6a55c4a404a8a48d076de45'
        self.hash_md5 = hashlib.md5()

    def tearDown(self):
        del self.malshare
        self.malshare = None

    def test_m_api_daily_md5_string(self):
        self.setUp()
        self.assertIsNotNone(self.malshare.m_api_daily_md5_string())
        self.tearDown()

    def test_m_api_daily_md5_list(self):
        self.setUp()
        self.assertIsNotNone(self.malshare.m_api_daily_md5_list())
        self.tearDown()

    def test_m_api_daily_sources_string(self):
        self.setUp()
        self.assertIsNotNone(self.malshare.m_api_daily_sources_string())
        self.tearDown()

    def test_m_api_daily_sources_list(self):
        self.setUp()
        self.assertIsNotNone(self.malshare.m_api_daily_sources_list())
        self.tearDown()

    def test_m_api_raw_sample(self):
        self.setUp()
        response = self.malshare.m_api_raw_sample(self.md5)
        self.assertTrue(response)
        self.hash_md5.update(response.read())
        self.assertEqual(self.hash_md5.hexdigest(),self.md5)
        self.tearDown()

    def test_m_api_file_details(self):
        self.setUp()
        self.assertIsNotNone(self.malshare.m_api_file_details(self.md5))
        self.tearDown()

    def test_m_api_daily_md5_file_type(self):
        self.setUp()
        self.assertIsNotNone(self.malshare.m_api_daily_md5_file_type('PE32'))
        self.tearDown()

class TestVTIAPI(unittest.TestCase):
    def setUp(self):
        self.vti = VTI_API()
        self.md5 = '231a8de70336d7dbfff05de94d0c33a2'

    def tearDown(self):
        del self.vti
        self.vti = None

    def test_m_api_md5_download(self):
        self.setUp()
        self.assertIsNotNone(self.vti.m_api_md5_download(md5))
        self.tearDown()

    def test_m_api_scan_file(self):

#assert vti.m_api_scan_file("./"+md5)
#print "PASS: m_api_scan_file"
#os.remove("./"+md5)
#
## Large test file : WARNING: Malicious File
#md5 = '4f5902bf3aef48a4b20b65fff434c98e'
#
#vti.m_api_md5_download(md5)
#
#assert vti.m_api_scan_large_file("./"+md5)
#print "PASS: m_api_scan_large_file"
#os.remove("./"+md5)

    def test_m_api_md5_report(md5)
        #assert vti.m_api_md5_report(md5)
        #print "PASS: m_api_md5_report"

    def test_m_api_md5_behaviour(md5)
        #assert vti.m_api_md5_behaviour(md5)
        #print "PASS: m_api_md5_behaviour"

    def test_m_api_md5_pcap(self):
        ##assert vti.m_api_md5_pcap(md5, "./"+md5)
        ##print "PASS: m_api_md5_pcap"
        ##os.remove("./"+md5)

    def test_m_api_search(self):
        #assert vti.m_api_search('type:peexe size:90kb+ positives:5+ behaviour:"taskkill"')
        #print "PASS: m_api_search"

    def test_m_api_fp_report(self):
        ##assert vti.m_api_fp_report()
        ##print "PASS: m_api_fp_report"

class TestOTXAPI(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
