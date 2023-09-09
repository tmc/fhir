# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MessageDefinition:
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
    replaces: Canonical
    status: MessageDefinition_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    base: Canonical
    parent: Canonical
    event: MessageDefinition_EventX
    category: MessageDefinition_CategoryCode
    focus: MessageDefinition_Focus
    response_required: MessageDefinition_ResponseRequiredCode
    allowed_response: MessageDefinition_AllowedResponse
    graph: Canonical


@dataclass
class MessageDefinition_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class MessageDefinition_EventX:
    coding: Coding
    uri: Uri


@dataclass
class MessageDefinition_CategoryCode:
    value: MessageSignificanceCategoryCode_Value
    id: String
    extension: Extension


@dataclass
class MessageDefinition_Focus:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: MessageDefinition_Focus_CodeType
    profile: Canonical
    min: UnsignedInt
    max: String


@dataclass
class MessageDefinition_Focus_CodeType:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class MessageDefinition_ResponseRequiredCode:
    value: MessageheaderResponseRequestCode_Value
    id: String
    extension: Extension


@dataclass
class MessageDefinition_AllowedResponse:
    id: String
    extension: Extension
    modifier_extension: Extension
    message: Canonical
    situation: Markdown

