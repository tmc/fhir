# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class SubstancePolymer:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    class_value: CodeableConcept
    geometry: CodeableConcept
    copolymer_connectivity: CodeableConcept
    modification: String
    monomer_set: SubstancePolymer_MonomerSet
    repeat: SubstancePolymer_Repeat


@dataclass
class SubstancePolymer_MonomerSet:
    id: String
    extension: Extension
    modifier_extension: Extension
    ratio_type: CodeableConcept
    starting_material: SubstancePolymer_MonomerSet_StartingMaterial


@dataclass
class SubstancePolymer_MonomerSet_StartingMaterial:
    id: String
    extension: Extension
    modifier_extension: Extension
    material: CodeableConcept
    type: CodeableConcept
    is_defining: Boolean
    amount: SubstanceAmount


@dataclass
class SubstancePolymer_Repeat:
    id: String
    extension: Extension
    modifier_extension: Extension
    number_of_units: Integer
    average_molecular_formula: String
    repeat_unit_amount_type: CodeableConcept
    repeat_unit: SubstancePolymer_Repeat_RepeatUnit


@dataclass
class SubstancePolymer_Repeat_RepeatUnit:
    id: String
    extension: Extension
    modifier_extension: Extension
    orientation_of_polymerisation: CodeableConcept
    repeat_unit: String
    amount: SubstanceAmount
    degree_of_polymerisation: SubstancePolymer_Repeat_RepeatUnit_DegreeOfPolymerisation
    structural_representation: SubstancePolymer_Repeat_RepeatUnit_StructuralRepresentation


@dataclass
class SubstancePolymer_Repeat_RepeatUnit_DegreeOfPolymerisation:
    id: String
    extension: Extension
    modifier_extension: Extension
    degree: CodeableConcept
    amount: SubstanceAmount


@dataclass
class SubstancePolymer_Repeat_RepeatUnit_StructuralRepresentation:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    representation: String
    attachment: Attachment

