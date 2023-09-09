# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ObservationVitalspanel:
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
    status: ObservationVitalspanel_StatusCode
    category: CodeableConcept
    code: ObservationVitalspanel_CodeableConceptForCode
    subject: Reference
    focus: Reference
    encounter: Reference
    effective: ObservationVitalspanel_EffectiveX
    issued: Instant
    performer: Reference
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    note: Annotation
    body_site: CodeableConcept
    method: CodeableConcept
    specimen: Reference
    device: Reference
    reference_range: ObservationVitalspanel_ReferenceRange
    has_member: Reference
    derived_from: Reference
    component: ObservationVitalspanel_Component


@dataclass
class ObservationVitalspanel_StatusCode:
    value: ObservationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ObservationVitalspanel_CodeableConceptForCode:
    id: String
    extension: Extension
    coding: Coding
    text: String
    vitals_panel_code: CodingWithFixedCode


@dataclass
class ObservationVitalspanel_EffectiveX:
    date_time: DateTime
    period: Period


@dataclass
class ObservationVitalspanel_ReferenceRange:
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
class ObservationVitalspanel_Component:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: ObservationVitalspanel_Component_ValueX
    data_absent_reason: CodeableConcept
    interpretation: CodeableConcept
    reference_range: ObservationVitalspanel_ReferenceRange


@dataclass
class ObservationVitalspanel_Component_ValueX:
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

