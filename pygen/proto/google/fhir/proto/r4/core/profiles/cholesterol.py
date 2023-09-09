# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Cholesterol:
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
    status: Cholesterol_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    focus: Reference
    encounter: Reference
    effective: Cholesterol_EffectiveX
    issued: Instant
    performer: Reference
    value: Cholesterol_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Cholesterol_ReferenceRange
    component: Cholesterol_Component


@dataclass
class Cholesterol_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Cholesterol_EffectiveX:
    date_time: DateTime
    period: Period
    timing: Timing
    instant: Instant


@dataclass
class Cholesterol_ValueX:
    quantity: Quantity


@dataclass
class Cholesterol_ReferenceRange:
    id: String
    extension: Extension
    modifier_extension: Extension
    high: SimpleQuantity
    text: String


@dataclass
class Cholesterol_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Cholesterol_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Cholesterol_ReferenceRange


@dataclass
class Cholesterol_Component_ValueX:
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

