# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicinalProductIngredient:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    role: CodeableConcept
    allergenic_indicator: Boolean
    manufacturer: Reference
    specified_substance: MedicinalProductIngredient_SpecifiedSubstance
    substance: MedicinalProductIngredient_Substance


@dataclass
class MedicinalProductIngredient_SpecifiedSubstance:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    group: CodeableConcept
    confidentiality: CodeableConcept
    strength: MedicinalProductIngredient_SpecifiedSubstance_Strength


@dataclass
class MedicinalProductIngredient_SpecifiedSubstance_Strength:
    id: String
    extension: Extension
    modifier_extension: Extension
    presentation: Ratio
    presentation_low_limit: Ratio
    concentration: Ratio
    concentration_low_limit: Ratio
    measurement_point: String
    country: CodeableConcept
    reference_strength: MedicinalProductIngredient_SpecifiedSubstance_Strength_ReferenceStrength


@dataclass
class MedicinalProductIngredient_SpecifiedSubstance_Strength_ReferenceStrength:
    id: String
    extension: Extension
    modifier_extension: Extension
    substance: CodeableConcept
    strength: Ratio
    strength_low_limit: Ratio
    measurement_point: String
    country: CodeableConcept


@dataclass
class MedicinalProductIngredient_Substance:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    strength: MedicinalProductIngredient_SpecifiedSubstance_Strength

