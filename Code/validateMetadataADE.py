#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 19:50:36 2018

@author: kavisha
"""

import sys
from lxml import etree

citygml_src = "citygmldatasets/Part-1-Terrain-WaterBody-Vegetation-V2_metadata.gml"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, citygml_src)
print ("\n CityGML input file: ", abs_file_path)

metadata_schema = "/XSD/3DMD_ADE.xsd"
schema_dir = os.path.abspath(os.path.join(__file__ ,"../.."))
abs_file_path2 = (schema_dir + metadata_schema)
print ("\n CityGML Metadata ADE schema: ", abs_file_path2)

try:
    parser = etree.XMLParser(ns_clean=True)
    xsd = etree.parse(abs_file_path2)
    xmlschema = etree.XMLSchema(xsd)
    xmlschema.assertValid(tree)
    print ("document validates!")

except etree.XMLSyntaxError as e:
    print ("PARSING ERROR", e)
    
except AssertionError as e:
    print ("INVALID DOCUMENT", e)