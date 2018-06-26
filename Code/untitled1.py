#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 10:55:10 2018

@author: kavisha
"""

import json
import jsonschema


filename =  r'/Users/kavisha/Desktop/PhDwork/2018/mei/cityjson/extensions/noiseExample.json'
schema = r'/Users/kavisha/Desktop/PhDwork/2018/mei/cityjson/extensions/noiseExtension.json'
    
fin = open(filename)
data = fin.read()
#print data
j = json.loads(data.decode('utf-8-sig'))
print j

fins = open(schema)
schema = fins.read()
#print schema
js = json.loads(schema.decode('utf-8-sig'))
print js

print os.path.abspath(os.path.dirname(__file__))
resolver = jsonschema.RefResolver('file://%s/' % os.path.abspath(os.path.dirname(__file__)), None)
try:
    jsonschema.validate(j,js)
except jsonschema.ValidationError as e:
    print e.message
except jsonschema.SchemaError as e:
    print e