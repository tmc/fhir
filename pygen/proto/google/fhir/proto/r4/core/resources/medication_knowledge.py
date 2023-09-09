# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class MedicationKnowledge:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    text: Narrative
    contained: Any
    extension: Extension
    modifier_extension: Extension
    code: CodeableConcept
    status: MedicationKnowledge_StatusCode
    manufacturer: Reference
    dose_form: CodeableConcept
    amount: SimpleQuantity
    synonym: String
    related_medication_knowledge: MedicationKnowledge_RelatedMedicationKnowledge
    associated_medication: Reference
    product_type: CodeableConcept
    monograph: MedicationKnowledge_Monograph
    ingredient: MedicationKnowledge_Ingredient
    preparation_instruction: Markdown
    intended_route: CodeableConcept
    cost: MedicationKnowledge_Cost
    monitoring_program: MedicationKnowledge_MonitoringProgram
    administration_guidelines: MedicationKnowledge_AdministrationGuidelines
    medicine_classification: MedicationKnowledge_MedicineClassification
    packaging: MedicationKnowledge_Packaging
    drug_characteristic: MedicationKnowledge_DrugCharacteristic
    contraindication: Reference
    regulatory: MedicationKnowledge_Regulatory
    kinetics: MedicationKnowledge_Kinetics


@dataclass
class MedicationKnowledge_StatusCode:
    value: MedicationKnowledgeStatusCode_Value
    id: String
    extension: Extension


@dataclass
class MedicationKnowledge_RelatedMedicationKnowledge:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    reference: Reference


@dataclass
class MedicationKnowledge_Monograph:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    source: Reference


@dataclass
class MedicationKnowledge_Ingredient:
    id: String
    extension: Extension
    modifier_extension: Extension
    item: MedicationKnowledge_Ingredient_ItemX
    is_active: Boolean
    strength: Ratio


@dataclass
class MedicationKnowledge_Ingredient_ItemX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class MedicationKnowledge_Cost:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    source: String
    cost: Money


@dataclass
class MedicationKnowledge_MonitoringProgram:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    name: String


@dataclass
class MedicationKnowledge_AdministrationGuidelines:
    id: String
    extension: Extension
    modifier_extension: Extension
    dosage: MedicationKnowledge_AdministrationGuidelines_Dosage
    indication: MedicationKnowledge_AdministrationGuidelines_IndicationX
    patient_characteristics: MedicationKnowledge_AdministrationGuidelines_PatientCharacteristics


@dataclass
class MedicationKnowledge_AdministrationGuidelines_Dosage:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    dosage: Dosage


@dataclass
class MedicationKnowledge_AdministrationGuidelines_IndicationX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class MedicationKnowledge_AdministrationGuidelines_PatientCharacteristics:
    id: String
    extension: Extension
    modifier_extension: Extension
    characteristic: MedicationKnowledge_AdministrationGuidelines_PatientCharacteristics_CharacteristicX
    value: String


@dataclass
class MedicationKnowledge_AdministrationGuidelines_PatientCharacteristics_CharacteristicX:
    codeable_concept: CodeableConcept
    quantity: SimpleQuantity


@dataclass
class MedicationKnowledge_MedicineClassification:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    classification: CodeableConcept


@dataclass
class MedicationKnowledge_Packaging:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    quantity: SimpleQuantity


@dataclass
class MedicationKnowledge_DrugCharacteristic:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    value: MedicationKnowledge_DrugCharacteristic_ValueX


@dataclass
class MedicationKnowledge_DrugCharacteristic_ValueX:
    codeable_concept: CodeableConcept
    string_value: String
    quantity: SimpleQuantity
    base64_binary: Base64Binary


@dataclass
class MedicationKnowledge_Regulatory:
    id: String
    extension: Extension
    modifier_extension: Extension
    regulatory_authority: Reference
    substitution: MedicationKnowledge_Regulatory_Substitution
    schedule: MedicationKnowledge_Regulatory_Schedule
    max_dispense: MedicationKnowledge_Regulatory_MaxDispense


@dataclass
class MedicationKnowledge_Regulatory_Substitution:
    id: String
    extension: Extension
    modifier_extension: Extension
    type: CodeableConcept
    allowed: Boolean


@dataclass
class MedicationKnowledge_Regulatory_Schedule:
    id: String
    extension: Extension
    modifier_extension: Extension
    schedule: CodeableConcept


@dataclass
class MedicationKnowledge_Regulatory_MaxDispense:
    id: String
    extension: Extension
    modifier_extension: Extension
    quantity: SimpleQuantity
    period: Duration


@dataclass
class MedicationKnowledge_Kinetics:
    id: String
    extension: Extension
    modifier_extension: Extension
    area_under_curve: SimpleQuantity
    lethal_dose50: SimpleQuantity
    half_life_period: Duration

