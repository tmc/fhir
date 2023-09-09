# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class VerificationResult:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    target: Reference
    target_location: String
    need: CodeableConcept
    status: VerificationResult_StatusCode
    status_date: DateTime
    validation_type: CodeableConcept
    validation_process: CodeableConcept
    frequency: Timing
    last_performed: DateTime
    next_scheduled: Date
    failure_action: CodeableConcept
    primary_source: VerificationResult_PrimarySource
    attestation: VerificationResult_Attestation
    validator: VerificationResult_Validator


@dataclass
class VerificationResult_StatusCode:
    value: StatusCode_Value
    id: String
    extension: Extension


@dataclass
class VerificationResult_PrimarySource:
    id: String
    extension: Extension
    modifier_extension: Extension
    who: Reference
    type: CodeableConcept
    communication_method: CodeableConcept
    validation_status: CodeableConcept
    validation_date: DateTime
    can_push_updates: CodeableConcept
    push_type_available: CodeableConcept


@dataclass
class VerificationResult_Attestation:
    id: String
    extension: Extension
    modifier_extension: Extension
    who: Reference
    on_behalf_of: Reference
    communication_method: CodeableConcept
    date: Date
    source_identity_certificate: String
    proxy_identity_certificate: String
    proxy_signature: Signature
    source_signature: Signature


@dataclass
class VerificationResult_Validator:
    id: String
    extension: Extension
    modifier_extension: Extension
    organization: Reference
    identity_certificate: String
    attestation_signature: Signature

