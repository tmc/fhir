# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class GroupDefinition:
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
    type: GroupDefinition_TypeCode
    actual: Boolean
    code: CodeableConcept
    name: String
    quantity: UnsignedInt
    managing_entity: Reference
    characteristic: GroupDefinition_Characteristic


@dataclass
class GroupDefinition_TypeCode:
    value: GroupTypeCode_Value
    id: String
    extension: Extension


@dataclass
class GroupDefinition_Characteristic:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: GroupDefinition_Characteristic_ValueX
    exclude: Boolean
    period: Period


@dataclass
class GroupDefinition_Characteristic_ValueX:
    codeable_concept: CodeableConcept
    boolean: Boolean
    quantity: Quantity
    range: Range
    reference: Reference

