# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CQFQuestionnaire:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    url: Uri
    identifier: Identifier
    version: String
    name: String
    title: String
    derived_from: Canonical
    status: CQFQuestionnaire_StatusCode
    experimental: Boolean
    subject_type: CQFQuestionnaire_SubjectTypeCode
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    approval_date: Date
    last_review_date: Date
    effective_period: Period
    code: Coding
    item: CQFQuestionnaire_Item
    library: Canonical


@dataclass
class CQFQuestionnaire_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CQFQuestionnaire_SubjectTypeCode:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class CQFQuestionnaire_Item:
    id: String
    extension: Extension
    modifier_extension: Extension
    link_id: String
    definition: Uri
    code: Coding
    prefix: String
    text: String
    type: CQFQuestionnaire_Item_TypeCode
    enable_when: CQFQuestionnaire_Item_EnableWhen
    enable_behavior: CQFQuestionnaire_Item_EnableBehaviorCode
    required: Boolean
    repeats: Boolean
    read_only: Boolean
    max_length: Integer
    answer_value_set: Canonical
    answer_option: CQFQuestionnaire_Item_AnswerOption
    initial: CQFQuestionnaire_Item_Initial
    item: CQFQuestionnaire_Item


@dataclass
class CQFQuestionnaire_Item_TypeCode:
    value: QuestionnaireItemTypeCode_Value
    id: String
    extension: Extension


@dataclass
class CQFQuestionnaire_Item_EnableWhen:
    id: String
    extension: Extension
    modifier_extension: Extension
    question: String
    operator: CQFQuestionnaire_Item_EnableWhen_OperatorCode
    answer: CQFQuestionnaire_Item_EnableWhen_AnswerX


@dataclass
class CQFQuestionnaire_Item_EnableWhen_OperatorCode:
    value: QuestionnaireItemOperatorCode_Value
    id: String
    extension: Extension


@dataclass
class CQFQuestionnaire_Item_EnableWhen_AnswerX:
    boolean: Boolean
    decimal: Decimal
    integer: Integer
    date: Date
    date_time: DateTime
    time: Time
    string_value: String
    coding: Coding
    quantity: Quantity
    reference: Reference


@dataclass
class CQFQuestionnaire_Item_EnableBehaviorCode:
    value: EnableWhenBehaviorCode_Value
    id: String
    extension: Extension


@dataclass
class CQFQuestionnaire_Item_AnswerOption:
    id: String
    extension: Extension
    modifier_extension: Extension
    value: CQFQuestionnaire_Item_AnswerOption_ValueX
    initial_selected: Boolean


@dataclass
class CQFQuestionnaire_Item_AnswerOption_ValueX:
    integer: Integer
    date: Date
    time: Time
    string_value: String
    coding: Coding
    reference: Reference


@dataclass
class CQFQuestionnaire_Item_Initial:
    id: String
    extension: Extension
    modifier_extension: Extension
    value: CQFQuestionnaire_Item_Initial_ValueX


@dataclass
class CQFQuestionnaire_Item_Initial_ValueX:
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

