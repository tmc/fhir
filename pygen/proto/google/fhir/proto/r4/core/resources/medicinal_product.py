# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicinalProduct:
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
    domain: Coding
    combined_pharmaceutical_dose_form: CodeableConcept
    legal_status_of_supply: CodeableConcept
    additional_monitoring_indicator: CodeableConcept
    special_measures: String
    paediatric_use_indicator: CodeableConcept
    product_classification: CodeableConcept
    marketing_status: MarketingStatus
    pharmaceutical_product: Reference
    packaged_medicinal_product: Reference
    attached_document: Reference
    master_file: Reference
    contact: Reference
    clinical_trial: Reference
    name: MedicinalProduct_Name
    cross_reference: Identifier
    manufacturing_business_operation: MedicinalProduct_ManufacturingBusinessOperation
    special_designation: MedicinalProduct_SpecialDesignation


@dataclass
class MedicinalProduct_Name:
    id: String
    extension: Extension
    modifier_extension: Extension
    product_name: String
    name_part: MedicinalProduct_Name_NamePart
    country_language: MedicinalProduct_Name_CountryLanguage


@dataclass
class MedicinalProduct_Name_NamePart:
    id: String
    extension: Extension
    modifier_extension: Extension
    part: String
    type: Coding


@dataclass
class MedicinalProduct_Name_CountryLanguage:
    id: String
    extension: Extension
    modifier_extension: Extension
    country: CodeableConcept
    jurisdiction: CodeableConcept
    language: CodeableConcept


@dataclass
class MedicinalProduct_ManufacturingBusinessOperation:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation_type: CodeableConcept
    authorisation_reference_number: Identifier
    effective_date: DateTime
    confidentiality_indicator: CodeableConcept
    manufacturer: Reference
    regulator: Reference


@dataclass
class MedicinalProduct_SpecialDesignation:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type: CodeableConcept
    intended_use: CodeableConcept
    indication: MedicinalProduct_SpecialDesignation_IndicationX
    status: CodeableConcept
    date: DateTime
    species: CodeableConcept


@dataclass
class MedicinalProduct_SpecialDesignation_IndicationX:
    codeable_concept: CodeableConcept
    reference: Reference

