# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Group:
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
    type: Group_TypeCode
    actual: Boolean
    code: CodeableConcept
    name: String
    quantity: UnsignedInt
    managing_entity: Reference
    characteristic: Group_Characteristic
    member: Group_Member


@dataclass
class Group_TypeCode:
    value: GroupTypeCode_Value
    id: String
    extension: Extension


@dataclass
class Group_Characteristic:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: Group_Characteristic_ValueX
    exclude: Boolean
    period: Period


@dataclass
class Group_Characteristic_ValueX:
    codeable_concept: CodeableConcept
    boolean: Boolean
    quantity: Quantity
    range: Range
    reference: Reference


@dataclass
class Group_Member:
    id: String
    extension: Extension
    modifier_extension: Extension
    entity: Reference
    period: Period
    inactive: Boolean

