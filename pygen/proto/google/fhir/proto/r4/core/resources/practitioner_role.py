# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class PractitionerRole:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    active: Boolean
    period: Period
    practitioner: Reference
    organization: Reference
    code: CodeableConcept
    specialty: CodeableConcept
    location: Reference
    healthcare_service: Reference
    telecom: ContactPoint
    available_time: PractitionerRole_AvailableTime
    not_available: PractitionerRole_NotAvailable
    availability_exceptions: String
    endpoint: Reference


@dataclass
class PractitionerRole_AvailableTime:
    id: String
    extension: Extension
    modifier_extension: Extension
    days_of_week: PractitionerRole_AvailableTime_DaysOfWeekCode
    all_day: Boolean
    available_start_time: Time
    available_end_time: Time


@dataclass
class PractitionerRole_AvailableTime_DaysOfWeekCode:
    value: DaysOfWeekCode_Value
    id: String
    extension: Extension


@dataclass
class PractitionerRole_NotAvailable:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    during: Period

