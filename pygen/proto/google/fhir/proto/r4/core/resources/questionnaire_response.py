# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class QuestionnaireResponse:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    based_on: Reference
    part_of: Reference
    questionnaire: Canonical
    status: QuestionnaireResponse_StatusCode
    subject: Reference
    encounter: Reference
    authored: DateTime
    author: Reference
    source: Reference
    item: QuestionnaireResponse_Item


@dataclass
class QuestionnaireResponse_StatusCode:
    value: QuestionnaireResponseStatusCode_Value
    id: String
    extension: Extension


@dataclass
class QuestionnaireResponse_Item:
    id: String
    extension: Extension
    modifier_extension: Extension
    link_id: String
    definition: Uri
    text: String
    answer: QuestionnaireResponse_Item_Answer
    item: QuestionnaireResponse_Item


@dataclass
class QuestionnaireResponse_Item_Answer:
    id: String
    extension: Extension
    modifier_extension: Extension
    value: QuestionnaireResponse_Item_Answer_ValueX
    item: QuestionnaireResponse_Item


@dataclass
class QuestionnaireResponse_Item_Answer_ValueX:
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

