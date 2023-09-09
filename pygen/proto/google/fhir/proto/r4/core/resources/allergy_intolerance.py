# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class AllergyIntolerance:
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
    type: AllergyIntolerance_TypeCode
    category: AllergyIntolerance_CategoryCode
    criticality: AllergyIntolerance_CriticalityCode
    code: CodeableConcept
    patient: Reference
    encounter: Reference
    onset: AllergyIntolerance_OnsetX
    recorded_date: DateTime
    recorder: Reference
    asserter: Reference
    last_occurrence: DateTime
    note: Annotation
    reaction: AllergyIntolerance_Reaction


@dataclass
class AllergyIntolerance_TypeCode:
    value: AllergyIntoleranceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class AllergyIntolerance_CategoryCode:
    value: AllergyIntoleranceCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class AllergyIntolerance_CriticalityCode:
    value: AllergyIntoleranceCriticalityCode_Value
    id: String
    extension: Extension


@dataclass
class AllergyIntolerance_OnsetX:
    date_time: DateTime
    age: Age
    period: Period
    range: Range
    string_value: String


@dataclass
class AllergyIntolerance_Reaction:
    id: String
    extension: Extension
    modifier_extension: Extension
    substance: CodeableConcept
    manifestation: CodeableConcept
    description: String
    onset: DateTime
    severity: AllergyIntolerance_Reaction_SeverityCode
    exposure_route: CodeableConcept
    note: Annotation


@dataclass
class AllergyIntolerance_Reaction_SeverityCode:
    value: AllergyIntoleranceSeverityCode_Value
    id: String
    extension: Extension

