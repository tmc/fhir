# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class DeviceMetricObservationProfile:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    part_of: Reference
    status: DeviceMetricObservationProfile_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    focus: Reference
    effective: DeviceMetricObservationProfile_EffectiveX
    performer: Reference
    value: DeviceMetricObservationProfile_ValueX
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    device: Reference
    reference_range: DeviceMetricObservationProfile_ReferenceRange
    has_member: Reference
    derived_from: Reference
    component: DeviceMetricObservationProfile_Component


@dataclass
class DeviceMetricObservationProfile_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceMetricObservationProfile_EffectiveX:
    date_time: DateTime


@dataclass
class DeviceMetricObservationProfile_ValueX:
    quantity: Quantity
    codeable_concept: CodeableConcept
    string_value: String
    range: Range
    ratio: Ratio
    sampled_data: SampledData
    time: Time
    date_time: DateTime
    period: Period


@dataclass
class DeviceMetricObservationProfile_ReferenceRange:
    id: String
    extension: Extension
    modifier_extension: Extension
    low: SimpleQuantity
    high: SimpleQuantity
    type: CodeableConcept
    applies_to: CodeableConcept
    age: Range
    text: String


@dataclass
class DeviceMetricObservationProfile_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: DeviceMetricObservationProfile_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: DeviceMetricObservationProfile_ReferenceRange


@dataclass
class DeviceMetricObservationProfile_Component_ValueX:
    quantity: Quantity
    codeable_concept: CodeableConcept
    string_value: String
    boolean: Boolean
    integer: Integer
    range: Range
    ratio: Ratio
    sampled_data: SampledData
    time: Time
    date_time: DateTime
    period: Period

