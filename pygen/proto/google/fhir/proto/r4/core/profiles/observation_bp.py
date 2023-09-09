# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ObservationBp:
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
    status: ObservationBp_StatusCode
    category: CodeableConcept
    code: ObservationBp_CodeableConceptForCode
    subject: Reference
    focus: Reference
    encounter: Reference
    effective: ObservationBp_EffectiveX
    issued: Instant
    performer: Reference
    value: ObservationBp_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: ObservationBp_ReferenceRange
    has_member: Reference
    derived_from: Reference
    component: ObservationBp_Component


@dataclass
class ObservationBp_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ObservationBp_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    bp_code: CodingWithFixedCode


@dataclass
class ObservationBp_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class ObservationBp_ValueX:
    quantity: Quantity


@dataclass
class ObservationBp_ReferenceRange:
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
class ObservationBp_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: ObservationBp_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: ObservationBp_ReferenceRange


@dataclass
class ObservationBp_Component_ValueX:
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

