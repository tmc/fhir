# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class EHRSFMRecordLifecycleEventProvenance:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    target: Reference
    occurred: EHRSFMRecordLifecycleEventProvenance_OccurredX
    recorded: Instant
    policy: Uri
    location: Reference
    reason: CodeableConcept
    activity: CodeableConcept
    agent: EHRSFMRecordLifecycleEventProvenance_Agent
    entity: EHRSFMRecordLifecycleEventProvenance_Entity
    signature: Signature


@dataclass
class EHRSFMRecordLifecycleEventProvenance_OccurredX:
    period: Period
    date_time: DateTime


@dataclass
class EHRSFMRecordLifecycleEventProvenance_Agent:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    role: CodeableConcept
    who: Reference
    on_behalf_of: Reference


@dataclass
class EHRSFMRecordLifecycleEventProvenance_Entity:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: EHRSFMRecordLifecycleEventProvenance_Entity_RoleCode
    what: Reference
    agent: EHRSFMRecordLifecycleEventProvenance_Agent


@dataclass
class EHRSFMRecordLifecycleEventProvenance_Entity_RoleCode:
    value: ProvenanceEntityRoleCode_Value
    id: String
    extension: Extension

