# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ObservationHeartrate:
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
    status: ObservationHeartrate_StatusCode
    category: CodeableConcept
    code: ObservationHeartrate_CodeableConceptForCode
    subject: Reference
    focus: Reference
    encounter: Reference
    effective: ObservationHeartrate_EffectiveX
    issued: Instant
    performer: Reference
    value: ObservationHeartrate_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: ObservationHeartrate_ReferenceRange
    has_member: Reference
    derived_from: Reference
    component: ObservationHeartrate_Component


@dataclass
class ObservationHeartrate_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ObservationHeartrate_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    heart_rate_code: CodingWithFixedCode


@dataclass
class ObservationHeartrate_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class ObservationHeartrate_ValueX:
    quantity: Quantity


@dataclass
class ObservationHeartrate_ReferenceRange:
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
class ObservationHeartrate_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: ObservationHeartrate_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: ObservationHeartrate_ReferenceRange


@dataclass
class ObservationHeartrate_Component_ValueX:
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

