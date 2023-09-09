# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class AppointmentResponse:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    appointment: Reference
    start: Instant
    end: Instant
    participant_type: CodeableConcept
    actor: Reference
    participant_status: AppointmentResponse_ParticipantStatusCode
    comment: String


@dataclass
class AppointmentResponse_ParticipantStatusCode:
    value: ParticipationStatusCode_Value
    id: String
    extension: Extension

