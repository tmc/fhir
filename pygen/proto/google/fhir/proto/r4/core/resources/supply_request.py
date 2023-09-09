# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class SupplyRequest:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: SupplyRequest_StatusCode
    category: CodeableConcept
    priority: SupplyRequest_PriorityCode
    item: SupplyRequest_ItemX
    quantity: Quantity
    parameter: SupplyRequest_Parameter
    occurrence: SupplyRequest_OccurrenceX
    authored_on: DateTime
    requester: Reference
    supplier: Reference
    reason_code: CodeableConcept
    reason_reference: Reference
    deliver_from: Reference
    deliver_to: Reference


@dataclass
class SupplyRequest_StatusCode:
    value: SupplyRequestStatusCode_Value
    id: String
    extension: Extension


@dataclass
class SupplyRequest_PriorityCode:
    value: RequestPriorityCode_Value
    id: String
    extension: Extension


@dataclass
class SupplyRequest_ItemX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class SupplyRequest_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    value: SupplyRequest_Parameter_ValueX


@dataclass
class SupplyRequest_Parameter_ValueX:
    codeable_concept: CodeableConcept
    quantity: Quantity
    range: Range
    boolean: Boolean


@dataclass
class SupplyRequest_OccurrenceX:
    date_time: DateTime
    period: Period
    timing: Timing

