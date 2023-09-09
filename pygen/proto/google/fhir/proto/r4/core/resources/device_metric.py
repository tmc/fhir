# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class DeviceMetric:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type: CodeableConcept
    unit: CodeableConcept
    source: Reference
    parent: Reference
    operational_status: DeviceMetric_OperationalStatusCode
    color: DeviceMetric_ColorCode
    category: DeviceMetric_CategoryCode
    measurement_period: Timing
    calibration: DeviceMetric_Calibration


@dataclass
class DeviceMetric_OperationalStatusCode:
    value: DeviceMetricOperationalStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceMetric_ColorCode:
    value: DeviceMetricColorCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceMetric_CategoryCode:
    value: DeviceMetricCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceMetric_Calibration:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: DeviceMetric_Calibration_TypeCode
    state: DeviceMetric_Calibration_StateCode
    time: Instant


@dataclass
class DeviceMetric_Calibration_TypeCode:
    value: DeviceMetricCalibrationTypeCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceMetric_Calibration_StateCode:
    value: DeviceMetricCalibrationStateCode_Value
    id: String
    extension: Extension

