# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class TestReport:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    identifier: Identifier
    name: String
    status: TestReport_StatusCode
    test_script: Reference
    result: TestReport_ResultCode
    score: Decimal
    tester: String
    issued: DateTime
    participant: TestReport_Participant
    setup: TestReport_Setup
    test: TestReport_Test
    teardown: TestReport_Teardown


@dataclass
class TestReport_StatusCode:
    value: TestReportStatusCode_Value
    id: String
    extension: Extension


@dataclass
class TestReport_ResultCode:
    value: TestReportResultCode_Value
    id: String
    extension: Extension


@dataclass
class TestReport_Participant:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: TestReport_Participant_TypeCode
    uri: Uri
    display: String


@dataclass
class TestReport_Participant_TypeCode:
    value: TestReportParticipantTypeCode_Value
    id: String
    extension: Extension


@dataclass
class TestReport_Setup:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: TestReport_Setup_SetupAction


@dataclass
class TestReport_Setup_SetupAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation: TestReport_Setup_SetupAction_Operation
    assert_value: TestReport_Setup_SetupAction_Assert


@dataclass
class TestReport_Setup_SetupAction_Operation:
    id: String
    extension: Extension
    modifier_extension: Extension
    result: TestReport_Setup_SetupAction_Operation_ResultCode
    message: Markdown
    detail: Uri


@dataclass
class TestReport_Setup_SetupAction_Operation_ResultCode:
    value: TestReportActionResultCode_Value
    id: String
    extension: Extension


@dataclass
class TestReport_Setup_SetupAction_Assert:
    id: String
    extension: Extension
    modifier_extension: Extension
    result: TestReport_Setup_SetupAction_Assert_ResultCode
    message: Markdown
    detail: String


@dataclass
class TestReport_Setup_SetupAction_Assert_ResultCode:
    value: TestReportActionResultCode_Value
    id: String
    extension: Extension


@dataclass
class TestReport_Test:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    description: String
    action: TestReport_Test_TestAction


@dataclass
class TestReport_Test_TestAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation: TestReport_Setup_SetupAction_Operation
    assert_value: TestReport_Setup_SetupAction_Assert


@dataclass
class TestReport_Teardown:
    id: String
    extension: Extension
    modifier_extension: Extension
    action: TestReport_Teardown_TeardownAction


@dataclass
class TestReport_Teardown_TeardownAction:
    id: String
    extension: Extension
    modifier_extension: Extension
    operation: TestReport_Setup_SetupAction_Operation

