# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ObservationBodyheight:
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
    status: ObservationBodyheight_StatusCode
    category: CodeableConcept
    code: ObservationBodyheight_CodeableConceptForCode
    subject: Reference
    focus: Reference
    encounter: Reference
    effective: ObservationBodyheight_EffectiveX
    issued: Instant
    performer: Reference
    value: ObservationBodyheight_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: ObservationBodyheight_ReferenceRange
    has_member: Reference
    derived_from: Reference
    component: ObservationBodyheight_Component


@dataclass
class ObservationBodyheight_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ObservationBodyheight_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    body_height_code: CodingWithFixedCode


@dataclass
class ObservationBodyheight_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class ObservationBodyheight_ValueX:
    quantity: Quantity


@dataclass
class ObservationBodyheight_ReferenceRange:
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
class ObservationBodyheight_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: ObservationBodyheight_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: ObservationBodyheight_ReferenceRange


@dataclass
class ObservationBodyheight_Component_ValueX:
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

