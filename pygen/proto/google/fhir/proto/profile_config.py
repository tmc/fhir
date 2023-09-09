# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.proto
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict


class SizeRestriction(Enum):
    SizeRestriction_UNSET = 0  # Does not set a size restriction on the field.
    SizeRestriction_ABSENT = 1  # Field should have zero values, i.e. omitted from the record.
    SizeRestriction_REQUIRED = 2  # Field must have exactly one value.
    SizeRestriction_OPTIONAL = 3  # Field may have zero or one value.
    SizeRestriction_AT_LEAST_ONE = 4  # Repeated field that should have at least one value.
    SizeRestriction_REPEATED = 5  # Repeated field that may have zero or more values.


@dataclass
class ProtogenConfig:
    proto_package: str
    java_proto_package: str
    go_proto_package: str
    source_directory: str
    license_date: str
    fhir_version: FhirVersion


@dataclass
class PackageInfo:
    fhir_version: FhirVersion
    base_url: str
    proto_package: str
    java_proto_package: str
    go_proto_package: str
    local_contained_resource: bool # Generates a local ContainedResource
    contained_resource_package: str # A fully-qualified
    publisher: str
    telcom_url: str
    license: PackageInfo_License
    license_date: str
    contained_resource_behavior: PackageInfo_ContainedResourceBehavior
    file_splitting_behavior: PackageInfo_FileSplittingBehavior
    version: str


@dataclass
class Profiles:
    profile: Profile


@dataclass
class Extensions:
    simple_extension: SimpleExtension
    complex_extension: ComplexExtension


@dataclass
class Terminologies:
    code_system: CodeSystemConfig
    value_set: ValueSetConfig


@dataclass
class Profile:
    element_data: ElementData
    base_url: str
    element_definition: ElementDefinition
    extension_slice: ExtensionSlice
    codeable_concept_slice: CodeableConceptSlice
    restriction: FieldRestriction


@dataclass
class FieldRestriction:
    field_id: str
    size_restriction: SizeRestriction
    reference_restriction: ReferenceRestriction
    choice_type_restriction: ChoiceTypeRestriction
    fhir_path_constraint: FhirPathConstraint
    value_set_binding: ValueSetBinding


@dataclass
class ReferenceRestriction:
    allowed: str


@dataclass
class ChoiceTypeRestriction:
    allowed: str


@dataclass
class FhirPathConstraint:
    severity: FhirPathConstraint_Severity
    description: str
    expression: str


@dataclass
class ExtensionSlice:
    field_id: str
    element_data: ElementData
    url: str
    must_support: bool


@dataclass
class CodeableConceptSlice:
    field_id: str
    coding_slice: CodeableConceptSlice_CodingSlice
    rules: SlicingRulesCode_Value


@dataclass
class CodeableConceptSlice_CodingSlice:
    element_data: ElementData
    code_data: ValueSetBinding


@dataclass
class ComplexExtension:
    element_data: ElementData
    can_have_additional_extensions: bool
    simple_field: SimpleExtension
    complex_field: ComplexExtension


@dataclass
class SimpleExtension:
    element_data: ElementData
    type: str
    code_type: ValueSetBinding
    can_have_extensions: bool


@dataclass
class ElementData:
    name: str
    size_restriction: SizeRestriction
    description: str
    short: str
    comment: str
    url_override: str


@dataclass
class ValueSetBinding:
    system: str
    binding_strength: BindingStrengthCode_Value
    fixed_value: str
    description: str


@dataclass
class CodeSystemConfig:
    name: str
    status: PublicationStatusCode_Value
    description: str
    url_override: str
    concept: CodeSystemConfig_Concept


@dataclass
class CodeSystemConfig_Concept:
    code: str
    display: str
    definition: str
    deprecated: bool


@dataclass
class ValueSetConfig:
    name: str
    status: PublicationStatusCode_Value
    description: str
    url_override: str
    system: ValueSetConfig_System


@dataclass
class ValueSetConfig_System:
    url: str
    include: str
    exclude: str

