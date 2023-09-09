# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ClinicalDocument:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ClinicalDocument_StatusCode
    type: CodeableConcept
    category: CodeableConcept
    subject: Reference
    encounter: Reference
    date: DateTime
    author: Reference
    title: String
    confidentiality: ClinicalDocument_ConfidentialityCode
    attester: ClinicalDocument_Attester
    custodian: Reference
    relates_to: ClinicalDocument_RelatesTo
    event: ClinicalDocument_Event
    section: ClinicalDocument_Section
    version_number: String


@dataclass
class ClinicalDocument_StatusCode:
    value: CompositionStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ClinicalDocument_ConfidentialityCode:
    value: V3ConfidentialityClassificationValueSet_Value
    id: String
    extension: Extension


@dataclass
class ClinicalDocument_Attester:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: ClinicalDocument_Attester_ModeCode
    time: DateTime
    party: Reference


@dataclass
class ClinicalDocument_Attester_ModeCode:
    value: CompositionAttestationModeCode_Value
    id: String
    extension: Extension


@dataclass
class ClinicalDocument_RelatesTo:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: ClinicalDocument_RelatesTo_CodeType
    target: ClinicalDocument_RelatesTo_TargetX


@dataclass
class ClinicalDocument_RelatesTo_CodeType:
    value: DocumentRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ClinicalDocument_RelatesTo_TargetX:
    identifier: Identifier
    reference: Reference


@dataclass
class ClinicalDocument_Event:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    period: Period
    detail: Reference


@dataclass
class ClinicalDocument_Section:
    id: String
    extension: Extension
    modifier_extension: Extension
    title: String
    code: CodeableConcept
    author: Reference
    focus: Reference
    text: Narrative
    mode: ClinicalDocument_Section_ModeCode
    ordered_by: CodeableConcept
    entry: Reference
    empty_reason: CodeableConcept
    section: ClinicalDocument_Section


@dataclass
class ClinicalDocument_Section_ModeCode:
    value: ListModeCode_Value
    id: String
    extension: Extension

