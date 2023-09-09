# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Substance:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Substance_StatusCode
    category: CodeableConcept
    code: CodeableConcept
    description: String
    instance: Substance_Instance
    ingredient: Substance_Ingredient


@dataclass
class Substance_StatusCode:
    value: FHIRSubstanceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Substance_Instance:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    expiry: DateTime
    quantity: SimpleQuantity


@dataclass
class Substance_Ingredient:
    id: String
    extension: Extension
    modifier_extension: Extension
    quantity: Ratio
    substance: Substance_Ingredient_SubstanceX


@dataclass
class Substance_Ingredient_SubstanceX:
    codeable_concept: CodeableConcept
    reference: Reference

