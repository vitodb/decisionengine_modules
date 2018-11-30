#!/usr/bin/env python
"""
Publishes price / performance data

"""
import argparse
import os
import copy
import pprint
import pandas as pd

from decisionengine_modules.graphite.publishers.generic_publisher import GenericPublisher as publisher
import decisionengine.framework.configmanager.ConfigManager as configmanager
import decisionengine.framework.dataspace.datablock as datablock
import decisionengine.framework.dataspace.dataspace as dataspace
import decisionengine_modules.graphite_client as graphite
from decisionengine.framework.modules import de_logger

DEFAULT_GRAPHITE_CONTEXT="hepcloud.de.glideinwms"
CONSUMES=['job_clusters']

class JobClusteringPublisher(publisher):
    def __init__(self, config):
        super(JobClusteringPublisher, self).__init__(config)
        self.logger = de_logger.get_logger()

    def consumes(self):
        return CONSUMES

    def graphite_context(self, datablock):
        d = {}
        for i, row in datablock.iterrows():
            key = ('%s.job_cluster'%(graphite.sanitize_key(row['Job_Bucket_Criteria_Expr'])))
            d[key] = row['Totals']
        return self.graphite_context_header, d


def module_config_template():
    """
    print a template for this module configuration data
    """

    d = {"JobClusteringPublisher": {
         "module": "modules.glideinwms.publishers.JobClustering_publisher",
         "name": "JobClusteringPublisher",
         },}
    print "Entry in channel cofiguration"
    pprint.pprint(d)
    print "where"
    print "\t name - name of the class to be instantiated by task manager"
    print "\t publish_to_graphite - publish to graphite if True"
    print "\t graphite_host - graphite host name"


def module_config_info():
    """
    print this module configuration information
    """

    print "consumes", CONSUMES
    module_config_template()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--configtemplate',
        action='store_true',
        help='prints the expected module configuration')

    parser.add_argument(
        '--configinfo',
        action='store_true',
        help='prints config template along with produces and consumes info')
    args = parser.parse_args()

    if args.configtemplate:
        module_config_template()
    elif args.configinfo:
        module_config_info()
    else:
        pass


if __name__ == '__main__':
    main()