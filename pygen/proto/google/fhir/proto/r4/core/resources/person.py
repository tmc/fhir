# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Person:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    name: HumanName
    telecom: ContactPoint
    gender: Person_GenderCode
    birth_date: Date
    address: Address
    photo: Attachment
    managing_organization: Reference
    active: Boolean
    link: Person_Link


@dataclass
class Person_GenderCode:
    value: AdministrativeGenderCode_Value
    id: String
    extension: Extension


@dataclass
class Person_Link:
    id: String
    extension: Extension
    modifier_extension: Extension
    target: Reference
    assurance: Person_Link_AssuranceCode


@dataclass
class Person_Link_AssuranceCode:
    value: IdentityAssuranceLevelCode_Value
    id: String
    extension: Extension

