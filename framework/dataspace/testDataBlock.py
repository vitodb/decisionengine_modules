#!/usr/bin/python

from dataspace import DataSpace
from datablock import DataBlock
import os

filename = '/tmp/test-wdd.db'

if os.path.exists(filename):
    os.unlink(filename)

dataspace = DataSpace(filename)

dataspace.create()

taskmanager_id = 1
generation_id = 1

datablock = DataBlock(taskmanager_id, generation_id, dataspace)

key = 'aKey'
value = { "m1": "v1" }

#datablock.put(key, value)
datablock[key] = value

print datablock.get(key)

dataspace.close()

