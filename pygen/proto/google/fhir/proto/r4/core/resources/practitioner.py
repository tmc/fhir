# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Practitioner:
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
    address: Address
    gender: Practitioner_GenderCode
    birth_date: Date
    photo: Attachment
    qualification: Practitioner_Qualification
    communication: CodeableConcept


@dataclass
class Practitioner_GenderCode:
    value: AdministrativeGenderCode_Value
    id: String
    extension: Extension


@dataclass
class Practitioner_Qualification:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    code: CodeableConcept
    period: Period
    issuer: Reference

