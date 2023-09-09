# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Appointment:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Appointment_StatusCode
    cancelation_reason: CodeableConcept
    service_category: CodeableConcept
    service_type: CodeableConcept
    specialty: CodeableConcept
    appointment_type: CodeableConcept
    reason_code: CodeableConcept
    reason_reference: Reference
    priority: UnsignedInt
    description: String
    supporting_information: Reference
    start: Instant
    end: Instant
    minutes_duration: PositiveInt
    slot: Reference
    created: DateTime
    comment: String
    patient_instruction: String
    based_on: Reference
    participant: Appointment_Participant
    requested_period: Period


@dataclass
class Appointment_StatusCode:
    value: AppointmentStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Appointment_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    actor: Reference
    required: Appointment_Participant_RequiredCode
    status: Appointment_Participant_StatusCode
    period: Period


@dataclass
class Appointment_Participant_RequiredCode:
    value: ParticipantRequiredCode_Value
    id: String
    extension: Extension


@dataclass
class Appointment_Participant_StatusCode:
    value: ParticipationStatusCode_Value
    id: String
    extension: Extension

