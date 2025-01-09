<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)

Entity: SeaConditions
=====================
<!-- /10-Header -->
<!-- 15-License -->


[Open License](https://github.com/smart-data-models/dataModel.Weather/blob/master/SeaConditions/LICENSE.md)


Document generated automatically
<!-- /15-License -->
<!-- 20-Description -->


Global description: **This entity contains a harmonised geographic description of sea conditions**


Version: 0.0.1
<!-- /20-Description -->
<!-- 25-Description -->


If you use this data model fill out [this form](https://smartdatamodels.org/index.php/adopters-form/)


You will appear in the ADOPTERS.yaml ([see example](https://github.com/smart-data-models/dataModel.Weather/blob/master/WeatherObserved/ADOPTERS.yaml)) file and in [the database of adopters](https://smartdatamodels.org/index.php/adopters/)
<!-- /25-Description -->
<!-- 30-PropertiesList -->


## List of properties


<sup><sub>[*] If there is not a type in an attribute, it could have several types or different formats/patterns</sub></sup>
- `address` (object): The mailing address
- `alternateName` (string): An alternative name for this item
- `areaServed` (string): The geographic area where a service or offered item is provided
- `dataProvider` (string): A sequence of characters identifying the provider of the harmonised data entity
- `dateCreated` (string): Entity creation timestamp. This will usually be allocated by the storage platform
- `dateModified` (string): Timestamp of the last modification of the entity. This will usually be allocated by the storage platform
- `dateObserved` (string): The date and time of this observation in ISO8601 UTC format
- `description` (string): A description of this item
- `id` ([*]): Unique identifier of the entity
- `location` ([*]): Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
- `name` (string): The name of this item
- `owner` (array): A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)
- `pH` (number): Acidity or basicity of an aqueous solution
- `salinity` (number): Amount of salts dissolved in water
- `seeAlso` ([*]): list of uri pointing to additional resources about the item
- `source` (string): A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object
- `surfaceTemperature` (number): Sea surface temperature
- `type` (string): NGSI-LD Entity Type. It has to be SeaConditions
- `waveHeight` (number): Height of the waves
- `waveLevel` (number): It indicates the height of the waves and also measures the swell of the sea
- `wavePeriod` (number): Indicates the time between the crests of a wave
<!-- /30-PropertiesList -->
<!-- 35-RequiredProperties -->


## Required properties
- `id`
- `type`
<!-- /35-RequiredProperties -->
<!-- 40-NotesYaml -->


<!-- /40-NotesYaml -->
<!-- 50-DataModelHeader -->

## Data Model description of properties


Sorted alphabetically (click for details)
<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>

```yaml
SeaConditions:
  description: This entity contains a harmonised geographic description of sea conditions
  properties:
    address:
      description: The mailing address
      properties:
        addressCountry:
          description: The country. For example, Spain
          type: string
          x-ngsi:
            model: https://schema.org/addressCountry
            type: Property
        addressLocality:
          description: The locality in which the street address is, and which is in the region
          type: string
          x-ngsi:
            model: https://schema.org/addressLocality
            type: Property
        addressRegion:
          description: The region in which the locality is, and which is in the country
          type: string
          x-ngsi:
            model: https://schema.org/addressRegion
            type: Property
        district:
          description: A district is a type of administrative division that, in some countries, is managed by the local government
          type: string
          x-ngsi:
            type: Property
        postOfficeBoxNumber:
          description: The post office box number for PO box addresses. For example, 03578
          type: string
          x-ngsi:
            model: https://schema.org/postOfficeBoxNumber
            type: Property
        postalCode:
          description: The postal code. For example, 24004
          type: string
          x-ngsi:
            model: https://schema.org/https://schema.org/postalCode
            type: Property
        streetAddress:
          description: The street address
          type: string
          x-ngsi:
            model: https://schema.org/streetAddress
            type: Property
        streetNr:
          description: Number identifying a specific property on a public street
          type: string
          x-ngsi:
            type: Property
      type: object
      x-ngsi:
        model: https://schema.org/address
        type: Property
    alternateName:
      description: An alternative name for this item
      type: string
      x-ngsi:
        type: Property
    areaServed:
      description: The geographic area where a service or offered item is provided
      type: string
      x-ngsi:
        model: https://schema.org/Text
        type: Property
    dataProvider:
      description: A sequence of characters identifying the provider of the harmonised data entity
      type: string
      x-ngsi:
        type: Property
    dateCreated:
      description: Entity creation timestamp. This will usually be allocated by the storage platform
      format: date-time
      type: string
      x-ngsi:
        type: Property
    dateModified:
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform
      format: date-time
      type: string
      x-ngsi:
        type: Property
    dateObserved:
      description: The date and time of this observation in ISO8601 UTC format
      format: date-time
      type: string
      x-ngsi:
        model: https://schema.org/DateTime
        type: Property
    description:
      description: A description of this item
      type: string
      x-ngsi:
        type: Property
    id:
      anyOf:
        - description: Identifier format of any NGSI entity
          maxLength: 256
          minLength: 1
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$
          type: string
          x-ngsi:
            type: Property
        - description: Identifier format of any NGSI entity
          format: uri
          type: string
          x-ngsi:
            type: Property
      description: Unique identifier of the entity
      x-ngsi:
        type: Relationship
    location:
      description: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon
      oneOf:
        - description: Geojson reference to the item. Point
          properties:
            bbox:
              items:
                type: number
              minItems: 4
              type: array
            coordinates:
              items:
                type: number
              minItems: 2
              type: array
            type:
              enum:
                - Point
              type: string
          required:
            - type
            - coordinates
          title: GeoJSON Point
          type: object
          x-ngsi:
            type: GeoProperty
        - description: Geojson reference to the item. LineString
          properties:
            bbox:
              items:
                type: number
              minItems: 4
              type: array
            coordinates:
              items:
                items:
                  type: number
                minItems: 2
                type: array
              minItems: 2
              type: array
            type:
              enum:
                - LineString
              type: string
          required:
            - type
            - coordinates
          title: GeoJSON LineString
          type: object
          x-ngsi:
            type: GeoProperty
        - description: Geojson reference to the item. Polygon
          properties:
            bbox:
              items:
                type: number
              minItems: 4
              type: array
            coordinates:
              items:
                items:
                  items:
                    type: number
                  minItems: 2
                  type: array
                minItems: 4
                type: array
              type: array
            type:
              enum:
                - Polygon
              type: string
          required:
            - type
            - coordinates
          title: GeoJSON Polygon
          type: object
          x-ngsi:
            type: GeoProperty
        - description: Geojson reference to the item. MultiPoint
          properties:
            bbox:
              items:
                type: number
              minItems: 4
              type: array
            coordinates:
              items:
                items:
                  type: number
                minItems: 2
                type: array
              type: array
            type:
              enum:
                - MultiPoint
              type: string
          required:
            - type
            - coordinates
          title: GeoJSON MultiPoint
          type: object
          x-ngsi:
            type: GeoProperty
        - description: Geojson reference to the item. MultiLineString
          properties:
            bbox:
              items:
                type: number
              minItems: 4
              type: array
            coordinates:
              items:
                items:
                  items:
                    type: number
                  minItems: 2
                  type: array
                minItems: 2
                type: array
              type: array
            type:
              enum:
                - MultiLineString
              type: string
          required:
            - type
            - coordinates
          title: GeoJSON MultiLineString
          type: object
          x-ngsi:
            type: GeoProperty
        - description: Geojson reference to the item. MultiLineString
          properties:
            bbox:
              items:
                type: number
              minItems: 4
              type: array
            coordinates:
              items:
                items:
                  items:
                    items:
                      type: number
                    minItems: 2
                    type: array
                  minItems: 4
                  type: array
                type: array
              type: array
            type:
              enum:
                - MultiPolygon
              type: string
          required:
            - type
            - coordinates
          title: GeoJSON MultiPolygon
          type: object
          x-ngsi:
            type: GeoProperty
      x-ngsi:
        type: GeoProperty
    name:
      description: The name of this item
      type: string
      x-ngsi:
        type: Property
    owner:
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)
      items:
        anyOf:
          - description: Identifier format of any NGSI entity
            maxLength: 256
            minLength: 1
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$
            type: string
            x-ngsi:
              type: Property
          - description: Identifier format of any NGSI entity
            format: uri
            type: string
            x-ngsi:
              type: Property
        description: Unique identifier of the entity
        x-ngsi:
          type: Relationship
      type: array
      x-ngsi:
        type: Property
    pH:
      description: Acidity or basicity of an aqueous solution
      maximum: 14
      minimum: 0
      type: number
      x-ngsi:
        model: https://schema.org/Number
        type: Property
    salinity:
      description: Amount of salts dissolved in water
      minimum: 0
      type: number
      x-ngsi:
        model: https://schema.org/Number
        type: Property
        units: Parts per thousand
    seeAlso:
      description: list of uri pointing to additional resources about the item
      oneOf:
        - items:
            format: uri
            type: string
          minItems: 1
          type: array
        - format: uri
          type: string
      x-ngsi:
        type: Property
    source:
      description: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object
      type: string
      x-ngsi:
        type: Property
    surfaceTemperature:
      description: Sea surface temperature
      type: number
      x-ngsi:
        model: https://schema.org/Number
        type: Property
        units: Celsius degrees
    type:
      description: NGSI-LD Entity Type. It has to be SeaConditions
      enum:
        - SeaConditions
      type: string
      x-ngsi:
        type: Property
    waveHeight:
      description: Height of the waves
      type: number
      x-ngsi:
        model: https://schema.org/Number
        type: Property
        units: Meters
    waveLevel:
      description: It indicates the height of the waves and also measures the swell of the sea
      maximum: 9
      minimum: 0
      type: number
      x-ngsi:
        model: https://schema.org/Number
        type: Property
        units: Douglas sea scale
    wavePeriod:
      description: Indicates the time between the crests of a wave
      type: number
      x-ngsi:
        model: https://schema.org/Number
        type: Property
        units: Seconds
  required:
    - id
    - type
  type: object
  x-derived-from: ''
  x-disclaimer: Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2025 Contributors to Smart Data Models Program
  x-license-url: https://example.com/license
  x-model-schema: https://smart-data-models.github.io/dataModel.Environment/SeaConditions/schema.json
  x-model-tags: ''
  x-version: 0.0.1
```
</details>
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->


<!-- /70-MiddleNotes -->
<!-- 80-Examples -->


## Example payloads
#### SeaConditions NGSI-v2 key-values Example


Here is an example of a SeaConditions in NGSI-v2 key-values Example.
<details><summary><strong>show/hide example</strong></summary>

```json
{
  "id": "SeaCondition-PlayaLevante-Benidorm-123456",
  "type": "SeaConditions",
  "dateObserved": "2021-02-20T06:45:00Z",
  "location": {
    "type": "Point",
    "coordinates": [
      -8.768460000000001,
      42.60214472222222
    ]
  },
  "name": "Mar en la Playa Levante",
  "description": "Informaci\u00f3n del estado del mar en la playa Levante",
  "address": {
    "addressCountry": "ES",
    "addressLocality": "Benidorm"
  },
  "dataProvider": "Water-sensor-12345",
  "waveLevel": 1,
  "surfaceTemperature": 14.7,
  "waveHeight": 0.05,
  "wavePeriod": 1.5,
  "pH": 8.5,
  "salinity": 35
}
```
</details>

#### SeaConditions NGSI-v2 normalized Example


Here is an example of a SeaConditions in NGSI-v2 normalized Example.
<details><summary><strong>show/hide example</strong></summary>

```json
{
  "id": "SeaCondition-PlayaLevante-Benidorm-123456",
  "type": "SeaConditions",
  "dateCreated": {
    "type": "DateTime",
    "value": "2021-02-20T06:45:00Z"
  },
  "dateModified": {
    "type": "DateTime",
    "value": "2021-02-20T06:45:00Z"
  },
  "source": {
    "type": "Text",
    "value": ""
  },
  "name": {
    "type": "Text",
    "value": "Mar en la Playa Levante"
  },
  "alternateName": {
    "type": "Text",
    "value": "Playa Levante"
  },
  "description": {
    "type": "Text",
    "value": "Informaci\u00f3n del estado del mar en la playa Levante"
  },
  "dataProvider": {
    "type": "Text",
    "value": "Water-sensor-12345"
  },
  "owner": {
    "type": "StructuredValue",
    "value": [
      "urn:ngsi-ld:SeaConditions:items:JVPZ:12516420",
      "urn:ngsi-ld:SeaConditions:items:XVAE:29040891"
    ]
  },
  "seeAlso": {
    "type": "StructuredValue",
    "value": [
      "urn:ngsi-ld:SeaConditions:items:KFKA:73977455",
      "urn:ngsi-ld:SeaConditions:items:GPZI:53207694"
    ]
  },
  "location": {
    "type": "geo:json",
    "value": {
      "type": "Point",
      "coordinates": [
        -8.768460000000001,
        42.60214472222222
      ]
    }
  },
  "address": {
    "type": "StructuredValue",
    "value": {
      "streetAddress": "",
      "addressLocality": "Benidorm",
      "addressRegion": "Valencia",
      "addressCountry": "ES",
      "postalCode": "",
      "postOfficeBoxNumber": ""
    }
  },
  "areaServed": {
    "type": "Text",
    "value": ""
  },
  "waveLevel": {
    "type": "Number",
    "value": 1
  },
  "surfaceTemperature": {
    "type": "Number",
    "value": 14.7
  },
  "waveHeight": {
    "type": "Number",
    "value": 0.05
  },
  "wavePeriod": {
    "type": "Number",
    "value": 1.5
  },
  "pH": {
    "type": "Number",
    "value": 8.5
  },
  "salinity": {
    "type": "Number",
    "value": 35
  },
  "dateObserved": {
    "type": "DateTime",
    "value": "2021-02-20T06:45:00Z"
  }
}

```
</details>

#### SeaConditions NGSI-LD key-values Example


Here is an example of a SeaConditions in NGSI-LD key-values Example.
<details><summary><strong>show/hide example</strong></summary>

```json
{
  "id": "urn:ngsi-ld:SeaCondition:SeaCondition-PlayaLevante-Benidorm-123456",
  "type": "SeaConditions",
  "address": {
    "addressCountry": "ES",
    "addressLocality": "Benidorm"
  },
  "dataProvider": "Water-sensor-12345",
  "dateObserved": "2021-02-20T06:45:00Z",
  "description": "Informaci\u00f3n del estado del mar en la playa Levante",
  "location": {
    "coordinates": [
      -8.768460000000001,
      42.60214472222222
    ],
    "type": "Point"
  },
  "name": "Mar en la Playa Levante",
  "pH": 8.5,
  "salinity": 35,
  "surfaceTemperature": 14.7,
  "waveHeight": 0.05,
  "waveLevel": 1,
  "wavePeriod": 1.5,
  "@context": [
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/context.jsonld"
  ]
}
```
</details>

#### SeaConditions NGSI-LD normalized Example


Here is an example of a SeaConditions in NGSI-LD normalized Example.
<details><summary><strong>show/hide example</strong></summary>

```json
{
  "id": "urn:ngsi-ld:SeaCondition:SeaCondition-PlayaLevante-Benidorm-123456",
  "type": "SeaConditions",
  "address": {
    "type": "Property",
    "value": {
      "streetAddress": "",
      "addressLocality": "Benidorm",
      "addressRegion": "Valencia",
      "addressCountry": "ES",
      "postalCode": "",
      "postOfficeBoxNumber": ""
    }
  },
  "alternateName": {
    "type": "Property",
    "value": "Playa Levante"
  },
  "areaServed": {
    "type": "Property",
    "value": ""
  },
  "dataProvider": {
    "type": "Property",
    "value": "Water-sensor-12345"
  },
  "dateCreated": {
    "type": "Property",
    "value": {
      "@type": "DateTime",
      "@value": "2021-02-20T06:45:00Z"
    }
  },
  "dateModified": {
    "type": "Property",
    "value": {
      "@type": "DateTime",
      "@value": "2021-02-20T06:45:00Z"
    }
  },
  "dateObserved": {
    "type": "Property",
    "value": "2021-02-20T06:45:00Z"
  },
  "description": {
    "type": "Property",
    "value": "Informaci\u00f3n del estado del mar en la playa Levante"
  },
  "location": {
    "type": "Property",
    "value": {
      "type": "Point",
      "coordinates": [
        -8.768460000000001,
        42.60214472222222
      ]
    }
  },
  "name": {
    "type": "Property",
    "value": "Mar en la Playa Levante"
  },
  "owner": {
    "type": "Property",
    "value": [
      "urn:ngsi-ld:SeaConditions:items:JVPZ:12516420",
      "urn:ngsi-ld:SeaConditions:items:XVAE:29040891"
    ]
  },
  "pH": {
    "type": "Property",
    "value": 8.5
  },
  "salinity": {
    "type": "Property",
    "value": 35
  },
  "seeAlso": {
    "type": "Property",
    "value": [
      "urn:ngsi-ld:SeaConditions:items:KFKA:73977455",
      "urn:ngsi-ld:SeaConditions:items:GPZI:53207694"
    ]
  },
  "source": {
    "type": "Property",
    "value": ""
  },
  "surfaceTemperature": {
    "type": "Property",
    "value": 14.7
  },
  "waveHeight": {
    "type": "Property",
    "value": 0.05
  },
  "waveLevel": {
    "type": "Property",
    "value": 1
  },
  "wavePeriod": {
    "type": "Property",
    "value": 1.5
  },
  "@context": [
    "https://raw.githubusercontent.com/smart-data-models/dataModel.Weather/master/context.jsonld"
  ]
}
```
</details>

<!-- /80-Examples -->
<!-- 90-FooterNotes -->


<!-- /90-FooterNotes -->
<!-- 95-Units -->


See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units
<!-- /95-Units -->
<!-- 97-LastFooter -->
---
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->
