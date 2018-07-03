#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:54:40 2018

@author: kavisha
"""
# Python3+ required

import os
from lxml import etree
import time
import uuid
import argparse
import getcityobjects

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

def argRead(ar, default=None):
    
    """Corrects the argument input in case it is not in the format True/False."""
    if ar == "0" or ar == "False":
        ar = False
    elif ar == "1" or ar == "True":
        ar = True
    elif ar is None:
        if default:
            ar = default
        else:
            ar = False
    else:
        raise ValueError("Argument value not recognised.")
    return ar


# function for generating metadata for a CityGML model
def generatemetadata(inputfile, outputfile):
    tree = etree.parse(inputfile)
    root = tree.getroot()
    for key in root.nsmap.keys():
        if root.nsmap[key].find('http://www.opengis.net/citygml') != -1:
            if (root.nsmap[key][-3:] == '1.0'):
                citygmlversion = '1.0'
                break
            if (root.nsmap[key][-3:] == '2.0'):
                citygmlversion = '2.0'
                break    
    if citygmlversion == "1.0":
        print ("CityGML version not supported!")
    elif citygmlversion == "2.0":
        ns="http://www.opengis.net/citygml/2.0"
        ns_gml  = "http://www.opengis.net/gml"
        ns_xAL="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"
        ns_xsi="http://www.w3.org/2001/XMLSchema-instance"
        ns_xlink="http://www.w3.org/1999/xlink"
        ns_dem="http://www.opengis.net/citygml/relief/2.0"
        ns_bldg="http://www.opengis.net/citygml/building/2.0"
        ns_app="http://www.opengis.net/citygml/appearance/2.0"
        ns_wtr="http://www.opengis.net/citygml/waterbody/2.0"
        ns_gen="http://www.opengis.net/citygml/generics/2.0"
        ns_luse="http://www.opengis.net/citygml/landuse/2.0"
        ns_tran="http://www.opengis.net/citygml/transportation/2.0"
        ns_frn="http://www.opengis.net/citygml/cityfurniture/2.0"
        ns_veg="http://www.opengis.net/citygml/vegetation/2.0"
        ns_tun="http://www.opengis.net/citygml/tunnel/2.0"
        ns_tex="http://www.opengis.net/citygml/texturedsurface/2.0"
        ns_brid="http://www.opengis.net/citygml/bridge/2.0"
        ns_core="http://www.opengis.net/citygml/base/2.0"
        ns_grp="http://www.opengis.net/citygml/cityobjectgroup/2.0"
        ns_md = "http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE"
        schemalocs="http://www.opengis.net/citygml/2.0 http://schemas.opengis.net/citygml/2.0/cityGMLBase.xsd \
        http://www.opengis.net/citygml/building/2.0 http://schemas.opengis.net/citygml/building/2.0/building.xsd \
        http://www.opengis.net/citygml/appearance/2.0 http://schemas.opengis.net/citygml/appearance/2.0/appearance.xsd \
        http://www.opengis.net/citygml/bridge/2.0 http://schemas.opengis.net/citygml/bridge/2.0/bridge.xsd \
        http://www.opengis.net/citygml/cityfurniture/2.0 http://schemas.opengis.net/citygml/cityfurniture/2.0/cityFurniture.xsd \
        http://www.opengis.net/citygml/waterbody/2.0 http://schemas.opengis.net/citygml/waterbody/2.0/waterBody.xsd \
        http://www.opengis.net/citygml/tunnel/2.0 http://schemas.opengis.net/citygml/tunnel/2.0/tunnel.xsd \
        http://www.opengis.net/citygml/vegetation/2.0 http://schemas.opengis.net/citygml/vegetation/2.0/vegetation.xsd \
        http://www.opengis.net/citygml/transportation/2.0 http://schemas.opengis.net/citygml/transportation/2.0/transportation.xsd \
        http://www.opengis.net/citygml/texturedsurface/2.0 http://schemas.opengis.net/citygml/texturedsurface/2.0/texturedSurface.xsd \
        http://www.opengis.net/citygml/relief/2.0 http://schemas.opengis.net/citygml/relief/2.0/relief.xsd \
        http://www.opengis.net/citygml/landuse/2.0 http://schemas.opengis.net/citygml/landuse/2.0/landUse.xsd \
        http://www.opengis.net/citygml/generics/2.0 http://schemas.opengis.net/citygml/generics/2.0/generics.xsd \
        http://www.opengis.net/citygml/cityobjectgroup/2.0 http://schemas.opengis.net/citygml/cityobjectgroup/2.0/cityObjectGroup.xsd\
        http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE /Users/kavisha/Desktop/githubpvt/3D_Metadata_ADE/XSD/3DMD_ADE.xsd"      
        
    nsmap = {None : ns,
        'gml' : ns_gml,
        'xAL':ns_xAL,
        'xsi':ns_xsi,
        'xlink':ns_xlink ,
        'dem':ns_dem,
        'bldg':ns_bldg,
        'app':ns_app,
        'wtr':ns_wtr,
        'gen':ns_gen,
        'luse':ns_luse,
        'tran':ns_tran,
        'frn':ns_frn,
        'veg':ns_veg,
        'tun':ns_tun,
        'tex':ns_tex,
        'brid':ns_brid,
        'core':ns_core,
        'grp':ns_grp,
        'md':ns_md
        
        }
    print ("\nReading elements ......")
    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance","schemaLocation")
    cityModel = etree.Element("CityModel", {attr_qname: schemalocs}, nsmap=nsmap) 
    
    # MDcitymodel {Metadata city model}
    cityObjectMember = etree.SubElement(cityModel, "{%s}cityObjectMember" %ns)
    mdcitymodel = etree.SubElement(cityObjectMember, "{%s}MDcitymodel" %ns_md)
    
    # metadata identifier
    metadataIdentifier =  etree.SubElement(mdcitymodel, "{%s}metadataIdentifier" %ns_md)
    metadataIdentifier.text = "GML_" + str(uuid.uuid1())
    
    # citymodel identifier
    citymodelIdentifier =  etree.SubElement(mdcitymodel, "{%s}citymodelIdentifier" %ns_md)
    if root.find('.//{%s}id' %ns_gml)!=None:
        gmlid = root.find('.//{%s}id' %ns_gml)
        citymodelIdentifier.text = gmlid.text
    else:
        citymodelIdentifier.text = "GML_" + str(uuid.uuid1())
        print ("\ncitymodelIdentifier not defined!! An arbitrary value is given.")
          
    # ISO metadata
    print ("\nISO metadata: ") 
    isometadata = etree.SubElement(mdcitymodel, "{%s}ISOmetadata" %ns_md)
    isoidentifier = etree.SubElement(isometadata, "{%s}ISOidentifier" %ns_md)
    # dataset title
    datasetTitle = etree.SubElement(isoidentifier, "{%s}datasetTitle" %ns_md)
    if root.find('{%s}name' %ns_gml)!=None:
        name = root.find('{%s}name' %ns_gml)
        datasetTitle.text = name.text
    else:
        datasetTitle.text = "Name not defined!"
        print ("datasetTitle is not defined!!")
    # dataset reference date
    datasetReferenceDate = etree.SubElement(isoidentifier, "{%s}datasetReferenceDate" %ns_md)
    if root.find('{%s}creationDate' %ns)!=None:
        creationDate = root.find('.//{%s}creationDate' %ns_gml)
        datasetReferenceDate.text = creationDate.text
    else:
        datasetReferenceDate.text = time.strftime("%Y-%m-%d")
        print ("datasetReferenceDate is not defined!!")
    # dataset responsible party
    datasetResponsibleParty = etree.SubElement(isoidentifier, "{%s}datasetResponsibleParty" %ns_md)
    organizationalContact = etree.SubElement(datasetResponsibleParty, "{%s}OrganizationalContact" %ns_md)
    contactName = etree.SubElement(organizationalContact, "{%s}contactName" %ns_md)
    contactName.text = "House of Slytherin"
    phone = etree.SubElement(organizationalContact, "{%s}phone" %ns_md)
    phone.text = "+00 00000000"
    address = etree.SubElement(organizationalContact, "{%s}address" %ns_md)
    address.text = "Hogwarts Castle, Highlands, Scotland, Great Britain"
    emailAddress = etree.SubElement(organizationalContact, "{%s}emailAddress" %ns_md)
    emailAddress.text ="slytherin@HogwartsSchoolofWitchcraftandWizardry.com"
    website = etree.SubElement(organizationalContact, "{%s}website" %ns_md)
    website.text = "http://www.HogwartsSchoolofWitchcraftandWizardry.com/Slytherin"
    print ("datasetResponsibleParty is not defined!!")
    # geographic location
    geoLocation = etree.SubElement(isoidentifier, "{%s}geoLocation" %ns_md)
    geoLocation.text = "No geoLocation available!"
    print ("geoLocation is not defined!!")
    # dataset language
    datasetLanguage = etree.SubElement(isoidentifier, "{%s}datasetLanguage" %ns_md)
    datasetLanguage.text = "English"
    #
    datasetCharacterSet = etree.SubElement(isoidentifier, "{%s}datasetCharacterSet" %ns_md)
    datasetCharacterSet.text = "UTF-8"
    # dataset topic category
    datasetTopicCategory = etree.SubElement(isoidentifier, "{%s}datasetTopicCategory" %ns_md)
    datasetTopicCategory.attrib['codeSpace'] = "http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE//codelists/MDtopicCategory.xml"
    datasetTopicCategory.text = "geoscientificInformation"
    # dataset description
    datasetDescription = etree.SubElement(isoidentifier, "{%s}datasetDescription" %ns_md)
    if root.find('{%s}description' %ns_gml)!=None:
        descrip = root.find('{%s}name' %ns_gml)
        datasetDescription.text = descrip.text
    else:
        datasetDescription.text = "No description available!"
        print ("datasetDescription is not defined!!")
    # distribution format version
    distributionFormatVersion = etree.SubElement(isoidentifier, "{%s}distributionFormatVersion" %ns_md)
    distributionFormatVersion.text = "CityGML 2.0"
    # spatial representation type
    spatialRepresentationType = etree.SubElement(isoidentifier, "{%s}spatialRepresentationType" %ns_md)
    spatialRepresentationType.attrib['codeSpace'] = "http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE//codelists/MDspatialRepTypeCode.xml"
    spatialRepresentationType.text = "vector"
    # reference system/crs
    referenceSystem = etree.SubElement(isoidentifier, "{%s}referenceSystem" %ns_md)
    # temporal information
    temporalInformation = etree.SubElement(isoidentifier, "{%s}temporalInformation" %ns_md)
    temporalInformation.text = time.strftime("%Y-%m-%d")
    print ("temporalInformation is not defined!!")
    # online resource
    onlineResource = etree.SubElement(isoidentifier, "{%s}onlineResource" %ns_md)
    onlineResource.text = "https://www.citygml.org/samplefiles/"
    print ("onlineResource is not defined!!")
    # file identifier
    fileIdentifier = etree.SubElement(isoidentifier, "{%s}fileIdentifier" %ns_md)
    fileIdentifier.text = os.path.split(inputfile)[1]
    # metadata standard
    metadataStandard = etree.SubElement(isoidentifier, "{%s}metadataStandard" %ns_md)
    metadataStandard.text = "ISO 19115 - Geographic Information -Metadata"
    # metadata standard version
    metadataStandardVersion = etree.SubElement(isoidentifier, "{%s}metadataStandardVersion" %ns_md)
    metadataStandardVersion.text = "19115:2014(E)"
    # metadata language
    metadataLanguage = etree.SubElement(isoidentifier, "{%s}metadataLanguage" %ns_md)
    metadataLanguage.text = "English"
    # metadata character set
    metadataCharacterSet = etree.SubElement(isoidentifier, "{%s}metadataCharacterSet" %ns_md)
    metadataCharacterSet.text = "UTF-8"
    # metadata point of contact
    metadataPointOfContact = etree.SubElement(isoidentifier, "{%s}metadataPointOfContact" %ns_md)
    organizationalContact = etree.SubElement(metadataPointOfContact, "{%s}OrganizationalContact" %ns_md)
    contactName = etree.SubElement(organizationalContact, "{%s}contactName" %ns_md)
    contactName.text = "House of Slytherin"
    phone = etree.SubElement(organizationalContact, "{%s}phone" %ns_md)
    phone.text = "+00 00000000"
    address = etree.SubElement(organizationalContact, "{%s}address" %ns_md)
    address.text = "Hogwarts Castle, Highlands, Scotland, Great Britain"
    emailAddress = etree.SubElement(organizationalContact, "{%s}emailAddress" %ns_md)
    emailAddress.text ="slytherin@HogwartsSchoolofWitchcraftandWizardry.com"
    website = etree.SubElement(organizationalContact, "{%s}website" %ns_md)
    website.text = "http://www.HogwartsSchoolofWitchcraftandWizardry.com/Slytherin"
    print ("datasetResponsibleParty is not defined!!")
    # metadata datestamp
    metadataDateStamp = etree.SubElement(isoidentifier, "{%s}metadataDateStamp" %ns_md)
    metadataDateStamp.text = time.strftime("%Y-%m-%d")
    # lineage
    lineage = etree.SubElement(isoidentifier, "{%s}lineage" %ns_md)
    Lineage = etree.SubElement(lineage, "{%s}Lineage" %ns_md)
    source = etree.SubElement(Lineage, "{%s}source" %ns_md)
    source.text = "Put source here.."
    processStep = etree.SubElement(Lineage, "{%s}processStep" %ns_md)
    processStep.text = "Put processStep here.."
    print ("lineage source and process steps are not defined!!")
    # bounding box
    boundingBox3D = etree.SubElement(isoidentifier, "{%s}boundingBox3D" %ns_md)
    if root.find('{%s}boundedBy' %ns_gml)!=None:
        bby = root.find('{%s}boundedBy' %ns_gml)
        if bby.find('{%s}Envelope' %ns_gml)!=None:
            gmlEnvelope =  etree.SubElement(boundingBox3D, "{%s}Envelope" %ns_gml)
            if bby.find('{%s}Envelope' %ns_gml)!=None:
                envlp = bby.find('{%s}Envelope' %ns_gml)
                if envlp.get("srsName")!=None:
#                   print (envlp.get("srsName"))
                    referenceSystem.text = envlp.get("srsName")
                if envlp.find('{%s}lowerCorner' %ns_gml)!=None:
                    envlplc = envlp.find('{%s}lowerCorner' %ns_gml)
                    gmlLowerCorner = etree.SubElement(gmlEnvelope, "{%s}lowerCorner" %ns_gml)
                    gmlLowerCorner.text = envlplc.text
                if envlp.find('{%s}upperCorner' %ns_gml)!=None:
                    envlpuc = envlp.find('{%s}upperCorner' %ns_gml)
                    gmlUpperCorner = etree.SubElement(gmlEnvelope, "{%s}upperCorner" %ns_gml)
                    gmlUpperCorner.text = envlpuc.text   
    # abstract                
    abstract = etree.SubElement(isoidentifier, "{%s}abstract" %ns_md)
    abstract.text = "la la la ....."
    print ("abstract is not defined!!")
    # specific usage
    specificUsage = etree.SubElement(isoidentifier, "{%s}specificUsage" %ns_md)
    specificUsage.text = "3D Geoinformation modelling"
    print ("specificUsage is not defined!!")
    # keywords
    keywords = etree.SubElement(isoidentifier, "{%s}keywords" %ns_md)
    keywords.text = "CityGML, 3D city modelling, Metadata"
    print ("keywords is not defined!!")
    # constraints
    constraints = etree.SubElement(isoidentifier, "{%s}constraints" %ns_md)
    constraintsOnUsage = etree.SubElement(constraints, "{%s}ConstraintsOnUsage" %ns_md)
    legalConstraints = etree.SubElement(constraintsOnUsage, "{%s}legalConstraints" %ns_md)
    legalConstraints.attrib['codeSpace'] = "http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE//codelists/MDlegalConstraints.xml"
    legalConstraints.text = "unrestricted"
    securityConstraints = etree.SubElement(constraintsOnUsage, "{%s}legalConstraints" %ns_md)
    securityConstraints.attrib['codeSpace'] = "http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE//codelists/MDsecurityConstraints.xml"
    securityConstraints.text = "owner"
    userNote = etree.SubElement(constraintsOnUsage, "{%s}legalConstraints" %ns_md)
    userNote.text = "Draco Dormiens Nunquam Titillandus"
    print ("constraints not defined!!")
    
    
    # thematic models
    thematicModels = etree.SubElement(mdcitymodel, "{%s}thematicModels" %ns_md)
    presentThematicModels = etree.SubElement(thematicModels, "{%s}presentThematicModels" %ns_md) 
    
    
     # textures 
    textures = etree.SubElement(mdcitymodel, "{%s}textures" %ns_md)
    if root.find('.//{%s}ParameterizedTexture' %ns_app)!=None:
        textures.text = "present"
    else:
        textures.text = "absent"
    
    
    # materials
    materials = etree.SubElement(mdcitymodel, "{%s}materials" %ns_md)
    if root.find('.//{%s}X3DMaterial' %ns_app)!=None:
        materials.text = "present"
    else:
        materials.text = "absent"
        
    # MDcityfeatures
    thematicModelsSet = set()
    terrainTypeSet = set()
    cogSet = set()
    buildingCount = 0
    buildingpartsCount = 0
    buildinginstallationsCount = 0
    bridgeCount = 0
    bridgepartsCount = 0
    bridgeinstallationsCount = 0
    bridgeconstructionelementsCount = 0
    tunnelCount = 0
    tunnelpartsCount = 0
    tunnelinstallationsCount = 0
    vegCount = 0
    svoCount = 0
    plantcoverCount = 0
    waterCount = 0
    tinreliefCount = 0
    transportationCount = 0
    roadCount = 0
    railwayCount = 0
    squareCount = 0
    trackCount = 0
    genericsCount = 0
    cityfurnitureCount = 0
    cityobjectgroupCount = 0
    landuseCount = 0
    numberOfTriangles = 0
    
    lod0bldgCount = 0
    lod1bldgCount = 0
    lod2bldgCount = 0
    lod3bldgCount = 0
    lod4bldgCount = 0
    
    lod1bridgeCount = 0
    lod2bridgeCount = 0
    lod3bridgeCount = 0
    lod4bridgeCount = 0
    
    lod1tunnelCount = 0
    lod2tunnelCount = 0
    lod3tunnelCount = 0
    lod4tunnelCount = 0
    
    lod0tranCount = 0
    lod1tranCount = 0
    lod2tranCount = 0
    lod3tranCount = 0
    lod4tranCount = 0
    
    lod1vegCount = 0
    lod2vegCount = 0
    lod3vegCount = 0
    lod4vegCount = 0
    
    lod0waterCount = 0
    lod1waterCount = 0
    lod2waterCount = 0
    lod3waterCount = 0
    lod4waterCount = 0
    
    lod0tinreliefCount = 0
    lod1tinreliefCount = 0
    lod2tinreliefCount = 0
    lod3tinreliefCount = 0
    lod4tinreliefCount = 0
      
    lod0genCount = 0
    lod1genCount = 0
    lod2genCount = 0
    lod3genCount = 0
    lod4genCount = 0
    
    lod1cfCount = 0
    lod2cfCount = 0
    lod3cfCount = 0
    lod4cfCount = 0
    
    
    lod0luseCount = 0
    lod1luseCount = 0
    lod2luseCount = 0
    lod3luseCount = 0
    lod4luseCount = 0
    
    #for cityobject groups
    
    cogbuildingCount = 0
    cogbuildingpartsCount = 0
    cogbuildinginstallationsCount = 0
    cogbridgeCount = 0
    cogbridgepartsCount = 0
    cogbridgeinstallationsCount = 0
    cogbridgeconstructionelementsCount = 0
    cogtunnelCount = 0
    cogtunnelpartsCount = 0
    cogtunnelinstallationsCount = 0
    cogvegCount = 0
    cogsvoCount = 0
    cogplantcoverCount = 0
    cogwaterCount = 0
    cogtinreliefCount = 0
    cogtransportationCount = 0
    cogroadCount = 0
    cograilwayCount = 0
    cogsquareCount = 0
    cogtrackCount = 0
    coggenericsCount = 0
    cogcityfurnitureCount = 0
    coglanduseCount = 0
    cognumberOfTriangles = 0
    
    lod0cogbldgCount = 0
    lod1cogbldgCount = 0
    lod2cogbldgCount = 0
    lod3cogbldgCount = 0
    lod4cogbldgCount = 0
    
    lod1cogbridgeCount = 0
    lod2cogbridgeCount = 0
    lod3cogbridgeCount = 0
    lod4cogbridgeCount = 0
    
    lod1cogtunnelCount = 0
    lod2cogtunnelCount = 0
    lod3cogtunnelCount = 0
    lod4cogtunnelCount = 0
    
    lod0cogtranCount = 0
    lod1cogtranCount = 0
    lod2cogtranCount = 0
    lod3cogtranCount = 0
    lod4cogtranCount = 0
    
    lod1cogvegCount = 0
    lod2cogvegCount = 0
    lod3cogvegCount = 0
    lod4cogvegCount = 0
    
    lod0cogwaterCount = 0
    lod1cogwaterCount = 0
    lod2cogwaterCount = 0
    lod3cogwaterCount = 0
    lod4cogwaterCount = 0
    
    lod0coggenCount = 0
    lod1coggenCount = 0
    lod2coggenCount = 0
    lod3coggenCount = 0
    lod4coggenCount = 0
    
    lod1cogcfCount = 0
    lod2cogcfCount = 0
    lod3cogcfCount = 0
    lod4cogcfCount = 0
    
    
    lod0cogluseCount = 0
    lod1cogluseCount = 0
    lod2cogluseCount = 0
    lod3cogluseCount = 0
    lod4cogluseCount = 0

    lod0cogtinreliefCount = 0
    lod1cogtinreliefCount = 0
    lod2cogtinreliefCount = 0
    lod3cogtinreliefCount = 0
    lod4cogtinreliefCount = 0
    
    for obj in root.getiterator('{%s}cityObjectMember'% ns):
        for child in obj.getchildren():
            if child.tag not in thematicModelsSet:
                
                if child.tag == '{%s}Building' %ns_bldg:
                    thematicModelsSet.add("Building")
                    buildingCount = buildingCount + 1
                    lodcount = getcityobjects.getbuilding(child)                    
                    lod0bldgCount = lod0bldgCount + lodcount[0]
                    lod1bldgCount = lod1bldgCount + lodcount[1]
                    lod2bldgCount = lod2bldgCount + lodcount[2]
                    lod3bldgCount = lod3bldgCount + lodcount[3]   
                    lod4bldgCount = lod4bldgCount + lodcount[4]
                    buildinginstallationsCount = buildinginstallationsCount + lodcount[5]   
                    buildingpartsCount = buildingpartsCount + lodcount[6]
                            
                if child.tag == '{%s}Bridge' %ns_brid:
                    thematicModelsSet.add("Bridge") 
                    bridgeCount = bridgeCount + 1
                    lodcount = getcityobjects.getbridge(child)
                    lod1bridgeCount = lod1bridgeCount + lodcount[0]
                    lod2bridgeCount = lod2bridgeCount + lodcount[1]
                    lod3bridgeCount = lod3bridgeCount + lodcount[2]
                    lod4bridgeCount = lod4bridgeCount + lodcount[3]   
                    bridgeinstallationsCount = bridgeinstallationsCount + lodcount[4]   
                    bridgepartsCount = bridgepartsCount + lodcount[5] 
                    bridgeconstructionelementsCount = bridgeconstructionelementsCount +lodcount[6] 
                    
                if child.tag == '{%s}Tunnel' %ns_tun:
                    thematicModelsSet.add("Tunnel")
                    tunnelCount = tunnelCount + 1
                    lodcount = getcityobjects.gettunnel(child)
                    lod1tunnelCount = lod1tunnelCount + lodcount[0]
                    lod2tunnelCount = lod2tunnelCount + lodcount[1]
                    lod3tunnelCount = lod3tunnelCount + lodcount[2]
                    lod4tunnelCount = lod4tunnelCount + lodcount[3]   
                    tunnelinstallationsCount = tunnelinstallationsCount + lodcount[4]   
                    tunnelpartsCount = tunnelpartsCount + lodcount[5]   
                    
                if child.tag == '{%s}SolitaryVegetationObject' %ns_veg or \
                child.tag == '{%s}PlantCover' %ns_veg:
                    thematicModelsSet.add("Vegetation")
                    vegCount = vegCount + 1
                    lodcount = getcityobjects.getveg(child)
                    lod1vegCount = lod1vegCount + lodcount[0]
                    lod2vegCount = lod2vegCount + lodcount[1]
                    lod3vegCount = lod3vegCount + lodcount[2]
                    lod4vegCount = lod4vegCount + lodcount[3] 
                    svoCount = svoCount + lodcount[4]  
                    plantcoverCount = plantcoverCount + lodcount[5]                      
                    
                if child.tag == '{%s}WaterBody' %ns_wtr:
                    thematicModelsSet.add("WaterBody")
                    waterCount = waterCount + 1
                    lodcount = getcityobjects.getwater(child)
                    lod0waterCount = lod0waterCount + lodcount[0]
                    lod1waterCount = lod1waterCount + lodcount[1]
                    lod2waterCount = lod2waterCount + lodcount[2]
                    lod3waterCount = lod3waterCount + lodcount[3]
                    lod4waterCount = lod4waterCount + lodcount[4]
                    
                if child.tag == '{%s}ReliefFeature' %ns_dem:
                    if child.findall('.//{%s}TINRelief'  %ns_dem):
                        thematicModelsSet.add("Relief")
                        terrainTypeSet.add("TINRelief")
                        tinreliefCount = tinreliefCount + 1
                        lodcount = getcityobjects.getrelief(child)
                        lod0tinreliefCount = lod0tinreliefCount + lodcount[0]
                        lod1tinreliefCount = lod1tinreliefCount + lodcount[1]
                        lod2tinreliefCount = lod2tinreliefCount + lodcount[2]
                        lod3tinreliefCount = lod3tinreliefCount + lodcount[3]
                        lod4tinreliefCount = lod4tinreliefCount + lodcount[4]
                        numberOfTriangles = numberOfTriangles + lodcount[5]
                      
                if child.tag == '{%s}Road' %ns_tran or \
                child.tag == '{%s}Railway' %ns_tran or \
                child.tag == '{%s}Square' %ns_tran or \
                child.tag == '{%s}Track' %ns_tran:
                    thematicModelsSet.add("Transportation")
                    transportationCount = transportationCount + 1
                    lodcount = getcityobjects.gettransport(child)
                    lod0tranCount = lod0tranCount + lodcount[0]
                    lod1tranCount = lod1tranCount + lodcount[1]
                    lod2tranCount = lod2tranCount + lodcount[2]
                    lod3tranCount = lod3tranCount + lodcount[3]
                    lod4tranCount = lod4tranCount + lodcount[4]
                    roadCount = roadCount + lodcount[5]
                    railwayCount = railwayCount + lodcount[6]
                    squareCount = squareCount + lodcount[7]
                    trackCount = trackCount + lodcount[8]                  
                    
                if child.tag == '{%s}GenericCityObject' %ns_gen:                  
                    thematicModelsSet.add("Generics")
                    genericsCount = genericsCount + 1
                    lodcount = getcityobjects.getgenerics(child)
                    lod0genCount = lod0genCount + lodcount[0]
                    lod1genCount = lod1genCount + lodcount[1]
                    lod2genCount = lod2genCount + lodcount[2]
                    lod3genCount = lod3genCount + lodcount[3]
                    lod4genCount = lod4genCount + lodcount[4]                    
                    
                if child.tag == '{%s}CityFurniture' %ns_frn:                
                    thematicModelsSet.add("CityFurniture")
                    cityfurnitureCount = cityfurnitureCount + 1
                    lodcount = getcityobjects.getcityfurniture(child)
                    lod1cfCount = lod1cfCount + lodcount[0]
                    lod2cfCount = lod2cfCount + lodcount[1]
                    lod3cfCount = lod3cfCount + lodcount[2]
                    lod4cfCount = lod4cfCount + lodcount[3]
                    
                if child.tag == '{%s}LandUse' %ns_luse:               
                    thematicModelsSet.add("LandUse")
                    landuseCount = landuseCount + 1
                    lodcount = getcityobjects.getlanduse(child)
                    lod0luseCount = lod0luseCount + lodcount[0]
                    lod1luseCount = lod1luseCount + lodcount[1]
                    lod2luseCount = lod2luseCount + lodcount[2]
                    lod3luseCount = lod3luseCount + lodcount[3]
                    lod4luseCount = lod4luseCount + lodcount[4]
                    
                if child.tag == '{%s}CityObjectGroup' %ns_grp:                
                    thematicModelsSet.add("CityObjectGroup")
                    cityobjectgroupCount = cityobjectgroupCount + 1
                    if child.findall('{%s}groupMember'%ns_grp):
                        for gm in child.findall('{%s}groupMember'%ns_grp):
                            for node in gm.getiterator():
                                if (node.tag =='{%s}SolitaryVegetationObject' %ns_veg) or \
                                (node.tag =='{%s}PlantCover' %ns_veg):
                                    cogSet.add("Vegetation")
                                    cogvegCount = cogvegCount + 1
                                    lodcount = getcityobjects.getveg(node)
                                    lod1cogvegCount = lod1cogvegCount + lodcount[0]
                                    lod2cogvegCount = lod2cogvegCount + lodcount[1]
                                    lod3cogvegCount = lod3cogvegCount + lodcount[2]
                                    lod4cogvegCount = lod4cogvegCount + lodcount[3]
                                    cogsvoCount = cogsvoCount + lodcount[4]  
                                    cogplantcoverCount = cogplantcoverCount + lodcount[5]  
                                
                                if (node.tag =='{%s}LandUse' %ns_luse):
                                    cogSet.add("LandUse")
                                    coglanduseCount = coglanduseCount + 1
                                    lodcount = getcityobjects.getlanduse(node)
                                    lod0cogluseCount = lod0cogluseCount + lodcount[0]
                                    lod1cogluseCount = lod1cogluseCount + lodcount[1]
                                    lod2cogluseCount = lod2cogluseCount + lodcount[2]
                                    lod3cogluseCount = lod3cogluseCount + lodcount[3]
                                    lod4cogluseCount = lod4cogluseCount + lodcount[4]
                                
                                if (node.tag =='{%s}GenericCityObject' %ns_gen):
                                    cogSet.add("Generics")
                                    coggenericsCount = coggenericsCount + 1
                                    lodcount = getcityobjects.getgenerics(node)
                                    lod0coggenCount = lod0coggenCount + lodcount[0]
                                    lod1coggenCount = lod1coggenCount + lodcount[1]
                                    lod2coggenCount = lod2coggenCount + lodcount[2]
                                    lod3coggenCount = lod3coggenCount + lodcount[3]
                                    lod4coggenCount = lod4coggenCount + lodcount[4]
                                    
                                if (node.tag =='{%s}Road' %ns_tran) or \
                                (node.tag =='{%s}Railway' %ns_tran) or \
                                (node.tag =='{%s}Square' %ns_tran) or \
                                (node.tag =='{%s}Track' %ns_tran):
                                    cogSet.add("Transportation")
                                    cogtransportationCount = cogtransportationCount + 1
                                    lodcount = getcityobjects.gettransport(node)
                                    lod0cogtranCount = lod0cogtranCount + lodcount[0]
                                    lod1cogtranCount = lod1cogtranCount + lodcount[1]
                                    lod2cogtranCount = lod2cogtranCount + lodcount[2]
                                    lod3cogtranCount = lod3cogtranCount + lodcount[3]
                                    lod4cogtranCount = lod4cogtranCount + lodcount[4]
                                    cogroadCount = cogroadCount + lodcount[5]
                                    cograilwayCount = cograilwayCount + lodcount[6]
                                    cogsquareCount = cogsquareCount + lodcount[7]
                                    cogtrackCount = cogtrackCount + lodcount[8] 
                                    
                                if (node.tag =='{%s}WaterBody' %ns_wtr):
                                    cogSet.add("WaterBody")
                                    cogwaterCount = cogwaterCount + 1
                                    lodcount = getcityobjects.getwater(node)
                                    lod0cogwaterCount = lod0cogwaterCount + lodcount[0]
                                    lod1cogwaterCount = lod1cogwaterCount + lodcount[1]
                                    lod2cogwaterCount = lod2cogwaterCount + lodcount[2]
                                    lod3cogwaterCount = lod3cogwaterCount + lodcount[3]
                                    lod4cogwaterCount = lod4cogwaterCount + lodcount[4]
                                
                                if (node.tag =='{%s}CityFurniture' %ns_frn):
                                    cogSet.add("CityFurniture")
                                    cogcityfurnitureCount = cogcityfurnitureCount + 1
                                    lodcount = getcityobjects.getcityfurniture(node)
                                    lod1cogcfCount = lod1cogcfCount + lodcount[0]
                                    lod2cogcfCount = lod2cogcfCount + lodcount[1]
                                    lod3cogcfCount = lod3cogcfCount + lodcount[2]
                                    lod4cogcfCount = lod4cogcfCount + lodcount[3]
                                    
                                if (node.tag =='{%s}Tunnel' %ns_tun):
                                    cogSet.add("Tunnel")
                                    cogtunnelCount = cogtunnelCount + 1
                                    lodcount = getcityobjects.gettunnel(node)
                                    lod1cogtunnelCount = lod1cogtunnelCount + lodcount[0]
                                    lod2cogtunnelCount = lod2cogtunnelCount + lodcount[1]
                                    lod3cogtunnelCount = lod3cogtunnelCount + lodcount[2]
                                    lod4cogtunnelCount = lod4cogtunnelCount + lodcount[3]   
                                    cogtunnelinstallationsCount = cogtunnelinstallationsCount + lodcount[4]   
                                    cogtunnelpartsCount = cogtunnelpartsCount + lodcount[5]
                                    
                                if (node.tag =='{%s}Bridge' %ns_brid):
                                    cogSet.add("Bridge")
                                    cogbridgeCount = cogbridgeCount + 1
                                    lodcount = getcityobjects.getbridge(node)
                                    lod1cogbridgeCount = lod1cogbridgeCount + lodcount[0]
                                    lod2cogbridgeCount = lod2cogbridgeCount + lodcount[1]
                                    lod3cogbridgeCount = lod3cogbridgeCount + lodcount[2]
                                    lod4cogbridgeCount = lod4cogbridgeCount + lodcount[3]   
                                    cogbridgeinstallationsCount = cogbridgeinstallationsCount + lodcount[4]   
                                    cogbridgepartsCount = cogbridgepartsCount + lodcount[5] 
                                    cogbridgeconstructionelementsCount = cogbridgeconstructionelementsCount +lodcount[6]
                                    
                                if (node.tag =='{%s}Building' %ns_bldg):
                                    cogSet.add("Building")
                                    cogbuildingCount = cogbuildingCount + 1
                                    lodcount = getcityobjects.getbuilding(node)                    
                                    lod0cogbldgCount = lod0cogbldgCount + lodcount[0]
                                    lod1cogbldgCount = lod1cogbldgCount + lodcount[1]
                                    lod2cogbldgCount = lod2cogbldgCount + lodcount[2]
                                    lod3cogbldgCount = lod3cogbldgCount + lodcount[3]   
                                    lod4cogbldgCount = lod4cogbldgCount + lodcount[4]
                                    cogbuildinginstallationsCount = cogbuildinginstallationsCount + lodcount[5]   
                                    cogbuildingpartsCount = cogbuildingpartsCount + lodcount[6]
                                if (node.tag =='{%s}Relief' %ns_bldg):
                                    cogSet.add("Relief")
                                    cogtinreliefCount = cogtinreliefCount + 1
                                    lodcount = getcityobjects.getrelief(child)
                                    lod0cogtinreliefCount = lod0cogtinreliefCount + lodcount[0]
                                    lod1cogtinreliefCount = lod1cogtinreliefCount + lodcount[1]
                                    lod2cogtinreliefCount = lod2cogtinreliefCount + lodcount[2]
                                    lod3cogtinreliefCount = lod3cogtinreliefCount + lodcount[3]
                                    lod4cogtinreliefCount = lod4cogtinreliefCount + lodcount[4]
                                    cognumberOfTriangles = cognumberOfTriangles + lodcount[5]
                    
    
    print ("\nThematic Models Present: ") 
    for item in thematicModelsSet:
        print (item)
        thematicModel = etree.SubElement(presentThematicModels, "{%s}thematicModel" %ns_md)
        thematicModel.text = item 
        mdCityfeatures = etree.SubElement(mdcitymodel, "{%s}MDcityfeatures" %ns_md)
        if item == "Building":
            mdbuilding = etree.SubElement(mdCityfeatures, "{%s}MDbuilding" %ns_md)
            featureType = etree.SubElement(mdbuilding, "{%s}featureType" %ns_md)
            featureType.text = "Building"
            featureCount = etree.SubElement(mdbuilding, "{%s}featureCount" %ns_md)
            featureCount.text = str(buildingCount)
            lods = etree.SubElement(mdbuilding, "{%s}LevelsOfDetail" %ns_md)
            if lod0bldgCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "1"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod0bldgCount)
            if lod1bldgCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "1"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod1bldgCount)
            if lod2bldgCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "2"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod2bldgCount)
            if lod3bldgCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "3"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod3bldgCount)
            if lod4bldgCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "4"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod4bldgCount)
            
            buildingParts = etree.SubElement(mdbuilding, "{%s}buildingParts" %ns_md)
            buildingParts.text = str(buildingpartsCount)
            buildingInstallations = etree.SubElement(mdbuilding, "{%s}buildingInstallations" %ns_md)
            buildingInstallations.text = str(buildinginstallationsCount)
        
        if item == "Bridge":
            mdbridge = etree.SubElement(mdCityfeatures, "{%s}MDbridge" %ns_md)
            featureType = etree.SubElement(mdbridge, "{%s}featureType" %ns_md)
            featureType.text = "Bridge"
            featureCount = etree.SubElement(mdbridge, "{%s}featureCount" %ns_md)
            featureCount.text = str(bridgeCount)
            lods = etree.SubElement(mdbridge, "{%s}LevelsOfDetail" %ns_md)
            if lod1bridgeCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "1"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod1bridgeCount)
            if lod2bridgeCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "2"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod2bridgeCount)
            if lod3bridgeCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "3"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod3bridgeCount)
            if lod4bridgeCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "4"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod4bridgeCount)
            bridgeParts = etree.SubElement(mdbridge, "{%s}bridgeParts" %ns_md)
            bridgeParts.text = str(bridgepartsCount)
            bridgeInstallations = etree.SubElement(mdbridge, "{%s}bridgeInstallations" %ns_md)
            bridgeInstallations.text = str(bridgeinstallationsCount)
            bridgeConstructionElements = etree.SubElement(mdbridge, "{%s}bridgeConstructionElements" %ns_md)
            bridgeConstructionElements.text = str(bridgeconstructionelementsCount)
              
        if item == "Tunnel":
            mdtunnel = etree.SubElement(mdCityfeatures, "{%s}MDtunnel" %ns_md)
            featureType = etree.SubElement(mdtunnel, "{%s}featureType" %ns_md)
            featureType.text = "Tunnel"
            featureCount = etree.SubElement(mdtunnel, "{%s}featureCount" %ns_md)
            featureCount.text = str(tunnelCount)
            lods = etree.SubElement(mdtunnel, "{%s}LevelsOfDetail" %ns_md)
            if lod1tunnelCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "1"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod1tunnelCount)
            if lod2tunnelCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "2"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod2tunnelCount)
            if lod3tunnelCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "3"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod3tunnelCount)
            if lod4tunnelCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "4"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod4tunnelCount)
            tunnelParts = etree.SubElement(mdtunnel, "{%s}tunnelParts" %ns_md)
            tunnelParts.text = str(tunnelpartsCount)
            tunnelInstallations = etree.SubElement(mdtunnel, "{%s}tunnelInstallations" %ns_md)
            tunnelInstallations.text = str(tunnelinstallationsCount)
                
        if item == "Vegetation":
            mdvegetation = etree.SubElement(mdCityfeatures, "{%s}MDvegetation" %ns_md)
            featureType = etree.SubElement(mdvegetation, "{%s}featureType" %ns_md)
            featureType.text = "Vegetation"
            featureCount = etree.SubElement(mdvegetation, "{%s}featureCount" %ns_md)
            featureCount.text = str(vegCount)
            lods = etree.SubElement(mdvegetation, "{%s}LevelsOfDetail" %ns_md)
            if lod1vegCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "1"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod1vegCount)
            if lod2vegCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "2"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod2vegCount)
            if lod3vegCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "3"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod3vegCount)
            if lod4vegCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "4"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod4vegCount)
            plantCovers = etree.SubElement(mdvegetation, "{%s}plantCovers" %ns_md)
            plantCovers.text = str(plantcoverCount)
            solitaryVegetationObjects = etree.SubElement(mdvegetation, "{%s}solitaryVegetationObjects" %ns_md)
            solitaryVegetationObjects.text = str(svoCount)
            
        if item == "WaterBody":
            mdwaterbody = etree.SubElement(mdCityfeatures, "{%s}MDwaterBody" %ns_md)
            featureType = etree.SubElement(mdwaterbody, "{%s}featureType" %ns_md)
            featureType.text = "WaterBody"
            featureCount = etree.SubElement(mdwaterbody, "{%s}featureCount" %ns_md)
            featureCount.text = str(waterCount)
            lods = etree.SubElement(mdwaterbody, "{%s}LevelsOfDetail" %ns_md)
            if lod0waterCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "0"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod0waterCount)
            if lod1waterCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "1"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod1waterCount)
            if lod2waterCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "2"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod2waterCount)
            if lod3waterCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "3"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod3waterCount)
            if lod4waterCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "4"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod4waterCount)
        
        if item == "Relief":
            for terrainItem in terrainTypeSet:
                if terrainItem == "TINRelief":
                    mdrelief = etree.SubElement(mdCityfeatures, "{%s}MDterrain" %ns_md)
                    featureType = etree.SubElement(mdrelief, "{%s}featureType" %ns_md)
                    featureType.text = "Relief"
                    featureCount = etree.SubElement(mdrelief, "{%s}featureCount" %ns_md)
                    featureCount.text = str(tinreliefCount)
                    lods = etree.SubElement(mdrelief, "{%s}LevelsOfDetail" %ns_md)
                    if lod0tinreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "0"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod0tinreliefCount)
                    if lod1tinreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1tinreliefCount)
                    if lod2tinreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2tinreliefCount)
                    if lod3tinreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3tinreliefCount)
                    if lod4tinreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4tinreliefCount)
                    terrainType = etree.SubElement(mdrelief, "{%s}terrainType" %ns_md)
                    terrainType.text = "TINRelief"
                    terrainProperties = etree.SubElement(mdrelief, "{%s}TerrainProperties" %ns_md)
                    mdTINRelief = etree.SubElement(terrainProperties, "{%s}MDTINRelief" %ns_md)
                    triangleCount = etree.SubElement(mdTINRelief, "{%s}triangleCount" %ns_md)
                    triangleCount.text = str(numberOfTriangles)
                  
        if item == "Transportation":
            mdtransportation = etree.SubElement(mdCityfeatures, "{%s}MDtransportation" %ns_md)
            featureType = etree.SubElement(mdtransportation, "{%s}featureType" %ns_md)
            featureType.text = "Transportation"
            featureCount = etree.SubElement(mdtransportation, "{%s}featureCount" %ns_md)
            featureCount.text = str(transportationCount)
            lods = etree.SubElement(mdtransportation, "{%s}LevelsOfDetail" %ns_md)
            if lod0tranCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "0"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod0tranCount)
            if lod1tranCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "1"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod1tranCount)
            if lod2tranCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "2"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod2tranCount)
            if lod3tranCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "3"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod3tranCount)
            if lod4tranCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "4"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod4tranCount)
            roads = etree.SubElement(mdtransportation, "{%s}roads" %ns_md)
            roads.text = str(roadCount)
            railways = etree.SubElement(mdtransportation, "{%s}railways" %ns_md)
            railways.text = str(railwayCount)
            tracks = etree.SubElement(mdtransportation, "{%s}tracks" %ns_md)
            tracks.text = str(trackCount)
            squares = etree.SubElement(mdtransportation, "{%s}squares" %ns_md)
            squares.text = str(squareCount)
            
        if item == "Generics":
            mdgenerics = etree.SubElement(mdCityfeatures, "{%s}MDgenerics" %ns_md)
            featureType = etree.SubElement(mdgenerics, "{%s}featureType" %ns_md)
            featureType.text = "Generics"
            featureCount = etree.SubElement(mdgenerics, "{%s}featureCount" %ns_md)
            featureCount.text = str(genericsCount)
            lods = etree.SubElement(mdgenerics, "{%s}LevelsOfDetail" %ns_md)
            if lod0genCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "1"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod0genCount)
            if lod1genCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "1"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod1genCount)
            if lod2genCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "2"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod2genCount)
            if lod3genCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "3"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod3genCount)
            if lod4genCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "4"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod4genCount)
            
        if item == "CityFurniture":
            mdcityfurniture = etree.SubElement(mdCityfeatures, "{%s}MDcityFurniture" %ns_md)
            featureType = etree.SubElement(mdcityfurniture, "{%s}featureType" %ns_md)
            featureType.text = "CityFurniture"
            featureCount = etree.SubElement(mdcityfurniture, "{%s}featureCount" %ns_md)
            featureCount.text = str(cityfurnitureCount)
            lods = etree.SubElement(mdcityfurniture, "{%s}LevelsOfDetail" %ns_md)
            if lod1cfCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "1"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod1cfCount)
            if lod2cfCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "2"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod2cfCount)
            if lod3cfCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "3"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod3cfCount)
            if lod4cfCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "4"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod4cfCount)
            
          
        if item == "LandUse":
            mdlanduse = etree.SubElement(mdCityfeatures, "{%s}MDlandUse" %ns_md)
            featureType = etree.SubElement(mdlanduse, "{%s}featureType" %ns_md)
            featureType.text = "LandUse"
            featureCount = etree.SubElement(mdlanduse, "{%s}featureCount" %ns_md)
            featureCount.text = str(landuseCount)
            lods = etree.SubElement(mdlanduse, "{%s}LevelsOfDetail" %ns_md)
            if lod0luseCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "0"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod0luseCount)
            if lod1luseCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "1"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod1luseCount)
            if lod2luseCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "2"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod2luseCount)
            if lod3luseCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "3"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod3luseCount)
            if lod4luseCount != 0:
                lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                mdlod.text = "4"
                mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                mdlodcount.text = str(lod4luseCount)
        
        if item == "CityObjectGroup":
            mdcityobjectgroup = etree.SubElement(mdCityfeatures, "{%s}MDcityObjectGroup" %ns_md)
            featureType = etree.SubElement(mdcityobjectgroup, "{%s}featureType" %ns_md)
            featureType.text = "CityObjectGroup"
            featureCount = etree.SubElement(mdcityobjectgroup, "{%s}featureCount" %ns_md)
            featureCount.text = str(cityobjectgroupCount)
            for cogItem in cogSet:
                mdcogMember = etree.SubElement(mdcityobjectgroup, "{%s}MDcityObjectGroupMember" %ns_md)
                if cogItem == "Vegetation":
                    mdvegetation = etree.SubElement(mdcogMember, "{%s}MDvegetation" %ns_md)    
                    featureType = etree.SubElement(mdvegetation, "{%s}featureType" %ns_md)
                    featureType.text = "Vegetation"
                    featureCount = etree.SubElement(mdvegetation, "{%s}featureCount" %ns_md)
                    featureCount.text = str(cogvegCount)
                    lods = etree.SubElement(mdvegetation, "{%s}LevelsOfDetail" %ns_md)
                    if lod1cogvegCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1cogvegCount)
                    if lod2cogvegCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2cogvegCount)
                    if lod3cogvegCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3cogvegCount)
                    if lod4cogvegCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4cogvegCount)
                    plantCovers = etree.SubElement(mdvegetation, "{%s}plantCovers" %ns_md)
                    plantCovers.text = str(plantcoverCount)
                    solitaryVegetationObjects = etree.SubElement(mdvegetation, "{%s}solitaryVegetationObjects" %ns_md)
                    solitaryVegetationObjects.text = str(svoCount)
                if cogItem == "LandUse":
                    mdlanduse = etree.SubElement(mdcogMember, "{%s}MDlandUse" %ns_md)
                    featureType = etree.SubElement(mdlanduse, "{%s}featureType" %ns_md)
                    featureType.text = "LandUse"
                    featureCount = etree.SubElement(mdlanduse, "{%s}featureCount" %ns_md)
                    featureCount.text = str(coglanduseCount)
                    lods = etree.SubElement(mdlanduse, "{%s}LevelsOfDetail" %ns_md)
                    if lod0cogluseCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "0"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod0cogluseCount)
                    if lod1cogluseCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1cogluseCount)
                    if lod2cogluseCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2cogluseCount)
                    if lod3cogluseCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3cogluseCount)
                    if lod4cogluseCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4cogluseCount)
                if cogItem == "CityFurniture":
                    mdcityfurniture = etree.SubElement(mdcogMember, "{%s}MDcityFurniture" %ns_md)
                    featureType = etree.SubElement(mdcityfurniture, "{%s}featureType" %ns_md)
                    featureType.text = "CityFurniture"
                    featureCount = etree.SubElement(mdcityfurniture, "{%s}featureCount" %ns_md)
                    featureCount.text = str(cogcityfurnitureCount)
                    lods = etree.SubElement(mdcityfurniture, "{%s}LevelsOfDetail" %ns_md)
                    if lod1cogcfCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1cogcfCount)
                    if lod2cogcfCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2cogcfCount)
                    if lod3cogcfCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3cogcfCount)
                    if lod4cogcfCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4cogcfCount)
                if cogItem == "Generics":
                    mdgenerics = etree.SubElement(mdcogMember, "{%s}MDgenerics" %ns_md)
                    featureType = etree.SubElement(mdgenerics, "{%s}featureType" %ns_md)
                    featureType.text = "Generics"
                    featureCount = etree.SubElement(mdgenerics, "{%s}featureCount" %ns_md)
                    featureCount.text = str(coggenericsCount)
                    lods = etree.SubElement(mdgenerics, "{%s}LevelsOfDetail" %ns_md)
                    if lod0coggenCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod0coggenCount)
                    if lod1coggenCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1coggenCount)
                    if lod2coggenCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2coggenCount)
                    if lod3coggenCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3coggenCount)
                    if lod4coggenCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4coggenCount)
                if cogItem == "Transportation":
                    mdtransportation = etree.SubElement(mdcogMember, "{%s}MDtransportation" %ns_md)
                    featureType = etree.SubElement(mdtransportation, "{%s}featureType" %ns_md)
                    featureType.text = "Transportation"
                    featureCount = etree.SubElement(mdtransportation, "{%s}featureCount" %ns_md)
                    featureCount.text = str(cogtransportationCount)
                    lods = etree.SubElement(mdtransportation, "{%s}LevelsOfDetail" %ns_md)
                    if lod0cogtranCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "0"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod0cogtranCount)
                    if lod1cogtranCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1cogtranCount)
                    if lod2cogtranCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2cogtranCount)
                    if lod3cogtranCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3cogtranCount)
                    if lod4cogtranCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4cogtranCount)
                    roads = etree.SubElement(mdtransportation, "{%s}roads" %ns_md)
                    roads.text = str(cogroadCount)
                    railways = etree.SubElement(mdtransportation, "{%s}railways" %ns_md)
                    railways.text = str(cograilwayCount)
                    tracks = etree.SubElement(mdtransportation, "{%s}tracks" %ns_md)
                    tracks.text = str(cogtrackCount)
                    squares = etree.SubElement(mdtransportation, "{%s}squares" %ns_md)
                    squares.text = str(cogsquareCount)
                if cogItem == "WaterBody":
                    mdwaterbody = etree.SubElement(mdcogMember, "{%s}MDwaterBody" %ns_md)
                    featureType = etree.SubElement(mdwaterbody, "{%s}featureType" %ns_md)
                    featureType.text = "WaterBody"
                    featureCount = etree.SubElement(mdwaterbody, "{%s}featureCount" %ns_md)
                    featureCount.text = str(cogwaterCount)
                    lods = etree.SubElement(mdwaterbody, "{%s}LevelsOfDetail" %ns_md)
                    if lod0cogwaterCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "0"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod0cogwaterCount)
                    if lod1cogwaterCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1cogwaterCount)
                    if lod2cogwaterCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2cogwaterCount)
                    if lod3cogwaterCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3cogwaterCount)
                    if lod4cogwaterCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4cogwaterCount)
                if cogItem == "Tunnel":
                    mdtunnel = etree.SubElement(mdcogMember, "{%s}MDtunnel" %ns_md)
                    featureType = etree.SubElement(mdtunnel, "{%s}featureType" %ns_md)
                    featureType.text = "Tunnel"
                    featureCount = etree.SubElement(mdtunnel, "{%s}featureCount" %ns_md)
                    featureCount.text = str(cogtunnelCount)
                    lods = etree.SubElement(mdtunnel, "{%s}LevelsOfDetail" %ns_md)
                    if lod1cogtunnelCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1cogtunnelCount)
                    if lod2cogtunnelCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2cogtunnelCount)
                    if lod3cogtunnelCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3cogtunnelCount)
                    if lod4cogtunnelCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4cogtunnelCount)
                    tunnelParts = etree.SubElement(mdtunnel, "{%s}tunnelParts" %ns_md)
                    tunnelParts.text = str(cogtunnelpartsCount)
                    tunnelInstallations = etree.SubElement(mdtunnel, "{%s}tunnelInstallations" %ns_md)
                    tunnelInstallations.text = str(cogtunnelinstallationsCount)
                if cogItem == "Bridge":
                    mdbridge = etree.SubElement(mdcogMember, "{%s}MDbridge" %ns_md)
                    featureType = etree.SubElement(mdbridge, "{%s}featureType" %ns_md)
                    featureType.text = "Bridge"
                    featureCount = etree.SubElement(mdbridge, "{%s}featureCount" %ns_md)
                    featureCount.text = str(cogbridgeCount)
                    lods = etree.SubElement(mdbridge, "{%s}LevelsOfDetail" %ns_md)
                    if lod1cogbridgeCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1cogbridgeCount)
                    if lod2cogbridgeCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2cogbridgeCount)
                    if lod3cogbridgeCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3cogbridgeCount)
                    if lod4cogbridgeCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4cogbridgeCount)
                    bridgeParts = etree.SubElement(mdbridge, "{%s}bridgeParts" %ns_md)
                    bridgeParts.text = str(cogbridgepartsCount)
                    bridgeInstallations = etree.SubElement(mdbridge, "{%s}bridgeInstallations" %ns_md)
                    bridgeInstallations.text = str(cogbridgeinstallationsCount)
                    bridgeConstructionElements = etree.SubElement(mdbridge, "{%s}bridgeConstructionElements" %ns_md)
                    bridgeConstructionElements.text = str(cogbridgeconstructionelementsCount)
                if cogItem == "Building":
                    mdbuilding = etree.SubElement(mdcogMember, "{%s}MDbuilding" %ns_md)
                    featureType = etree.SubElement(mdbuilding, "{%s}featureType" %ns_md)
                    featureType.text = "Building"
                    featureCount = etree.SubElement(mdbuilding, "{%s}featureCount" %ns_md)
                    featureCount.text = str(cogbuildingCount)
                    lods = etree.SubElement(mdbuilding, "{%s}LevelsOfDetail" %ns_md)
                    if lod0cogbldgCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod0cogbldgCount)
                    if lod1cogbldgCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1cogbldgCount)
                    if lod2cogbldgCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2cogbldgCount)
                    if lod3cogbldgCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3cogbldgCount)
                    if lod4cogbldgCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4cogbldgCount)
                    buildingParts = etree.SubElement(mdbuilding, "{%s}buildingParts" %ns_md)
                    buildingParts.text = str(cogbuildingpartsCount)
                    buildingInstallations = etree.SubElement(mdbuilding, "{%s}buildingInstallations" %ns_md)
                    buildingInstallations.text = str(cogbuildinginstallationsCount)
                if cogItem == "Relief":   
                    mdrelief = etree.SubElement(mdcogMember, "{%s}MDterrain" %ns_md)
                    featureType = etree.SubElement(mdrelief, "{%s}featureType" %ns_md)
                    featureType.text = "Relief"
                    featureCount = etree.SubElement(mdrelief, "{%s}featureCount" %ns_md)
                    featureCount.text = str(cogtinreliefCount)
                    lods = etree.SubElement(mdrelief, "{%s}LevelsOfDetail" %ns_md)
                    if lod0cogtinreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "0"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod0cogtinreliefCount)
                    if lod1cogtinreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1cogtinreliefCount)
                    if lod2cogtinreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2cogtinreliefCount)
                    if lod3cogtinreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3cogtinreliefCount)
                    if lod4cogtinreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4cogtinreliefCount)
                    terrainType = etree.SubElement(mdrelief, "{%s}terrainType" %ns_md)
                    terrainType.text = "TINRelief"
                    terrainProperties = etree.SubElement(mdrelief, "{%s}TerrainProperties" %ns_md)
                    mdTINRelief = etree.SubElement(terrainProperties, "{%s}MDTINRelief" %ns_md)
                    triangleCount = etree.SubElement(mdTINRelief, "{%s}triangleCount" %ns_md)
                    triangleCount.text = str(cognumberOfTriangles)
                  
    
    lod0total = 0
    lod1total = 0
    lod2total = 0
    lod3total = 0
    lod4total = 0
    
    lod0total = lod0bldgCount + lod0tranCount + lod0waterCount + \
                lod0tinreliefCount + \
                lod0genCount + lod0luseCount + \
                lod0cogbldgCount + lod0cogtranCount + lod0cogwaterCount + \
                lod0coggenCount + lod0cogluseCount
                
    lod1total = lod1bldgCount + lod1bridgeCount + lod1tunnelCount + \
                lod1tranCount + lod1vegCount + lod1waterCount + \
                lod1tinreliefCount  + \
                lod1genCount + lod1cfCount + lod1luseCount + \
                lod1cogbldgCount + lod1cogbridgeCount + lod1cogtunnelCount + \
                lod1cogtranCount + lod1cogvegCount + lod1cogwaterCount + \
                lod1coggenCount + lod1cogcfCount + lod1cogluseCount
                
    lod2total = lod2bldgCount + lod2bridgeCount + lod2tunnelCount+ \
                lod2tranCount + lod2vegCount + lod2waterCount +\
                lod2tinreliefCount + \
                lod2genCount + lod2cfCount + lod2luseCount + \
                lod2cogbldgCount + lod2cogbridgeCount + lod2cogtunnelCount + \
                lod2cogtranCount + lod2cogvegCount  + lod2cogwaterCount + \
                lod2coggenCount + lod2cogcfCount + lod2cogluseCount
                
    lod3total = lod3bldgCount + lod3bridgeCount + lod3tunnelCount + \
                lod3tranCount + lod3vegCount + lod3waterCount + \
                lod3tinreliefCount  + \
                lod3genCount + lod3cfCount + lod3luseCount + \
                lod3cogbldgCount + lod3cogbridgeCount + lod3cogtunnelCount + \
                lod3cogtranCount + lod3cogvegCount + lod3cogwaterCount + \
                lod3coggenCount + lod3cogcfCount + lod3cogluseCount
                
    lod4total = lod4bldgCount + lod4bridgeCount + lod4tunnelCount + \
                lod4tranCount + lod4vegCount +lod4waterCount + \
                lod4tinreliefCount + \
                lod4genCount + lod4cfCount + lod4luseCount + \
                lod4cogbldgCount + lod4cogbridgeCount + lod4cogtunnelCount + \
                lod4cogtranCount + lod4cogvegCount +lod4cogwaterCount + \
                lod4coggenCount + lod4cogcfCount + lod4cogluseCount
                
    
    # LevelsOfDetail
    lods = etree.SubElement(mdcitymodel, "{%s}LevelsOfDetail" %ns_md)
    if lod0total != 0:
        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
        mdlod.text = "0"
        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
        mdlodcount.text = str(lod0total)
    if lod1total != 0:
        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
        mdlod.text = "1"
        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
        mdlodcount.text = str(lod1total)
    if lod2total != 0:
        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
        mdlod.text = "2"
        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
        mdlodcount.text = str(lod2total)
    if lod3total != 0:
        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
        mdlod.text = "3"
        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
        mdlodcount.text = str(lod3total)
    if lod4total != 0:
        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
        mdlod.text = "4"
        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
        mdlodcount.text = str(lod4total)
                
        
    wf = open(outputfile,'wb')
    citygml = etree.tostring(cityModel, pretty_print=True, xml_declaration=True, encoding='UTF-8')
    wf.write(citygml)
    wf.close()

#-------------start of program-------------------#

argparser = argparse.ArgumentParser(description='******* Metadata Generator for 3D City Models *******')
argparser.add_argument('-c', '--citygml', help='CityGML format', required=False)
argparser.add_argument('-i', '--filename', help='CityGML Source input', required=False)
args = vars(argparser.parse_args())

#CityGML source
citygmlsource = args['filename']
citygmlmetadata = argRead(args['citygml'])
if citygmlsource:
    inputfile = str(citygmlsource)

if citygmlmetadata:
    print ("\n ******* Metadata Generation *******")
    print ("\nCityGML input file: ", citygmlsource)

    #--------------Output----------------#

    outputfile = citygmlsource.split(".")[0]+"_metadata.gml"
    print ("\nMetadata output file: ",outputfile)

    start = time.time()
    generatemetadata(inputfile,outputfile)
    end = time.time()
    
    print ("\nTime taken for metadata generation: ",end - start, " sec")