# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class TestScript:
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
    status: TestScript_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    origin: TestScript_Origin
    destination: TestScript_Destination
    metadata: TestScript_Metadata
    fixture: TestScript_Fixture
    profile: Reference
    variable: TestScript_Variable
    setup: TestScript_Setup
    test: TestScript_Test
    teardown: TestScript_Teardown


@dataclass
class TestScript_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class TestScript_Origin:
    id: String
    extension: Extension
    modifier_extension: Extension
    index: Integer
    profile: Coding


@dataclass
class TestScript_Destination:
    id: String
    extension: Extension
    modifier_extension: Extension
    index: Integer
    profile: Coding


@dataclass
class TestScript_Metadata:
    id: String
    extension: Extension
    modifier_extension: Extension
    link: TestScript_Metadata_Link
    capability: TestScript_Metadata_Capability


@dataclass
class TestScript_Metadata_Link:
    id: String
    extension: Extension
    modifier_extension: Extension
    url: Uri
    description: String


@dataclass
class TestScript_Metadata_Capability:
    id: String
    extension: Extension
    modifier_extension: Extension
    required: Boolean
    validated: Boolean
    description: String
    origin: Integer
    destination: Integer
    link: Uri
    capabilities: Canonical


@dataclass
class TestScript_Fixture:
    id: String
    extension: Extension
    modifier_extension: Extension
    autocreate: Boolean
    autodelete: Boolean
    resource: Reference


@dataclass
class TestScript_Variable:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    default_value: String
    description: String
    expression: String
    header_field: String
    hint: String
    path: String
    source_id: Id


@dataclass
class TestScript_Setup:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: TestScript_Setup_SetupAction


@dataclass
class TestScript_Setup_SetupAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation: TestScript_Setup_SetupAction_Operation
    assert_value: TestScript_Setup_SetupAction_Assert


@dataclass
class TestScript_Setup_SetupAction_Operation:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: Coding
    resource: TestScript_Setup_SetupAction_Operation_ResourceCode
    label: String
    description: String
    accept: TestScript_Setup_SetupAction_Operation_AcceptCode
    content_type: TestScript_Setup_SetupAction_Operation_ContentTypeCode
    destination: Integer
    encode_request_url: Boolean
    method: TestScript_Setup_SetupAction_Operation_MethodCode
    origin: Integer
    params: String
    request_header: TestScript_Setup_SetupAction_Operation_RequestHeader
    request_id: Id
    response_id: Id
    source_id: Id
    target_id: Id
    url: String


@dataclass
class TestScript_Setup_SetupAction_Operation_ResourceCode:
    value: FHIRDefinedTypeValueSet_Value
    id: String
    extension: Extension


@dataclass
class TestScript_Setup_SetupAction_Operation_AcceptCode:
    id: String
    extension: Extension
    value: str


@dataclass
class TestScript_Setup_SetupAction_Operation_ContentTypeCode:
    id: String
    extension: Extension
    value: str


@dataclass
class TestScript_Setup_SetupAction_Operation_MethodCode:
    value: TestScriptRequestMethodCode_Value
    id: String
    extension: Extension


@dataclass
class TestScript_Setup_SetupAction_Operation_RequestHeader:
    id: String
    extension: Extension
    modifier_extension: Extension
    field: String
    value: String


@dataclass
class TestScript_Setup_SetupAction_Assert:
    id: String
    extension: Extension
    modifier_extension: Extension
    label: String
    description: String
    direction: TestScript_Setup_SetupAction_Assert_DirectionCode
    compare_to_source_id: String
    compare_to_source_expression: String
    compare_to_source_path: String
    content_type: TestScript_Setup_SetupAction_Assert_ContentTypeCode
    expression: String
    header_field: String
    minimum_id: String
    navigation_links: Boolean
    operator: TestScript_Setup_SetupAction_Assert_OperatorCode
    path: String
    request_method: TestScript_Setup_SetupAction_Assert_RequestMethodCode
    request_url: String
    resource: TestScript_Setup_SetupAction_Assert_ResourceCode
    response: TestScript_Setup_SetupAction_Assert_ResponseCode
    response_code: String
    source_id: Id
    validate_profile_id: Id
    value: String
    warning_only: Boolean


@dataclass
class TestScript_Setup_SetupAction_Assert_DirectionCode:
    value: AssertionDirectionTypeCode_Value
    id: String
    extension: Extension


@dataclass
class TestScript_Setup_SetupAction_Assert_ContentTypeCode:
    id: String
    extension: Extension
    value: str


@dataclass
class TestScript_Setup_SetupAction_Assert_OperatorCode:
    value: AssertionOperatorTypeCode_Value
    id: String
    extension: Extension


@dataclass
class TestScript_Setup_SetupAction_Assert_RequestMethodCode:
    value: TestScriptRequestMethodCode_Value
    id: String
    extension: Extension


@dataclass
class TestScript_Setup_SetupAction_Assert_ResourceCode:
    value: FHIRDefinedTypeValueSet_Value
    id: String
    extension: Extension


@dataclass
class TestScript_Setup_SetupAction_Assert_ResponseCode:
    value: AssertionResponseTypesCode_Value
    id: String
    extension: Extension


@dataclass
class TestScript_Test:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    description: String
    action: TestScript_Test_TestAction


@dataclass
class TestScript_Test_TestAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation: TestScript_Setup_SetupAction_Operation
    assert_value: TestScript_Setup_SetupAction_Assert


@dataclass
class TestScript_Teardown:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: TestScript_Teardown_TeardownAction


@dataclass
class TestScript_Teardown_TeardownAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation: TestScript_Setup_SetupAction_Operation

