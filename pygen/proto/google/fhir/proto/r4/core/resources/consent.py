# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Consent:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Consent_StatusCode
    scope: CodeableConcept
    category: CodeableConcept
    patient: Reference
    date_time: DateTime
    performer: Reference
    organization: Reference
    source: Consent_SourceX
    policy: Consent_Policy
    policy_rule: CodeableConcept
    verification: Consent_Verification
    provision: Consent_Provision


@dataclass
class Consent_StatusCode:
    value: ConsentStateCode_Value
    id: String
    extension: Extension


@dataclass
class Consent_SourceX:
    attachment: Attachment
    reference: Reference


@dataclass
class Consent_Policy:
    id: String
    extension: Extension
    modifier_extension: Extension
    authority: Uri
    uri: Uri


@dataclass
class Consent_Verification:
    id: String
    extension: Extension
    modifier_extension: Extension
    verified: Boolean
    verified_with: Reference
    verification_date: DateTime


@dataclass
class Consent_Provision:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: Consent_Provision_TypeCode
    period: Period
    actor: Consent_Provision_ProvisionActor
    action: CodeableConcept
    security_label: Coding
    purpose: Coding
    class_value: Coding
    code: CodeableConcept
    data_period: Period
    data: Consent_Provision_ProvisionData
    provision: Consent_Provision


@dataclass
class Consent_Provision_TypeCode:
    value: ConsentProvisionTypeCode_Value
    id: String
    extension: Extension


@dataclass
class Consent_Provision_ProvisionActor:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    reference: Reference


@dataclass
class Consent_Provision_ProvisionData:
    id: String
    extension: Extension
    modifier_extension: Extension
    meaning: Consent_Provision_ProvisionData_MeaningCode
    reference: Reference


@dataclass
class Consent_Provision_ProvisionData_MeaningCode:
    value: ConsentDataMeaningCode_Value
    id: String
    extension: Extension

