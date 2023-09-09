# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.stu3.proto
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class DataElementAdministrativeStatus:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class DataElementChangeDescription:
    id: String
    value_string: String


@dataclass
class DataElementClassificationOrContext:
    id: String
    value_code: ClassificationOrContextCode


@dataclass
class DataElementContactAddress:
    id: String
    value_address: Address


@dataclass
class DataElementDocumentReference:
    id: String
    value_reference: Reference


@dataclass
class DataElementEffectivePeriod:
    id: String
    value_period: Period


@dataclass
class DataElementIsDataElementConcept:
    id: String
    value_boolean: Boolean


@dataclass
class DataElementRegistryOrg:
    id: String
    value_reference: Reference


@dataclass
class DataElementSubmitterOrg:
    id: String
    value_reference: Reference


@dataclass
class ElementDefinitionObjectClass:
    id: String
    value_coding: Coding


@dataclass
class ElementDefinitionObjectClassProperty:
    id: String
    value_coding: Coding


@dataclass
class PermittedValueConceptmap:
    id: String
    value_reference: Reference


@dataclass
class PermittedValueValueset:
    id: String
    value_reference: Reference


@dataclass
class AllergyIntoleranceCertainty:
    id: String
    value_code: AllergyIntoleranceCertaintyCode


@dataclass
class AllergyIntoleranceDuration:
    id: String
    value_duration: Duration


@dataclass
class AllergyIntoleranceReasonRefuted:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class AllergyIntoleranceResolutionAge:
    id: String
    value_age: Age


@dataclass
class AllergyIntoleranceSubstanceExposureRisk:
    id: String
    extension: Extension
    substance: CodeableConcept
    exposure_risk: CodeableConcept


@dataclass
class AuditEventAccession:
    id: String
    value_identifier: Identifier


@dataclass
class AuditEventAnonymized:
    id: String
    value_boolean: Boolean


@dataclass
class AuditEventEncrypted:
    id: String
    value_boolean: Boolean


@dataclass
class AuditEventInstance:
    id: String
    value_identifier: Identifier


@dataclass
class AuditEventMPPS:
    id: String
    value_identifier: Identifier


@dataclass
class AuditEventNumberOfInstances:
    id: String
    value_integer: Integer


@dataclass
class AuditEventParticipantObjectContainsStudy:
    id: String
    value_identifier: Identifier


@dataclass
class AuditEventSOPClass:
    id: String
    value_reference: Reference


@dataclass
class PatientBirthPlace:
    id: String
    value_address: Address


@dataclass
class BodySiteInstance:
    id: String
    value_reference: Reference


@dataclass
class CapabilityStatementExpectation:
    id: String
    value_code: ConformanceExpectationCode


@dataclass
class CapabilityStatementProhibited:
    id: String
    value_boolean: Boolean


@dataclass
class CapabilityStatementSearchParameterCombination:
    id: String
    extension: Extension
    required: String
    optional: String


@dataclass
class CapabilityStatementSupportedSystem:
    id: String
    value_uri: Uri


@dataclass
class CapabilityStatementWebsocket:
    id: String
    value_uri: Uri


@dataclass
class CarePlanActivityTitle:
    id: String
    value_string: String


@dataclass
class CodeSystemAuthor:
    id: String
    value_string: String


@dataclass
class CodeSystemComment:
    id: String
    extension: Extension
    content: String
    timestamp: Instant


@dataclass
class CodeSystemComments:
    id: String
    value_string: String


@dataclass
class CodeSystemConceptOrder:
    id: String
    value_integer: Integer


@dataclass
class CodeSystemDeprecated:
    id: String
    value_boolean: Boolean


@dataclass
class CodeSystemEffectiveDate:
    id: String
    value_date: Date


@dataclass
class CodeSystemExpirationDate:
    id: String
    value_date: Date


@dataclass
class CodeSystemHistory:
    id: String
    extension: Extension
    name: String
    revision: CodeSystemHistory_Revision


@dataclass
class CodeSystemHistory_Revision:
    id: String
    date: DateTime
    id_slice: String
    author: String
    notes: String


@dataclass
class CodeSystemKeyWord:
    id: String
    value_string: String


@dataclass
class CodeSystemLabel:
    id: String
    value_string: String


@dataclass
class CodeSystemMap:
    id: String
    value_reference: Reference


@dataclass
class CodeSystemOrdinalValue:
    id: String
    value_decimal: Decimal


@dataclass
class CodeSystemOtherName:
    id: String
    extension: Extension
    name: String
    preferred: Boolean


@dataclass
class CodeSystemReference:
    id: String
    value_uri: Uri


@dataclass
class CodeSystemReplacedby:
    id: String
    value_coding: Coding


@dataclass
class CodeSystemSourceReference:
    id: String
    value_uri: Uri


@dataclass
class CodeSystemSubsumes:
    id: String
    value_code: Code


@dataclass
class CodeSystemTrustedExpansion:
    id: String
    value_uri: Uri


@dataclass
class CodeSystemUsage:
    id: String
    extension: Extension
    user: String
    use: String


@dataclass
class CodeSystemWarning:
    id: String
    value_markdown: Markdown


@dataclass
class CodeSystemWorkflowStatus:
    id: String
    value_string: String


@dataclass
class CodingSctdescid:
    id: String
    value_id: Id


@dataclass
class CommunicationMedia:
    id: String
    value_attachment: Attachment


@dataclass
class CommunicationReasonNotPerformed:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class CommunicationRequestDefinition:
    id: String
    value: CommunicationRequestDefinition_Value


@dataclass
class CommunicationRequestDefinition_Value:
    reference: Reference


@dataclass
class CommunicationRequestOrderedBy:
    id: String
    value: CommunicationRequestOrderedBy_Value


@dataclass
class CommunicationRequestOrderedBy_Value:
    reference: Reference


@dataclass
class CommunicationRequestReasonRejected:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class CommunicationRequestRelevantHistory:
    id: String
    value_reference: Reference


@dataclass
class CommunicationRequestSupportingInfo:
    id: String
    value_reference: Reference


@dataclass
class CompositionOtherConfidentiality:
    id: String
    value_coding: Coding


@dataclass
class ConceptMapBidirectional:
    id: String
    value_boolean: Boolean


@dataclass
class ConditionBasedOn:
    id: String
    value: ConditionBasedOn_Value


@dataclass
class ConditionBasedOn_Value:
    reference: Reference


@dataclass
class ConditionCriticality:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ConditionDefinition:
    id: String
    value_reference: Reference


@dataclass
class ConditionDueTo:
    id: String
    value: ConditionDueTo_Value


@dataclass
class ConditionDueTo_Value:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ConditionOccurredFollowing:
    id: String
    value: ConditionOccurredFollowing_Value


@dataclass
class ConditionOccurredFollowing_Value:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ConditionOutcome:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ConditionPartOf:
    id: String
    value: ConditionPartOf_Value


@dataclass
class ConditionPartOf_Value:
    reference: Reference


@dataclass
class ConditionRuledOut:
    id: String
    value_reference: Reference


@dataclass
class ConditionTargetBodySite:
    id: String
    value_reference: Reference


@dataclass
class ConsentLocation:
    id: String
    value_reference: Reference


@dataclass
class ConsentNotificationEndpoint:
    id: String
    value_uri: Uri


@dataclass
class ConsentWitness:
    id: String
    value: ConsentWitness_Value


@dataclass
class ConsentWitness_Value:
    reference: Reference


@dataclass
class CalculatedValue:
    id: String
    value_string: String


@dataclass
class AttachmentCitation:
    id: String
    value_string: String


@dataclass
class CqifCondition:
    id: String
    value_string: String


@dataclass
class CqlExpression:
    id: String
    value_string: String


@dataclass
class FhirPathExpression:
    id: String
    value_string: String


@dataclass
class BasicEncounterClass:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class BasicEncounterType:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class BasicInitiatingOrganization:
    id: String
    value_reference: Reference


@dataclass
class BasicInitiatingPerson:
    id: String
    value: BasicInitiatingPerson_Value


@dataclass
class BasicInitiatingPerson_Value:
    reference: Reference


@dataclass
class BasicReceivingOrganization:
    id: String
    value_reference: Reference


@dataclass
class BasicReceivingPerson:
    id: String
    value: BasicReceivingPerson_Value


@dataclass
class BasicReceivingPerson_Value:
    reference: Reference


@dataclass
class BasicRecipientLanguage:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class BasicRecipientType:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class BasicSystemUserLanguage:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class BasicSystemUserTaskContext:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class BasicSystemUserType:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class InitialValue:
    id: String
    value_string: String


@dataclass
class CqifLibrary:
    id: String
    value_reference: Reference


@dataclass
class MeasureInfo:
    id: String
    extension: Extension
    measure: Reference
    group_identifier: Identifier
    population_identifier: Identifier


@dataclass
class QuestionnaireOptionCode:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class AttachmentQualityOfEvidence:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class CodingSourceValueSet:
    id: String
    value_uri: Uri


@dataclass
class AttachmentStrengthOfRecommendation:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class DataAbsentReason:
    id: String
    value_code: DataAbsentReasonCode


@dataclass
class StructureDefinitionDatadictionary:
    id: String
    value_string: String


@dataclass
class DeviceDin:
    id: String
    value_identifier: Identifier


@dataclass
class DeviceImplantStatus:
    id: String
    value_code: ImplantStatusCode


@dataclass
class DeviceRequestPatientInstruction:
    id: String
    extension: Extension
    lang: LanguageCode
    content: String


@dataclass
class DeviceRequestReasonRejected:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class DiagnosticReportAddendumOf:
    id: String
    value_reference: Reference


@dataclass
class DiagnosticReportExtends:
    id: String
    value_reference: Reference


@dataclass
class DiagnosticReportAnalysis:
    id: String
    extension: Extension
    type: CodeableConcept
    interpretation: CodeableConcept


@dataclass
class DiagnosticReportAssessedCondition:
    id: String
    value_reference: Reference


@dataclass
class DiagnosticReportFamilyMemberHistory:
    id: String
    value_reference: Reference


@dataclass
class DiagnosticReportLocationPerformed:
    id: String
    value_reference: Reference


@dataclass
class DiagnosticReportReplaces:
    id: String
    value_reference: Reference


@dataclass
class DiagnosticReportSummaryOf:
    id: String
    value_reference: Reference


@dataclass
class ElementDefinitionAllowedUnits:
    id: String
    value: ElementDefinitionAllowedUnits_Value


@dataclass
class ElementDefinitionAllowedUnits_Value:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ElementDefinitionBestpractice:
    id: String
    value: ElementDefinitionBestpractice_Value


@dataclass
class ElementDefinitionBestpractice_Value:
    boolean: Boolean
    codeable_concept: CodeableConcept


@dataclass
class ElementDefinitionBindingName:
    id: String
    value_string: String


@dataclass
class ElementDefinitionEquivalence:
    id: String
    value_code: ConceptMapEquivalenceCode


@dataclass
class ElementDefinitionIdentifier:
    id: String
    value_identifier: Identifier


@dataclass
class ElementDefinitionInheritedExtensibleValueSet:
    id: String
    value: ElementDefinitionInheritedExtensibleValueSet_Value


@dataclass
class ElementDefinitionInheritedExtensibleValueSet_Value:
    uri: Uri
    reference: Reference


@dataclass
class ElementDefinitionIsCommonBinding:
    id: String
    value_boolean: Boolean


@dataclass
class ElementDefinitionMaxValueSet:
    id: String
    value: ElementDefinitionMaxValueSet_Value


@dataclass
class ElementDefinitionMaxValueSet_Value:
    uri: Uri
    reference: Reference


@dataclass
class ElementDefinitionMinValueSet:
    id: String
    value: ElementDefinitionMinValueSet_Value


@dataclass
class ElementDefinitionMinValueSet_Value:
    uri: Uri
    reference: Reference


@dataclass
class Namespace:
    id: String
    value_uri: Uri


@dataclass
class ElementDefinitionQuestion:
    id: String
    value_string: String


@dataclass
class ElementDefinitionSelector:
    id: String
    value_string: String


@dataclass
class ElementDefinitionTranslatable:
    id: String
    value_boolean: Boolean


@dataclass
class EncounterAssociatedEncounter:
    id: String
    value_reference: Reference


@dataclass
class EncounterModeOfArrival:
    id: String
    value_coding: Coding


@dataclass
class EncounterPrimaryDiagnosis:
    id: String
    value_positive_int: PositiveInt


@dataclass
class EncounterReasonCancelled:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class EntryFormat:
    id: String
    value_string: String


@dataclass
class Definition:
    id: String
    value: Definition_Value


@dataclass
class Definition_Value:
    reference: Reference


@dataclass
class DiagnosticReportNotDone:
    id: String
    value_boolean: Boolean


@dataclass
class OnBehalfOf:
    id: String
    value_reference: Reference


@dataclass
class PartOf:
    id: String
    value_reference: Reference


@dataclass
class ObservationPerformerRole:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ReasonCode:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ReasonReference:
    id: String
    value: ReasonReference_Value


@dataclass
class ReasonReference_Value:
    reference: Reference


@dataclass
class FamilyMemberHistoryObservation:
    id: String
    value_reference: Reference


@dataclass
class FamilyMemberHistoryParent:
    id: String
    extension: Extension
    type: CodeableConcept
    reference: Reference


@dataclass
class FamilyMemberHistorySibling:
    id: String
    extension: Extension
    type: CodeableConcept
    reference: Reference


@dataclass
class FamilyMemberHistoryAbatement:
    id: String
    value: FamilyMemberHistoryAbatement_Value


@dataclass
class FamilyMemberHistoryAbatement_Value:
    date: Date
    age: Age
    boolean: Boolean


@dataclass
class FamilyMemberHistoryPatientRecord:
    id: String
    value_reference: Reference


@dataclass
class FamilyMemberHistorySeverity:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class FamilyMemberHistoryType:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class FlagDetail:
    id: String
    value_reference: Reference


@dataclass
class FlagPriority:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class AddressGeolocation:
    id: String
    extension: Extension
    latitude: Decimal
    longitude: Decimal


@dataclass
class GoalAcceptance:
    id: String
    extension: Extension
    individual: Reference
    status: GoalAcceptanceStatusCode
    priority: CodeableConcept


@dataclass
class ResourcePertainsToGoal:
    id: String
    value_reference: Reference


@dataclass
class GoalReasonRejected:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class GoalRelationship:
    id: String
    extension: Extension
    type: CodeableConcept
    target: Reference


@dataclass
class DiagnosticReportAlleleDatabase:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class DiagnosticReportGlstring:
    id: String
    extension: Extension
    url: Uri
    text: String


@dataclass
class DiagnosticReportHaploid:
    id: String
    extension: Extension
    locus: CodeableConcept
    type: CodeableConcept
    method: CodeableConcept


@dataclass
class DiagnosticReportMethod:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class BundleHttpResponseHeader:
    id: String
    value_string: String


@dataclass
class HumanNameAssemblyOrder:
    id: String
    value_code: HumanNameAssemblyOrderCode


@dataclass
class HumanNameFathersFamily:
    id: String
    value_string: String


@dataclass
class HumanNameMothersFamily:
    id: String
    value_string: String


@dataclass
class HumanNameOwnName:
    id: String
    value_string: String


@dataclass
class HumanNameOwnPrefix:
    id: String
    value_string: String


@dataclass
class HumanNamePartnerName:
    id: String
    value_string: String


@dataclass
class HumanNamePartnerPrefix:
    id: String
    value_string: String


@dataclass
class IdentifierValidDate:
    id: String
    value_date_time: DateTime


@dataclass
class ImplementationGuidePage:
    id: String
    value_uri: Uri


@dataclass
class AddressADUse:
    id: String
    value_code: PostalAddressUseTypeCode


@dataclass
class AddressADXPAdditionalLocator:
    id: String
    value_string: String


@dataclass
class AddressADXPBuildingNumberSuffix:
    id: String
    value_string: String


@dataclass
class AddressADXPCareOf:
    id: String
    value_string: String


@dataclass
class AddressADXPCensusTract:
    id: String
    value_string: String


@dataclass
class AddressADXPDelimiter:
    id: String
    value_string: String


@dataclass
class AddressADXPDeliveryAddressLine:
    id: String
    value_string: String


@dataclass
class AddressADXPDeliveryInstallationArea:
    id: String
    value_string: String


@dataclass
class AddressADXPDeliveryInstallationQualifier:
    id: String
    value_string: String


@dataclass
class AddressADXPDeliveryInstallationType:
    id: String
    value_string: String


@dataclass
class AddressADXPDeliveryMode:
    id: String
    value_string: String


@dataclass
class AddressADXPDeliveryModeIdentifier:
    id: String
    value_string: String


@dataclass
class AddressADXPDirection:
    id: String
    value_string: String


@dataclass
class AddressADXPHouseNumber:
    id: String
    value_string: String


@dataclass
class AddressADXPHouseNumberNumeric:
    id: String
    value_string: String


@dataclass
class AddressADXPPostBox:
    id: String
    value_string: String


@dataclass
class AddressADXPPrecinct:
    id: String
    value_string: String


@dataclass
class AddressADXPStreetAddressLine:
    id: String
    value_string: String


@dataclass
class AddressADXPStreetName:
    id: String
    value_string: String


@dataclass
class AddressADXPStreetNameBase:
    id: String
    value_string: String


@dataclass
class AddressADXPStreetNameType:
    id: String
    value_string: String


@dataclass
class AddressADXPUnitID:
    id: String
    value_string: String


@dataclass
class AddressADXPUnitType:
    id: String
    value_string: String


@dataclass
class CodingCOValue:
    id: String
    value_decimal: Decimal


@dataclass
class HumanNameENQualifier:
    id: String
    value_code: EntityNamePartQualifierCode


@dataclass
class HumanNameENRepresentation:
    id: String
    value_code: NameRepresentationUseCode


@dataclass
class AnyNullFlavor:
    id: String
    value_code: NullFlavorCode


@dataclass
class AnyPreferred:
    id: String
    value_boolean: Boolean


@dataclass
class StringSCCoding:
    id: String
    value_coding: Coding


@dataclass
class ContactPointTELAddress:
    id: String
    value_uri: Uri


@dataclass
class QuantityUncertainty:
    id: String
    value_decimal: Decimal


@dataclass
class QuantityUncertaintyType:
    id: String
    value_code: ProbabilityDistributionTypeCode


@dataclass
class AnyVerification:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class LocationAlias:
    id: String
    value_string: String


@dataclass
class BundleLocationDistance:
    id: String
    value_distance: Distance


@dataclass
class DataElementMapSourcePublisher:
    id: String
    value_string: String


@dataclass
class BundleMatchGrade:
    id: String
    value_code: MatchGradeCode


@dataclass
class MaxDecimalPlaces:
    id: String
    value_integer: Integer


@dataclass
class MaxSize:
    id: String
    value_decimal: Decimal


@dataclass
class QuestionnaireMaxValue:
    id: String
    value: QuestionnaireMaxValue_Value


@dataclass
class QuestionnaireMaxValue_Value:
    date: Date
    date_time: DateTime
    time: Time
    instant: Instant
    decimal: Decimal
    integer: Integer


@dataclass
class MedicationUsualRoute:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class MedicationDispenseValidityPeriod:
    id: String
    value_period: Period


@dataclass
class MedicationStatementPrescriber:
    id: String
    value_reference: Reference


@dataclass
class MessageHeaderMessageheaderResponseRequest:
    id: String
    value_code: MessageHeaderResponseRequestCode


@dataclass
class MimeType:
    id: String
    value_code: MimeTypeCode


@dataclass
class MinLength:
    id: String
    value_integer: Integer


@dataclass
class QuestionnaireMinValue:
    id: String
    value: QuestionnaireMinValue_Value


@dataclass
class QuestionnaireMinValue_Value:
    date: Date
    date_time: DateTime
    time: Time
    instant: Instant
    decimal: Decimal
    integer: Integer


@dataclass
class ObservationBodyPosition:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationDelta:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationEventTiming:
    id: String
    extension: Extension
    code: CodeableConcept
    offset: Quantity


@dataclass
class ObservationFocalSubject:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationAlleleName:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationAllelicFrequency:
    id: String
    value_decimal: Decimal


@dataclass
class ObservationAllelicState:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationAminoAcidChangeName:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationAminoAcidChangeType:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationCopyNumberEvent:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationDNARegionName:
    id: String
    value_string: String


@dataclass
class ObservationDNASequenceVariantName:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationDNASequenceVariantType:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationDNAVariantId:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationGene:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationGenomicSourceClass:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationInterpretation:
    id: String
    value_reference: Reference


@dataclass
class ObservationPhaseSet:
    id: String
    value_uri: Uri


@dataclass
class ObservationSequence:
    id: String
    value_reference: Reference


@dataclass
class ObservationTimeOffset:
    id: String
    value_integer: Integer


@dataclass
class AllergyIntoleranceAdministration:
    id: String
    value_reference: Reference


@dataclass
class AllergyIntoleranceCareplan:
    id: String
    value_reference: Reference


@dataclass
class AllergyIntoleranceExposureDate:
    id: String
    value_date_time: DateTime


@dataclass
class AllergyIntoleranceExposureDescription:
    id: String
    value_string: String


@dataclass
class AllergyIntoleranceExposureDuration:
    id: String
    value_duration: Duration


@dataclass
class AllergyIntoleranceLocation:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class AllergyIntoleranceManagement:
    id: String
    value_string: String


@dataclass
class AllergyIntoleranceTest:
    id: String
    value: AllergyIntoleranceTest_Value


@dataclass
class AllergyIntoleranceTest_Value:
    reference: Reference


@dataclass
class OperationOutcomeAuthority:
    id: String
    value_uri: Uri


@dataclass
class OperationOutcomeDetectedIssue:
    id: String
    value_reference: Reference


@dataclass
class OperationOutcomeIssueSource:
    id: String
    value_string: String


@dataclass
class OrganizationAlias:
    id: String
    value_string: String


@dataclass
class OrganizationPeriod:
    id: String
    value_period: Period


@dataclass
class OrganizationPreferredContact:
    id: String
    value_boolean: Boolean


@dataclass
class PatientAdoptionInfo:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class PatientBirthTime:
    id: String
    value_date_time: DateTime


@dataclass
class PatientCadavericDonor:
    id: String
    value_boolean: Boolean


@dataclass
class PatientCitizenship:
    id: String
    extension: Extension
    code: CodeableConcept
    period: Period


@dataclass
class PatientClinicalTrial:
    id: String
    extension: Extension
    nct: String
    period: Period
    reason: CodeableConcept


@dataclass
class PatientCongregation:
    id: String
    value_string: String


@dataclass
class PatientDisability:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class PatientImportance:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class PatientInterpreterRequired:
    id: String
    value_boolean: Boolean


@dataclass
class PatientMothersMaidenName:
    id: String
    value_string: String


@dataclass
class PatientNationality:
    id: String
    extension: Extension
    code: CodeableConcept
    period: Period


@dataclass
class PatientReligion:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class DoseType:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class InfuseOver:
    id: String
    value_duration: Duration


@dataclass
class MaxDeliveryRate:
    id: String
    value_ratio: Ratio


@dataclass
class MaxDeliveryVolume:
    id: String
    value_quantity: Quantity


@dataclass
class MinDosePerPeriod:
    id: String
    value_ratio: Ratio


@dataclass
class RateGoal:
    id: String
    value_ratio: Ratio


@dataclass
class RateIncrement:
    id: String
    value_ratio: Ratio


@dataclass
class RateIncrementInterval:
    id: String
    value_duration: Duration


@dataclass
class RefillsRemaining:
    id: String
    value_integer: Integer


@dataclass
class AnimalSpecies:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class PractitionerClassification:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class PractitionerRolePrimaryInd:
    id: String
    value_boolean: Boolean


@dataclass
class ProcedureApproachBodySite:
    id: String
    value_reference: Reference


@dataclass
class ProcedureCausedBy:
    id: String
    value: ProcedureCausedBy_Value


@dataclass
class ProcedureCausedBy_Value:
    reference: Reference


@dataclass
class ProcedureIncisionDateTime:
    id: String
    value_date_time: DateTime


@dataclass
class ProcedureMethod:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ProcedureProgressStatus:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ProcedureSchedule:
    id: String
    value_timing: Timing


@dataclass
class ProcedureTargetBodySite:
    id: String
    value_reference: Reference


@dataclass
class ProcedureRequestApproachBodySite:
    id: String
    value_reference: Reference


@dataclass
class ProcedureRequestAuthorizedBy:
    id: String
    value_reference: Reference


@dataclass
class DiagnosticReportItem:
    id: String
    extension: Extension
    code: CodeableConcept
    genetics_observation: Reference
    specimen: Reference
    status: Code


@dataclass
class ProcedureRequestPrecondition:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ProcedureRequestQuestionnaireRequest:
    id: String
    value_reference: Reference


@dataclass
class ProcedureRequestReasonRefused:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ProcedureRequestReasonRejected:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ProcedureRequestTargetBodySite:
    id: String
    value_reference: Reference


@dataclass
class QuestionnaireAllowedProfile:
    id: String
    value_reference: Reference


@dataclass
class QuestionnaireAllowedResource:
    id: String
    value_code: ResourceTypeCode


@dataclass
class QuestionnaireBaseType:
    id: String
    value_code: DataTypeCode


@dataclass
class QuestionnaireChoiceOrientation:
    id: String
    value_code: ChoiceListOrientationCode


@dataclass
class QuestionnaireDeMap:
    id: String
    value_reference: Reference


@dataclass
class QuestionnaireDisplayCategory:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class QuestionnaireFhirType:
    id: String
    value_string: String


@dataclass
class QuestionnaireHidden:
    id: String
    value_boolean: Boolean


@dataclass
class QuestionnaireItemControl:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class QuestionnaireLookupQuestionnaire:
    id: String
    value_uri: Uri


@dataclass
class QuestionnaireMaxOccurs:
    id: String
    value_integer: Integer


@dataclass
class QuestionnaireMinOccurs:
    id: String
    value_integer: Integer


@dataclass
class QuestionnaireOptionExclusive:
    id: String
    value_boolean: Boolean


@dataclass
class QuestionnaireOptionPrefix:
    id: String
    value_string: String


@dataclass
class QuestionnaireOrdinalValue:
    id: String
    value_decimal: Decimal


@dataclass
class QuestionnaireReferenceFilter:
    id: String
    value_string: String


@dataclass
class QuestionnaireSourceStructureMap:
    id: String
    value_reference: Reference


@dataclass
class QuestionnaireStudyprotocolIdentifier:
    id: String
    value_identifier: Identifier


@dataclass
class QuestionnaireSupportLink:
    id: String
    value_uri: Uri


@dataclass
class QuestionnaireTargetStructureMap:
    id: String
    value_reference: Reference


@dataclass
class QuestionnaireUnit:
    id: String
    value_coding: Coding


@dataclass
class QuestionnaireUsageMode:
    id: String
    value_code: QuestionnaireItemUsageModeCode


@dataclass
class QuestionnaireResponseAuthor:
    id: String
    value: QuestionnaireResponseAuthor_Value


@dataclass
class QuestionnaireResponseAuthor_Value:
    reference: Reference


@dataclass
class QuestionnaireResponseNote:
    id: String
    value_annotation: Annotation


@dataclass
class QuestionnaireResponseReason:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class QuestionnaireResponseReviewer:
    id: String
    value_reference: Reference


@dataclass
class ReferralRequestReasonRefused:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class Regex:
    id: String
    value_string: String


@dataclass
class RenderedValue:
    id: String
    value_string: String


@dataclass
class StringMarkdown:
    id: String
    value_markdown: Markdown


@dataclass
class Style:
    id: String
    value_string: String


@dataclass
class StyleSensitive:
    id: String
    value_boolean: Boolean


@dataclass
class StringXhtml:
    id: String
    value_string: String


@dataclass
class ApprovalDate:
    id: String
    value_date: Date


@dataclass
class EffectivePeriod:
    id: String
    value_period: Period


@dataclass
class LastReviewDate:
    id: String
    value_date: Date


@dataclass
class SpecimenCollectionPriority:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class SpecimenIsDryWeight:
    id: String
    value_boolean: Boolean


@dataclass
class SpecimenProcessingTime:
    id: String
    value: SpecimenProcessingTime_Value


@dataclass
class SpecimenProcessingTime_Value:
    period: Period
    duration: Duration


@dataclass
class SpecimenSequenceNumber:
    id: String
    value_integer: Integer


@dataclass
class SpecimenSpecialHandling:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class StructureDefinitionAncestor:
    id: String
    value_uri: Uri


@dataclass
class StructureDefinitionAnnotation:
    id: String
    value_annotation: Annotation


@dataclass
class BallotStatus:
    id: String
    value_string: String


@dataclass
class StructureDefinitionCategory:
    id: String
    value_string: String


@dataclass
class ElementDefinitionDisplayHint:
    id: String
    value_string: String


@dataclass
class ElementDefinitionExplicitTypeName:
    id: String
    value_string: String


@dataclass
class StructureDefinitionFmmNoWarnings:
    id: String
    value_integer: Integer


@dataclass
class Fmm:
    id: String
    value_integer: Integer


@dataclass
class ElementDefinitionJsonType:
    id: String
    value_string: String


@dataclass
class ElementDefinitionRdfType:
    id: String
    value_string: String


@dataclass
class ElementDefinitionRegex:
    id: String
    value_string: String


@dataclass
class StructureDefinitionSummary:
    id: String
    value_markdown: Markdown


@dataclass
class StructureDefinitionTableName:
    id: String
    value_string: String


@dataclass
class StructureDefinitionTemplateStatus:
    id: String
    value_code: TemplateStatusCodeCode


@dataclass
class Wg:
    id: String
    value_code: HL7WorkgroupCode


@dataclass
class ElementDefinitionXmlType:
    id: String
    value_string: String


@dataclass
class TaskCandidateList:
    id: String
    value: TaskCandidateList_Value


@dataclass
class TaskCandidateList_Value:
    reference: Reference


@dataclass
class TaskReplaces:
    id: String
    value_reference: Reference


@dataclass
class DaysOfCycle:
    id: String
    extension: Extension
    day: Integer


@dataclass
class TimingExact:
    id: String
    value_boolean: Boolean


@dataclass
class Translation:
    id: String
    extension: Extension
    lang: LanguageCode
    content: Translation_Content


@dataclass
class Translation_Content:
    string_value: String
    markdown: Markdown


@dataclass
class UsageContextGroup:
    id: String
    value_string: String


@dataclass
class ValueSetAuthor:
    id: String
    value_string: String


@dataclass
class ValueSetCaseSensitive:
    id: String
    value_boolean: Boolean


@dataclass
class ValueSetComment:
    id: String
    extension: Extension
    content: String
    timestamp: Instant


@dataclass
class ValueSetComments:
    id: String
    value_string: String


@dataclass
class ValueSetConceptOrder:
    id: String
    value_integer: Integer


@dataclass
class ValueSetDefinition:
    id: String
    value_string: String


@dataclass
class ValueSetEffectiveDate:
    id: String
    value_date: Date


@dataclass
class ValueSetExpansionSource:
    id: String
    value_uri: Uri


@dataclass
class ValueSetExpirationDate:
    id: String
    value_date: Date


@dataclass
class ValueSetHistory:
    id: String
    extension: Extension
    name: String
    revision: ValueSetHistory_Revision


@dataclass
class ValueSetHistory_Revision:
    id: String
    date: DateTime
    id_slice: String
    author: String
    notes: String


@dataclass
class ValueSetKeyWord:
    id: String
    value_string: String


@dataclass
class ValueSetLabel:
    id: String
    value_string: String


@dataclass
class ValueSetMap:
    id: String
    value_reference: Reference


@dataclass
class ValueSetOrdinalValue:
    id: String
    value_decimal: Decimal


@dataclass
class ValueSetOtherName:
    id: String
    extension: Extension
    name: String
    preferred: Boolean


@dataclass
class ValueSetReference:
    id: String
    value_uri: Uri


@dataclass
class ValueSetSourceReference:
    id: String
    value_uri: Uri


@dataclass
class ValueSetSystem:
    id: String
    value_reference: Reference


@dataclass
class ValueSetSystemName:
    id: String
    value_string: String


@dataclass
class ValueSetSystemRef:
    id: String
    value_uri: Uri


@dataclass
class ValueSetToocostly:
    id: String
    value_boolean: Boolean


@dataclass
class ValueSetTrustedExpansion:
    id: String
    value_uri: Uri


@dataclass
class ValueSetUnclosed:
    id: String
    value_boolean: Boolean


@dataclass
class ValueSetUsage:
    id: String
    extension: Extension
    user: String
    use: String


@dataclass
class ValueSetWarning:
    id: String
    value_markdown: Markdown


@dataclass
class ValueSetWorkflowStatus:
    id: String
    value_string: String

