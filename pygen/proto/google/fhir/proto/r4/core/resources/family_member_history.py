# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class FamilyMemberHistory:
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
    status: FamilyMemberHistory_StatusCode
    data_absent_reason: CodeableConcept
    patient: Reference
    date: DateTime
    name: String
    relationship: CodeableConcept
    sex: CodeableConcept
    born: FamilyMemberHistory_BornX
    age: FamilyMemberHistory_AgeX
    estimated_age: Boolean
    deceased: FamilyMemberHistory_DeceasedX
    reason_code: CodeableConcept
    reason_reference: Reference
    note: Annotation
    condition: FamilyMemberHistory_Condition


@dataclass
class FamilyMemberHistory_StatusCode:
    value: FamilyHistoryStatusCode_Value
    id: String
    extension: Extension


@dataclass
class FamilyMemberHistory_BornX:
    period: Period
    date: Date
    string_value: String


@dataclass
class FamilyMemberHistory_AgeX:
    age: Age
    range: Range
    string_value: String


@dataclass
class FamilyMemberHistory_DeceasedX:
    boolean: Boolean
    age: Age
    range: Range
    date: Date
    string_value: String


@dataclass
class FamilyMemberHistory_Condition:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    outcome: CodeableConcept
    contributed_to_death: Boolean
    onset: FamilyMemberHistory_Condition_OnsetX
    note: Annotation


@dataclass
class FamilyMemberHistory_Condition_OnsetX:
    age: Age
    range: Range
    period: Period
    string_value: String

