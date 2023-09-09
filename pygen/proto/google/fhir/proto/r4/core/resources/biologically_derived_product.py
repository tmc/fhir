# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class BiologicallyDerivedProduct:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    product_category: BiologicallyDerivedProduct_ProductCategoryCode
    product_code: CodeableConcept
    status: BiologicallyDerivedProduct_StatusCode
    request: Reference
    quantity: Integer
    parent: Reference
    collection: BiologicallyDerivedProduct_Collection
    processing: BiologicallyDerivedProduct_Processing
    manipulation: BiologicallyDerivedProduct_Manipulation
    storage: BiologicallyDerivedProduct_Storage


@dataclass
class BiologicallyDerivedProduct_ProductCategoryCode:
    value: BiologicallyDerivedProductCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class BiologicallyDerivedProduct_StatusCode:
    value: BiologicallyDerivedProductStatusCode_Value
    id: String
    extension: Extension


@dataclass
class BiologicallyDerivedProduct_Collection:
    id: String
    extension: Extension
    modifier_extension: Extension
    collector: Reference
    source: Reference
    collected: BiologicallyDerivedProduct_Collection_CollectedX


@dataclass
class BiologicallyDerivedProduct_Collection_CollectedX:
    date_time: DateTime
    period: Period


@dataclass
class BiologicallyDerivedProduct_Processing:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    procedure: CodeableConcept
    additive: Reference
    time: BiologicallyDerivedProduct_Processing_TimeX


@dataclass
class BiologicallyDerivedProduct_Processing_TimeX:
    date_time: DateTime
    period: Period


@dataclass
class BiologicallyDerivedProduct_Manipulation:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    time: BiologicallyDerivedProduct_Manipulation_TimeX


@dataclass
class BiologicallyDerivedProduct_Manipulation_TimeX:
    date_time: DateTime
    period: Period


@dataclass
class BiologicallyDerivedProduct_Storage:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    temperature: Decimal
    scale: BiologicallyDerivedProduct_Storage_ScaleCode
    duration: Period


@dataclass
class BiologicallyDerivedProduct_Storage_ScaleCode:
    value: BiologicallyDerivedProductStorageScaleCode_Value
    id: String
    extension: Extension

