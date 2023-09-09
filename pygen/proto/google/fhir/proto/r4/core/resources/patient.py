# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Patient:
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
    name: HumanName
    telecom: ContactPoint
    gender: Patient_GenderCode
    birth_date: Date
    deceased: Patient_DeceasedX
    address: Address
    marital_status: CodeableConcept
    multiple_birth: Patient_MultipleBirthX
    photo: Attachment
    contact: Patient_Contact
    communication: Patient_Communication
    general_practitioner: Reference
    managing_organization: Reference
    link: Patient_Link


@dataclass
class Patient_GenderCode:
    value: AdministrativeGenderCode_Value
    id: String
    extension: Extension


@dataclass
class Patient_DeceasedX:
    boolean: Boolean
    date_time: DateTime


@dataclass
class Patient_MultipleBirthX:
    boolean: Boolean
    integer: Integer


@dataclass
class Patient_Contact:
    id: String
    extension: Extension
    modifier_extension: Extension
    relationship: CodeableConcept
    name: HumanName
    telecom: ContactPoint
    address: Address
    gender: Patient_Contact_GenderCode
    organization: Reference
    period: Period


@dataclass
class Patient_Contact_GenderCode:
    value: AdministrativeGenderCode_Value
    id: String
    extension: Extension


@dataclass
class Patient_Communication:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: CodeableConcept
    preferred: Boolean


@dataclass
class Patient_Link:
    id: String
    extension: Extension
    modifier_extension: Extension
    other: Reference
    type: Patient_Link_TypeCode


@dataclass
class Patient_Link_TypeCode:
    value: LinkTypeCode_Value
    id: String
    extension: Extension

