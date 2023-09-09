# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ClaimResponse:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ClaimResponse_StatusCode
    type: CodeableConcept
    sub_type: CodeableConcept
    use: ClaimResponse_UseCode
    patient: Reference
    created: DateTime
    insurer: Reference
    requestor: Reference
    request: Reference
    outcome: ClaimResponse_OutcomeCode
    disposition: String
    pre_auth_ref: String
    pre_auth_period: Period
    payee_type: CodeableConcept
    item: ClaimResponse_Item
    add_item: ClaimResponse_AddedItem
    adjudication: ClaimResponse_Item_Adjudication
    total: ClaimResponse_Total
    payment: ClaimResponse_Payment
    funds_reserve: CodeableConcept
    form_code: CodeableConcept
    form: Attachment
    process_note: ClaimResponse_Note
    communication_request: Reference
    insurance: ClaimResponse_Insurance
    error: ClaimResponse_Error


@dataclass
class ClaimResponse_StatusCode:
    value: FinancialResourceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ClaimResponse_UseCode:
    value: UseCode_Value
    id: String
    extension: Extension


@dataclass
class ClaimResponse_OutcomeCode:
    value: ClaimProcessingCode_Value
    id: String
    extension: Extension


@dataclass
class ClaimResponse_Item:
    id: String
    extension: Extension
    modifier_extension: Extension
    item_sequence: PositiveInt
    note_number: PositiveInt
    adjudication: ClaimResponse_Item_Adjudication
    detail: ClaimResponse_Item_ItemDetail


@dataclass
class ClaimResponse_Item_Adjudication:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    reason: CodeableConcept
    amount: Money
    value: Decimal


@dataclass
class ClaimResponse_Item_ItemDetail:
    id: String
    extension: Extension
    modifier_extension: Extension
    detail_sequence: PositiveInt
    note_number: PositiveInt
    adjudication: ClaimResponse_Item_Adjudication
    sub_detail: ClaimResponse_Item_ItemDetail_SubDetail


@dataclass
class ClaimResponse_Item_ItemDetail_SubDetail:
    id: String
    extension: Extension
    modifier_extension: Extension
    sub_detail_sequence: PositiveInt
    note_number: PositiveInt
    adjudication: ClaimResponse_Item_Adjudication


@dataclass
class ClaimResponse_AddedItem:
    id: String
    extension: Extension
    modifier_extension: Extension
    item_sequence: PositiveInt
    detail_sequence: PositiveInt
    subdetail_sequence: PositiveInt
    provider: Reference
    product_or_service: CodeableConcept
    modifier: CodeableConcept
    program_code: CodeableConcept
    serviced: ClaimResponse_AddedItem_ServicedX
    location: ClaimResponse_AddedItem_LocationX
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    body_site: CodeableConcept
    sub_site: CodeableConcept
    note_number: PositiveInt
    adjudication: ClaimResponse_Item_Adjudication
    detail: ClaimResponse_AddedItem_AddedItemDetail


@dataclass
class ClaimResponse_AddedItem_ServicedX:
    date: Date
    period: Period


@dataclass
class ClaimResponse_AddedItem_LocationX:
    codeable_concept: CodeableConcept
    address: Address
    reference: Reference


@dataclass
class ClaimResponse_AddedItem_AddedItemDetail:
    id: String
    extension: Extension
    modifier_extension: Extension
    product_or_service: CodeableConcept
    modifier: CodeableConcept
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    note_number: PositiveInt
    adjudication: ClaimResponse_Item_Adjudication
    sub_detail: ClaimResponse_AddedItem_AddedItemDetail_AddedItemSubDetail


@dataclass
class ClaimResponse_AddedItem_AddedItemDetail_AddedItemSubDetail:
    id: String
    extension: Extension
    modifier_extension: Extension
    product_or_service: CodeableConcept
    modifier: CodeableConcept
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    note_number: PositiveInt
    adjudication: ClaimResponse_Item_Adjudication


@dataclass
class ClaimResponse_Total:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    amount: Money


@dataclass
class ClaimResponse_Payment:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    adjustment: Money
    adjustment_reason: CodeableConcept
    date: Date
    amount: Money
    identifier: Identifier


@dataclass
class ClaimResponse_Note:
    id: String
    extension: Extension
    modifier_extension: Extension
    number: PositiveInt
    type: ClaimResponse_Note_TypeCode
    text: String
    language: CodeableConcept


@dataclass
class ClaimResponse_Note_TypeCode:
    value: NoteTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ClaimResponse_Insurance:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    focal: Boolean
    coverage: Reference
    business_arrangement: String
    claim_response: Reference


@dataclass
class ClaimResponse_Error:
    id: String
    extension: Extension
    modifier_extension: Extension
    item_sequence: PositiveInt
    detail_sequence: PositiveInt
    sub_detail_sequence: PositiveInt
    code: CodeableConcept

