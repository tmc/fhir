# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Condition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    clinical_status: CodeableConcept
    verification_status: CodeableConcept
    category: CodeableConcept
    severity: CodeableConcept
    code: CodeableConcept
    body_site: CodeableConcept
    subject: Reference
    encounter: Reference
    onset: Condition_OnsetX
    abatement: Condition_AbatementX
    recorded_date: DateTime
    recorder: Reference
    asserter: Reference
    stage: Condition_Stage
    evidence: Condition_Evidence
    note: Annotation


@dataclass
class Condition_OnsetX:
    date_time: DateTime
    age: Age
    period: Period
    range: Range
    string_value: String


@dataclass
class Condition_AbatementX:
    date_time: DateTime
    age: Age
    period: Period
    range: Range
    string_value: String


@dataclass
class Condition_Stage:
    id: String
    extension: Extension
    modifier_extension: Extension
    summary: CodeableConcept
    assessment: Reference
    type: CodeableConcept


@dataclass
class Condition_Evidence:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    detail: Reference

