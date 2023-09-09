# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class NamingSystem:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    name: String
    status: NamingSystem_StatusCode
    kind: NamingSystem_KindCode
    date: DateTime
    publisher: String
    contact: ContactDetail
    responsible: String
    type: CodeableConcept
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    usage: String
    unique_id: NamingSystem_UniqueId


@dataclass
class NamingSystem_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class NamingSystem_KindCode:
    value: NamingSystemTypeCode_Value
    id: String
    extension: Extension


@dataclass
class NamingSystem_UniqueId:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: NamingSystem_UniqueId_TypeCode
    value: String
    preferred: Boolean
    comment: String
    period: Period


@dataclass
class NamingSystem_UniqueId_TypeCode:
    value: NamingSystemIdentifierTypeCode_Value
    id: String
    extension: Extension

