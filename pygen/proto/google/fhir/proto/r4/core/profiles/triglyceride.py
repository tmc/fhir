# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Triglyceride:
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
    status: Triglyceride_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    focus: Reference
    encounter: Reference
    effective: Triglyceride_EffectiveX
    issued: Instant
    performer: Reference
    value: Triglyceride_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: Triglyceride_ReferenceRange
    component: Triglyceride_Component


@dataclass
class Triglyceride_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Triglyceride_EffectiveX:
    date_time: DateTime
    period: Period
    timing: Timing
    instant: Instant


@dataclass
class Triglyceride_ValueX:
    quantity: Quantity


@dataclass
class Triglyceride_ReferenceRange:
    id: String
    extension: Extension
    modifier_extension: Extension
    high: SimpleQuantity
    text: String


@dataclass
class Triglyceride_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Triglyceride_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: Triglyceride_ReferenceRange


@dataclass
class Triglyceride_Component_ValueX:
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

