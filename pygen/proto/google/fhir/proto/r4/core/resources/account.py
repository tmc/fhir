# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Account:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Account_StatusCode
    type: CodeableConcept
    name: String
    subject: Reference
    service_period: Period
    coverage: Account_Coverage
    owner: Reference
    description: String
    guarantor: Account_Guarantor
    part_of: Reference


@dataclass
class Account_StatusCode:
    value: AccountStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Account_Coverage:
    id: String
    extension: Extension
    modifier_extension: Extension
    coverage: Reference
    priority: PositiveInt


@dataclass
class Account_Guarantor:
    id: String
    extension: Extension
    modifier_extension: Extension
    party: Reference
    on_hold: Boolean
    period: Period

