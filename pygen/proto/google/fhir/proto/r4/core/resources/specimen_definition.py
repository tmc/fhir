# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class SpecimenDefinition:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type_collected: CodeableConcept
    patient_preparation: CodeableConcept
    time_aspect: String
    collection: CodeableConcept
    type_tested: SpecimenDefinition_TypeTested


@dataclass
class SpecimenDefinition_TypeTested:
    id: String
    extension: Extension
    modifier_extension: Extension
    is_derived: Boolean
    type: CodeableConcept
    preference: SpecimenDefinition_TypeTested_PreferenceCode
    container: SpecimenDefinition_TypeTested_Container
    requirement: String
    retention_time: Duration
    rejection_criterion: CodeableConcept
    handling: SpecimenDefinition_TypeTested_Handling


@dataclass
class SpecimenDefinition_TypeTested_PreferenceCode:
    value: SpecimenContainedPreferenceCode_Value
    id: String
    extension: Extension


@dataclass
class SpecimenDefinition_TypeTested_Container:
    id: String
    extension: Extension
    modifier_extension: Extension
    material: CodeableConcept
    type: CodeableConcept
    cap: CodeableConcept
    description: String
    capacity: SimpleQuantity
    minimum_volume: SpecimenDefinition_TypeTested_Container_MinimumVolumeX
    additive: SpecimenDefinition_TypeTested_Container_Additive
    preparation: String


@dataclass
class SpecimenDefinition_TypeTested_Container_MinimumVolumeX:
    quantity: SimpleQuantity
    string_value: String


@dataclass
class SpecimenDefinition_TypeTested_Container_Additive:
    id: String
    extension: Extension
    modifier_extension: Extension
    additive: SpecimenDefinition_TypeTested_Container_Additive_AdditiveX


@dataclass
class SpecimenDefinition_TypeTested_Container_Additive_AdditiveX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class SpecimenDefinition_TypeTested_Handling:
    id: String
    extension: Extension
    modifier_extension: Extension
    temperature_qualifier: CodeableConcept
    temperature_range: Range
    max_duration: Duration
    instruction: String

