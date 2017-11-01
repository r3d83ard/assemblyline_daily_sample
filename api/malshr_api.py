import os
import json
import urllib
import urllib2
import requests
import shutil
import logging

from utilities import logger_util

class Malshare_API:
    a_malshare_api_key = ''

    a_api_daily_md5_html = ''
    a_api_daily_md5_text = ''
    a_api_daily_sources_html = ''
    a_api_daily_sources_text = ''
    a_api_download_sample = ''
    a_api_file_details = ''
    a_api_daily_md5_file_type = ''
    a_api_query_md5_file_sample = ''

    def __init__(self):
        try:
            logger_util.setup_logger('master_logger', 'master.log', logging.INFO)
            logger_util.setup_logger('api_logger', 'api.log', logging.INFO)
            self.master_logger = logging.getLogger('master_logger')
            self.api_logger = logging.getLogger('api_logger')

            self.api_logger.debug('Getting environment variable $%s', 'MALSHR_API_KEY')
            self.a_malshare_api_key = os.environ['MALSHR_API_KEY']
            self.api_logger.debug('Successfully found api key')
        except:
            self.master_logger.error('Environment variable $%s does not exist', 'MALSHR_API_KEY')
            self.api_logger.error('Environment variable $%s does not exist', 'MALSHR_API_KEY')
            raise

        else:
            self.api_logger.debug('Set all api calls')
            self.a_api_daily_md5_html = 'https://malshare.com/api.php?api_key='+self.a_malshare_api_key+'&action=getlist'							# List MD5 hashes from the past 24 hours :						format: List seperated by HTML line break
            self.a_api_daily_md5_text = 'https://malshare.com/api.php?api_key='+self.a_malshare_api_key+'&action=getlistraw'						# List MD5 hashes from the past 24 hours :						format: Raw Text List
            self.a_api_daily_sources_html = 'https://malshare.com/api.php?api_key='+self.a_malshare_api_key+'&action=getsources'					# List of sample sources from the past 24 hours :				format: List seperated by HTML line break
            self.a_api_daily_sources_text = 'https://malshare.com/api.php?api_key='+self.a_malshare_api_key+'&action=getsourcesraw'				# List of sample sources from the past 24 hours :				format: Raw Text List
            self.a_api_download_sample = 'https://malshare.com/api.php?api_key='+self.a_malshare_api_key+'&action=getfile&hash='#[HASH]			# Download File :												format: Raw data
            self.a_api_file_details = 'https://malshare.com/api.php?api_key='+self.a_malshare_api_key+'&action=details&hash='#[HASH]			    # Get stored file details :										format: JSON
            self.a_api_daily_md5_file_type = 'https://malshare.com/api.php?api_key='+self.a_malshare_api_key+'&action=type&type='#[FILE TYPE]		# List MD5 hashes of a specific type from the past 24 hours :	format: JSON
            self.api_logger.debug('Successfully set all api calls')

            # TODO: Implement
            # self.a_api_query_md5_file_sample = '/api.php?api_key='+a_malshare_api_key+'&action=search&query='#[SEARCH QUERY]		# Search sample hashes, sources and file names : 				format: Raw data

    def m_api_daily_md5_string(self):
        """
        Description:
        ------------
        performs an api query for the daily md5 list

        Parameters:
        -----------
        none

        Returns:
        --------
        string : daily_md5_string
            daily md5 string with html <br>
        """
        request = urllib2.Request(self.a_api_daily_md5_html)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            self.master_logger.error('HTTP-specific ERROR: %s', e.code)
            self.api_logger.error('HTTP-specific ERROR: %s', e.code)
            raise
        except urllib2.URLError as e:
            self.master_logger.error('Other URL ERROR: %s', e)
            self.api_logger.error('Ohter URL ERROR: %s', e)
            raise
        else:
            daily_md5_string = response.read()
            if daily_md5_string == "ERROR! => Account not activated":
                self.master_logger.error('API call failed: %s', body)
                self.api_logger.error('API call failed: %s', body)
                return False
            else:
                self.master_logger.info('Successful md5 query')
                self.api_logger.info('Successful md5 query')
                return daily_md5_string

    def m_api_daily_md5_list(self):
        """
        Description:
        ------------
        performs an api query for the daily md5 list

        Parameters:
        -----------
        none

        Returns:
        --------
        list : daily_md5_list
            daily md5 as list
        """
        request = urllib2.Request(self.a_api_daily_md5_text)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            self.master_logger.error('HTTP-specific ERROR: %s', e.code)
            self.api_logger.error('HTTP-specific ERROR: %s', e.code)
            raise
        except urllib2.URLError as e:
            self.master_logger.error('Other URL ERROR: %s', e)
            self.api_logger.error('Ohter URL ERROR: %s', e)
            raise
        else:
            daily_md5_string = response.read()
            if daily_md5_string == 'ERROR! => Account not activated':
                self.master_logger.error('API ERROR: %s', body)
                self.api_logger.error('API ERROR: %s', body)
                return False
            else:
                daily_md5_list = daily_md5_string.split()
                self.master_logger.info('Successful md5 query')
                self.api_logger.info('Successful md5 query')
                return daily_md5_list

    def m_api_daily_sources_string(self):
        """
        Description:
        ------------
        performs an api query for the daily file source list

        Parameters:
        -----------
        none

        Returns:
        --------
        string : daily_sources_string
            daily file sources as string with html <br>
        """
        request = urllib2.Request(self.a_api_daily_sources_html)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            self.master_logger.error('HTTP-specific ERROR: %s', e.code)
            self.api_logger.error('HTTP-specific ERROR: %s', e.code)
            raise
        except urllib2.URLError as e:
            self.master_logger.error('Other URL ERROR: %s', e)
            self.api_logger.error('Ohter URL ERROR: %s', e)
            raise
        else:
            daily_sources_string = response.read()
            if daily_sources_string == 'ERROR! => Account not activated':
                self.master_logger.error('API ERROR: %s', body)
                self.api_logger.error('API ERROR: %s', body)
                return False
            else:
                self.master_logger.info('Successful source query')
                self.api_logger.info('Successful source query')
                return daily_sources_string

    def m_api_daily_sources_list(self):
        """
        Description:
        ------------
        performs an api query for the daily file source list

        Parameters:
        -----------
        none

        Returns:
        --------
        list : daily_sources_list
            daily file sources as a list
        """
        request = urllib2.Request(self.a_api_daily_sources_html)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            self.master_logger.error('HTTP-specific ERROR: %s', e.code)
            self.api_logger.error('HTTP-specific ERROR: %s', e.code)
            raise
        except urllib2.URLError as e:
            self.master_logger.error('Other URL ERROR: %s', e)
            self.api_logger.error('Ohter URL ERROR: %s', e)
            raise
        else:
            daily_sources_string = response.read()
            if daily_sources_string == 'ERROR! => Account not activated':
                self.master_logger.error('API ERROR: %s', body)
                self.api_logger.error('API ERROR: %s', body)
                return False
            else:
                daily_sources_list = daily_sources_string.split()
                self.master_logger.info('Successful source query')
                self.api_logger.info('Successful source query')
                return daily_sources_list

    def m_api_raw_sample(self, md5):
        """
        Description:
        ------------
        performs an api query to download a sample

        Parameters:
        -----------
        string : md5
            hash value of file
        string : file_location
            path for file storage as string

        Returns:
        --------
        string : file_location
            path for file storage as string
        """
        request = urllib2.Request(self.a_api_download_sample+md5)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            self.master_logger.error('HTTP-specific ERROR: %s', e.code)
            self.api_logger.error('HTTP-specific ERROR: %s', e.code)
            raise
        except urllib2.URLError as e:
            self.master_logger.error('Other URL ERROR: %s', e)
            self.api_logger.error('Ohter URL ERROR: %s', e)
            raise
        else:
            self.master_logger.info('Successful raw sample download')
            self.api_logger.info('Successful raw sample download')
            return response

    def m_api_download_sample(self, md5, file_location='.'):
        """
        Description:
        ------------
        performs an api query to download a sample

        Parameters:
        -----------
        string : md5
            hash value of file
        string : file_location
            path for file storage as string

        Returns:
        --------
        string : file_location
            path for file storage as string
        """
        file_location = file_location+'/'+md5
        request = urllib2.Request(self.a_api_download_sample+md5)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            self.master_logger.error('HTTP-specific ERROR: %s', e.code)
            self.api_logger.error('HTTP-specific ERROR: %s', e.code)
            raise
        except urllib2.URLError as e:
            self.master_logger.error('Other URL ERROR: %s', e)
            self.api_logger.error('Ohter URL ERROR: %s', e)
            raise
        else:
            try:
                CHUNK=16*1024
                with open(file_location, 'wb') as f:
                    shutil.copyfileobj(response, f, CHUNK)
                self.master_logger.info('Successful file sample download')
                self.api_logger.info('Successful file sample download')
                return file_location
            except:
                self.master_logger.error('shutil library failed')
                self.api_logger.error('shutil library failed')
                raise

    def m_api_file_details(self, md5):
        """
        Description:
        ------------
        performs an api query for file details

        Parameters:
        -----------
        string : md5
            hash value of file

        Returns:
        --------
        json object : json_data
            file md5 list as a json object
        """
        request = urllib2.Request(self.a_api_file_details+md5)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            self.master_logger.error('HTTP-specific ERROR: %s', e.code)
            self.api_logger.error('HTTP-specific ERROR: %s', e.code)
            raise
        except urllib2.URLError as e:
            self.master_logger.error('Other URL ERROR: %s', e)
            self.api_logger.error('Ohter URL ERROR: %s', e)
            raise
        else:
            body = response.read()
            if body == 'ERROR! => Account not activated':
                self.master_logger.error('API ERROR: %s', body)
                self.api_logger.error('API ERROR: %s', body)
                return False
            else:
                try:
                    json_data= json.loads(body)
                    self.master_logger.info('Successful file details query')
                    self.api_logger.info('Successful file details query')
                    return json_data
                except ValueError:
                    self.master_logger.error('JSON Decode failed')
                    self.api_logger.error('JSON Decode failed')
                    raise

    def m_api_daily_md5_file_type(self, file_type):
        """
        Description:
        ------------
        performs an api query for file details

        Parameters:
        -----------
        string : file_type
            PE32
            HTML
            Zip

        Returns:
        --------
        json object : json_data
            file md5 list as a json object
        """
        request = urllib2.Request(self.a_api_daily_md5_file_type+file_type)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError as e:
            self.master_logger.error('HTTP-specific ERROR: %s', e.code)
            self.api_logger.error('HTTP-specific ERROR: %s', e.code)
            raise
        except urllib2.URLError as e:
            self.master_logger.error('Other URL ERROR: %s', e)
            self.api_logger.error('Ohter URL ERROR: %s', e)
            raise
        else:
            body = response.read()
            if body == 'ERROR! => Account not activated':
                self.master_logger.error('API ERROR: %s', body)
                self.api_logger.error('API ERROR: %s', body)
                return False
            else:
                try:
                    json_data= json.loads(body)
                    self.master_logger.info('Successful file type query')
                    self.api_logger.info('Successful file type query')
                    return json_data
                except ValueError:
                    self.master_logger.error('JSON Decode failed')
                    self.api_logger.error('JSON Decode failed')
