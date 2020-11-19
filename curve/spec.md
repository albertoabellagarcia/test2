
Entity: Curve
=============
  
  
Global description: **This entity contains a harmonised description of a generic curve made for the Water Network Management domain. This entity is primarily associated with the water management vertical and related IoT applications.**
## Data Model description of properties


Ordered alphabetically

```<br>---
ThreePhaseAcMeasurement:
  description: 'An electrical  measurement from a system that uses three phase alternating current.'
  properties:
    activeEnergyExport:
      description: 'Active energy exported per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3.'
      properties:
        L1:
          minimum: 0
          type: number
        L2:
          minimum: 0
          type: number
        L3:
          minimum: 0
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: 'kilowatt hour (kWh)'
    activeEnergyImport:
      description: 'Active energy imported i.e. consumed per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3.'
      properties:
        L1:
          minimum: 0
          type: number
        L2:
          minimum: 0
          type: number
        L3:
          minimum: 0
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: 'kilowatt hour (kWh)'
    activePower:
      description: 'The actual values will beconveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3. '
      properties:
        L1:
          type: number
        L2:
          type: number
        L3:
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: 'watt (W).Active power consumed per phase'
    address:
      properties:
        addressCountry:
          type: string
        addressLocality:
          type: string
        addressRegion:
          type: string
        areaServed:
          type: string
        postOfficeBoxNumber:
          type: string
        postalCode:
          type: string
        streetAddress:
          type: string
      type: object
    alternateName:
      type: string
    apparentEnergyExport:
      description: 'Apparent energy exported per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3.'
      properties:
        L1:
          minimum: 0
          type: number
        L2:
          minimum: 0
          type: number
        L3:
          minimum: 0
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: 'kilovolt-ampere-hour (kVAh)'
    apparentEnergyImport:
      description: 'Apparent energy imported i.e. consumed per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3.'
      properties:
        L1:
          minimum: 0
          type: number
        L2:
          minimum: 0
          type: number
        L3:
          minimum: 0
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: 'kilovolt-ampere-hour (kVAh)'
    apparentPower:
      description: 'Apparent power consumed per phase. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3'
      properties:
        L1:
          minimum: 0
          type: number
        L2:
          minimum: 0
          type: number
        L3:
          minimum: 0
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: 'volt-ampere (VA)'
    areaServed:
      type: string
    current:
      description: 'Electrical current. The actual values will be conveyed by one subproperty per alternating current phase and the neutral wire: L1, L2, L3 and N.'
      properties:
        L1:
          type: number
        L2:
          type: number
        L3:
          type: number
        N:
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: 'Ampers (A)'
    dataProvider:
      type: string
    dateCreated:
      format: date-time
      type: string
    dateEnergyMeteringStarted:
      description: 'The starting date for metering energy.'
      format: date-time
      type: Property
      x-ngsi:
        model: http://schema.org/DateTime
    dateModified:
      format: date-time
      type: string
    description:
      type: string
    displacementPowerFactor:
      description: 'Displacement power factor for each phase. The quantity is based on the fundamental frequency of the system. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'
      properties:
        L1:
          maximum: 1
          minimum: -1
          type: number
        L2:
          maximum: 1
          minimum: -1
          type: number
        L3:
          maximum: 1
          minimum: -1
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: '-1 to +1'
    frequency:
      description: 'The frequency of the circuit.'
      minimum: 0
      type: Property
      x-ngsi:
        model: http://schema.org/Number
        units: 'Hertz (Hz)'
    id:
      anyOf: &threephaseacmeasurement_-_properties_-_owner_-_items_-_anyof
        - maxLength: 256
          minLength: 1
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$
          type: string
        - format: uri
          type: string
    location:
      $id: https://geojson.org/schema/Geometry.json
      $schema: "http://json-schema.org/draft-07/schema#"
      oneOf:
        - properties:
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
          title: 'GeoJSON Point'
          type: object
        - properties:
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
          title: 'GeoJSON LineString'
          type: object
        - properties:
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
          title: 'GeoJSON Polygon'
          type: object
        - properties:
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
          title: 'GeoJSON MultiPoint'
          type: object
        - properties:
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
          title: 'GeoJSON MultiLineString'
          type: object
        - properties:
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
          title: 'GeoJSON MultiPolygon'
          type: object
      title: 'GeoJSON Geometry'
    name:
      type: string
    owner:
      items:
        anyOf: *threephaseacmeasurement_-_properties_-_owner_-_items_-_anyof
      type: array
    phaseToPhaseVoltage:
      description: 'Voltage between phases. A value for each phase pair: phases 1 and 2 (L12), phases 2 and 3 (L32), phases 3 and 1 (L31).'
      properties:
        L12:
          minimum: 0
          type: number
        L23:
          minimum: 0
          type: number
        L31:
          minimum: 0
          type: number
      type: Property
      x-ngsi:
        model: (http://schema.org/StructuredValue
        units: 'Volts (V)'
    phaseVoltage:
      description: 'The voltage between each phase and neutral conductor. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'
      properties:
        L1:
          minimum: 0
          type: number
        L2:
          minimum: 0
          type: number
        L3:
          minimum: 0
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: 'Volts (V)'
    powerFactor:
      description: 'Power factor for each phase. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'
      properties:
        L1:
          maximum: 1
          minimum: -1
          type: number
        L2:
          maximum: 1
          minimum: -1
          type: number
        L3:
          maximum: 1
          minimum: -1
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: '-1 to +1'
    reactiveEnergyExport:
      description: 'Fundamental frequency reactive energy exported per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3.'
      properties:
        L1:
          minimum: 0
          type: number
        L2:
          minimum: 0
          type: number
        L3:
          minimum: 0
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: 'kilovolt-ampere-reactive-hour (kVArh)'
    reactiveEnergyImport:
      description: 'Fundamental frequency reactive energy imported i.e. consumed per phase since the metering start date. The actual values will be conveyed by subproperties which names will be equal to the name of each of the alternating current phases: L1, L2, L3.'
      properties:
        L1:
          minimum: 0
          type: number
        L2:
          minimum: 0
          type: number
        L3:
          minimum: 0
          type: number
      type: Property
      x-ngsi:
        model: 'kilovolt-ampere-reactive-hour (kVArh)'
        units: http://schema.org/StructuredValue
    reactivePower:
      description: 'Fundamental frequency reactive power. The actual values will be conveyed by subproperties whose names will be equal to the name of each of the alternating current phases: L1, L2, L3.'
      properties:
        L1:
          type: number
        L2:
          type: number
        L3:
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: 'volts-ampere-reactive (VAr)'
    refDevice:
      description: 'Relationship. Device(s) used to obtain the measurement.'
      items:
        anyOf: *threephaseacmeasurement_-_properties_-_owner_-_items_-_anyof
      minItems: 1
      type: array
      uniqueItems: true
    refTargetDevice:
      description: 'Relationship. Device(s) for which the measurement was taken.'
      items:
        anyOf: *threephaseacmeasurement_-_properties_-_owner_-_items_-_anyof
      minItems: 1
      type: array
      uniqueItems: true
    seeAlso:
      oneOf:
        - items:
            - format: uri
              type: string
          minItems: 1
          type: array
        - format: uri
          type: string
    source:
      type: string
    thdCurrent:
      description: 'Total harmonic distortion of electrical current. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'
      properties:
        L1:
          maximum: 1
          minimum: 0
          type: number
        L2:
          maximum: 1
          minimum: 0
          type: number
        L3:
          maximum: 1
          minimum: 0
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: '0 to 1'
    thdVoltage:
      description: 'Total harmonic distortion of voltage for each phase. The actual values will be conveyed by one subproperty per alternating current phase: L1, L2 and L3'
      properties:
        L1:
          maximum: 1
          minimum: 0
          type: number
        L2:
          maximum: 1
          minimum: 0
          type: number
        L3:
          maximum: 1
          minimum: 0
          type: number
      type: Property
      x-ngsi:
        model: http://schema.org/StructuredValue
        units: '0 to 1'
    totalActiveEnergyExport:
      description: 'Total energy exported since metering started (since `dateEnergyMeteringStarted`).'
      minimum: 0
      type: Property
      x-ngsi:
        model: https://schema.org/Number
        units: 'kilowatt hour (kWh)'
    totalActiveEnergyImport:
      description: 'Total energy imported i.e. consumed since metering started (since `dateEnergyMeteringStarted`).'
      minimum: 0
      type: Property
      x-ngsi:
        model: https://schema.org/Number
        units: 'kilowatt hour (kWh)'
    totalActivePower:
      description: 'Active power consumed (counting all phases)'
      type: Property
      x-ngsi:
        model: http://schema.org/Number
        units: 'watt (W)'
    totalApparentEnergyExport:
      description: 'Total energy exported (with regards to apparent power) since the metering start date (`dateEnergyMeteringStarted`)'
      minimum: 0
      type: Property
      x-ngsi:
        model: https://schema.org/Number
        units: 'kilovolt-ampere-reactive-hour (kVArh)'
    totalApparentEnergyImport:
      description: 'Total energy imported i.e. consumed (with regards to apparent power) since the metering start date (`dateEnergyMeteringStarted`)'
      minimum: 0
      type: Property
      x-ngsi:
        model: https://schema.org/Number
        units: 'kilovolt-ampere-hour (kVAh)'
    totalApparentPower:
      description: 'Apparent power consumed (counting all phases).'
      minimum: 0
      type: Property
      x-ngsi:
        model: http://schema.org/Number
        units: 'volt-ampere (VA)'
    totalDisplacementPowerFactor:
      description: 'Displacement power factor including all phases. The quantity is based on the fundamental frequency of the system'
      maximum: 1
      minimum: -1
      type: Property
      x-ngsi:
        model: http://schema.org/Number
        units: '-1 to +1'
    totalPowerFactor:
      description: 'Power factor including all phases'
      maximum: 1
      minimum: -1
      type: Property
      x-ngsi:
        model: http://schema.org/Number
        units: '-1 to +1'
    totalReactiveEnergyExport:
      description: 'Total fundamental frequency reactive energy exported since metering started (since `dateEnergyMeteringStarted`).'
      minimum: 0
      type: Property
      x-ngsi:
        model: https://schema.org/Number
        units: 'kilovolt-ampere-reactive-hour (kVArh)'
    totalReactiveEnergyImport:
      description: 'Total energy imported i.e. consumed (with regards to fundamental frequency reactive power) since the metering start date (`dateEnergyMeteringStarted`)'
      minimum: 0
      type: Property
      x-ngsi:
        model: https://schema.org/Number
        units: 'kilovolt-ampere-reactive-hour (kVArh)'
    totalReactivePower:
      description: 'Reactive power consumed (counting all phases)'
      type: Property
      x-ngsi:
        model: http://schema.org/Number
        units: 'volt-ampere-reactive (VAr)'
    type:
      description: 'It must be equal to `ThreePhaseAcMeasurement`.'
      enum:
        - ThreePhaseAcMeasurement
      type: Property
  required:
    - id
    - type
  type: object
```

## Examples
NGSI V2 key-values Example
```json
{
  "id": "fAM-8ca3-4533-a2eb-12015",
  "type": "Curve",
  "curveType": {
    "type": "Property",
    "value": "FLOW-HEAD"
  },
  "xData": {
    "type": "Property",
    "value": [
      0.5692,
      0.4647
    ]
  },
  "yData": {
    "type": "Property",
    "value": [
      0.5692,
      0.4647
    ]
  },
  "description": {
    "type": "Property",
    "value": "Free Text"
  },
  "tag": {
    "type": "Property",
    "value": "DMA1"
  }
}
```
NGSI V2 normalized Example
```json
{
    "id": "fAM-8ca3-4533-a2eb-12015",
    "type": "Curve",
    "dateCreated": {
        "type": "DateTime",
        "value": "2020-02-16T17:43:00Z"
    },
    "dateModified": {
        "type": "DateTime",
        "value": "2020-02-16T17:43:00Z"
    },
    "curveType": {
        "value": "FLOW-HEAD"
    },
    "xData": {
        "value": [
            0.5692,
            0.4647
        ]
    },
    "yData": {
        "value": [
            0.5692,
            0.4647
        ]
    },
    "description": {
        "value": "Free Text"
    },
    "tag": {
        "value": "DMA1"
    }
}
```
NGSI-LD key-values Example
```json
{
  "@context": [
    "https://schema.lab.fiware.org/ld/context"
  ],
  "id": "fAM-8ca3-4533-a2eb-12015",
  "type": "Curve",
  "curveType": {
    "type": "Property",
    "value": "FLOW-HEAD"
  },
  "xData": {
    "type": "Property",
    "value": [
      0.5692,
      0.4647
    ]
  },
  "yData": {
    "type": "Property",
    "value": [
      0.5692,
      0.4647
    ]
  },
  "description": {
    "type": "Property",
    "value": "Free Text"
  },
  "tag": {
    "type": "Property",
    "value": "DMA1"
  }
}
```
NGSI-LD normalized Example
```json
{
    "id": "urn:ngsi-ld:Curve:fAM-8ca3-4533-a2eb-12015",
    "type": "Curve",
    "createdAt": "2020-02-16T17:43:00Z",
    "modifiedAt": "2020-02-16T17:43:00Z",
    "curveType":{
        "type": "Property",
        "value": "FLOW-HEAD"
    },
    "xData": {
        "type": "Property",
        "value": [0.5692, 0.4647],
        "unitCode":"C62"
    },
    "yData": {
        "type": "Property",
        "value": [0.5692, 0.4647],
        "unitCode":"C62"
    },
    "description": {
        "type": "Property",
        "value": "Free Text"
    },
    "tag": {
        "type": "Property",
        "value": "DMA1"
    },
    "@context": [
        "https://schema.lab.fiware.org/ld/context"
    ]
}
```
