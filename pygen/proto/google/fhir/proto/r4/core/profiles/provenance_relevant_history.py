# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ProvenanceRelevantHistory:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    target: Reference
    occurred: ProvenanceRelevantHistory_OccurredX
    recorded: Instant
    policy: Uri
    location: Reference
    reason: CodeableConcept
    activity: CodeableConcept
    agent: ProvenanceRelevantHistory_Agent
    entity: ProvenanceRelevantHistory_Entity
    signature: Signature


@dataclass
class ProvenanceRelevantHistory_OccurredX:
    date_time: DateTime


@dataclass
class ProvenanceRelevantHistory_Agent:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    role: CodeableConcept
    who: Reference
    on_behalf_of: Reference


@dataclass
class ProvenanceRelevantHistory_Entity:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: ProvenanceRelevantHistory_Entity_RoleCode
    what: Reference
    agent: ProvenanceRelevantHistory_Agent


@dataclass
class ProvenanceRelevantHistory_Entity_RoleCode:
    value: ProvenanceEntityRoleCode_Value
    id: String
    extension: Extension

