# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Medication:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    code: CodeableConcept
    status: Medication_StatusCode
    manufacturer: Reference
    form: CodeableConcept
    amount: Ratio
    ingredient: Medication_Ingredient
    batch: Medication_Batch


@dataclass
class Medication_StatusCode:
    value: MedicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Medication_Ingredient:
    id: String
    extension: Extension
    modifier_extension: Extension
    item: Medication_Ingredient_ItemX
    is_active: Boolean
    strength: Ratio


@dataclass
class Medication_Ingredient_ItemX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Medication_Batch:
    id: String
    extension: Extension
    modifier_extension: Extension
    lot_number: String
    expiration_date: DateTime

