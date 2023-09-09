# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Invoice:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Invoice_StatusCode
    cancelled_reason: String
    type: CodeableConcept
    subject: Reference
    recipient: Reference
    date: DateTime
    participant: Invoice_Participant
    issuer: Reference
    account: Reference
    line_item: Invoice_LineItem
    total_price_component: Invoice_LineItem_PriceComponent
    total_net: Money
    total_gross: Money
    payment_terms: Markdown
    note: Annotation


@dataclass
class Invoice_StatusCode:
    value: InvoiceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Invoice_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    role: CodeableConcept
    actor: Reference


@dataclass
class Invoice_LineItem:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    charge_item: Invoice_LineItem_ChargeItemX
    price_component: Invoice_LineItem_PriceComponent


@dataclass
class Invoice_LineItem_ChargeItemX:
    reference: Reference
    codeable_concept: CodeableConcept


@dataclass
class Invoice_LineItem_PriceComponent:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: Invoice_LineItem_PriceComponent_TypeCode
    code: CodeableConcept
    factor: Decimal
    amount: Money


@dataclass
class Invoice_LineItem_PriceComponent_TypeCode:
    value: InvoicePriceComponentTypeCode_Value
    id: String
    extension: Extension

