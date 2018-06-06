<?xml version="1.0" encoding="UTF-8"?>

<CityModel 
    xmlns:app="http://www.opengis.net/citygml/appearance/2.0" 
    xmlns:bldg="http://www.opengis.net/citygml/building/2.0" 
    xmlns:dem="http://www.opengis.net/citygml/relief/2.0" 
    xmlns:gen="http://www.opengis.net/citygml/generics/2.0" 
    xmlns:gml="http://www.opengis.net/gml" 
    xmlns:wtr="http://www.opengis.net/citygml/waterbody/2.0" 
    xmlns:xAL="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0" 
    xmlns:xlink="http://www.w3.org/1999/xlink" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns="http://www.opengis.net/citygml/2.0" 
    xmlns:md="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE"
    xsi:schemaLocation="http://www.opengis.net/citygml/2.0 http://schemas.opengis.net/citygml/2.0/cityGMLBase.xsd         
    http://www.opengis.net/citygml/building/2.0 http://schemas.opengis.net/citygml/building/2.0/building.xsd         
    http://www.opengis.net/citygml/appearance/2.0 http://schemas.opengis.net/citygml/appearance/2.0/appearance.xsd         
    http://www.opengis.net/citygml/bridge/2.0 http://schemas.opengis.net/citygml/bridge/2.0/bridge.xsd         
    http://www.opengis.net/citygml/cityfurniture/2.0 http://schemas.opengis.net/citygml/cityfurniture/2.0/cityFurniture.xsd         
    http://www.opengis.net/citygml/waterbody/2.0 http://schemas.opengis.net/citygml/waterbody/2.0/waterBody.xsd         
    http://www.opengis.net/citygml/tunnel/2.0 http://schemas.opengis.net/citygml/tunnel/2.0/tunnel.xsd         
    http://www.opengis.net/citygml/vegetation/2.0 http://schemas.opengis.net/citygml/vegetation/2.0/vegetation.xsd         
    http://www.opengis.net/citygml/transportation/2.0 http://schemas.opengis.net/citygml/transportation/2.0/transportation.xsd
    http://www.opengis.net/citygml/texturedsurface/2.0 http://schemas.opengis.net/citygml/texturedsurface/2.0/texturedSurface.xsd
    http://www.opengis.net/citygml/relief/2.0 http://schemas.opengis.net/citygml/relief/2.0/relief.xsd         
    http://www.opengis.net/citygml/landuse/2.0 http://schemas.opengis.net/citygml/landuse/2.0/landUse.xsd         
    http://www.opengis.net/citygml/generics/2.0 http://schemas.opengis.net/citygml/generics/2.0/generics.xsd         
    http://www.opengis.net/citygml/cityobjectgroup/2.0 http://schemas.opengis.net/citygml/cityobjectgroup/2.0/cityObjectGroup.xsd
    http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE ../XSD/3DMD_ADE.xsd">

    <gml:name>LOD1_451304</gml:name>
    <gml:boundedBy>
        <gml:Envelope srsName="urn:ogc:def:crs,crs:EPSG:6.12:31466,crs:EPSG:6.12:5783">
            <gml:pos srsDimension="3">3423800.0 5705800.0 140.4</gml:pos>
            <gml:pos srsDimension="3">3426200.0 5708200.0 252.6</gml:pos>
        </gml:Envelope>
    </gml:boundedBy>
    
    
    <cityObjectMember>
        <md:MDcitymodel>
            <md:citymodelIdentifier>MM_12345</md:citymodelIdentifier>
            <md:ISOmetadata>
                <md:ISOidentifier>
                    <md:datasetTitle>3D City Model</md:datasetTitle>
                    <md:datasetReferenceDate>2017-01-01</md:datasetReferenceDate>
                    <md:geoLocation>Delft</md:geoLocation>
                    <md:datasetLanguage>English</md:datasetLanguage>
                    <md:datasetTopicCategory 
                        codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE//codelists/MDtopicCategory.xml">
                        geoscientificInformation
                    </md:datasetTopicCategory>
                    <md:datasetDescription>Metadata associated with the 3D city model</md:datasetDescription>
                    <md:distributionFormatVersion>CityGML 2.0</md:distributionFormatVersion>
                    <md:spatialRepresentationType 
                        codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/MDspatialRepTypeCode.xml">
                        Vector
                    </md:spatialRepresentationType>
                    <md:referenceSystem>urn:ogc:def:crs,crs:EPSG:6.12:31466,crs:EPSG:6.12:5783</md:referenceSystem>
                    <md:temporalInformation>2017-01-02</md:temporalInformation>
                    <md:onlineResource>https://3d.bk.tudelft.nl/opendata/3dfier/</md:onlineResource>
                    <md:fileIdentifier>Sample01.xml</md:fileIdentifier>
                    <md:metadataStandard>ISO 19115</md:metadataStandard>
                    <md:metadataStandardVersion>v01</md:metadataStandardVersion>
                    <md:metadataLanguage>English</md:metadataLanguage>
                    <md:metadataCharacterSet>UTF-8</md:metadataCharacterSet>
                    <md:metadataPointOfContact>
                        <md:OrganizationalContact>
                            <md:contactName>3D Geoinformation Group</md:contactName>
                            <md:phone>+31 666666666</md:phone>
                            <md:address>Julianalaan 134, 2628 BL, TU Delft</md:address>
                            <md:emailAddress>3dtud@tudelft.nl</md:emailAddress>
                            <md:website>https://3d.bk.tudelft.nl</md:website>
                        </md:OrganizationalContact>
                    </md:metadataPointOfContact>
                    <md:metadataDateStamp>2017-02-01</md:metadataDateStamp>
                    <md:lineage>
                        <md:Lineage>
                            <md:source>Point cloud</md:source>
                            <md:processStep>3Dfier processing</md:processStep>
                        </md:Lineage>
                    </md:lineage>
                    <md:boundingBox3D>
                        <gml:Envelope>
                            <gml:lowerCorner>3423800.0 5705800.0 140.4</gml:lowerCorner>
                            <gml:upperCorner>3426200.0 5708200.0 252.6</gml:upperCorner>
                        </gml:Envelope>
                    </md:boundingBox3D>
                    <md:abstract>Metadata associated with the 3D city model</md:abstract>
                    <md:specificUsage>Geoinformation model</md:specificUsage>
                    <md:keywords>3D CityGML, 3D Metadata</md:keywords>
                    <md:constraints>
                        <md:ConstraintsOnUsage>
                            <md:legalConstraints codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/MDlegalConstraints.xml">unrestricted</md:legalConstraints>
                            <md:securityConstraints codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/MDsecurityConstraints.xml">owner</md:securityConstraints>
                            <md:userNote>open access</md:userNote>
                        </md:ConstraintsOnUsage>
                    </md:constraints>
                </md:ISOidentifier>
            </md:ISOmetadata>
            <md:thematicModels>
                <md:presentThematicModels>
                    <md:thematicModel>Building</md:thematicModel>
                    <md:thematicModel>Bridge</md:thematicModel>
                    <md:thematicModel>Tunnel</md:thematicModel>
                    <md:thematicModel>Vegetation</md:thematicModel>
                    <md:thematicModel>WaterBody</md:thematicModel>
                    <md:thematicModel>Transportation</md:thematicModel>
                    <md:thematicModel>Generics</md:thematicModel>
                    <md:thematicModel>CityFurniture</md:thematicModel>
                    <md:thematicModel>CityObjectGroup</md:thematicModel>
                    <md:thematicModel>Relief</md:thematicModel>
                </md:presentThematicModels>
            </md:thematicModels>
            <md:textures>present</md:textures>
            <md:materials>present</md:materials>
            <md:ADEmetadata>
                <md:ADEidentifier>
                    <md:adeName>CityGML iTINs ADE</md:adeName>
                    <md:adeVersion>0.1</md:adeVersion>
                    <md:namespace>http://godzilla.bk.tudelft.nl/schemas/CityGML_iTINs_ADE</md:namespace>
                    <md:status>Implemented</md:status>
                    <md:authority>
                        <md:OrganizationalContact>
                            <md:contactName>3D Geoinformation Group</md:contactName>
                            <md:phone>+31 666666666</md:phone>
                            <md:address>Julianalaan 134, 2628 BL, TU Delft</md:address>
                            <md:emailAddress>3dtud@tudelft.nl</md:emailAddress>
                            <md:website>https://3d.bk.tudelft.nl</md:website>
                        </md:OrganizationalContact>
                    </md:authority>
                    <md:summary>CityGML ADE for storing massive TIN terrainns.</md:summary>
                    <md:xmlSchema>https://github.com/tudelft3d/CityGML_iTINs_ADE/blob/master/XSD/CityGML_iTINs_ADE.xsd</md:xmlSchema>
                    <md:umlModel>https://github.com/tudelft3d/CityGML_iTINs_ADE/blob/master/UML/CityGML_iTINs_ADE_0_1.eap</md:umlModel>
                    <md:documentation>https://github.com/tudelft3d/CityGML_iTINs_ADE/tree/master/Documentation</md:documentation>
                </md:ADEidentifier>
            </md:ADEmetadata>
            <md:MDcityfeatures>
                <md:MDbuilding>
                    <md:featureType>Building</md:featureType>
                    <md:featureCount>100</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail>
                    </md:LevelsOfDetail>
                    <md:buildingParts>10</md:buildingParts>
                    <md:buildingInstallations>15</md:buildingInstallations>
                </md:MDbuilding>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDbridge>
                    <md:featureType>Bridge</md:featureType>
                    <md:featureCount>100</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail> 
                    </md:LevelsOfDetail>
                    <md:bridgeParts>10</md:bridgeParts>
                    <md:bridgeInstallations>15</md:bridgeInstallations>
                    <md:bridgeConstructionElements>15</md:bridgeConstructionElements>
                </md:MDbridge>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDtunnel>
                    <md:featureType>Tunnel</md:featureType>
                    <md:featureCount>100</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail> 
                    </md:LevelsOfDetail>
                    <md:tunnelParts>10</md:tunnelParts>
                    <md:tunnelInstallations>15</md:tunnelInstallations>
                </md:MDtunnel>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDvegetation>
                    <md:featureType>Vegetation</md:featureType>
                    <md:featureCount>100</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail> 
                    </md:LevelsOfDetail>
                    <md:plantCovers>50</md:plantCovers>
                    <md:solitaryVegetationObjects>50</md:solitaryVegetationObjects>
                </md:MDvegetation>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDtransportation>
                    <md:featureType>Transportation</md:featureType>
                    <md:featureCount>100</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail> 
                    </md:LevelsOfDetail>
                    <md:roads>40</md:roads>
                    <md:railways>20</md:railways>
                    <md:tracks>20</md:tracks>
                    <md:squares>20</md:squares>
                </md:MDtransportation>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDwaterBody>
                    <md:featureType>WaterBody</md:featureType>
                    <md:featureCount>100</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail> 
                    </md:LevelsOfDetail>
                </md:MDwaterBody>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDlanduse>
                    <md:featureType>LandUse</md:featureType>
                    <md:featureCount>100</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail> 
                    </md:LevelsOfDetail>
                </md:MDlanduse>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDcityFurniture>
                    <md:featureType>CityFurniture</md:featureType>
                    <md:featureCount>100</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>2</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail> 
                    </md:LevelsOfDetail>
                </md:MDcityFurniture>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDcityObjectGroup>
                    <md:featureType>CityObjectGroup</md:featureType>
                    <md:featureCount>100</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail> 
                    </md:LevelsOfDetail>
                </md:MDcityObjectGroup>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDgenerics>
                    <md:featureType>Generics</md:featureType>
                    <md:featureCount>100</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail> 
                    </md:LevelsOfDetail>
                </md:MDgenerics>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDterrain>
                    <md:featureType>Relief</md:featureType>
                    <md:featureCount>1</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>1</md:objectCount>
                        </md:LevelOfDetail>
                        </md:LevelsOfDetail>
                    <md:terrainType>TINRelief</md:terrainType>
                    <md:TerrainProperties>
                        <md:MDTINRelief>
                            <md:triangleCount>1000</md:triangleCount>
                        </md:MDTINRelief>
                    </md:TerrainProperties>
                </md:MDterrain>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDterrain>
                    <md:featureType>Relief</md:featureType>
                    <md:featureCount>1</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>1</md:objectCount>
                        </md:LevelOfDetail>
                    </md:LevelsOfDetail>
                    <md:terrainType>RasterRelief</md:terrainType>
                    <md:TerrainProperties>
                        <md:MDRasterRelief>
                            <md:extent>
                                <gml:Envelope>
                                    <gml:lowerCorner>3423800.0 5705800.0 140.4</gml:lowerCorner>
                                    <gml:upperCorner>3426200.0 5708200.0 252.6</gml:upperCorner>
                                </gml:Envelope>
                            </md:extent>
                            <md:resolution uom="cm">20</md:resolution>
                        </md:MDRasterRelief>
                    </md:TerrainProperties>
                </md:MDterrain>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDterrain>
                    <md:featureType>Relief</md:featureType>
                    <md:featureCount>1</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>1</md:objectCount>
                        </md:LevelOfDetail>
                    </md:LevelsOfDetail>
                    <md:terrainType>MassPointRelief</md:terrainType>
                    <md:TerrainProperties>
                        <md:MDMasspointRelief>
                            <md:pointCount>10000</md:pointCount>
                        </md:MDMasspointRelief>
                    </md:TerrainProperties>
                </md:MDterrain>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDterrain>
                    <md:featureType>Relief</md:featureType>
                    <md:featureCount>1</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>1</md:objectCount>
                        </md:LevelOfDetail>
                    </md:LevelsOfDetail>
                    <md:terrainType>BreaklineRelief</md:terrainType>
                    <md:TerrainProperties>
                        <md:MDBreaklineRelief>
                            <md:lineCount>10</md:lineCount>
                        </md:MDBreaklineRelief>
                    </md:TerrainProperties>
                </md:MDterrain>
            </md:MDcityfeatures>
            <md:LevelsOfDetail>
                <md:LevelOfDetail>
                    <md:lod>1</md:lod>
                    <md:objectCount>904</md:objectCount>
                </md:LevelOfDetail>
            </md:LevelsOfDetail>
            <md:LevelsOfDetail>
                <md:LevelOfDetail>
                    <md:lod>2</md:lod>
                    <md:objectCount>100</md:objectCount>
                </md:LevelOfDetail> 
            </md:LevelsOfDetail>
        </md:MDcitymodel>     
    </cityObjectMember>
</CityModel>