# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class List:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    status: List_StatusCode
    mode: List_ModeCode
    title: String
    code: CodeableConcept
    subject: Reference
    encounter: Reference
    date: DateTime
    source: Reference
    ordered_by: CodeableConcept
    note: Annotation
    entry: List_Entry
    empty_reason: CodeableConcept


@dataclass
class List_StatusCode:
    value: ListStatusCode_Value
    id: String
    extension: Extension


@dataclass
class List_ModeCode:
    value: ListModeCode_Value
    id: String
    extension: Extension


@dataclass
class List_Entry:
    id: String
    extension: Extension
    modifier_extension: Extension
    flag: CodeableConcept
    deleted: Boolean
    date: DateTime
    item: Reference

