# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicinalProductPackaged:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    subject: Reference
    description: String
    legal_status_of_supply: CodeableConcept
    marketing_status: MarketingStatus
    marketing_authorization: Reference
    manufacturer: Reference
    batch_identifier: MedicinalProductPackaged_BatchIdentifier
    package_item: MedicinalProductPackaged_PackageItem


@dataclass
class MedicinalProductPackaged_BatchIdentifier:
    id: String
    extension: Extension
    modifier_extension: Extension
    outer_packaging: Identifier
    immediate_packaging: Identifier


@dataclass
class MedicinalProductPackaged_PackageItem:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    type: CodeableConcept
    quantity: Quantity
    material: CodeableConcept
    alternate_material: CodeableConcept
    device: Reference
    manufactured_item: Reference
    package_item: MedicinalProductPackaged_PackageItem
    physical_characteristics: ProdCharacteristic
    other_characteristics: CodeableConcept
    shelf_life_storage: ProductShelfLife
    manufacturer: Reference

