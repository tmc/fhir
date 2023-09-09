# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class PaymentReconciliation:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: PaymentReconciliation_StatusCode
    period: Period
    created: DateTime
    payment_issuer: Reference
    request: Reference
    requestor: Reference
    outcome: PaymentReconciliation_OutcomeCode
    disposition: String
    payment_date: Date
    payment_amount: Money
    payment_identifier: Identifier
    detail: PaymentReconciliation_Details
    form_code: CodeableConcept
    process_note: PaymentReconciliation_Notes


@dataclass
class PaymentReconciliation_StatusCode:
    value: FinancialResourceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class PaymentReconciliation_OutcomeCode:
    value: ClaimProcessingCode_Value
    id: String
    extension: Extension


@dataclass
class PaymentReconciliation_Details:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    predecessor: Identifier
    type: CodeableConcept
    request: Reference
    submitter: Reference
    response: Reference
    date: Date
    responsible: Reference
    payee: Reference
    amount: Money


@dataclass
class PaymentReconciliation_Notes:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: PaymentReconciliation_Notes_TypeCode
    text: String


@dataclass
class PaymentReconciliation_Notes_TypeCode:
    value: NoteTypeCode_Value
    id: String
    extension: Extension

