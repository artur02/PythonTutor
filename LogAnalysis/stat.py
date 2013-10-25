# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:13:25 2013

@author: Artur_Herczeg
"""

import pandas as pd
import httplib

frame = pd.read_hdf("processed_full.hdf", "stat")


def hostCount():
    grpHost = frame.groupby("Host")
    return grpHost.Host.count()


def hostCountDesc(hostCount):
    return hostCount.order(ascending=False)


def setStatusDType():
    frame.Status = frame.Status.astype(int)


def setResponseSizeDType():
    frame.ResponseSize.replace(['-'], 0, inplace=True)
    frame.ResponseSize = frame.ResponseSize.astype(int)


def hostsWithResponseSize0():
    return frame[frame.ResponseSize == 0].Host.drop_duplicates()


def statusHistogram():
    frame.Status.hist()


def statusMapping():
    return frame.Status.map(lambda x: httplib.responses[x])


if __name__ == "__main__":
    hostCount = hostCount()
    print hostCount
