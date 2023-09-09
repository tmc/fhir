# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Encounter:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Encounter_StatusCode
    status_history: Encounter_StatusHistory
    class_value: Coding
    class_history: Encounter_ClassHistory
    type: CodeableConcept
    service_type: CodeableConcept
    priority: CodeableConcept
    subject: Reference
    episode_of_care: Reference
    based_on: Reference
    participant: Encounter_Participant
    appointment: Reference
    period: Period
    length: Duration
    reason_code: CodeableConcept
    reason_reference: Reference
    diagnosis: Encounter_Diagnosis
    account: Reference
    hospitalization: Encounter_Hospitalization
    location: Encounter_Location
    service_provider: Reference
    part_of: Reference


@dataclass
class Encounter_StatusCode:
    value: EncounterStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Encounter_StatusHistory:
    id: String
    extension: Extension
    modifier_extension: Extension
    status: Encounter_StatusHistory_StatusCode
    period: Period


@dataclass
class Encounter_StatusHistory_StatusCode:
    value: EncounterStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Encounter_ClassHistory:
    id: String
    extension: Extension
    modifier_extension: Extension
    class_value: Coding
    period: Period


@dataclass
class Encounter_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    period: Period
    individual: Reference


@dataclass
class Encounter_Diagnosis:
    id: String
    extension: Extension
    modifier_extension: Extension
    condition: Reference
    use: CodeableConcept
    rank: PositiveInt


@dataclass
class Encounter_Hospitalization:
    id: String
    extension: Extension
    modifier_extension: Extension
    pre_admission_identifier: Identifier
    origin: Reference
    admit_source: CodeableConcept
    re_admission: CodeableConcept
    diet_preference: CodeableConcept
    special_courtesy: CodeableConcept
    special_arrangement: CodeableConcept
    destination: Reference
    discharge_disposition: CodeableConcept


@dataclass
class Encounter_Location:
    id: String
    extension: Extension
    modifier_extension: Extension
    location: Reference
    status: Encounter_Location_StatusCode
    physical_type: CodeableConcept
    period: Period


@dataclass
class Encounter_Location_StatusCode:
    value: EncounterLocationStatusCode_Value
    id: String
    extension: Extension

