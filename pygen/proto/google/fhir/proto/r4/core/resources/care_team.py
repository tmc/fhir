# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CareTeam:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: CareTeam_StatusCode
    category: CodeableConcept
    name: String
    subject: Reference
    encounter: Reference
    period: Period
    participant: CareTeam_Participant
    reason_code: CodeableConcept
    reason_reference: Reference
    managing_organization: Reference
    telecom: ContactPoint
    note: Annotation


@dataclass
class CareTeam_StatusCode:
    value: CareTeamStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CareTeam_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    member: Reference
    on_behalf_of: Reference
    period: Period

