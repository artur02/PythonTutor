# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:13:25 2013

@author: Artur_Herczeg
"""

import pandas as pd
import httplib


def hostCount(frame):
    grpHost = frame.groupby("Host")
    return grpHost.Host.count()


def hostCountDesc(hostCount):
    return hostCount.order(ascending=False)


def setStatusDType(frame):
    frame.Status = frame.Status.astype(int)


def setResponseSizeDType(frame):
    frame.ResponseSize.replace(['-'], 0, inplace=True)
    frame.ResponseSize = frame.ResponseSize.astype(int)


def hostsWithResponseSize0(frame):
    return frame[frame.ResponseSize == 0].Host.drop_duplicates()


def statusHistogram(frame):
    frame.Status.hist()


def statusMapping(frame):
    return frame.Status.map(lambda x: httplib.responses[x])


if __name__ == "__main__":
    frame = pd.read_hdf("processed_full.hdf", "stat")

    hostCount = hostCount(frame)
    print hostCount
