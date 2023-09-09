# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Contract:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    url: Uri
    version: String
    status: Contract_StatusCode
    legal_state: CodeableConcept
    instantiates_canonical: Reference
    instantiates_uri: Uri
    content_derivative: CodeableConcept
    issued: DateTime
    applies: Period
    expiration_type: CodeableConcept
    subject: Reference
    authority: Reference
    domain: Reference
    site: Reference
    name: String
    title: String
    subtitle: String
    alias: String
    author: Reference
    scope: CodeableConcept
    topic: Contract_TopicX
    type: CodeableConcept
    sub_type: CodeableConcept
    content_definition: Contract_ContentDefinition
    term: Contract_Term
    supporting_info: Reference
    relevant_history: Reference
    signer: Contract_Signatory
    friendly: Contract_FriendlyLanguage
    legal: Contract_LegalLanguage
    rule: Contract_ComputableLanguage
    legally_binding: Contract_LegallyBindingX


@dataclass
class Contract_StatusCode:
    value: ContractResourceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Contract_TopicX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Contract_ContentDefinition:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    sub_type: CodeableConcept
    publisher: Reference
    publication_date: DateTime
    publication_status: Contract_ContentDefinition_PublicationStatusCode
    copyright: Markdown


@dataclass
class Contract_ContentDefinition_PublicationStatusCode:
    value: ContractResourcePublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class Contract_Term:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    issued: DateTime
    applies: Period
    topic: Contract_Term_TopicX
    type: CodeableConcept
    sub_type: CodeableConcept
    text: String
    security_label: Contract_Term_SecurityLabel
    offer: Contract_Term_ContractOffer
    asset: Contract_Term_ContractAsset
    action: Contract_Term_Action
    group: Contract_Term


@dataclass
class Contract_Term_TopicX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Contract_Term_SecurityLabel:
    id: String
    extension: Extension
    modifier_extension: Extension
    number: UnsignedInt
    classification: Coding
    category: Coding
    control: Coding


@dataclass
class Contract_Term_ContractOffer:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    party: Contract_Term_ContractOffer_ContractParty
    topic: Reference
    type: CodeableConcept
    decision: CodeableConcept
    decision_mode: CodeableConcept
    answer: Contract_Term_ContractOffer_Answer
    text: String
    link_id: String
    security_label_number: UnsignedInt


@dataclass
class Contract_Term_ContractOffer_ContractParty:
    id: String
    extension: Extension
    modifier_extension: Extension
    reference: Reference
    role: CodeableConcept


@dataclass
class Contract_Term_ContractOffer_Answer:
    id: String
    extension: Extension
    modifier_extension: Extension
    value: Contract_Term_ContractOffer_Answer_ValueX


@dataclass
class Contract_Term_ContractOffer_Answer_ValueX:
    boolean: Boolean
    decimal: Decimal
    integer: Integer
    date: Date
    date_time: DateTime
    time: Time
    string_value: String
    uri: Uri
    attachment: Attachment
    coding: Coding
    quantity: Quantity
    reference: Reference


@dataclass
class Contract_Term_ContractAsset:
    id: String
    extension: Extension
    modifier_extension: Extension
    scope: CodeableConcept
    type: CodeableConcept
    type_reference: Reference
    subtype: CodeableConcept
    relationship: Coding
    context: Contract_Term_ContractAsset_AssetContext
    condition: String
    period_type: CodeableConcept
    period: Period
    use_period: Period
    text: String
    link_id: String
    answer: Contract_Term_ContractOffer_Answer
    security_label_number: UnsignedInt
    valued_item: Contract_Term_ContractAsset_ValuedItem


@dataclass
class Contract_Term_ContractAsset_AssetContext:
    id: String
    extension: Extension
    modifier_extension: Extension
    reference: Reference
    code: CodeableConcept
    text: String


@dataclass
class Contract_Term_ContractAsset_ValuedItem:
    id: String
    extension: Extension
    modifier_extension: Extension
    entity: Contract_Term_ContractAsset_ValuedItem_EntityX
    identifier: Identifier
    effective_time: DateTime
    quantity: SimpleQuantity
    unit_price: Money
    factor: Decimal
    points: Decimal
    net: Money
    payment: String
    payment_date: DateTime
    responsible: Reference
    recipient: Reference
    link_id: String
    security_label_number: UnsignedInt


@dataclass
class Contract_Term_ContractAsset_ValuedItem_EntityX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class Contract_Term_Action:
    id: String
    extension: Extension
    modifier_extension: Extension
    do_not_perform: Boolean
    type: CodeableConcept
    subject: Contract_Term_Action_ActionSubject
    intent: CodeableConcept
    link_id: String
    status: CodeableConcept
    context: Reference
    context_link_id: String
    occurrence: Contract_Term_Action_OccurrenceX
    requester: Reference
    requester_link_id: String
    performer_type: CodeableConcept
    performer_role: CodeableConcept
    performer: Reference
    performer_link_id: String
    reason_code: CodeableConcept
    reason_reference: Reference
    reason: String
    reason_link_id: String
    note: Annotation
    security_label_number: UnsignedInt


@dataclass
class Contract_Term_Action_ActionSubject:
    id: String
    extension: Extension
    modifier_extension: Extension
    reference: Reference
    role: CodeableConcept


@dataclass
class Contract_Term_Action_OccurrenceX:
    date_time: DateTime
    period: Period
    timing: Timing


@dataclass
class Contract_Signatory:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: Coding
    party: Reference
    signature: Signature


@dataclass
class Contract_FriendlyLanguage:
    id: String
    extension: Extension
    modifier_extension: Extension
    content: Contract_FriendlyLanguage_ContentX


@dataclass
class Contract_FriendlyLanguage_ContentX:
    attachment: Attachment
    reference: Reference


@dataclass
class Contract_LegalLanguage:
    id: String
    extension: Extension
    modifier_extension: Extension
    content: Contract_LegalLanguage_ContentX


@dataclass
class Contract_LegalLanguage_ContentX:
    attachment: Attachment
    reference: Reference


@dataclass
class Contract_ComputableLanguage:
    id: String
    extension: Extension
    modifier_extension: Extension
    content: Contract_ComputableLanguage_ContentX


@dataclass
class Contract_ComputableLanguage_ContentX:
    attachment: Attachment
    reference: Reference


@dataclass
class Contract_LegallyBindingX:
    attachment: Attachment
    reference: Reference

