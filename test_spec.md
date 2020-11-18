
Entity ThreePhaseAcMeasurement
==============================


Text to be included between overall title and description.  
  
Global description: An electrical  measurement from a system that uses three phase alternating current.
## Data Model


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
Text to be included after list of properties
```

## Examples
NGSI V2 key-values Example
```json
{
  "id": "ThreePhaseAcMeasurement:LV3_Ventilation",
  "type": "ThreePhaseAcMeasurement",
  "dateEnergyMeteringStarted": "2018-07-07T15:05:59.408Z",
  "refDevice": ["Device:eQL-EDF3GL-2006201705"],
  "name": "HKAPK0200",
  "description": "measurement corresponding to the ventilation machine rooms",
  "totalActiveEnergyImport": 150781.96448,
  "totalReactiveEnergyImport": 20490.3392,
  "totalActiveEnergyExport": 1059.80176,
  "totalReactiveEnergyExport": 93275.02176,
  "totalActivePower": 31700.269531,
  "activePower": {
    "L1": 11996.416016,
    "L2": 9461.501953,
    "L3": 10242.351562
  },
  "totalReactivePower": -7830.332031,
  "reactivePower": {
    "L1": -2612.606934,
    "L2": -2209.906006,
    "L3": -3007.81958
  },
  "totalApparentPower": 36019.089844,
  "apparentPower": {
    "L1": 13201.412109,
    "L2": 10755.304688,
    "L3": 11941.094727
  },
  "powerFactor": {
    "L1": 0.908817,
    "L2": 0.879906,
    "L3": 0.859293
  },
  "displacementPowerFactor": {
    "L1": 0.978013,
    "L2": 0.973317,
    "L3": 0.960382
  },
  "frequency": 50.020672,
  "current": {
    "L1": 56.126038,
    "L2": 45.894356,
    "L3": 50.872452,
    "N": 0.0
  },
  "phaseVoltage": {
    "L1": 234.961304,
    "L2": 234.563477,
    "L3": 235.354034
  },
  "phaseToPhaseVoltage": {
    "L12": 406.769196,
    "L23": 407.081238,
    "L31": 407.734558
  },
  "thdVoltage": {
    "L1": 0.01471114,
    "L2": 0.01600046,
    "L3": 0.01541459
  },
  "thdCurrent": {
    "L1": 0.38497337,
    "L2": 0.45807529,
    "L3": 0.4938652
  }
}
```
NGSI V2 normalized Example
```json
{
  "id": "ThreePhaseAcMeasurement:LV3_Ventilation",
  "type": "ThreePhaseAcMeasurement",
  "dateEnergyMeteringStarted": {
    "type": "DateTime",
    "value": "2018-07-07T15:05:59.408Z"
  },
  "refDevice": {
    "type": "Relationship",
    "value": ["Device:eQL-EDF3GL-2006201705"]
  },
  "name": {
    "value": "HKAPK0200"
  },
  "description": {
    "value": "measurement corresponding to the ventilation machine rooms"
  },
  "totalActiveEnergyImport": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      }
    },
    "value": 150781.96448
  },
  "totalReactiveEnergyImport": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      }
    },
    "value": 20490.3392
  },
  "totalActiveEnergyExport": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      }
    },
    "value": 1059.80176
  },
  "totalReactiveEnergyExport": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      }
    },
    "value": 93275.02176
  },
  "totalActivePower": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "average"
      },
      "measurementInterval": {
        "value": 1
      }
    },
    "value": 31700.269531
  },
  "activePower": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "average"
      },
      "measurementInterval": {
        "value": 1
      }
    },
    "type": "StructuredValue",
    "value": {
      "L1": 11996.416016,
      "L2": 9461.501953,
      "L3": 10242.351562
    }
  },
  "totalReactivePower": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "average"
      },
      "measurementInterval": {
        "value": 1
      }
    },
    "value": -7830.332031
  },
  "reactivePower": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "average"
      },
      "measurementInterval": {
        "value": 1
      }
    },
    "type": "StructuredValue",
    "value": {
      "L1": -2612.606934,
      "L2": -2209.906006,
      "L3": -3007.81958
    }
  },
  "totalApparentPower": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "average"
      },
      "measurementInterval": {
        "value": 1
      }
    },
    "value": 36019.089844
  },
  "apparentPower": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "average"
      },
      "measurementInterval": {
        "value": 1
      }
    },
    "type": "StructuredValue",
    "value": {
      "L1": 13201.412109,
      "L2": 10755.304688,
      "L3": 11941.094727
    }
  },
  "powerFactor": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "average"
      },
      "measurementInterval": {
        "value": 1
      },
      "onlyPositive": {
        "value": true
      }
    },
    "type": "StructuredValue",
    "value": {
      "L1": 0.908817,
      "L2": 0.879906,
      "L3": 0.859293
    }
  },
  "displacementPowerFactor": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "average"
      },
      "measurementInterval": {
        "value": 1
      },
      "onlyPositive": {
        "value": true
      }
    },
    "type": "StructuredValue",
    "value": {
      "L1": 0.978013,
      "L2": 0.973317,
      "L3": 0.960382
    }
  },
  "frequency": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "average"
      },
      "measurementInterval": {
        "value": 1
      }
    },
    "value": 50.020672
  },
  "current": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "rms"
      },
      "measurementInterval": {
        "value": 1
      }
    },
    "type": "StructuredValue",
    "value": {
      "L1": 56.126038,
      "L2": 45.894356,
      "L3": 50.872452,
      "N": 0.0
    }
  },
  "phaseVoltage": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "rms"
      },
      "measurementInterval": {
        "value": 1
      }
    },
    "type": "StructuredValue",
    "value": {
      "L1": 234.961304,
      "L2": 234.563477,
      "L3": 235.354034
    }
  },
  "phaseToPhaseVoltage": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "rms"
      },
      "measurementInterval": {
        "value": 1
      }
    },
    "type": "StructuredValue",
    "value": {
      "L12": 406.769196,
      "L23": 407.081238,
      "L31": 407.734558
    }
  },
  "thdVoltage": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "average"
      },
      "measurementInterval": {
        "value": 1
      }
    },
    "type": "StructuredValue",
    "value": {
      "L1": 0.01471114,
      "L2": 0.01600046,
      "L3": 0.01541459
    }
  },
  "thdCurrent": {
    "metadata": {
      "timestamp": {
        "type": "DateTime",
        "value": "2019-01-24T22:00:00.173Z"
      },
      "measurementType": {
        "value": "average"
      },
      "measurementInterval": {
        "value": 1
      }
    },
    "type": "StructuredValue",
    "value": {
      "L1": 0.38497337,
      "L2": 0.45807529,
      "L3": 0.4938652
    }
  }
}
```
NGSI-LD key-values Example
```json
{"@context": ["https://schema.lab.fiware.org/ld/context",
              "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"],
 "activePower": {"L1": 11996.416016, "L2": 9461.501953, "L3": 10242.351562},
 "apparentPower": {"L1": 13201.412109, "L2": 10755.304688, "L3": 11941.094727},
 "current": {"L1": 56.126038, "L2": 45.894356, "L3": 50.872452, "N": 0.0},
 "dateEnergyMeteringStarted": {"@type": "DateTime",
                               "@value": "2018-07-07T15:05:59.408Z"},
 "description": "measurement corresponding to the ventilation machine rooms",
 "displacementPowerFactor": {"L1": 0.978013, "L2": 0.973317, "L3": 0.960382},
 "frequency": 50.020672,
 "id": "urn:ngsi-ld:ThreePhaseAcMeasurement:ThreePhaseAcMeasurement:LV3_Ventilation",
 "name": "HKAPK0200",
 "phaseToPhaseVoltage": {"L12": 406.769196,
                         "L23": 407.081238,
                         "L31": 407.734558},
 "phaseVoltage": {"L1": 234.961304, "L2": 234.563477, "L3": 235.354034},
 "powerFactor": {"L1": 0.908817, "L2": 0.879906, "L3": 0.859293},
 "reactivePower": {"L1": -2612.606934, "L2": -2209.906006, "L3": -3007.81958},
 "refDevice": ["urn:ngsi-ld:Device:Device:eQL-EDF3GL-2006201705"],
 "thdCurrent": {"L1": 0.38497337, "L2": 0.45807529, "L3": 0.4938652},
 "thdVoltage": {"L1": 0.01471114, "L2": 0.01600046, "L3": 0.01541459},
 "totalActiveEnergyExport": 1059.80176,
 "totalActiveEnergyImport": 150781.96448,
 "totalActivePower": 31700.269531,
 "totalApparentPower": 36019.089844,
 "totalReactiveEnergyExport": 93275.02176,
 "totalReactiveEnergyImport": 20490.3392,
 "totalReactivePower": -7830.332031,
 "type": "ThreePhaseAcMeasurement"}
```
NGSI-LD normalized Example
```json
{
    "id": "urn:ngsi-ld:ThreePhaseAcMeasurement:ThreePhaseAcMeasurement:LV3_Ventilation",
    "type": "ThreePhaseAcMeasurement",
    "dateEnergyMeteringStarted": {
        "type": "Property",
        "value": {
            "@type": "DateTime",
            "@value": "2018-07-07T15:05:59.408Z"
        }
    },
    "refDevice": {
        "type": "Relationship",
        "object": [
            "urn:ngsi-ld:Device:Device:eQL-EDF3GL-2006201705"
        ]
    },
    "name": {
        "type": "Property",
        "value": "HKAPK0200"
    },
    "description": {
        "type": "Property",
        "value": "measurement corresponding to the ventilation machine rooms"
    },
    "totalActiveEnergyImport": {
        "type": "Property",
        "value": 150781.96448,
        "observedAt": "2019-01-24T22:00:00.173Z"
    },
    "totalReactiveEnergyImport": {
        "type": "Property",
        "value": 20490.3392,
        "observedAt": "2019-01-24T22:00:00.173Z"
    },
    "totalActiveEnergyExport": {
        "type": "Property",
        "value": 1059.80176,
        "observedAt": "2019-01-24T22:00:00.173Z"
    },
    "totalReactiveEnergyExport": {
        "type": "Property",
        "value": 93275.02176,
        "observedAt": "2019-01-24T22:00:00.173Z"
    },
    "totalActivePower": {
        "type": "Property",
        "value": 31700.269531,
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "average"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        }
    },
    "activePower": {
        "type": "Property",
        "value": {
            "L1": 11996.416016,
            "L2": 9461.501953,
            "L3": 10242.351562
        },
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "average"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        }
    },
    "totalReactivePower": {
        "type": "Property",
        "value": -7830.332031,
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "average"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        }
    },
    "reactivePower": {
        "type": "Property",
        "value": {
            "L1": -2612.606934,
            "L2": -2209.906006,
            "L3": -3007.81958
        },
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "average"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        }
    },
    "totalApparentPower": {
        "type": "Property",
        "value": 36019.089844,
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "average"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        }
    },
    "apparentPower": {
        "type": "Property",
        "value": {
            "L1": 13201.412109,
            "L2": 10755.304688,
            "L3": 11941.094727
        },
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "average"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        }
    },
    "powerFactor": {
        "type": "Property",
        "value": {
            "L1": 0.908817,
            "L2": 0.879906,
            "L3": 0.859293
        },
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "average"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        },
        "onlyPositive": {
            "type": "Property",
            "value": true
        }
    },
    "displacementPowerFactor": {
        "type": "Property",
        "value": {
            "L1": 0.978013,
            "L2": 0.973317,
            "L3": 0.960382
        },
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "average"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        },
        "onlyPositive": {
            "type": "Property",
            "value": true
        }
    },
    "frequency": {
        "type": "Property",
        "value": 50.020672,
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "average"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        }
    },
    "current": {
        "type": "Property",
        "value": {
            "L1": 56.126038,
            "L2": 45.894356,
            "L3": 50.872452,
            "N": 0.0
        },
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "rms"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        }
    },
    "phaseVoltage": {
        "type": "Property",
        "value": {
            "L1": 234.961304,
            "L2": 234.563477,
            "L3": 235.354034
        },
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "rms"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        }
    },
    "phaseToPhaseVoltage": {
        "type": "Property",
        "value": {
            "L12": 406.769196,
            "L23": 407.081238,
            "L31": 407.734558
        },
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "rms"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        }
    },
    "thdVoltage": {
        "type": "Property",
        "value": {
            "L1": 0.01471114,
            "L2": 0.01600046,
            "L3": 0.01541459
        },
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "average"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        }
    },
    "thdCurrent": {
        "type": "Property",
        "value": {
            "L1": 0.38497337,
            "L2": 0.45807529,
            "L3": 0.4938652
        },
        "observedAt": "2019-01-24T22:00:00.173Z",
        "measurementType": {
            "type": "Property",
            "value": "average"
        },
        "measurementInterval": {
            "type": "Property",
            "value": 1
        }
    },
    "@context": [
        "https://schema.lab.fiware.org/ld/context",
        "https://uri.etsi.org/ngsi-ld/v1/ngsi-ld-core-context.jsonld"
    ]
}
```
Text after  all
