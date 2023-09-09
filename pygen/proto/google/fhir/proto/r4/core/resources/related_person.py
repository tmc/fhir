# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class RelatedPerson:
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
    patient: Reference
    relationship: CodeableConcept
    name: HumanName
    telecom: ContactPoint
    gender: RelatedPerson_GenderCode
    birth_date: Date
    address: Address
    photo: Attachment
    period: Period
    communication: RelatedPerson_Communication


@dataclass
class RelatedPerson_GenderCode:
    value: AdministrativeGenderCode_Value
    id: String
    extension: Extension


@dataclass
class RelatedPerson_Communication:
    id: String
    extension: Extension
    modifier_extension: Extension
    language: CodeableConcept
    preferred: Boolean

