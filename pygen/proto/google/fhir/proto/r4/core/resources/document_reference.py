# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class DocumentReference:
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
    status: DocumentReference_StatusCode
    doc_status: DocumentReference_DocStatusCode
    type: CodeableConcept
    category: CodeableConcept
    subject: Reference
    date: Instant
    author: Reference
    authenticator: Reference
    custodian: Reference
    relates_to: DocumentReference_RelatesTo
    description: String
    security_label: CodeableConcept
    content: DocumentReference_Content
    context: DocumentReference_Context


@dataclass
class DocumentReference_StatusCode:
    value: DocumentReferenceStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DocumentReference_DocStatusCode:
    value: CompositionStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DocumentReference_RelatesTo:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: DocumentReference_RelatesTo_CodeType
    target: Reference


@dataclass
class DocumentReference_RelatesTo_CodeType:
    value: DocumentRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class DocumentReference_Content:
    id: String
    extension: Extension
    modifier_extension: Extension
    attachment: Attachment
    format: Coding


@dataclass
class DocumentReference_Context:
    id: String
    extension: Extension
    modifier_extension: Extension
    encounter: Reference
    event: CodeableConcept
    period: Period
    facility_type: CodeableConcept
    practice_setting: CodeableConcept
    source_patient_info: Reference
    related: Reference

