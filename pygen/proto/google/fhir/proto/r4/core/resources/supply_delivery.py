# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class SupplyDelivery:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    part_of: Reference
    status: SupplyDelivery_StatusCode
    patient: Reference
    type: CodeableConcept
    supplied_item: SupplyDelivery_SuppliedItem
    occurrence: SupplyDelivery_OccurrenceX
    supplier: Reference
    destination: Reference
    receiver: Reference


@dataclass
class SupplyDelivery_StatusCode:
    value: SupplyDeliveryStatusCode_Value
    id: String
    extension: Extension


@dataclass
class SupplyDelivery_SuppliedItem:
    id: String
    extension: Extension
    modifier_extension: Extension
    quantity: SimpleQuantity
    item: SupplyDelivery_SuppliedItem_ItemX


@dataclass
class SupplyDelivery_SuppliedItem_ItemX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class SupplyDelivery_OccurrenceX:
    date_time: DateTime
    period: Period
    timing: Timing

