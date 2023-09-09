# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class DeviceDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    udi_device_identifier: DeviceDefinition_UdiDeviceIdentifier
    manufacturer: DeviceDefinition_ManufacturerX
    device_name: DeviceDefinition_DeviceName
    model_number: String
    type: CodeableConcept
    specialization: DeviceDefinition_Specialization
    version: String
    safety: CodeableConcept
    shelf_life_storage: ProductShelfLife
    physical_characteristics: ProdCharacteristic
    language_code: CodeableConcept
    capability: DeviceDefinition_Capability
    property: DeviceDefinition_Property
    owner: Reference
    contact: ContactPoint
    url: Uri
    online_information: Uri
    note: Annotation
    quantity: Quantity
    parent_device: Reference
    material: DeviceDefinition_Material


@dataclass
class DeviceDefinition_UdiDeviceIdentifier:
    id: String
    extension: Extension
    modifier_extension: Extension
    device_identifier: String
    issuer: Uri
    jurisdiction: Uri


@dataclass
class DeviceDefinition_ManufacturerX:
    string_value: String
    reference: Reference


@dataclass
class DeviceDefinition_DeviceName:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    type: DeviceDefinition_DeviceName_TypeCode


@dataclass
class DeviceDefinition_DeviceName_TypeCode:
    value: DeviceNameTypeCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceDefinition_Specialization:
    id: String
    extension: Extension
    modifier_extension: Extension
    system_type: String
    version: String


@dataclass
class DeviceDefinition_Capability:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    description: CodeableConcept


@dataclass
class DeviceDefinition_Property:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    value_quantity: Quantity
    value_code: CodeableConcept


@dataclass
class DeviceDefinition_Material:
    id: String
    extension: Extension
    modifier_extension: Extension
    substance: CodeableConcept
    alternate: Boolean
    allergenic_indicator: Boolean

