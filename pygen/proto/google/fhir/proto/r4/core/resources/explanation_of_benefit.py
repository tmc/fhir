# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ExplanationOfBenefit:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: ExplanationOfBenefit_StatusCode
    type: CodeableConcept
    sub_type: CodeableConcept
    use: ExplanationOfBenefit_UseCode
    patient: Reference
    billable_period: Period
    created: DateTime
    enterer: Reference
    insurer: Reference
    provider: Reference
    priority: CodeableConcept
    funds_reserve_requested: CodeableConcept
    funds_reserve: CodeableConcept
    related: ExplanationOfBenefit_RelatedClaim
    prescription: Reference
    original_prescription: Reference
    payee: ExplanationOfBenefit_Payee
    referral: Reference
    facility: Reference
    claim: Reference
    claim_response: Reference
    outcome: ExplanationOfBenefit_OutcomeCode
    disposition: String
    pre_auth_ref: String
    pre_auth_ref_period: Period
    care_team: ExplanationOfBenefit_CareTeam
    supporting_info: ExplanationOfBenefit_SupportingInformation
    diagnosis: ExplanationOfBenefit_Diagnosis
    procedure: ExplanationOfBenefit_Procedure
    precedence: PositiveInt
    insurance: ExplanationOfBenefit_Insurance
    accident: ExplanationOfBenefit_Accident
    item: ExplanationOfBenefit_Item
    add_item: ExplanationOfBenefit_AddedItem
    adjudication: ExplanationOfBenefit_Item_Adjudication
    total: ExplanationOfBenefit_Total
    payment: ExplanationOfBenefit_Payment
    form_code: CodeableConcept
    form: Attachment
    process_note: ExplanationOfBenefit_Note
    benefit_period: Period
    benefit_balance: ExplanationOfBenefit_BenefitBalance


@dataclass
class ExplanationOfBenefit_StatusCode:
    value: ExplanationOfBenefitStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ExplanationOfBenefit_UseCode:
    value: UseCode_Value
    id: String
    extension: Extension


@dataclass
class ExplanationOfBenefit_RelatedClaim:
    id: String
    extension: Extension
    modifier_extension: Extension
    claim: Reference
    relationship: CodeableConcept
    reference: Identifier


@dataclass
class ExplanationOfBenefit_Payee:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    party: Reference


@dataclass
class ExplanationOfBenefit_OutcomeCode:
    value: ClaimProcessingCode_Value
    id: String
    extension: Extension


@dataclass
class ExplanationOfBenefit_CareTeam:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    provider: Reference
    responsible: Boolean
    role: CodeableConcept
    qualification: CodeableConcept


@dataclass
class ExplanationOfBenefit_SupportingInformation:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    category: CodeableConcept
    code: CodeableConcept
    timing: ExplanationOfBenefit_SupportingInformation_TimingX
    value: ExplanationOfBenefit_SupportingInformation_ValueX
    reason: Coding


@dataclass
class ExplanationOfBenefit_SupportingInformation_TimingX:
    date: Date
    period: Period


@dataclass
class ExplanationOfBenefit_SupportingInformation_ValueX:
    boolean: Boolean
    string_value: String
    quantity: Quantity
    attachment: Attachment
    reference: Reference


@dataclass
class ExplanationOfBenefit_Diagnosis:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    diagnosis: ExplanationOfBenefit_Diagnosis_DiagnosisX
    type: CodeableConcept
    on_admission: CodeableConcept
    package_code: CodeableConcept


@dataclass
class ExplanationOfBenefit_Diagnosis_DiagnosisX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ExplanationOfBenefit_Procedure:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    type: CodeableConcept
    date: DateTime
    procedure: ExplanationOfBenefit_Procedure_ProcedureX
    udi: Reference


@dataclass
class ExplanationOfBenefit_Procedure_ProcedureX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ExplanationOfBenefit_Insurance:
    id: String
    extension: Extension
    modifier_extension: Extension
    focal: Boolean
    coverage: Reference
    pre_auth_ref: String


@dataclass
class ExplanationOfBenefit_Accident:
    id: String
    extension: Extension
    modifier_extension: Extension
    date: Date
    type: CodeableConcept
    location: ExplanationOfBenefit_Accident_LocationX


@dataclass
class ExplanationOfBenefit_Accident_LocationX:
    address: Address
    reference: Reference


@dataclass
class ExplanationOfBenefit_Item:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    care_team_sequence: PositiveInt
    diagnosis_sequence: PositiveInt
    procedure_sequence: PositiveInt
    information_sequence: PositiveInt
    revenue: CodeableConcept
    category: CodeableConcept
    product_or_service: CodeableConcept
    modifier: CodeableConcept
    program_code: CodeableConcept
    serviced: ExplanationOfBenefit_Item_ServicedX
    location: ExplanationOfBenefit_Item_LocationX
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    udi: Reference
    body_site: CodeableConcept
    sub_site: CodeableConcept
    encounter: Reference
    note_number: PositiveInt
    adjudication: ExplanationOfBenefit_Item_Adjudication
    detail: ExplanationOfBenefit_Item_Detail


@dataclass
class ExplanationOfBenefit_Item_ServicedX:
    date: Date
    period: Period


@dataclass
class ExplanationOfBenefit_Item_LocationX:
    codeable_concept: CodeableConcept
    address: Address
    reference: Reference


@dataclass
class ExplanationOfBenefit_Item_Adjudication:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    reason: CodeableConcept
    amount: Money
    value: Decimal


@dataclass
class ExplanationOfBenefit_Item_Detail:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    revenue: CodeableConcept
    category: CodeableConcept
    product_or_service: CodeableConcept
    modifier: CodeableConcept
    program_code: CodeableConcept
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    udi: Reference
    note_number: PositiveInt
    adjudication: ExplanationOfBenefit_Item_Adjudication
    sub_detail: ExplanationOfBenefit_Item_Detail_SubDetail


@dataclass
class ExplanationOfBenefit_Item_Detail_SubDetail:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    revenue: CodeableConcept
    category: CodeableConcept
    product_or_service: CodeableConcept
    modifier: CodeableConcept
    program_code: CodeableConcept
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    udi: Reference
    note_number: PositiveInt
    adjudication: ExplanationOfBenefit_Item_Adjudication


@dataclass
class ExplanationOfBenefit_AddedItem:
    id: String
    extension: Extension
    modifier_extension: Extension
    item_sequence: PositiveInt
    detail_sequence: PositiveInt
    sub_detail_sequence: PositiveInt
    provider: Reference
    product_or_service: CodeableConcept
    modifier: CodeableConcept
    program_code: CodeableConcept
    serviced: ExplanationOfBenefit_AddedItem_ServicedX
    location: ExplanationOfBenefit_AddedItem_LocationX
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    body_site: CodeableConcept
    sub_site: CodeableConcept
    note_number: PositiveInt
    adjudication: ExplanationOfBenefit_Item_Adjudication
    detail: ExplanationOfBenefit_AddedItem_AddedItemDetail


@dataclass
class ExplanationOfBenefit_AddedItem_ServicedX:
    date: Date
    period: Period


@dataclass
class ExplanationOfBenefit_AddedItem_LocationX:
    codeable_concept: CodeableConcept
    address: Address
    reference: Reference


@dataclass
class ExplanationOfBenefit_AddedItem_AddedItemDetail:
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
    adjudication: ExplanationOfBenefit_Item_Adjudication
    sub_detail: ExplanationOfBenefit_AddedItem_AddedItemDetail_AddedItemDetailSubDetail


@dataclass
class ExplanationOfBenefit_AddedItem_AddedItemDetail_AddedItemDetailSubDetail:
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
    adjudication: ExplanationOfBenefit_Item_Adjudication


@dataclass
class ExplanationOfBenefit_Total:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    amount: Money


@dataclass
class ExplanationOfBenefit_Payment:
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
class ExplanationOfBenefit_Note:
    id: String
    extension: Extension
    modifier_extension: Extension
    number: PositiveInt
    type: ExplanationOfBenefit_Note_TypeCode
    text: String
    language: CodeableConcept


@dataclass
class ExplanationOfBenefit_Note_TypeCode:
    value: NoteTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ExplanationOfBenefit_BenefitBalance:
    id: String
    extension: Extension
    modifier_extension: Extension
    category: CodeableConcept
    excluded: Boolean
    name: String
    description: String
    network: CodeableConcept
    unit: CodeableConcept
    term: CodeableConcept
    financial: ExplanationOfBenefit_BenefitBalance_Benefit


@dataclass
class ExplanationOfBenefit_BenefitBalance_Benefit:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    allowed: ExplanationOfBenefit_BenefitBalance_Benefit_AllowedX
    used: ExplanationOfBenefit_BenefitBalance_Benefit_UsedX


@dataclass
class ExplanationOfBenefit_BenefitBalance_Benefit_AllowedX:
    unsigned_int: UnsignedInt
    string_value: String
    money: Money


@dataclass
class ExplanationOfBenefit_BenefitBalance_Benefit_UsedX:
    unsigned_int: UnsignedInt
    money: Money

