# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Claim:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: Claim_StatusCode
    type: CodeableConcept
    sub_type: CodeableConcept
    use: Claim_UseCode
    patient: Reference
    billable_period: Period
    created: DateTime
    enterer: Reference
    insurer: Reference
    provider: Reference
    priority: CodeableConcept
    funds_reserve: CodeableConcept
    related: Claim_RelatedClaim
    prescription: Reference
    original_prescription: Reference
    payee: Claim_Payee
    referral: Reference
    facility: Reference
    care_team: Claim_CareTeam
    supporting_info: Claim_SupportingInformation
    diagnosis: Claim_Diagnosis
    procedure: Claim_Procedure
    insurance: Claim_Insurance
    accident: Claim_Accident
    item: Claim_Item
    total: Money


@dataclass
class Claim_StatusCode:
    value: FinancialResourceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Claim_UseCode:
    value: UseCode_Value
    id: String
    extension: Extension


@dataclass
class Claim_RelatedClaim:
    id: String
    extension: Extension
    modifier_extension: Extension
    claim: Reference
    relationship: CodeableConcept
    reference: Identifier


@dataclass
class Claim_Payee:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    party: Reference


@dataclass
class Claim_CareTeam:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    provider: Reference
    responsible: Boolean
    role: CodeableConcept
    qualification: CodeableConcept


@dataclass
class Claim_SupportingInformation:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    category: CodeableConcept
    code: CodeableConcept
    timing: Claim_SupportingInformation_TimingX
    value: Claim_SupportingInformation_ValueX
    reason: CodeableConcept


@dataclass
class Claim_SupportingInformation_TimingX:
    date: Date
    period: Period


@dataclass
class Claim_SupportingInformation_ValueX:
    boolean: Boolean
    string_value: String
    quantity: Quantity
    attachment: Attachment
    reference: Reference


@dataclass
class Claim_Diagnosis:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    diagnosis: Claim_Diagnosis_DiagnosisX
    type: CodeableConcept
    on_admission: CodeableConcept
    package_code: CodeableConcept


@dataclass
class Claim_Diagnosis_DiagnosisX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Claim_Procedure:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    type: CodeableConcept
    date: DateTime
    procedure: Claim_Procedure_ProcedureX
    udi: Reference


@dataclass
class Claim_Procedure_ProcedureX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Claim_Insurance:
    id: String
    extension: Extension
    modifier_extension: Extension
    sequence: PositiveInt
    focal: Boolean
    identifier: Identifier
    coverage: Reference
    business_arrangement: String
    pre_auth_ref: String
    claim_response: Reference


@dataclass
class Claim_Accident:
    id: String
    extension: Extension
    modifier_extension: Extension
    date: Date
    type: CodeableConcept
    location: Claim_Accident_LocationX


@dataclass
class Claim_Accident_LocationX:
    address: Address
    reference: Reference


@dataclass
class Claim_Item:
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
    serviced: Claim_Item_ServicedX
    location: Claim_Item_LocationX
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    net: Money
    udi: Reference
    body_site: CodeableConcept
    sub_site: CodeableConcept
    encounter: Reference
    detail: Claim_Item_Detail


@dataclass
class Claim_Item_ServicedX:
    date: Date
    period: Period


@dataclass
class Claim_Item_LocationX:
    codeable_concept: CodeableConcept
    address: Address
    reference: Reference


@dataclass
class Claim_Item_Detail:
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
    sub_detail: Claim_Item_Detail_SubDetail


@dataclass
class Claim_Item_Detail_SubDetail:
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

