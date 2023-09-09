# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class CapabilityStatement:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    url: Uri
    version: String
    name: String
    title: String
    status: CapabilityStatement_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    purpose: Markdown
    copyright: Markdown
    kind: CapabilityStatement_KindCode
    instantiates: Canonical
    imports: Canonical
    software: CapabilityStatement_Software
    implementation: CapabilityStatement_Implementation
    fhir_version: CapabilityStatement_FhirVersionCode
    format: CapabilityStatement_FormatCode
    patch_format: CapabilityStatement_PatchFormatCode
    implementation_guide: Canonical
    rest: CapabilityStatement_Rest
    messaging: CapabilityStatement_Messaging
    document: CapabilityStatement_Document


@dataclass
class CapabilityStatement_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_KindCode:
    value: CapabilityStatementKindCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_Software:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    version: String
    release_date: DateTime


@dataclass
class CapabilityStatement_Implementation:
    id: String
    extension: Extension
    modifier_extension: Extension
    description: String
    url: Url
    custodian: Reference


@dataclass
class CapabilityStatement_FhirVersionCode:
    value: FHIRVersionCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_FormatCode:
    id: String
    extension: Extension
    value: str


@dataclass
class CapabilityStatement_PatchFormatCode:
    id: String
    extension: Extension
    value: str


@dataclass
class CapabilityStatement_Rest:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: CapabilityStatement_Rest_ModeCode
    documentation: Markdown
    security: CapabilityStatement_Rest_Security
    resource: CapabilityStatement_Rest_Resource
    interaction: CapabilityStatement_Rest_SystemInteraction
    search_param: CapabilityStatement_Rest_Resource_SearchParam
    operation: CapabilityStatement_Rest_Resource_Operation
    compartment: Canonical


@dataclass
class CapabilityStatement_Rest_ModeCode:
    value: RestfulCapabilityModeCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_Rest_Security:
    id: String
    extension: Extension
    modifier_extension: Extension
    cors: Boolean
    service: CodeableConcept
    description: Markdown


@dataclass
class CapabilityStatement_Rest_Resource:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CapabilityStatement_Rest_Resource_TypeCode
    profile: Canonical
    supported_profile: Canonical
    documentation: Markdown
    interaction: CapabilityStatement_Rest_Resource_ResourceInteraction
    versioning: CapabilityStatement_Rest_Resource_VersioningCode
    read_history: Boolean
    update_create: Boolean
    conditional_create: Boolean
    conditional_read: CapabilityStatement_Rest_Resource_ConditionalReadCode
    conditional_update: Boolean
    conditional_delete: CapabilityStatement_Rest_Resource_ConditionalDeleteCode
    reference_policy: CapabilityStatement_Rest_Resource_ReferencePolicyCode
    search_include: String
    search_rev_include: String
    search_param: CapabilityStatement_Rest_Resource_SearchParam
    operation: CapabilityStatement_Rest_Resource_Operation


@dataclass
class CapabilityStatement_Rest_Resource_TypeCode:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_Rest_Resource_ResourceInteraction:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CapabilityStatement_Rest_Resource_ResourceInteraction_CodeType
    documentation: Markdown


@dataclass
class CapabilityStatement_Rest_Resource_ResourceInteraction_CodeType:
    value: TypeRestfulInteractionValueSet_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_Rest_Resource_VersioningCode:
    value: ResourceVersionPolicyCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_Rest_Resource_ConditionalReadCode:
    value: ConditionalReadStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_Rest_Resource_ConditionalDeleteCode:
    value: ConditionalDeleteStatusCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_Rest_Resource_ReferencePolicyCode:
    value: ReferenceHandlingPolicyCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_Rest_Resource_SearchParam:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    definition: Canonical
    type: CapabilityStatement_Rest_Resource_SearchParam_TypeCode
    documentation: Markdown


@dataclass
class CapabilityStatement_Rest_Resource_SearchParam_TypeCode:
    value: SearchParamTypeCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_Rest_Resource_Operation:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    definition: Canonical
    documentation: Markdown


@dataclass
class CapabilityStatement_Rest_SystemInteraction:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: CapabilityStatement_Rest_SystemInteraction_CodeType
    documentation: Markdown


@dataclass
class CapabilityStatement_Rest_SystemInteraction_CodeType:
    value: SystemRestfulInteractionValueSet_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_Messaging:
    id: String
    extension: Extension
    modifier_extension: Extension
    endpoint: CapabilityStatement_Messaging_Endpoint
    reliable_cache: UnsignedInt
    documentation: Markdown
    supported_message: CapabilityStatement_Messaging_SupportedMessage


@dataclass
class CapabilityStatement_Messaging_Endpoint:
    id: String
    extension: Extension
    modifier_extension: Extension
    protocol: Coding
    address: Url


@dataclass
class CapabilityStatement_Messaging_SupportedMessage:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: CapabilityStatement_Messaging_SupportedMessage_ModeCode
    definition: Canonical


@dataclass
class CapabilityStatement_Messaging_SupportedMessage_ModeCode:
    value: EventCapabilityModeCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatement_Document:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: CapabilityStatement_Document_ModeCode
    documentation: Markdown
    profile: Canonical


@dataclass
class CapabilityStatement_Document_ModeCode:
    value: DocumentModeCode_Value
    id: String
    extension: Extension

