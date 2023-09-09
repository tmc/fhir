# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ActualGroup:
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
    type: ActualGroup_TypeCode
    actual: Boolean
    code: CodeableConcept
    name: String
    quantity: UnsignedInt
    managing_entity: Reference
    member: ActualGroup_Member


@dataclass
class ActualGroup_TypeCode:
    value: GroupTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ActualGroup_Member:
    id: String
    extension: Extension
    modifier_extension: Extension
    entity: Reference
    period: Period
    inactive: Boolean

