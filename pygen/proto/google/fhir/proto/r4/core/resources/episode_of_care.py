# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class EpisodeOfCare:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: EpisodeOfCare_StatusCode
    status_history: EpisodeOfCare_StatusHistory
    type: CodeableConcept
    diagnosis: EpisodeOfCare_Diagnosis
    patient: Reference
    managing_organization: Reference
    period: Period
    referral_request: Reference
    care_manager: Reference
    team: Reference
    account: Reference


@dataclass
class EpisodeOfCare_StatusCode:
    value: EpisodeOfCareStatusCode_Value
    id: String
    extension: Extension


@dataclass
class EpisodeOfCare_StatusHistory:
    id: String
    extension: Extension
    modifier_extension: Extension
    status: EpisodeOfCare_StatusHistory_StatusCode
    period: Period


@dataclass
class EpisodeOfCare_StatusHistory_StatusCode:
    value: EpisodeOfCareStatusCode_Value
    id: String
    extension: Extension


@dataclass
class EpisodeOfCare_Diagnosis:
    id: String
    extension: Extension
    modifier_extension: Extension
    condition: Reference
    role: CodeableConcept
    rank: PositiveInt

