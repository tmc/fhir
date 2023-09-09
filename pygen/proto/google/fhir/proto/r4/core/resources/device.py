# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Device:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    definition: Reference
    udi_carrier: Device_UdiCarrier
    status: Device_StatusCode
    status_reason: CodeableConcept
    distinct_identifier: String
    manufacturer: String
    manufacture_date: DateTime
    expiration_date: DateTime
    lot_number: String
    serial_number: String
    device_name: Device_DeviceName
    model_number: String
    part_number: String
    type: CodeableConcept
    specialization: Device_Specialization
    version: Device_Version
    property: Device_Property
    patient: Reference
    owner: Reference
    contact: ContactPoint
    location: Reference
    url: Uri
    note: Annotation
    safety: CodeableConcept
    parent: Reference


@dataclass
class Device_UdiCarrier:
    id: String
    extension: Extension
    modifier_extension: Extension
    device_identifier: String
    issuer: Uri
    jurisdiction: Uri
    carrier_aidc: Base64Binary
    carrier_hrf: String
    entry_type: Device_UdiCarrier_EntryTypeCode


@dataclass
class Device_UdiCarrier_EntryTypeCode:
    value: UDIEntryTypeCode_Value
    id: String
    extension: Extension


@dataclass
class Device_StatusCode:
    value: FHIRDeviceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Device_DeviceName:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    type: Device_DeviceName_TypeCode


@dataclass
class Device_DeviceName_TypeCode:
    value: DeviceNameTypeCode_Value
    id: String
    extension: Extension


@dataclass
class Device_Specialization:
    id: String
    extension: Extension
    modifier_extension: Extension
    system_type: CodeableConcept
    version: String


@dataclass
class Device_Version:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    component: Identifier
    value: String


@dataclass
class Device_Property:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    value_quantity: Quantity
    value_code: CodeableConcept

