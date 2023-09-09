# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class ImplementationGuide:
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
    status: ImplementationGuide_StatusCode
    experimental: Boolean
    date: DateTime
    publisher: String
    contact: ContactDetail
    description: Markdown
    use_context: UsageContext
    jurisdiction: CodeableConcept
    copyright: Markdown
    package_id: Id
    license: ImplementationGuide_LicenseCode
    fhir_version: ImplementationGuide_FhirVersionCode
    depends_on: ImplementationGuide_DependsOn
    global: ImplementationGuide_Global
    definition: ImplementationGuide_Definition
    manifest: ImplementationGuide_Manifest


@dataclass
class ImplementationGuide_StatusCode:
    value: PublicationStatusCode_Value
    id: String
    extension: Extension


@dataclass
class ImplementationGuide_LicenseCode:
    value: SPDXLicenseCode_Value
    id: String
    extension: Extension


@dataclass
class ImplementationGuide_FhirVersionCode:
    value: FHIRVersionCode_Value
    id: String
    extension: Extension


@dataclass
class ImplementationGuide_DependsOn:
    id: String
    extension: Extension
    modifier_extension: Extension
    uri: Canonical
    package_id: Id
    version: String


@dataclass
class ImplementationGuide_Global:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: ImplementationGuide_Global_TypeCode
    profile: Canonical


@dataclass
class ImplementationGuide_Global_TypeCode:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class ImplementationGuide_Definition:
    id: String
    extension: Extension
    modifier_extension: Extension
    grouping: ImplementationGuide_Definition_Grouping
    resource: ImplementationGuide_Definition_Resource
    page: ImplementationGuide_Definition_Page
    parameter: ImplementationGuide_Definition_Parameter
    template: ImplementationGuide_Definition_Template


@dataclass
class ImplementationGuide_Definition_Grouping:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    description: String


@dataclass
class ImplementationGuide_Definition_Resource:
    id: String
    extension: Extension
    modifier_extension: Extension
    reference: Reference
    fhir_version: ImplementationGuide_Definition_Resource_FhirVersionCode
    name: String
    description: String
    example: ImplementationGuide_Definition_Resource_ExampleX
    grouping_id: Id


@dataclass
class ImplementationGuide_Definition_Resource_FhirVersionCode:
    value: FHIRVersionCode_Value
    id: String
    extension: Extension


@dataclass
class ImplementationGuide_Definition_Resource_ExampleX:
    boolean: Boolean
    canonical: Canonical


@dataclass
class ImplementationGuide_Definition_Page:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: ImplementationGuide_Definition_Page_NameX
    title: String
    generation: ImplementationGuide_Definition_Page_GenerationCode
    page: ImplementationGuide_Definition_Page


@dataclass
class ImplementationGuide_Definition_Page_NameX:
    url: Url
    reference: Reference


@dataclass
class ImplementationGuide_Definition_Page_GenerationCode:
    value: GuidePageGenerationCode_Value
    id: String
    extension: Extension


@dataclass
class ImplementationGuide_Definition_Parameter:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: ImplementationGuide_Definition_Parameter_CodeType
    value: String


@dataclass
class ImplementationGuide_Definition_Parameter_CodeType:
    value: GuideParameterCode_Value
    id: String
    extension: Extension


@dataclass
class ImplementationGuide_Definition_Template:
    id: String
    extension: Extension
    modifier_extension: Extension
    code: Code
    source: String
    scope: String


@dataclass
class ImplementationGuide_Manifest:
    id: String
    extension: Extension
    modifier_extension: Extension
    rendering: Url
    resource: ImplementationGuide_Manifest_ManifestResource
    page: ImplementationGuide_Manifest_ManifestPage
    image: String
    other: String


@dataclass
class ImplementationGuide_Manifest_ManifestResource:
    id: String
    extension: Extension
    modifier_extension: Extension
    reference: Reference
    example: ImplementationGuide_Manifest_ManifestResource_ExampleX
    relative_path: Url


@dataclass
class ImplementationGuide_Manifest_ManifestResource_ExampleX:
    boolean: Boolean
    canonical: Canonical


@dataclass
class ImplementationGuide_Manifest_ManifestPage:
    id: String
    extension: Extension
    modifier_extension: Extension
    name: String
    title: String
    anchor: String

