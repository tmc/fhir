# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.proto
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict


class FhirVersion(Enum):
    FhirVersion_FHIR_VERSION_UNKNOWN = 0 
    FhirVersion_DSTU2 = 1 
    FhirVersion_STU3 = 2 
    FhirVersion_R4 = 4 
    FhirVersion_R4B = 45 
    FhirVersion_R5 = 5 

class StructureDefinitionKindValue(Enum):
    StructureDefinitionKindValue_KIND_UNKNOWN = 0 
    StructureDefinitionKindValue_KIND_PRIMITIVE_TYPE = 1 
    StructureDefinitionKindValue_KIND_COMPLEX_TYPE = 2 
    StructureDefinitionKindValue_KIND_RESOURCE = 3 
    StructureDefinitionKindValue_KIND_LOGICAL = 4 

class Requirement(Enum):
    Requirement_NOT_REQUIRED = 0 
    Requirement_REQUIRED_BY_FHIR = 1 

class SearchParameterType(Enum):
    SearchParameterType_INVALID_SEARCH_PARAMETER_TYPE = 0 
    SearchParameterType_NUMBER = 1 
    SearchParameterType_DATE = 2 
    SearchParameterType_STRING = 3 
    SearchParameterType_TOKEN = 4 
    SearchParameterType_REFERENCE = 5 
    SearchParameterType_COMPOSITE = 6 
    SearchParameterType_QUANTITY = 7 
    SearchParameterType_URI = 8 
    SearchParameterType_SPECIAL = 9 


@dataclass
class SearchParameter:
    name: str
    type: SearchParameterType
    expression: str

