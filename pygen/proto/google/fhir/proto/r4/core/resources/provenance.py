# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Provenance:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    target: Reference
    occurred: Provenance_OccurredX
    recorded: Instant
    policy: Uri
    location: Reference
    reason: CodeableConcept
    activity: CodeableConcept
    agent: Provenance_Agent
    entity: Provenance_Entity
    signature: Signature


@dataclass
class Provenance_OccurredX:
    period: Period
    date_time: DateTime


@dataclass
class Provenance_Agent:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    role: CodeableConcept
    who: Reference
    on_behalf_of: Reference


@dataclass
class Provenance_Entity:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: Provenance_Entity_RoleCode
    what: Reference
    agent: Provenance_Agent


@dataclass
class Provenance_Entity_RoleCode:
    value: ProvenanceEntityRoleCode_Value
    id: String
    extension: Extension

