# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ProfileForCatalog:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ProfileForCatalog_StatusCode
    type: CodeableConcept
    category: CodeableConcept
    encounter: Reference
    author: Reference
    title: String
    confidentiality: ProfileForCatalog_ConfidentialityCode
    attester: ProfileForCatalog_Attester
    custodian: Reference
    relates_to: ProfileForCatalog_RelatesTo
    event: ProfileForCatalog_Event
    section: ProfileForCatalog_Section
    validity_period: DateTime


@dataclass
class ProfileForCatalog_StatusCode:
    value: CompositionStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ProfileForCatalog_ConfidentialityCode:
    value: V3ConfidentialityClassificationValueSet_Value
    id: String
    extension: Extension


@dataclass
class ProfileForCatalog_Attester:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: ProfileForCatalog_Attester_ModeCode
    time: DateTime
    party: Reference


@dataclass
class ProfileForCatalog_Attester_ModeCode:
    value: CompositionAttestationModeCode_Value
    id: String
    extension: Extension


@dataclass
class ProfileForCatalog_RelatesTo:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: ProfileForCatalog_RelatesTo_CodeType
    target: ProfileForCatalog_RelatesTo_TargetX


@dataclass
class ProfileForCatalog_RelatesTo_CodeType:
    value: DocumentRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ProfileForCatalog_RelatesTo_TargetX:
    identifier: Identifier
    reference: Reference


@dataclass
class ProfileForCatalog_Event:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    period: Period
    detail: Reference


@dataclass
class ProfileForCatalog_Section:
    id: String
    extension: Extension
    modifier_extension: Extension
    title: String
    code: CodeableConcept
    author: Reference
    focus: Reference
    text: Narrative
    mode: ProfileForCatalog_Section_ModeCode
    ordered_by: CodeableConcept
    entry: Reference
    empty_reason: CodeableConcept
    section: ProfileForCatalog_Section


@dataclass
class ProfileForCatalog_Section_ModeCode:
    value: ListModeCode_Value
    id: String
    extension: Extension

