# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Procedure:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    instantiates_canonical: Canonical
    instantiates_uri: Uri
    based_on: Reference
    part_of: Reference
    status: Procedure_StatusCode
    status_reason: CodeableConcept
    category: CodeableConcept
    code: CodeableConcept
    subject: Reference
    encounter: Reference
    performed: Procedure_PerformedX
    recorder: Reference
    asserter: Reference
    performer: Procedure_Performer
    location: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    body_site: CodeableConcept
    outcome: CodeableConcept
    report: Reference
    complication: CodeableConcept
    complication_detail: Reference
    follow_up: CodeableConcept
    note: Annotation
    focal_device: Procedure_FocalDevice
    used_reference: Reference
    used_code: CodeableConcept


@dataclass
class Procedure_StatusCode:
    value: EventStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Procedure_PerformedX:
    date_time: DateTime
    period: Period
    string_value: String
    age: Age
    range: Range


@dataclass
class Procedure_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    function: CodeableConcept
    actor: Reference
    on_behalf_of: Reference


@dataclass
class Procedure_FocalDevice:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: CodeableConcept
    manipulated: Reference

