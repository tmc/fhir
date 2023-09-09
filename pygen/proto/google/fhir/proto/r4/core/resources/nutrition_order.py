# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class NutritionOrder:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    instantiates_canonical: Canonical
    instantiates_uri: Uri
    instantiates: Uri
    status: NutritionOrder_StatusCode
    intent: NutritionOrder_IntentCode
    patient: Reference
    encounter: Reference
    date_time: DateTime
    orderer: Reference
    allergy_intolerance: Reference
    food_preference_modifier: CodeableConcept
    exclude_food_modifier: CodeableConcept
    oral_diet: NutritionOrder_OralDiet
    supplement: NutritionOrder_Supplement
    enteral_formula: NutritionOrder_EnteralFormula
    note: Annotation


@dataclass
class NutritionOrder_StatusCode:
    value: RequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class NutritionOrder_IntentCode:
    value: RequestIntentCode_Value
    id: String
    extension: Extension


@dataclass
class NutritionOrder_OralDiet:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    schedule: Timing
    nutrient: NutritionOrder_OralDiet_Nutrient
    texture: NutritionOrder_OralDiet_Texture
    fluid_consistency_type: CodeableConcept
    instruction: String


@dataclass
class NutritionOrder_OralDiet_Nutrient:
    id: String
    extension: Extension
    modifier_extension: Extension
    modifier: CodeableConcept
    amount: SimpleQuantity


@dataclass
class NutritionOrder_OralDiet_Texture:
    id: String
    extension: Extension
    modifier_extension: Extension
    modifier: CodeableConcept
    food_type: CodeableConcept


@dataclass
class NutritionOrder_Supplement:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    product_name: String
    schedule: Timing
    quantity: SimpleQuantity
    instruction: String


@dataclass
class NutritionOrder_EnteralFormula:
    id: String
    extension: Extension
    modifier_extension: Extension
    base_formula_type: CodeableConcept
    base_formula_product_name: String
    additive_type: CodeableConcept
    additive_product_name: String
    caloric_density: SimpleQuantity
    routeof_administration: CodeableConcept
    administration: NutritionOrder_EnteralFormula_Administration
    max_volume_to_deliver: SimpleQuantity
    administration_instruction: String


@dataclass
class NutritionOrder_EnteralFormula_Administration:
    id: String
    extension: Extension
    modifier_extension: Extension
    schedule: Timing
    quantity: SimpleQuantity
    rate: NutritionOrder_EnteralFormula_Administration_RateX


@dataclass
class NutritionOrder_EnteralFormula_Administration_RateX:
    quantity: SimpleQuantity
    ratio: Ratio

