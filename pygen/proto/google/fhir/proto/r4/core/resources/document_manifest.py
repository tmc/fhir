# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class DocumentManifest:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    master_identifier: Identifier
    identifier: Identifier
    status: DocumentManifest_StatusCode
    type: CodeableConcept
    subject: Reference
    created: DateTime
    author: Reference
    recipient: Reference
    source: Uri
    description: String
    content: Reference
    related: DocumentManifest_Related


@dataclass
class DocumentManifest_StatusCode:
    value: DocumentReferenceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DocumentManifest_Related:
    id: String
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    ref: Reference

