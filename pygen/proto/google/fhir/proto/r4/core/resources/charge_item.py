# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ChargeItem:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    definition_uri: Uri
    definition_canonical: Canonical
    status: ChargeItem_StatusCode
    part_of: Reference
    code: CodeableConcept
    subject: Reference
    context: Reference
    occurrence: ChargeItem_OccurrenceX
    performer: ChargeItem_Performer
    performing_organization: Reference
    requesting_organization: Reference
    cost_center: Reference
    quantity: Quantity
    bodysite: CodeableConcept
    factor_override: Decimal
    price_override: Money
    override_reason: String
    enterer: Reference
    entered_date: DateTime
    reason: CodeableConcept
    service: Reference
    product: ChargeItem_ProductX
    account: Reference
    note: Annotation
    supporting_information: Reference


@dataclass
class ChargeItem_StatusCode:
    value: ChargeItemStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ChargeItem_OccurrenceX:
    date_time: DateTime
    period: Period
    timing: Timing


@dataclass
class ChargeItem_Performer:
    id: String
    extension: Extension
    modifier_extension: Extension
    function: CodeableConcept
    actor: Reference


@dataclass
class ChargeItem_ProductX:
    reference: Reference
    codeable_concept: CodeableConcept

