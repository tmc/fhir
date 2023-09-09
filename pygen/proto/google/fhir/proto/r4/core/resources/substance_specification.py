# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class SubstanceSpecification:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type: CodeableConcept
    status: CodeableConcept
    domain: CodeableConcept
    description: String
    source: Reference
    comment: String
    moiety: SubstanceSpecification_Moiety
    property: SubstanceSpecification_Property
    reference_information: Reference
    structure: SubstanceSpecification_Structure
    code: SubstanceSpecification_CodeType
    name: SubstanceSpecification_Name
    molecular_weight: SubstanceSpecification_Structure_Isotope_MolecularWeight
    relationship: SubstanceSpecification_Relationship
    nucleic_acid: Reference
    polymer: Reference
    protein: Reference
    source_material: Reference


@dataclass
class SubstanceSpecification_Moiety:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    identifier: Identifier
    name: String
    stereochemistry: CodeableConcept
    optical_activity: CodeableConcept
    molecular_formula: String
    amount: SubstanceSpecification_Moiety_AmountX


@dataclass
class SubstanceSpecification_Moiety_AmountX:
    quantity: Quantity
    string_value: String


@dataclass
class SubstanceSpecification_Property:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    code: CodeableConcept
    parameters: String
    defining_substance: SubstanceSpecification_Property_DefiningSubstanceX
    amount: SubstanceSpecification_Property_AmountX


@dataclass
class SubstanceSpecification_Property_DefiningSubstanceX:
    reference: Reference
    codeable_concept: CodeableConcept


@dataclass
class SubstanceSpecification_Property_AmountX:
    quantity: Quantity
    string_value: String


@dataclass
class SubstanceSpecification_Structure:
    id: String
    extension: Extension
    modifier_extension: Extension
    stereochemistry: CodeableConcept
    optical_activity: CodeableConcept
    molecular_formula: String
    molecular_formula_by_moiety: String
    isotope: SubstanceSpecification_Structure_Isotope
    molecular_weight: SubstanceSpecification_Structure_Isotope_MolecularWeight
    source: Reference
    representation: SubstanceSpecification_Structure_Representation


@dataclass
class SubstanceSpecification_Structure_Isotope:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    name: CodeableConcept
    substitution: CodeableConcept
    half_life: Quantity
    molecular_weight: SubstanceSpecification_Structure_Isotope_MolecularWeight


@dataclass
class SubstanceSpecification_Structure_Isotope_MolecularWeight:
    id: String
    extension: Extension
    modifier_extension: Extension
    method: CodeableConcept
    type: CodeableConcept
    amount: Quantity


@dataclass
class SubstanceSpecification_Structure_Representation:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    representation: String
    attachment: Attachment


@dataclass
class SubstanceSpecification_CodeType:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    status: CodeableConcept
    status_date: DateTime
    comment: String
    source: Reference


@dataclass
class SubstanceSpecification_Name:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    type: CodeableConcept
    status: CodeableConcept
    preferred: Boolean
    language: CodeableConcept
    domain: CodeableConcept
    jurisdiction: CodeableConcept
    synonym: SubstanceSpecification_Name
    translation: SubstanceSpecification_Name
    official: SubstanceSpecification_Name_Official
    source: Reference


@dataclass
class SubstanceSpecification_Name_Official:
    id: String
    extension: Extension
    modifier_extension: Extension
    authority: CodeableConcept
    status: CodeableConcept
    date: DateTime


@dataclass
class SubstanceSpecification_Relationship:
    id: String
    extension: Extension
    modifier_extension: Extension
    substance: SubstanceSpecification_Relationship_SubstanceX
    relationship: CodeableConcept
    is_defining: Boolean
    amount: SubstanceSpecification_Relationship_AmountX
    amount_ratio_low_limit: Ratio
    amount_type: CodeableConcept
    source: Reference


@dataclass
class SubstanceSpecification_Relationship_SubstanceX:
    reference: Reference
    codeable_concept: CodeableConcept


@dataclass
class SubstanceSpecification_Relationship_AmountX:
    quantity: Quantity
    range: Range
    ratio: Ratio
    string_value: String

