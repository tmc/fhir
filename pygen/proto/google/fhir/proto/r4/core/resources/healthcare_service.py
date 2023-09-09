# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class HealthcareService:
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
    provided_by: Reference
    category: CodeableConcept
    type: CodeableConcept
    specialty: CodeableConcept
    location: Reference
    name: String
    comment: String
    extra_details: Markdown
    photo: Attachment
    telecom: ContactPoint
    coverage_area: Reference
    service_provision_code: CodeableConcept
    eligibility: HealthcareService_Eligibility
    program: CodeableConcept
    characteristic: CodeableConcept
    communication: CodeableConcept
    referral_method: CodeableConcept
    appointment_required: Boolean
    available_time: HealthcareService_AvailableTime
    not_available: HealthcareService_NotAvailable
    availability_exceptions: String
    endpoint: Reference


@dataclass
class HealthcareService_Eligibility:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    comment: Markdown


@dataclass
class HealthcareService_AvailableTime:
    id: String
    extension: Extension
    modifier_extension: Extension
    days_of_week: HealthcareService_AvailableTime_DaysOfWeekCode
    all_day: Boolean
    available_start_time: Time
    available_end_time: Time


@dataclass
class HealthcareService_AvailableTime_DaysOfWeekCode:
    value: DaysOfWeekCode_Value
    id: String
    extension: Extension


@dataclass
class HealthcareService_NotAvailable:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    during: Period

