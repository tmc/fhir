# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Slot:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    service_category: CodeableConcept
    service_type: CodeableConcept
    specialty: CodeableConcept
    appointment_type: CodeableConcept
    schedule: Reference
    status: Slot_StatusCode
    start: Instant
    end: Instant
    overbooked: Boolean
    comment: String


@dataclass
class Slot_StatusCode:
    value: SlotStatusCode_Value
    id: String
    extension: Extension

