# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class PaymentNotice:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: PaymentNotice_StatusCode
    request: Reference
    response: Reference
    created: DateTime
    provider: Reference
    payment: Reference
    payment_date: Date
    payee: Reference
    recipient: Reference
    amount: Money
    payment_status: CodeableConcept


@dataclass
class PaymentNotice_StatusCode:
    value: FinancialResourceStatusCode_Value
    id: String
    extension: Extension

