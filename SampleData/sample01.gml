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
    http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE 3DMD_ADE.xsd">
    
    <md:metadataMember> 
        <md:MDcitymodel>
            
            <md:metadataIdentifier>MD_3D_MM_12345</md:metadataIdentifier>
            <md:citymodelIdentifier>GML_12345</md:citymodelIdentifier>
            
            <md:ISOmetadata>
                <md:ISOidentifier>
                    <md:datasetTitle>3D City Model</md:datasetTitle>
                    <md:datasetReferenceDate>2017-01-01</md:datasetReferenceDate>
                    <md:geoLocation>Delft</md:geoLocation>
                    <md:datasetLanguage>English</md:datasetLanguage>
                    <md:datasetTopicCategory codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE//codelists/MDtopicCategory.xml">
                      geoscientificInformation
                    </md:datasetTopicCategory>
                    <md:distributionFormatVersion>CityGML 2.0</md:distributionFormatVersion>
                    <md:spatialRepresentationType codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/MDspatialRepTypeCode.xml">
                      Vector
                    </md:spatialRepresentationType>
                    <md:referenceSystem>urn:ogc:def:crs,crs:EPSG:6.12:31466,crs:EPSG:6.12:5783</md:referenceSystem>
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
                    <md:extent>
                        <md:Extent>
                            <md:geographicElement>
                                <md:GeographicalExtent>
                                    <md:polygon3D>
                                        <gml:Envelope>
                                            <gml:lowerCorner>3423800.0 5705800.0 140.4</gml:lowerCorner>
                                            <gml:upperCorner>3426200.0 5708200.0 252.6</gml:upperCorner>
                                        </gml:Envelope>
                                    </md:polygon3D>
                                </md:GeographicalExtent>
                            </md:geographicElement>
                        </md:Extent>
                    </md:extent>
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
            
            <md:thematicModules>
                <md:presentThematicModules>
                    <md:thematicModule>Building</md:thematicModule>
                    <md:thematicModule>Bridge</md:thematicModule>
                    <md:thematicModule>CityFurniture</md:thematicModule>
                    <md:thematicModule>Generics</md:thematicModule>
                    <md:thematicModule>LandUse</md:thematicModule>
                    <md:thematicModule>Relief</md:thematicModule>
                    <md:thematicModule>Tunnel</md:thematicModule>
                </md:presentThematicModules>
            </md:thematicModules>
            
            <md:textures>absent</md:textures>
            <md:materials>absent</md:materials>
            <md:xlinks>absent</md:xlinks>
            <md:externalReferences>absent</md:externalReferences>
            
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
                    <md:uniqueFeatureCount>100</md:uniqueFeatureCount>
                    <md:aggregateFeatureCount>100</md:aggregateFeatureCount>
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
                    <md:uniqueFeatureCount>100</md:uniqueFeatureCount>
                    <md:aggregateFeatureCount>100</md:aggregateFeatureCount>
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
                <md:MDterrain>
                    <md:featureType>Relief</md:featureType>
                    <md:uniqueFeatureCount>1</md:uniqueFeatureCount>
                    <md:aggregateFeatureCount>1</md:aggregateFeatureCount>
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
                <md:MDtunnel>
                    <md:featureType>Tunnel</md:featureType>
                    <md:uniqueFeatureCount>100</md:uniqueFeatureCount>
                    <md:aggregateFeatureCount>100</md:aggregateFeatureCount>
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
                <md:MDtransportation>
                    <md:featureType>Transportation</md:featureType>
                    <md:uniqueFeatureCount>100</md:uniqueFeatureCount>
                    <md:aggregateFeatureCount>100</md:aggregateFeatureCount>
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
                <md:MDlanduse>
                    <md:featureType>LandUse</md:featureType>
                    <md:uniqueFeatureCount>100</md:uniqueFeatureCount>
                    <md:aggregateFeatureCount>100</md:aggregateFeatureCount>
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
                    <md:uniqueFeatureCount>100</md:uniqueFeatureCount>
                    <md:aggregateFeatureCount>100</md:aggregateFeatureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>2</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail> 
                    </md:LevelsOfDetail>
                </md:MDcityFurniture>
            </md:MDcityfeatures>
            <md:MDcityfeatures>
                <md:MDgenerics>
                    <md:featureType>Generics</md:featureType>
                    <md:uniqueFeatureCount>100</md:uniqueFeatureCount>
                    <md:aggregateFeatureCount>100</md:aggregateFeatureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail> 
                    </md:LevelsOfDetail>
                </md:MDgenerics>
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
    </md:metadataMember>
</CityModel>