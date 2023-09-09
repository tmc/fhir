# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ObservationBmi:
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
    status: ObservationBmi_StatusCode
    category: CodeableConcept
    code: ObservationBmi_CodeableConceptForCode
    subject: Reference
    focus: Reference
    encounter: Reference
    effective: ObservationBmi_EffectiveX
    issued: Instant
    performer: Reference
    value: ObservationBmi_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: ObservationBmi_ReferenceRange
    has_member: Reference
    derived_from: Reference
    component: ObservationBmi_Component


@dataclass
class ObservationBmi_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ObservationBmi_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    bmi_code: CodingWithFixedCode


@dataclass
class ObservationBmi_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class ObservationBmi_ValueX:
    quantity: Quantity


@dataclass
class ObservationBmi_ReferenceRange:
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
class ObservationBmi_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: ObservationBmi_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: ObservationBmi_ReferenceRange


@dataclass
class ObservationBmi_Component_ValueX:
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

