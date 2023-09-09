# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class Bundle:
    id: Id
    meta: Meta
    implicit_rules: Uri
    language: Code
    identifier: Identifier
    type: Bundle_TypeCode
    timestamp: Instant
    total: UnsignedInt
    link: Bundle_Link
    entry: Bundle_Entry
    signature: Signature


@dataclass
class Bundle_TypeCode:
    value: BundleTypeCode_Value
    id: String
    extension: Extension


@dataclass
class Bundle_Link:
    id: String
    extension: Extension
    modifier_extension: Extension
    relation: String
    url: Uri


@dataclass
class Bundle_Entry:
    id: String
    extension: Extension
    modifier_extension: Extension
    link: Bundle_Link
    full_url: Uri
    resource: ContainedResource
    search: Bundle_Entry_Search
    request: Bundle_Entry_Request
    response: Bundle_Entry_Response


@dataclass
class Bundle_Entry_Search:
    id: String
    extension: Extension
    modifier_extension: Extension
    mode: Bundle_Entry_Search_ModeCode
    score: Decimal


@dataclass
class Bundle_Entry_Search_ModeCode:
    value: SearchEntryModeCode_Value
    id: String
    extension: Extension


@dataclass
class Bundle_Entry_Request:
    id: String
    extension: Extension
    modifier_extension: Extension
    method: Bundle_Entry_Request_MethodCode
    url: Uri
    if_none_match: String
    if_modified_since: Instant
    if_match: String
    if_none_exist: String


@dataclass
class Bundle_Entry_Request_MethodCode:
    value: HTTPVerbCode_Value
    id: String
    extension: Extension


@dataclass
class Bundle_Entry_Response:
    id: String
    extension: Extension
    modifier_extension: Extension
    status: String
    location: Uri
    etag: String
    last_modified: Instant
    outcome: ContainedResource


@dataclass
class ContainedResource:
    account: Account
    activity_definition: ActivityDefinition
    adverse_event: AdverseEvent
    allergy_intolerance: AllergyIntolerance
    appointment: Appointment
    appointment_response: AppointmentResponse
    audit_event: AuditEvent
    basic: Basic
    binary: Binary
    biologically_derived_product: BiologicallyDerivedProduct
    body_structure: BodyStructure
    bundle: Bundle
    capability_statement: CapabilityStatement
    care_plan: CarePlan
    care_team: CareTeam
    catalog_entry: CatalogEntry
    charge_item: ChargeItem
    charge_item_definition: ChargeItemDefinition
    claim: Claim
    claim_response: ClaimResponse
    clinical_impression: ClinicalImpression
    code_system: CodeSystem
    communication: Communication
    communication_request: CommunicationRequest
    compartment_definition: CompartmentDefinition
    composition: Composition
    concept_map: ConceptMap
    condition: Condition
    consent: Consent
    contract: Contract
    coverage: Coverage
    coverage_eligibility_request: CoverageEligibilityRequest
    coverage_eligibility_response: CoverageEligibilityResponse
    detected_issue: DetectedIssue
    device: Device
    device_definition: DeviceDefinition
    device_metric: DeviceMetric
    device_request: DeviceRequest
    device_use_statement: DeviceUseStatement
    diagnostic_report: DiagnosticReport
    document_manifest: DocumentManifest
    document_reference: DocumentReference
    effect_evidence_synthesis: EffectEvidenceSynthesis
    encounter: Encounter
    endpoint: Endpoint
    enrollment_request: EnrollmentRequest
    enrollment_response: EnrollmentResponse
    episode_of_care: EpisodeOfCare
    event_definition: EventDefinition
    evidence: Evidence
    evidence_variable: EvidenceVariable
    example_scenario: ExampleScenario
    explanation_of_benefit: ExplanationOfBenefit
    family_member_history: FamilyMemberHistory
    flag: Flag
    goal: Goal
    graph_definition: GraphDefinition
    group: Group
    guidance_response: GuidanceResponse
    healthcare_service: HealthcareService
    imaging_study: ImagingStudy
    immunization: Immunization
    immunization_evaluation: ImmunizationEvaluation
    immunization_recommendation: ImmunizationRecommendation
    implementation_guide: ImplementationGuide
    insurance_plan: InsurancePlan
    invoice: Invoice
    library: Library
    linkage: Linkage
    list: List
    location: Location
    measure: Measure
    measure_report: MeasureReport
    media: Media
    medication: Medication
    medication_administration: MedicationAdministration
    medication_dispense: MedicationDispense
    medication_knowledge: MedicationKnowledge
    medication_request: MedicationRequest
    medication_statement: MedicationStatement
    medicinal_product: MedicinalProduct
    medicinal_product_authorization: MedicinalProductAuthorization
    medicinal_product_contraindication: MedicinalProductContraindication
    medicinal_product_indication: MedicinalProductIndication
    medicinal_product_ingredient: MedicinalProductIngredient
    medicinal_product_interaction: MedicinalProductInteraction
    medicinal_product_manufactured: MedicinalProductManufactured
    medicinal_product_packaged: MedicinalProductPackaged
    medicinal_product_pharmaceutical: MedicinalProductPharmaceutical
    medicinal_product_undesirable_effect: MedicinalProductUndesirableEffect
    message_definition: MessageDefinition
    message_header: MessageHeader
    molecular_sequence: MolecularSequence
    naming_system: NamingSystem
    nutrition_order: NutritionOrder
    observation: Observation
    observation_definition: ObservationDefinition
    operation_definition: OperationDefinition
    operation_outcome: OperationOutcome
    organization: Organization
    organization_affiliation: OrganizationAffiliation
    parameters: Parameters
    patient: Patient
    payment_notice: PaymentNotice
    payment_reconciliation: PaymentReconciliation
    person: Person
    plan_definition: PlanDefinition
    practitioner: Practitioner
    practitioner_role: PractitionerRole
    procedure: Procedure
    provenance: Provenance
    questionnaire: Questionnaire
    questionnaire_response: QuestionnaireResponse
    related_person: RelatedPerson
    request_group: RequestGroup
    research_definition: ResearchDefinition
    research_element_definition: ResearchElementDefinition
    research_study: ResearchStudy
    research_subject: ResearchSubject
    risk_assessment: RiskAssessment
    risk_evidence_synthesis: RiskEvidenceSynthesis
    schedule: Schedule
    search_parameter: SearchParameter
    service_request: ServiceRequest
    slot: Slot
    specimen: Specimen
    specimen_definition: SpecimenDefinition
    structure_definition: StructureDefinition
    structure_map: StructureMap
    subscription: Subscription
    substance: Substance
    substance_nucleic_acid: SubstanceNucleicAcid
    substance_polymer: SubstancePolymer
    substance_protein: SubstanceProtein
    substance_reference_information: SubstanceReferenceInformation
    substance_source_material: SubstanceSourceMaterial
    substance_specification: SubstanceSpecification
    supply_delivery: SupplyDelivery
    supply_request: SupplyRequest
    task: Task
    terminology_capabilities: TerminologyCapabilities
    test_report: TestReport
    test_script: TestScript
    value_set: ValueSet
    verification_result: VerificationResult
    vision_prescription: VisionPrescription

