# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Composition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Composition_StatusCode
    type: CodeableConcept
    category: CodeableConcept
    subject: Reference
    encounter: Reference
    date: DateTime
    author: Reference
    title: String
    confidentiality: Composition_ConfidentialityCode
    attester: Composition_Attester
    custodian: Reference
    relates_to: Composition_RelatesTo
    event: Composition_Event
    section: Composition_Section


@dataclass
class Composition_StatusCode:
    value: CompositionStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Composition_ConfidentialityCode:
    value: V3ConfidentialityClassificationValueSet_Value
    id: String
    extension: Extension


@dataclass
class Composition_Attester:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: Composition_Attester_ModeCode
    time: DateTime
    party: Reference


@dataclass
class Composition_Attester_ModeCode:
    value: CompositionAttestationModeCode_Value
    id: String
    extension: Extension


@dataclass
class Composition_RelatesTo:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Composition_RelatesTo_CodeType
    target: Composition_RelatesTo_TargetX


@dataclass
class Composition_RelatesTo_CodeType:
    value: DocumentRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class Composition_RelatesTo_TargetX:
    identifier: Identifier
    reference: Reference


@dataclass
class Composition_Event:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    period: Period
    detail: Reference


@dataclass
class Composition_Section:
    id: String
    extension: Extension
    modifier_extension: Extension
    title: String
    code: CodeableConcept
    author: Reference
    focus: Reference
    text: Narrative
    mode: Composition_Section_ModeCode
    ordered_by: CodeableConcept
    entry: Reference
    empty_reason: CodeableConcept
    section: Composition_Section


@dataclass
class Composition_Section_ModeCode:
    value: ListModeCode_Value
    id: String
    extension: Extension

