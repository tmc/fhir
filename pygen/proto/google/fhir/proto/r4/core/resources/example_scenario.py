# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ExampleScenario:
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
    status: ExampleScenario_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    use_context: UsageContext
    jurisdiction: CodeableConcept
    copyright: Markdown
    purpose: Markdown
    actor: ExampleScenario_Actor
    instance: ExampleScenario_Instance
    process: ExampleScenario_Process
    workflow: Canonical


@dataclass
class ExampleScenario_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ExampleScenario_Actor:
    id: String
    extension: Extension
    modifier_extension: Extension
    actor_id: String
    type: ExampleScenario_Actor_TypeCode
    name: String
    description: Markdown


@dataclass
class ExampleScenario_Actor_TypeCode:
    value: ExampleScenarioActorTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ExampleScenario_Instance:
    id: String
    extension: Extension
    modifier_extension: Extension
    resource_id: String
    resource_type: ExampleScenario_Instance_ResourceTypeCode
    name: String
    description: Markdown
    version: ExampleScenario_Instance_Version
    contained_instance: ExampleScenario_Instance_ContainedInstance


@dataclass
class ExampleScenario_Instance_ResourceTypeCode:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ExampleScenario_Instance_Version:
    id: String
    extension: Extension
    modifier_extension: Extension
    version_id: String
    description: Markdown


@dataclass
class ExampleScenario_Instance_ContainedInstance:
    id: String
    extension: Extension
    modifier_extension: Extension
    resource_id: String
    version_id: String


@dataclass
class ExampleScenario_Process:
    id: String
    extension: Extension
    modifier_extension: Extension
    title: String
    description: Markdown
    pre_conditions: Markdown
    post_conditions: Markdown
    step: ExampleScenario_Process_Step


@dataclass
class ExampleScenario_Process_Step:
    id: String
    extension: Extension
    modifier_extension: Extension
    process: ExampleScenario_Process
    pause: Boolean
    operation: ExampleScenario_Process_Step_Operation
    alternative: ExampleScenario_Process_Step_Alternative


@dataclass
class ExampleScenario_Process_Step_Operation:
    id: String
    extension: Extension
    modifier_extension: Extension
    number: String
    type: String
    name: String
    initiator: String
    receiver: String
    description: Markdown
    initiator_active: Boolean
    receiver_active: Boolean
    request: ExampleScenario_Instance_ContainedInstance
    response: ExampleScenario_Instance_ContainedInstance


@dataclass
class ExampleScenario_Process_Step_Alternative:
    id: String
    extension: Extension
    modifier_extension: Extension
    title: String
    description: Markdown
    step: ExampleScenario_Process_Step

