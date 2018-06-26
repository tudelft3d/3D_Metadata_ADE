#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:54:40 2018

@author: kavisha
"""

import os
from lxml import etree
import time
import uuid

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# get lod of the cityobject
def getlod(object):
    pass
    
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
        ns="http://www.opengis.net/citygml/1.0"
        ns_gml  = "http://www.opengis.net/gml"
        ns_xAL="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"
        ns_xsi="http://www.w3.org/2001/XMLSchema-instance"
        ns_xlink="http://www.w3.org/1999/xlink"
        ns_dem="http://www.opengis.net/citygml/relief/1.0"
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
        ns_core="http://www.opengis.net/citygml/base/1.0"
        ns_grp="http://www.opengis.net/citygml/cityobjectgroup/2.0"
        ns_md = "http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE"
        schemalocs="http://www.opengis.net/citygml/1.0 http://schemas.opengis.net/citygml/1.0/cityGMLBase.xsd \
        http://www.opengis.net/citygml/building/1.0 http://schemas.opengis.net/citygml/building/1.0/building.xsd \
        http://www.opengis.net/citygml/appearance/1.0 http://schemas.opengis.net/citygml/appearance/1.0/appearance.xsd \
        http://www.opengis.net/citygml/cityfurniture/1.0 http://schemas.opengis.net/citygml/cityfurniture/1.0/cityFurniture.xsd \
        http://www.opengis.net/citygml/waterbody/1.0 http://schemas.opengis.net/citygml/waterbody/1.0/waterBody.xsd \
        http://www.opengis.net/citygml/vegetation/1.0 http://schemas.opengis.net/citygml/vegetation/1.0/vegetation.xsd \
        http://www.opengis.net/citygml/transportation/1.0 http://schemas.opengis.net/citygml/transportation/1.0/transportation.xsd \
        http://www.opengis.net/citygml/texturedsurface/1.0 http://schemas.opengis.net/citygml/texturedsurface/1.0/texturedSurface.xsd \
        http://www.opengis.net/citygml/relief/1.0 http://schemas.opengis.net/citygml/relief/1.0/relief.xsd \
        http://www.opengis.net/citygml/landuse/1.0 http://schemas.opengis.net/citygml/landuse/1.0/landUse.xsd \
        http://www.opengis.net/citygml/generics/1.0 http://schemas.opengis.net/citygml/generics/1.0/generics.xsd \
        http://www.opengis.net/citygml/cityobjectgroup/1.0 http://schemas.opengis.net/citygml/cityobjectgroup/1.0/cityObjectGroup.xsd \
        http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE ../../XSD/3DMD_ADE.xsd" 

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
    rasterreliefCount = 0
    mpreliefCount = 0
    blreliefCount = 0
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
    
    lod0rasterreliefCount = 0
    lod1rasterreliefCount = 0
    lod2rasterreliefCount = 0
    lod3rasterreliefCount = 0
    lod4rasterreliefCount = 0
    
    lod0mpreliefCount = 0
    lod1mpreliefCount = 0
    lod2mpreliefCount = 0
    lod3mpreliefCount = 0
    lod4mpreliefCount = 0
    
    lod0blreliefCount = 0
    lod1blreliefCount = 0
    lod2blreliefCount = 0
    lod3blreliefCount = 0
    lod4blreliefCount = 0
      
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
    
    for obj in root.getiterator('{%s}cityObjectMember'% ns):
        for child in obj.getchildren():
            if child.tag not in thematicModelsSet:
                
                if child.tag == '{%s}Building' %ns_bldg:
                    thematicModelsSet.add("Building")
                    buildingCount = buildingCount + 1
                    if child.findall('.//{%s}BuildingInstallation'  %ns_bldg):
                        buildinginstallationsCount = buildinginstallationsCount + (len(child.findall('.//{%s}BuildingInstallation'  %ns_bldg)))
                    if child.findall('.//{%s}BuildingPart'  %ns_bldg):
                        buildingpartsCount = buildingpartsCount + (len(child.findall('.//{%s}BuildingPart'  %ns_bldg)))
                    if child.findall('{%s}lod0FootPrint'  %ns_bldg) or \
                    child.findall('{%s}lod0RoofEdge'  %ns_bldg):
                        lod0bldgCount = lod0bldgCount + (len(child.findall('{%s}lod0FootPrint'  %ns_bldg)))
                        lod0bldgCount = lod0bldgCount + (len(child.findall('{%s}lod0RoofEdge'  %ns_bldg)))
                    if child.findall('{%s}lod1MultiSurface'  %ns_bldg) or \
                    child.findall('{%s}lod1Solid'  %ns_bldg):
                        lod1bldgCount = lod1bldgCount + (len(child.findall('{%s}lod1MultiSurface'  %ns_bldg)))
                        lod1bldgCount = lod1bldgCount + (len(child.findall('{%s}lod1Solid'  %ns_bldg)))
                    if child.findall('{%s}lod2MultiSurface'  %ns_bldg) or \
                    child.findall('{%s}lod2Solid'  %ns_bldg):
                        lod2bldgCount = lod2bldgCount + (len(child.findall('{%s}lod2MultiSurface'  %ns_bldg)))
                        lod2bldgCount = lod2bldgCount + (len(child.findall('{%s}lod2Solid'  %ns_bldg)))
                    if child.findall('{%s}lod3MultiSurface'  %ns_bldg) or \
                    child.findall('{%s}lod3Solid'  %ns_bldg):
                        lod3bldgCount = lod3bldgCount + (len(child.findall('{%s}lod3MultiSurface'  %ns_bldg)))
                        lod3bldgCount = lod3bldgCount + (len(child.findall('{%s}lod3Solid'  %ns_bldg)))
                    if child.findall('{%s}lod4MultiSurface'  %ns_bldg) or \
                    child.findall('{%s}lod4Solid'  %ns_bldg):
                        lod4bldgCount = lod4bldgCount + (len(child.findall('{%s}lod4MultiSurface'  %ns_bldg)))
                        lod4bldgCount = lod4bldgCount + (len(child.findall('{%s}lod4Solid'  %ns_bldg)))
                    if child.findall('{%s}boundedBy'  %ns_bldg):
                        bb = child.find('{%s}boundedBy'  %ns_bldg)
                        if bb.findall('.//{%s}lod2MultiSurface'  %ns_bldg):
                            lod2bldgCount = lod2bldgCount + 1
                        if bb.findall('.//{%s}lod3MultiSurface'  %ns_bldg):
                            lod3bldgCount = lod3bldgCount + 1
                        if bb.findall('.//{%s}lod4MultiSurface'  %ns_bldg):
                            lod4bldgCount = lod4bldgCount + 1  
                            
                if child.tag == '{%s}Bridge' %ns_brid:
                    thematicModelsSet.add("Bridge") 
                    bridgeCount = bridgeCount + 1
                    if child.findall('.//{%s}BridgeInstallation'  %ns_brid):
                        bridgeinstallationsCount = bridgeinstallationsCount + (len(child.findall('.//{%s}BridgeInstallation'  %ns_brid)))
                    if child.findall('.//{%s}BridgePart'  %ns_brid):
                        bridgepartsCount = bridgepartsCount + (len(child.findall('.//{%s}BridgePart'  %ns_brid)))
                    if child.findall('.//{%s}BridgeConstructionElement'  %ns_brid):
                        bridgeconstructionelementsCount = bridgeconstructionelementsCount + (len(child.findall('.//{%s}BridgeConstructionElement'  %ns_brid)))
                    if child.findall('{%s}lod1MultiSurface'  %ns_brid) or \
                    child.findall('{%s}lod1Solid'  %ns_brid):
                        lod1bridgeCount = lod1bridgeCount + (len(child.findall('{%s}lod1MultiSurface'  %ns_brid)))
                        lod1bridgeCount = lod1bridgeCount + (len(child.findall('{%s}lod1Solid'  %ns_brid)))
                    if child.findall('{%s}lod2MultiSurface'  %ns_brid) or \
                    child.findall('{%s}lod2MultiCurve'  %ns_brid) or \
                    child.findall('{%s}lod2Solid'  %ns_brid):
                        lod2bridgeCount = lod2bridgeCount + (len(child.findall('{%s}lod2MultiSurface'  %ns_brid)))
                        lod2bridgeCount = lod2bridgeCount + (len(child.findall('{%s}lod2MultiCurve'  %ns_brid)))
                        lod2bridgeCount = lod2bridgeCount + (len(child.findall('{%s}lod2Solid'  %ns_brid)))
                    if child.findall('{%s}lod3MultiSurface'  %ns_brid) or \
                    child.findall('{%s}lod3MultiCurve'  %ns_brid) or \
                    child.findall('{%s}lod3Solid'  %ns_brid):
                        lod3bridgeCount = lod3bridgeCount + (len(child.findall('{%s}lod3MultiSurface'  %ns_brid)))
                        lod3bridgeCount = lod3bridgeCount + (len(child.findall('{%s}lod3Solid'  %ns_brid)))
                        lod3bridgeCount = lod3bridgeCount + (len(child.findall('{%s}lod3MultiCurve'  %ns_brid)))
                    if child.findall('{%s}lod4MultiSurface'  %ns_brid) or \
                    child.findall('{%s}lod4MultiCurve'  %ns_brid) or \
                    child.findall('{%s}lod4Solid'  %ns_brid):
                        lod4bridgeCount = lod4bridgeCount + (len(child.findall('{%s}lod4MultiSurface'  %ns_brid)))
                        lod4bridgeCount = lod4bridgeCount + (len(child.findall('{%s}lod4Solid'  %ns_brid)))
                        lod4bridgeCount = lod4bridgeCount + (len(child.findall('{%s}lod4MultiCurve'  %ns_brid)))
                    if child.findall('{%s}boundedBy'  %ns_brid):
                        bb = child.find('{%s}boundedBy'  %ns_brid)
                        if bb.findall('.//{%s}lod2MultiSurface'  %ns_brid):
                            lod2tunnelCount = lod2tunnelCount + 1
                        if bb.findall('.//{%s}lod3MultiSurface'  %ns_brid):
                            lod3tunnelCount = lod3tunnelCount + 1
                        if bb.findall('.//{%s}lod4MultiSurface'  %ns_brid):
                            lod4tunnelCount = lod4tunnelCount + 1   
                    
                if child.tag == '{%s}Tunnel' %ns_tun:
                    thematicModelsSet.add("Tunnel")
                    tunnelCount = tunnelCount + 1
                    if child.findall('.//{%s}TunnelInstallation'  %ns_tun):
                        tunnelinstallationsCount = tunnelinstallationsCount + (len(child.findall('.//{%s}TunnelInstallation'  %ns_tun)))
                    if child.findall('.//{%s}TunnelPart'  %ns_tun):
                        tunnelpartsCount = tunnelpartsCount + (len(child.findall('.//{%s}TunnelPart'  %ns_tun)))
                    if child.findall('{%s}lod1MultiSurface'  %ns_tun) or \
                    child.findall('{%s}lod1Solid'  %ns_tun):
                        lod1tunnelCount = lod1tunnelCount + (len(child.findall('{%s}lod1MultiSurface'  %ns_tun)))
                        lod1tunnelCount = lod1tunnelCount + (len(child.findall('{%s}lod1Solid'  %ns_tun)))
                    if child.findall('{%s}lod2MultiSurface'  %ns_brid) or \
                    child.findall('{%s}lod2MultiCurve'  %ns_tun) or \
                    child.findall('{%s}lod2Solid'  %ns_tun):
                        lod2tunnelCount = lod2tunnelCount + (len(child.findall('{%s}lod2MultiSurface'  %ns_tun)))
                        lod2tunnelCount = lod2tunnelCount + (len(child.findall('{%s}lod2MultiCurve'  %ns_tun)))
                        lod2tunnelCount = lod2tunnelCount + (len(child.findall('{%s}lod2Solid'  %ns_tun)))
                    if child.find('{%s}lod3MultiSurface'  %ns_tun) or \
                    child.find('{%s}lod3MultiCurve'  %ns_tun) or \
                    child.find('{%s}lod3Solid'  %ns_tun):
                        print ("found")
                        lod3tunnelCount = lod3tunnelCount + (len(child.findall('{%s}lod3MultiSurface'  %ns_tun)))
                        lod3tunnelCount = lod3tunnelCount + (len(child.findall('{%s}lod3Solid'  %ns_tun)))
                        lod3tunnelCount = lod3tunnelCount + (len(child.findall('{%s}lod3MultiCurve'  %ns_tun)))
                    if child.findall('{%s}lod4MultiSurface'  %ns_tun) or \
                    child.findall('{%s}lod4MultiCurve'  %ns_tun) or \
                    child.findall('{%s}lod4Solid'  %ns_tun):
                        lod4tunnelCount = lod4tunnelCount + (len(child.findall('{%s}lod4MultiSurface'  %ns_tun)))
                        lod4tunnelCount = lod4tunnelCount + (len(child.findall('{%s}lod4Solid'  %ns_tun)))
                        lod4tunnelCount = lod4tunnelCount + (len(child.findall('{%s}lod4MultiCurve'  %ns_tun)))
                    if child.findall('{%s}boundedBy'  %ns_tun):
                        bb = child.find('{%s}boundedBy'  %ns_tun)
                        if bb.findall('.//{%s}lod2MultiSurface'  %ns_tun):
                            lod2tunnelCount = lod2tunnelCount + 1
                        if bb.findall('.//{%s}lod3MultiSurface'  %ns_tun):
                            lod3tunnelCount = lod3tunnelCount + 1
                        if bb.findall('.//{%s}lod4MultiSurface'  %ns_tun):
                            lod4tunnelCount = lod4tunnelCount + 1    
                
                if child.tag == '{%s}SolitaryVegetationObject' %ns_veg or \
                child.tag == '{%s}PlantCover' %ns_veg:
                    thematicModelsSet.add("Vegetation")
                    vegCount = vegCount + 1
                    if child.tag == '{%s}SolitaryVegetationObject' %ns_veg:
                        svoCount = svoCount + 1
                    if child.tag == '{%s}PlantCover' %ns_veg:
                        plantcoverCount = plantcoverCount + 1
                    
                    if child.findall('{%s}lod1Geometry'  %ns_veg) or \
                    child.findall('{%s}lod1ImplicitRepresentation'  %ns_veg) or \
                    child.findall('{%s}lod1MultiSurface'  %ns_veg) or \
                    child.findall('{%s}lod1MultiSolid'  %ns_veg):
                        lod1vegCount = lod1vegCount + (len(child.findall('{%s}lod1Geometry'  %ns_veg)))
                        lod1vegCount = lod1vegCount + (len(child.findall('{%s}lod1ImplicitRepresentation'  %ns_veg)))
                        lod1vegCount = lod1vegCount + (len(child.findall('{%s}lod1MultiSurface'  %ns_veg)))
                        lod1vegCount = lod1vegCount + (len(child.findall('{%s}lod1MultiSolid'  %ns_veg)))
                    if child.findall('{%s}lod2Geometry'  %ns_veg) or \
                    child.findall('{%s}lod2ImplicitRepresentation'  %ns_veg) or \
                    child.findall('{%s}lod2MultiSurface'  %ns_veg) or \
                    child.findall('{%s}lod2MultiSolid'  %ns_veg):
                        lod2vegCount = lod2vegCount + (len(child.findall('{%s}lod2Geometry'  %ns_veg)))
                        lod2vegCount = lod2vegCount + (len(child.findall('{%s}lod2ImplicitRepresentation'  %ns_veg)))
                        lod2vegCount = lod2vegCount + (len(child.findall('{%s}lod2MultiSurface'  %ns_veg)))
                        lod2vegCount = lod2vegCount + (len(child.findall('{%s}lod2MultiSolid'  %ns_veg)))
                    if child.findall('{%s}lod3Geometry'  %ns_veg) or \
                    child.findall('{%s}lod3ImplicitRepresentation'  %ns_veg) or \
                    child.findall('{%s}lod3MultiSurface'  %ns_veg) or \
                    child.findall('{%s}lod3MultiSolid'  %ns_veg):
                        lod3vegCount = lod3vegCount + (len(child.findall('{%s}lod3Geometry'  %ns_veg)))
                        lod3vegCount = lod3vegCount + (len(child.findall('{%s}lod3ImplicitRepresentation'  %ns_veg)))
                        lod3vegCount = lod3vegCount + (len(child.findall('{%s}lod3MultiSurface'  %ns_veg)))
                        lod3vegCount = lod3vegCount + (len(child.findall('{%s}lod3MultiSolid'  %ns_veg)))
                    if child.findall('{%s}lod4Geometry'  %ns_veg) or \
                    child.findall('{%s}lod4ImplicitRepresentation'  %ns_veg) or \
                    child.findall('{%s}lod4MultiSurface'  %ns_veg) or \
                    child.findall('{%s}lod4MultiSolid'  %ns_veg):
                        lod4vegCount = lod4vegCount + (len(child.findall('{%s}lod4Geometry'  %ns_veg)))
                        lod4vegCount = lod4vegCount + (len(child.findall('{%s}lod4ImplicitRepresentation'  %ns_veg)))
                        lod4vegCount = lod4vegCount + (len(child.findall('{%s}lod4MultiSurface'  %ns_veg)))
                        lod4vegCount = lod4vegCount + (len(child.findall('{%s}lod4MultiSolid'  %ns_veg)))                        
                    
                if child.tag == '{%s}WaterBody' %ns_wtr:
                    thematicModelsSet.add("WaterBody")
                    waterCount = waterCount + 1
                    if child.findall('{%s}lod0MultiSurface'  %ns_wtr) or \
                    child.findall('{%s}lod0MultiCurve'  %ns_wtr):
                        lod0waterCount = lod0waterCount + (len(child.findall('{%s}lod0MultiSurface'  %ns_wtr)))
                        lod0waterCount = lod0waterCount + (len(child.findall('{%s}lod0MultiCurve'  %ns_wtr)))
                    if child.findall('{%s}lod1MultiSurface'  %ns_wtr) or \
                    child.findall('{%s}lod1MultiCurve'  %ns_wtr) or \
                    child.findall('{%s}lod1Solid'  %ns_wtr):
                        lod1waterCount = lod1waterCount + (len(child.findall('{%s}lod1MultiSurface'  %ns_wtr)))
                        lod1waterCount = lod1waterCount + (len(child.findall('{%s}lod1Solid'  %ns_wtr)))
                        lod1waterCount = lod1waterCount + (len(child.findall('{%s}lod1MultiCurve'  %ns_wtr)))
                    if child.findall('{%s}lod2Solid'  %ns_wtr):
                        lod2waterCount = lod2waterCount + (len(child.findall('{%s}lod2Solid'  %ns_wtr)))
                    if child.findall('{%s}lod3Solid'  %ns_wtr):
                        lod3waterCount = lod3waterCount + (len(child.findall('{%s}lod3Solid'  %ns_wtr)))
                    if child.findall('{%s}lod4Solid'  %ns_wtr):
                        lod4waterCount = lod4waterCount + (len(child.findall('{%s}lod4Solid'  %ns_wtr)))
                    if child.findall('{%s}boundedBy'  %ns_wtr):
                        bb = child.find('{%s}boundedBy'  %ns_wtr)
                        if bb.findall('.//{%s}lod2Surface'  %ns_wtr):
                            lod2waterCount = lod2waterCount + 1
                        if bb.findall('.//{%s}lod3Surface'  %ns_wtr):
                            lod3waterCount = lod3waterCount + 1
                        if bb.findall('.//{%s}lod4Surface'  %ns_wtr):
                            lod4waterCount = lod4waterCount + 1 
                    
                if child.tag == '{%s}ReliefFeature' %ns_dem:
                    if child.findall('.//{%s}TINRelief'  %ns_dem):
                        thematicModelsSet.add("Relief")
                        terrainTypeSet.add("TINRelief")
                        tinreliefCount = tinreliefCount + 1
                        for tr in child.findall('.//{%s}TINRelief'  %ns_dem):
                            lodValue = (tr.find('.//{%s}lod' %ns_dem)).text
                            print (lodValue)    
                            if lodValue == "0":
                                lod0tinreliefCount = lod0tinreliefCount + 1
                            if lodValue == "1":
                                lod1tinreliefCount = lod1tinreliefCount + 1
                            if lodValue == "2":
                                lod2tinreliefCount = lod2tinreliefCount + 1
                            if lodValue == "3":
                                lod3tinreliefCount = lod3tinreliefCount + 1
                            if lodValue == "4":
                                lod4tinreliefCount = lod4tinreliefCount + 1
                            
                    if child.findall('.//{%s}RasterRelief'  %ns_dem):
                        thematicModelsSet.add("Relief")
                        rasterreliefCount = rasterreliefCount + 1
                        terrainTypeSet.add("RasterRelief")
                        rasterreliefCount = rasterreliefCount + 1
                        for tr in child.findall('.//{%s}RasterRelief'  %ns_dem):
                            lodValue = (tr.find('.//{%s}lod' %ns_dem)).text
                            print (lodValue)    
                            if lodValue == "0":
                                lod0rasterreliefCount = lod0rasterreliefCount + 1
                            if lodValue == "1":
                                lod1rasterreliefCount = lod1rasterreliefCount + 1
                            if lodValue == "2":
                                lod2rasterreliefCount = lod2rasterreliefCount + 1
                            if lodValue == "3":
                                lod3rasterreliefCount = lod3rasterreliefCount + 1
                            if lodValue == "4":
                                lod4rasterreliefCount = lod4rasterreliefCount + 1
                            
                    if child.findall('.//{%s}MassPointRelief'  %ns_dem):
                        thematicModelsSet.add("Relief")
                        mpreliefCount = mpreliefCount + 1
                        terrainTypeSet.add("MassPointRelief")
                        mpreliefCount = mpreliefCount + 1
                        for tr in child.findall('.//{%s}MassPointRelief'  %ns_dem):
                            lodValue = (tr.find('.//{%s}lod' %ns_dem)).text
                            print (lodValue)    
                            if lodValue == "0":
                                lod0mpreliefCount = lod0mpreliefCount + 1
                            if lodValue == "1":
                                lod1mpreliefCount = lod1mpreliefCount + 1
                            if lodValue == "2":
                                lod2mpreliefCount = lod2mpreliefCount + 1
                            if lodValue == "3":
                                lod3mpreliefCount = lod3mpreliefCount + 1
                            if lodValue == "4":
                                lod4mpreliefCount = lod4mpreliefCount + 1
                            
                    if child.findall('.//{%s}BreaklineRelief'  %ns_dem):
                        thematicModelsSet.add("Relief")
                        blreliefCount = blreliefCount + 1
                        terrainTypeSet.add("BreaklineRelief")
                        tinreliefCount = tinreliefCount + 1
                        for tr in child.findall('.//{%s}BreaklineRelief'  %ns_dem):
                            lodValue = (tr.find('.//{%s}lod' %ns_dem)).text
                            print (lodValue)    
                            if lodValue == "0":
                                lod0blreliefCount = lod0blreliefCount + 1
                            if lodValue == "1":
                                lod1blreliefCount = lod1blreliefCount + 1
                            if lodValue == "2":
                                lod2blreliefCount = lod2blreliefCount + 1
                            if lodValue == "3":
                                lod3blreliefCount = lod3blreliefCount + 1
                            if lodValue == "4":
                                lod4blreliefCount = lod4blreliefCount + 1
                            
                    
                if child.tag == '{%s}Road' %ns_tran or \
                child.tag == '{%s}Railway' %ns_tran or \
                child.tag == '{%s}Square' %ns_tran or \
                child.tag == '{%s}Track' %ns_tran:
                    thematicModelsSet.add("Transportation")
                    transportationCount = transportationCount + 1
                    if child.tag == '{%s}Road'  %ns_tran:
                        roadCount = roadCount + 1
                    if child.tag == '{%s}Railway' %ns_tran:
                        railwayCount = railwayCount + 1
                    if child.tag == '{%s}Square'  %ns_tran:
                        squareCount = squareCount + 1
                    if child.tag == '{%s}Track'  %ns_tran:
                        trackCount = trackCount + 1
                    if child.findall('{%s}lod0Network'  %ns_tran):
                        lod0tranCount = lod0tranCount + (len(child.findall('{%s}lod0Network'  %ns_tran)))
                    if child.findall('{%s}lod1MultiSurface'  %ns_tran):
                        lod1tranCount = lod1tranCount + (len(child.findall('{%s}lod1MultiSurface'  %ns_tran)))
                    if child.findall('{%s}lod2MultiSurface'  %ns_tran):
                        lod2tranCount = lod2tranCount + (len(child.findall('{%s}lod2MultiSurface'  %ns_tran)))
                    if child.findall('{%s}lod3MultiSurface'  %ns_tran):
                        lod3tranCount = lod3tranCount + (len(child.findall('{%s}lod3MultiSurface'  %ns_tran)))
                    if child.findall('{%s}lod4MultiSurface'  %ns_tran):
                        lod4tranCount = lod4tranCount + (len(child.findall('{%s}lod4MultiSurface'  %ns_tran)))
                    
                    
                if child.tag == '{%s}GenericCityObject' %ns_gen:                  
                    thematicModelsSet.add("Generics")
                    genericsCount = genericsCount + 1
                    if child.findall('{%s}lod0Geometry'  %ns_gen) or \
                    child.findall('{%s}lod0ImplicitRepresentation'  %ns_gen) or \
                    child.findall('{%s}lod0TerrainIntersection'  %ns_gen):
                        lod0genCount = lod0genCount + (len(child.findall('{%s}lod1Geometry'  %ns_gen)))
                        lod0genCount = lod0genCount + (len(child.findall('{%s}lod1ImplicitRepresentation'  %ns_gen)))
                        lod0genCount = lod0genCount + (len(child.findall('{%s}lod1TerrainIntersection'  %ns_frn)))    
                    if child.findall('{%s}lod1Geometry'  %ns_gen) or \
                    child.findall('{%s}lod1ImplicitRepresentation'  %ns_gen) or \
                    child.findall('{%s}lod1TerrainIntersection'  %ns_gen):
                        lod1genCount = lod1genCount + (len(child.findall('{%s}lod1Geometry'  %ns_gen)))
                        lod1genCount = lod1genCount + (len(child.findall('{%s}lod1ImplicitRepresentation'  %ns_gen)))
                        lod1genCount = lod1genCount + (len(child.findall('{%s}lod1TerrainIntersection'  %ns_frn)))
                    if child.findall('{%s}lod2Geometry'  %ns_gen) or \
                    child.findall('{%s}lod2ImplicitRepresentation'  %ns_gen) or \
                    child.findall('{%s}lod2TerrainIntersection'  %ns_gen):
                        lod2genCount = lod2genCount + (len(child.findall('{%s}lod2Geometry'  %ns_gen)))
                        lod2genCount = lod2genCount + (len(child.findall('{%s}lod2ImplicitRepresentation'  %ns_gen)))
                        lod2genCount = lod2genCount + (len(child.findall('{%s}lod2TerrainIntersection'  %ns_gen)))
                    if child.findall('{%s}lod3Geometry'  %ns_gen) or \
                    child.findall('{%s}lod3ImplicitRepresentation'  %ns_gen) or \
                    child.findall('{%s}lod3TerrainIntersection'  %ns_gen):
                        lod3genCount = lod3genCount + (len(child.findall('{%s}lod3Geometry'  %ns_gen)))
                        lod3genCount = lod3genCount + (len(child.findall('{%s}lod3ImplicitRepresentation'  %ns_gen)))
                        lod3genCount = lod3genCount + (len(child.findall('{%s}lod3TerrainIntersection'  %ns_gen)))
                    if child.findall('{%s}lod4Geometry'  %ns_gen) or \
                    child.findall('{%s}lod4ImplicitRepresentation'  %ns_gen) or \
                    child.findall('{%s}lod4TerrainIntersection'  %ns_gen):
                        lod4genCount = lod4genCount + (len(child.findall('{%s}lod4Geometry'  %ns_gen)))
                        lod4genCount = lod4genCount + (len(child.findall('{%s}lod4ImplicitRepresentation'  %ns_gen)))
                        lod4genCount = lod4genCount + (len(child.findall('{%s}lod4TerrainIntersection'  %ns_gen)))
                    
                    
                if child.tag == '{%s}CityFurniture' %ns_frn:                
                    thematicModelsSet.add("CityFurniture")
                    cityfurnitureCount = cityfurnitureCount + 1
                    if child.findall('.//{%s}lod1Geometry'  %ns_frn) or \
                    child.findall('.//{%s}lod1ImplicitRepresentation'  %ns_frn) or \
                    child.findall('.//{%s}lod1TerrainIntersection'  %ns_frn):
                        lod1cfCount = lod1cfCount + (len(child.findall('.//{%s}lod1Geometry'  %ns_frn)))
                        lod1cfCount = lod1cfCount + (len(child.findall('.//{%s}lod1ImplicitRepresentation'  %ns_frn)))
                        lod1cfCount = lod1cfCount + (len(child.findall('.//{%s}lod1TerrainIntersection'  %ns_frn)))
                    if child.findall('.//{%s}lod2Geometry'  %ns_frn) or \
                    child.findall('.//{%s}lod2ImplicitRepresentation'  %ns_frn) or \
                    child.findall('.//{%s}lod2TerrainIntersection'  %ns_frn):
                        lod2cfCount = lod2cfCount + (len(child.findall('.//{%s}lod2Geometry'  %ns_frn)))
                        lod2cfCount = lod2cfCount + (len(child.findall('.//{%s}lod2ImplicitRepresentation'  %ns_frn)))
                        lod2cfCount = lod2cfCount + (len(child.findall('.//{%s}lod2TerrainIntersection'  %ns_frn)))
                    if child.findall('.//{%s}lod3Geometry'  %ns_frn) or \
                    child.findall('.//{%s}lod3ImplicitRepresentation'  %ns_frn) or \
                    child.findall('.//{%s}lod3TerrainIntersection'  %ns_frn):
                        lod3cfCount = lod3cfCount + (len(child.findall('.//{%s}lod3Geometry'  %ns_frn)))
                        lod3cfCount = lod3cfCount + (len(child.findall('.//{%s}lod3ImplicitRepresentation'  %ns_frn)))
                        lod3cfCount = lod3cfCount + (len(child.findall('.//{%s}lod3TerrainIntersection'  %ns_frn)))
                    if child.findall('.//{%s}lod4Geometry'  %ns_frn) or \
                    child.findall('.//{%s}lod4ImplicitRepresentation'  %ns_frn) or \
                    child.findall('.//{%s}lod4TerrainIntersection'  %ns_frn):
                        lod4cfCount = lod4cfCount + (len(child.findall('.//{%s}lod4Geometry'  %ns_frn)))
                        lod4cfCount = lod4cfCount + (len(child.findall('.//{%s}lod4ImplicitRepresentation'  %ns_frn)))
                        lod4cfCount = lod4cfCount + (len(child.findall('.//{%s}lod4TerrainIntersection'  %ns_frn)))
                    
                if child.tag == '{%s}CityObjectGroup' %ns_grp:                
                    thematicModelsSet.add("CityObjectGroup")
                    cityobjectgroupCount = cityobjectgroupCount + 1
                    
                if child.tag == '{%s}LandUse' %ns_luse:               
                    thematicModelsSet.add("LandUse")
                    landuseCount = landuseCount + 1
                    if child.findall('.//{%s}lod0MultiSurface'  %ns_luse):
                        lod0luseCount = lod0luseCount + (len(child.findall('.//{%s}lod0MultiSurface'  %ns_luse)))
                    if child.findall('.//{%s}lod1MultiSurface'  %ns_luse):
                        lod1luseCount = lod1luseCount + (len(child.findall('.//{%s}lod1MultiSurface'  %ns_luse)))
                    if child.findall('.//{%s}lod2MultiSurface'  %ns_luse):
                        lod2luseCount = lod2luseCount + (len(child.findall('.//{%s}lod2MultiSurface'  %ns_luse)))
                    if child.findall('.//{%s}lod3MultiSurface'  %ns_luse):
                        lod3luseCount = lod3luseCount + (len(child.findall('.//{%s}lod3MultiSurface'  %ns_luse)))
                    if child.findall('.//{%s}lod4MultiSurface'  %ns_luse):
                        lod4luseCount = lod4luseCount + (len(child.findall('.//{%s}lod4MultiSurface'  %ns_luse)))
                    
    
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
                    triangleCount.text = "100"
                if terrainItem == "RasterRelief":
                    mdrelief = etree.SubElement(mdCityfeatures, "{%s}MDterrain" %ns_md)
                    featureType = etree.SubElement(mdrelief, "{%s}featureType" %ns_md)
                    featureType.text = "Relief"
                    featureCount = etree.SubElement(mdrelief, "{%s}featureCount" %ns_md)
                    featureCount.text = str(tinreliefCount)
                    lods = etree.SubElement(mdrelief, "{%s}LevelsOfDetail" %ns_md)
                    if lod0rasterreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "0"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod0rasterreliefCount)
                    if lod1rasterreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1rasterreliefCount)
                    if lod2rasterreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2rasterreliefCount)
                    if lod3rasterreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3rasterreliefCount)
                    if lod4rasterreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4rasterreliefCount)
                    terrainType = etree.SubElement(mdrelief, "{%s}terrainType" %ns_md)
                    terrainType.text = "RasterRelief"
#                    terrainProperties = etree.SubElement(mdrelief, "{%s}TerrainProperties" %ns_md)
#                    mdRasterRelief = etree.SubElement(terrainProperties, "{%s}MDRasterRelief" %ns_md)
#                    extent = etree.SubElement(mdRasterRelief, "{%s}extent" %ns_md)
#                    resolution = etree.SubElement(mdRasterRelief, "{%s}resolution" %ns_md)
#                    resolution.attrib['uom'] = "cm"
#                    resolution.text = ""
                if terrainItem == "MassPointRelief":
                    mdrelief = etree.SubElement(mdCityfeatures, "{%s}MDterrain" %ns_md)
                    featureType = etree.SubElement(mdrelief, "{%s}featureType" %ns_md)
                    featureType.text = "Relief"
                    featureCount = etree.SubElement(mdrelief, "{%s}featureCount" %ns_md)
                    featureCount.text = str(tinreliefCount)
                    lods = etree.SubElement(mdrelief, "{%s}LevelsOfDetail" %ns_md)
                    if lod0mpreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "0"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod0mpreliefCount)
                    if lod1mpreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1mpreliefCount)
                    if lod2mpreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2mpreliefCount)
                    if lod3mpreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3mpreliefCount)
                    if lod4mpreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4mpreliefCount)
                    terrainType = etree.SubElement(mdrelief, "{%s}terrainType" %ns_md)
                    terrainType.text = "MassPointRelief"
#                    terrainProperties = etree.SubElement(mdrelief, "{%s}TerrainProperties" %ns_md)
#                    mdMasspointRelief = etree.SubElement(terrainProperties, "{%s}MDMasspointRelief" %ns_md)
#                    pointCount = etree.SubElement(mdMasspointRelief, "{%s}pointCount" %ns_md)
#                    pointCount.text = "1000"
                if terrainItem == "BreaklineRelief":
                    mdrelief = etree.SubElement(mdCityfeatures, "{%s}MDterrain" %ns_md)
                    featureType = etree.SubElement(mdrelief, "{%s}featureType" %ns_md)
                    featureType.text = "Relief"
                    featureCount = etree.SubElement(mdrelief, "{%s}featureCount" %ns_md)
                    featureCount.text = str(tinreliefCount)
                    lods = etree.SubElement(mdrelief, "{%s}LevelsOfDetail" %ns_md)
                    if lod0blreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "0"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod0blreliefCount)
                    if lod1blreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "1"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod1blreliefCount)
                    if lod2blreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "2"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod2blreliefCount)
                    if lod3blreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "3"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod3blreliefCount)
                    if lod4blreliefCount != 0:
                        lod = etree.SubElement(lods, "{%s}LevelOfDetail" %ns_md)
                        mdlod = etree.SubElement(lod, "{%s}lod" %ns_md)
                        mdlod.text = "4"
                        mdlodcount = etree.SubElement(lod, "{%s}objectCount" %ns_md)
                        mdlodcount.text = str(lod4blreliefCount)
                    terrainType = etree.SubElement(mdrelief, "{%s}terrainType" %ns_md)
                    terrainType.text = "MassPointRelief"
#                    terrainProperties = etree.SubElement(mdrelief, "{%s}TerrainProperties" %ns_md)
#                    mdBreaklineRelief = etree.SubElement(terrainProperties, "{%s}MDBreaklineRelief" %ns_md)
#                    lineCount = etree.SubElement(mdBreaklineRelief, "{%s}pointCount" %ns_md)
#                    lineCount.text = "1000"
                    
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
            
        if item == "CityObjectGroup":
            mdcityobjectgroup = etree.SubElement(mdCityfeatures, "{%s}MDcityObjectGroup" %ns_md)
            featureType = etree.SubElement(mdcityobjectgroup, "{%s}featureType" %ns_md)
            featureType.text = "CityObjectGroup"
            featureCount = etree.SubElement(mdcityobjectgroup, "{%s}featureCount" %ns_md)
            featureCount.text = str(cityobjectgroupCount)
            
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
            
    lod0total = 0
    lod1total = 0
    lod2total = 0
    lod3total = 0
    lod4total = 0
    
    lod0total = lod0bldgCount + lod0tranCount + lod0waterCount + \
                lod0tinreliefCount + lod0rasterreliefCount + lod0blreliefCount + lod0mpreliefCount + \
                lod0genCount + lod0luseCount
    lod1total = lod1bldgCount + lod1bridgeCount + lod1tunnelCount + \
                lod1tranCount + lod1vegCount + lod1waterCount + \
                lod1tinreliefCount + lod1rasterreliefCount + lod1blreliefCount + lod1mpreliefCount + \
                lod1genCount + lod1cfCount + lod1luseCount
    lod2total = lod2bldgCount + lod2bridgeCount + lod2tunnelCount+ \
                lod2tranCount + lod2vegCount + lod2waterCount +\
                lod2tinreliefCount + lod2rasterreliefCount + lod2blreliefCount + lod2mpreliefCount + \
                lod2genCount + lod2cfCount + lod2luseCount
    lod3total = lod3bldgCount + lod3bridgeCount + lod3tunnelCount + \
                lod3tranCount + lod3vegCount + lod3waterCount + \
                lod3tinreliefCount + lod3rasterreliefCount + lod3blreliefCount + lod3mpreliefCount + \
                lod3genCount + lod3cfCount + lod3luseCount
    lod4total = lod4bldgCount + lod4bridgeCount + lod4tunnelCount + \
                lod4tranCount + lod4vegCount +lod4waterCount + \
                lod4tinreliefCount + lod4rasterreliefCount + lod4blreliefCount + lod4mpreliefCount + \
                lod4genCount + lod4cfCount + lod4luseCount
    
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

#CityGML source
print ("\n ******* Metadata Generation *******")
citygml_src = "citygmldatasets/Part-6-Generics-V1.gml"
script_dir = os.path.dirname(__file__)
abs_file_path = os.path.join(script_dir, citygml_src)
print ("\nCityGML input file: ", citygml_src)

#tree = etree.parse(abs_file_path)
#root = tree.getroot()


#--------------Output----------------#

metadata_dump = citygml_src.split(".")[0]+"_metadata.gml"
print ("\nMetadata output file: ",metadata_dump)
outputfile = os.path.join(script_dir, metadata_dump)
start = time.time()
generatemetadata(abs_file_path,outputfile)
end = time.time()
print ("\nTime taken for metadata generation: ",end - start, " sec")