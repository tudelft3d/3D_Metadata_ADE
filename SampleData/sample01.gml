<?xml version="1.0" encoding="UTF-8"?>

<CityModel xmlns="http://www.opengis.net/citygml/2.0" xmlns:bldg="http://www.opengis.net/citygml/building/2.0"
    xmlns:gml="http://www.opengis.net/gml"
    xmlns:xlink="http://www.w3.org/1999/xlink" 
    xmlns:xAL="urn:oasis:names:tc:ciq:xsdschema:xAL:2.0"
    xmlns:md="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation= "http://www.opengis.net/citygml/building/2.0 http://schemas.opengis.net/citygml/building/2.0/building.xsd 
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
            
            <md:ISOmetadata>
                <md:ISOidentifier>
                    <md:datasetTitle>3D City Model</md:datasetTitle>
                    <md:datasetReferenceDate>2017-01-01</md:datasetReferenceDate>
                    <md:geoLocation>Delft</md:geoLocation>
                    <md:datasetLanguage>English</md:datasetLanguage>
                    <md:datasetTopicCategory codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE//codelists/MDtopicCategory.xml">geoscientificInformation</md:datasetTopicCategory>
                    <md:datasetDescription>Metadata associated with the 3D city model</md:datasetDescription>
                    <md:distributionFormatVersion>CityGML 2.0</md:distributionFormatVersion>
                    <md:spatialRepresentationType codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/MDspatialRepTypeCode.xml">Vector</md:spatialRepresentationType>
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
                        <md:constraintsOnUsage>
                            <md:legalConstraints codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/MDlegalConstraints.xml">unrestricted</md:legalConstraints>
                            <md:securityConstraints codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/MDsecurityConstraints.xml">owner</md:securityConstraints>
                            <md:userNote>open access</md:userNote>
                        </md:constraintsOnUsage>
                    </md:constraints>
                </md:ISOidentifier>
            </md:ISOmetadata>
            
            <md:semanticsMetadata>
                <md:SemanticIdentifier>
                    <md:state>present</md:state>
                    <md:semanticClass>Building</md:semanticClass> 
                    <md:semanticClass>Terrain</md:semanticClass>
                    <md:semanticClass>Landuse</md:semanticClass>
                </md:SemanticIdentifier>
            </md:semanticsMetadata>
            
            <md:appearanceMetadata>
                <md:Textures>
                    <md:state>present</md:state>
                </md:Textures>
            </md:appearanceMetadata>
            
            <md:CityfeatureMetadata>
                <md:MDcityfeature>
                    <md:cityfeatureType codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/CityfeatureType.xml">Building</md:cityfeatureType>
                    <md:featureCount>100</md:featureCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>2</md:lod>
                            <md:objectCount>100</md:objectCount>
                        </md:LevelOfDetail> 
                    </md:LevelsOfDetail>
                    <md:CitySubfeatureMetadata>
                        <md:MDcitySubfeature> 
                        <md:citySubfeatureType codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/CitySubfeatureType.xml">Building</md:citySubfeatureType>  
                        <md:citySubfeatureCount>50</md:citySubfeatureCount>
                        <md:LevelsOfDetail>
                            <md:LevelOfDetail>
                                <md:lod>2</md:lod>
                                <md:objectCount>50</md:objectCount>
                            </md:LevelOfDetail> 
                        </md:LevelsOfDetail>
                       </md:MDcitySubfeature>
                    </md:CitySubfeatureMetadata>
                    <md:CitySubfeatureMetadata>
                    <md:MDcitySubfeature>
                        <md:citySubfeatureType codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/CitySubfeatureType.xml">BuildingPart</md:citySubfeatureType>  
                        <md:citySubfeatureCount>50</md:citySubfeatureCount>
                        <md:LevelsOfDetail>
                            <md:LevelOfDetail>
                                <md:lod>2</md:lod>
                                <md:objectCount>50</md:objectCount>
                            </md:LevelOfDetail> 
                        </md:LevelsOfDetail>
                    </md:MDcitySubfeature>
                   </md:CitySubfeatureMetadata>
                </md:MDcityfeature>
            </md:CityfeatureMetadata>
            
            <md:LevelsOfDetail>
                <md:LevelOfDetail>
                    <md:lod>1</md:lod>
                    <md:objectCount>3</md:objectCount>
                </md:LevelOfDetail> 
            </md:LevelsOfDetail>
            <md:LevelsOfDetail>
                <md:LevelOfDetail>
                    <md:lod>2</md:lod>
                    <md:objectCount>100</md:objectCount>
                </md:LevelOfDetail> 
            </md:LevelsOfDetail>
            
            <md:LanduseMetadata>
                <md:MDlanduse>                   
                    <md:landuseClass codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/LandUseClassCode.xml">SettlementArea</md:landuseClass>
                    <md:landuseFunction codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/LandUseFunctionUsageCode.xml">Residential</md:landuseFunction>
                    <md:landuseUsage codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/LandUseFunctionUsageCode.xml">Rsidential</md:landuseUsage>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>1</md:objectCount>
                        </md:LevelOfDetail>
                    </md:LevelsOfDetail>
                </md:MDlanduse>
            </md:LanduseMetadata>
          
            <md:TerrainMetadata>
                <md:MDterrain> 
                    <md:terrainType codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/TerrainTypeCode.xml">TINRelief</md:terrainType>
                    <md:terrainCount>1</md:terrainCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>1</md:objectCount>
                        </md:LevelOfDetail>
                    </md:LevelsOfDetail>
                    <md:TerrainProperties>
                        <md:TINproperties>
                            <md:triangleCount>10000</md:triangleCount>
                        </md:TINproperties>
                    </md:TerrainProperties>
                </md:MDterrain>
            </md:TerrainMetadata>
            
            <md:TerrainMetadata>
                <md:MDterrain>
                    <md:terrainType codeSpace="http://godzilla.bk.tudelft.nl/schemas/3DMD_ADE/codelists/TerrainTypeCode.xml">RasterRelief</md:terrainType>
                    <md:terrainCount>1</md:terrainCount>
                    <md:LevelsOfDetail>
                        <md:LevelOfDetail>
                            <md:lod>1</md:lod>
                            <md:objectCount>1</md:objectCount>
                        </md:LevelOfDetail>
                    </md:LevelsOfDetail>
                    <md:TerrainProperties>
                        <md:RasterProperties>
                            <md:extent>
                                <gml:Envelope>
                                    <gml:lowerCorner>3423800.0 5705800.0 140.4</gml:lowerCorner>
                                    <gml:upperCorner>3426200.0 5708200.0 252.6</gml:upperCorner>
                                </gml:Envelope>
                            </md:extent>
                            <md:resolution uom="cm">20</md:resolution>
                        </md:RasterProperties>
                    </md:TerrainProperties>
                </md:MDterrain>
            </md:TerrainMetadata>
                   
        </md:MDcitymodel>
    </cityObjectMember>
</CityModel>