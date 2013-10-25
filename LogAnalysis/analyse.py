# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:40:13 2013

@author: Artur_Herczeg
"""

import dateutil.parser

import mmap
import pandas as pd
import apachelog as alog


def processFile(path):
    logparser = alog.parser(alog.formats['common'])

    hosts = list()
    dates = list()
    statuses = list()
    respsizes = list()

    with open(path, "r+b") as log:
        map = None
        try:
            map = mmap.mmap(log.fileno(), 0, access=mmap.ACCESS_READ)
            for line in iter(map.readline, ""):
                try:
                    data = logparser.parse(line)
                    hosts.append(data['%h'])
                    cdate = dateutil.parser.parse(
                        data['%t'].strip('[]'),
                        fuzzy=True)
                    dates.append(cdate)
                    statuses.append(data['%>s'])
                    respsizes.append(data['%b'])
                except:
                    print "Unable to parse %s" % line

        finally:
            if map:
                map.close()

    index = pd.to_datetime(dates)

    frame = pd.DataFrame({
        'Host': pd.Series(hosts, index=index, dtype=str),
        'Status': pd.Series(statuses, index=index),
        'ResponseSize': pd.Series(respsizes, index=index)},
        index=index)

    frame.to_hdf('processed.hdf', 'stat')

    return frame

if __name__ == '__main__':

#    frame = processFile("access_log_Jul95")
    frame = processFile("access_log_short")
