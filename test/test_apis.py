import unittest
import hashlib

from utilities import logger_util
from api import malshr_api

class TestMalshrAPI(unittest.TestCase):
    malshare = ''
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
        pass

    def tearDown(self):
        pass

class TestOTXAPI(unittest.TestCase):
    def setUp(self):
        pass)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
