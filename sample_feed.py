#!/usr/bin/env python

from api import malshr_api
from utilities import logger_util

def main():
    logger_util.setup_logger('master_logger', 'master.log', logging.INFO)
    logger_util.setup_logger('sample_feed_logger', 'sample_feed_logger.log', logging.INFO)

    self.master_logger = logging.getLogger('master_logger')
    self.sample_feed_logger = logging.getLogger('sample_feed_logger')

    #TODO: Pull Malshare samples and push as many as possible
    #TODO: Record Metrics

    #TODO: Pull VTI samples and push as many as possible
    #TODO: Record Metrics

    #TODO: Pull OTX samples and push as many as possible
    #TODO: Record Metrics
