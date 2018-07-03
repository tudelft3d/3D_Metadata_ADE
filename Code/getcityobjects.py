#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:45:54 2018

@author: kavisha
"""
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

def getbuilding(child):
    
    lod0bldgCount = 0
    lod1bldgCount = 0
    lod2bldgCount = 0
    lod3bldgCount = 0
    lod4bldgCount = 0
    buildinginstallationsCount = 0
    buildingpartsCount = 0
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
            
    return [lod0bldgCount, lod1bldgCount, lod2bldgCount, lod3bldgCount, lod4bldgCount, buildinginstallationsCount, buildingpartsCount]


def getbridge(child):
    
    lod1bridgeCount = 0
    lod2bridgeCount = 0
    lod3bridgeCount = 0
    lod4bridgeCount = 0
    bridgeinstallationsCount = 0
    bridgepartsCount = 0
    bridgeconstructionelementsCount = 0
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
            lod2bridgeCount = lod2bridgeCount + 1
        if bb.findall('.//{%s}lod3MultiSurface'  %ns_brid):
            lod3bridgeCount = lod3bridgeCount + 1
        if bb.findall('.//{%s}lod4MultiSurface'  %ns_brid):
            lod4bridgeCount = lod4bridgeCount + 1   
    return [lod1bridgeCount, lod2bridgeCount, lod3bridgeCount, lod4bridgeCount, bridgeinstallationsCount, bridgepartsCount, bridgeconstructionelementsCount]
    
def gettunnel(child):
    
    lod1tunnelCount = 0
    lod2tunnelCount = 0
    lod3tunnelCount = 0
    lod4tunnelCount = 0
    tunnelinstallationsCount = 0
    tunnelpartsCount = 0
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
            
    return [lod1tunnelCount, lod2tunnelCount, lod3tunnelCount, lod4tunnelCount, tunnelinstallationsCount, tunnelpartsCount]
                            
def getwater(child):
    
    lod0waterCount = 0
    lod1waterCount = 0
    lod2waterCount = 0
    lod3waterCount = 0
    lod4waterCount = 0
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
        
    return [lod0waterCount, lod1waterCount, lod2waterCount, lod3waterCount, lod4waterCount]


def gettransport(child):
    
    lod0tranCount = 0 
    lod1tranCount = 0
    lod2tranCount = 0 
    lod3tranCount = 0
    lod4tranCount = 0
    roadCount = 0
    railwayCount = 0
    squareCount = 0
    trackCount = 0
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

    return [lod0tranCount, lod1tranCount, lod2tranCount, lod3tranCount, lod4tranCount, roadCount, railwayCount, squareCount, trackCount]                    


def getgenerics(child):

    lod0genCount = 0
    lod1genCount = 0
    lod2genCount = 0
    lod3genCount = 0
    lod4genCount = 0
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
        
    return [lod0genCount, lod1genCount, lod2genCount, lod3genCount, lod4genCount]


def getveg(child):
    
    lod1vegCount = 0
    lod2vegCount = 0
    lod3vegCount = 0
    lod4vegCount = 0
    svoCount = 0
    plantcoverCount = 0
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

    return [lod1vegCount, lod2vegCount, lod3vegCount, lod4vegCount, svoCount, plantcoverCount]


def getcityfurniture(child):
    
    lod1cfCount = 0
    lod2cfCount = 0
    lod3cfCount = 0
    lod4cfCount = 0
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

    return [lod1cfCount, lod2cfCount, lod3cfCount, lod4cfCount]

def getlanduse(child):
    
    lod0luseCount = 0
    lod1luseCount = 0
    lod2luseCount = 0
    lod3luseCount = 0
    lod4luseCount = 0
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
    
    return [lod0luseCount, lod1luseCount, lod2luseCount, lod3luseCount, lod4luseCount]


def getrelief(child):
    
    lod0tinreliefCount = 0
    lod1tinreliefCount = 0
    lod2tinreliefCount = 0
    lod3tinreliefCount = 0
    lod4tinreliefCount = 0
    numberOfTriangles = 0
    for tr in child.findall('.//{%s}TINRelief'  %ns_dem):
        lodValue = (tr.find('.//{%s}lod' %ns_dem)).text   
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
        triangles = tr.findall('.//{%s}Triangle' %ns_gml)
        numberOfTriangles = numberOfTriangles + (len(triangles))
    
    return [lod0tinreliefCount, lod1tinreliefCount, lod2tinreliefCount, lod3tinreliefCount,lod4tinreliefCount, numberOfTriangles]

     





