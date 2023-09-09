# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class AuditEvent:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    type: Coding
    subtype: Coding
    action: AuditEvent_ActionCode
    period: Period
    recorded: Instant
    outcome: AuditEvent_OutcomeCode
    outcome_desc: String
    purpose_of_event: CodeableConcept
    agent: AuditEvent_Agent
    source: AuditEvent_Source
    entity: AuditEvent_Entity


@dataclass
class AuditEvent_ActionCode:
    value: AuditEventActionCode_Value
    id: String
    extension: Extension


@dataclass
class AuditEvent_OutcomeCode:
    value: AuditEventOutcomeCode_Value
    id: String
    extension: Extension


@dataclass
class AuditEvent_Agent:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    role: CodeableConcept
    who: Reference
    alt_id: String
    name: String
    requestor: Boolean
    location: Reference
    policy: Uri
    media: Coding
    network: AuditEvent_Agent_Network
    purpose_of_use: CodeableConcept


@dataclass
class AuditEvent_Agent_Network:
    id: String
    extension: Extension
    modifier_extension: Extension
    address: String
    type: AuditEvent_Agent_Network_TypeCode


@dataclass
class AuditEvent_Agent_Network_TypeCode:
    value: AuditEventAgentNetworkTypeCode_Value
    id: String
    extension: Extension


@dataclass
class AuditEvent_Source:
    id: String
    extension: Extension
    modifier_extension: Extension
    site: String
    observer: Reference
    type: Coding


@dataclass
class AuditEvent_Entity:
    id: String
    extension: Extension
    modifier_extension: Extension
    what: Reference
    type: Coding
    role: Coding
    lifecycle: Coding
    security_label: Coding
    name: String
    description: String
    query: Base64Binary
    detail: AuditEvent_Entity_Detail


@dataclass
class AuditEvent_Entity_Detail:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: String
    value: AuditEvent_Entity_Detail_ValueX


@dataclass
class AuditEvent_Entity_Detail_ValueX:
    string_value: String
    base64_binary: Base64Binary

