# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class SubstanceSourceMaterial:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    source_material_class: CodeableConcept
    source_material_type: CodeableConcept
    source_material_state: CodeableConcept
    organism_id: Identifier
    organism_name: String
    parent_substance_id: Identifier
    parent_substance_name: String
    country_of_origin: CodeableConcept
    geographical_location: String
    development_stage: CodeableConcept
    fraction_description: SubstanceSourceMaterial_FractionDescription
    organism: SubstanceSourceMaterial_Organism
    part_description: SubstanceSourceMaterial_PartDescription


@dataclass
class SubstanceSourceMaterial_FractionDescription:
    id: String
    extension: Extension
    modifier_extension: Extension
    fraction: String
    material_type: CodeableConcept


@dataclass
class SubstanceSourceMaterial_Organism:
    id: String
    extension: Extension
    modifier_extension: Extension
    family: CodeableConcept
    genus: CodeableConcept
    species: CodeableConcept
    intraspecific_type: CodeableConcept
    intraspecific_description: String
    author: SubstanceSourceMaterial_Organism_Author
    hybrid: SubstanceSourceMaterial_Organism_Hybrid
    organism_general: SubstanceSourceMaterial_Organism_OrganismGeneral


@dataclass
class SubstanceSourceMaterial_Organism_Author:
    id: String
    extension: Extension
    modifier_extension: Extension
    author_type: CodeableConcept
    author_description: String


@dataclass
class SubstanceSourceMaterial_Organism_Hybrid:
    id: String
    extension: Extension
    modifier_extension: Extension
    maternal_organism_id: String
    maternal_organism_name: String
    paternal_organism_id: String
    paternal_organism_name: String
    hybrid_type: CodeableConcept


@dataclass
class SubstanceSourceMaterial_Organism_OrganismGeneral:
    id: String
    extension: Extension
    modifier_extension: Extension
    kingdom: CodeableConcept
    phylum: CodeableConcept
    class_value: CodeableConcept
    order: CodeableConcept


@dataclass
class SubstanceSourceMaterial_PartDescription:
    id: String
    extension: Extension
    modifier_extension: Extension
    part: CodeableConcept
    part_location: CodeableConcept

