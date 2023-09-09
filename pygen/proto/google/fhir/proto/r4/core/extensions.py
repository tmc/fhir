# -*- coding: utf-8 -*-
"""
Python Dataclasses for google.fhir.r4.core
"""
from dataclasses import dataclass
from collections import OrderedDict
from enum import Enum
from typing import Dict



@dataclass
class AddressADUse:
    id: String
    value_code: AddressADUse_ValueCode


@dataclass
class AddressADUse_ValueCode:
    value: PostalAddressUseValueSet_Value
    id: String
    extension: Extension


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
class AddressGeolocation:
    id: String
    extension: Extension
    latitude: Decimal
    longitude: Decimal


@dataclass
class AllergyIntoleranceAdministration:
    id: String
    value_reference: Reference


@dataclass
class AllergyIntoleranceAssertedDate:
    id: String
    value_date_time: DateTime


@dataclass
class AllergyIntoleranceCareplan:
    id: String
    value_reference: Reference


@dataclass
class AllergyIntoleranceCertainty:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class AllergyIntoleranceDuration:
    id: String
    value_duration: Duration


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
class AllergyIntoleranceTest:
    id: String
    value_reference: Reference


@dataclass
class AnimalSpecies:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ApproachBodyStructure:
    id: String
    value_reference: Reference


@dataclass
class ApprovalDate:
    id: String
    value_date: Date


@dataclass
class AttachmentCitation:
    id: String
    value_string: String


@dataclass
class AttachmentQualityOfEvidence:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class AttachmentStrengthOfRecommendation:
    id: String
    value_codeable_concept: CodeableConcept


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
    value_reference: Reference


@dataclass
class BasicReceivingOrganization:
    id: String
    value_reference: Reference


@dataclass
class BasicReceivingPerson:
    id: String
    value_reference: Reference


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
class BodyPosition:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class BodyStructureReference:
    id: String
    value_reference: Reference


@dataclass
class BundleHttpResponseHeader:
    id: String
    value_string: String


@dataclass
class BundleLocationDistance:
    id: String
    value_distance: Distance


@dataclass
class BundleMatchGrade:
    id: String
    value_code: BundleMatchGrade_ValueCode


@dataclass
class BundleMatchGrade_ValueCode:
    value: MatchGradeCode_Value
    id: String
    extension: Extension


@dataclass
class CalculatedValue:
    id: String
    value_string: String


@dataclass
class CanonicalDisplayName:
    id: String
    value_string: String


@dataclass
class CapabilityStatementCapabilities:
    id: String
    value_code: CapabilityStatementCapabilities_ValueCode


@dataclass
class CapabilityStatementCapabilities_ValueCode:
    value: SmartCapabilitiesCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatementExpectation:
    id: String
    value_code: CapabilityStatementExpectation_ValueCode


@dataclass
class CapabilityStatementExpectation_ValueCode:
    value: ConformanceExpectationCode_Value
    id: String
    extension: Extension


@dataclass
class CapabilityStatementOauthUris:
    id: String
    extension: Extension
    authorize: Uri
    token: Uri
    register: Uri
    manage: Uri


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
class CodeSystemAlternate:
    id: String
    extension: Extension
    code: Code
    use: Coding


@dataclass
class CodeSystemAuthor:
    id: String
    value_string: String


@dataclass
class CodeSystemConceptComments:
    id: String
    value_string: String


@dataclass
class CodeSystemConceptOrder:
    id: String
    value_integer: Integer


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
    value_canonical: Canonical


@dataclass
class CodeSystemOtherName:
    id: String
    extension: Extension
    name: String
    preferred: Boolean


@dataclass
class CodeSystemReplacedby:
    id: String
    value_coding: Coding


@dataclass
class CodeSystemSourceReference:
    id: String
    value_uri: Uri


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
class CommunicationRequestInitiatingLocation:
    id: String
    value_reference: Reference


@dataclass
class CompositionOtherConfidentiality:
    id: String
    value_coding: Coding


@dataclass
class CompositionSectionSubject:
    id: String
    value_string: String


@dataclass
class CompositionValidityPeriod:
    id: String
    value_date_time: DateTime


@dataclass
class CompositionVersionNumber:
    id: String
    value_string: String


@dataclass
class ConceptMapBidirectional:
    id: String
    value_boolean: Boolean


@dataclass
class ConditionAssertedDate:
    id: String
    value_date_time: DateTime


@dataclass
class ConditionBasedOn:
    id: String
    value_reference: Reference


@dataclass
class ConditionDueTo:
    id: String
    value: ConditionDueTo_ValueX


@dataclass
class ConditionDueTo_ValueX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ConditionOccurredFollowing:
    id: String
    value: ConditionOccurredFollowing_ValueX


@dataclass
class ConditionOccurredFollowing_ValueX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class ConditionOutcome:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ConditionRelated:
    id: String
    value_reference: Reference


@dataclass
class ConditionRuledOut:
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
class ConsentTranscriber:
    id: String
    value_reference: Reference


@dataclass
class ConsentWitness:
    id: String
    value_reference: Reference


@dataclass
class ContactPointArea:
    id: String
    value_string: String


@dataclass
class ContactPointCountry:
    id: String
    value_string: String


@dataclass
class ContactPointExtension:
    id: String
    value_string: String


@dataclass
class ContactPointLocal:
    id: String
    value_string: String


@dataclass
class ContactPointTELAddress:
    id: String
    value_url: Url


@dataclass
class CqfExpression:
    id: String
    value_expression: Expression


@dataclass
class CqfLibrary:
    id: String
    value_canonical: Canonical


@dataclass
class DataAbsentReason:
    id: String
    value_code: DataAbsentReason_ValueCode


@dataclass
class DataAbsentReason_ValueCode:
    value: DataAbsentReasonCode_Value
    id: String
    extension: Extension


@dataclass
class DateTimezoneOffset:
    id: String
    value_string: String


@dataclass
class DaysOfCycle:
    id: String
    extension: Extension
    day: Integer


@dataclass
class DecimalPrecision:
    id: String
    value_integer: Integer


@dataclass
class DesignNote:
    id: String
    value_markdown: Markdown


@dataclass
class DeviceImplantStatus:
    id: String
    value_code: DeviceImplantStatus_ValueCode


@dataclass
class DeviceImplantStatus_ValueCode:
    value: ImplantStatusCode_Value
    id: String
    extension: Extension


@dataclass
class DeviceRequestPatientInstruction:
    id: String
    extension: Extension
    lang: Code
    content: String


@dataclass
class DiagnosticReportAddendumOf:
    id: String
    value_reference: Reference


@dataclass
class DiagnosticReportAlleleDatabase:
    id: String
    value_codeable_concept: CodeableConcept


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
class DiagnosticReportExtends:
    id: String
    value_reference: Reference


@dataclass
class DiagnosticReportFamilyMemberHistory:
    id: String
    value_reference: Reference


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
class DiagnosticReportItem:
    id: String
    extension: Extension
    code: CodeableConcept
    genetics_observation: Reference
    specimen: Reference
    status: Code


@dataclass
class DiagnosticReportLocationPerformed:
    id: String
    value_reference: Reference


@dataclass
class DiagnosticReportMethod:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class DiagnosticReportReferences:
    id: String
    extension: Extension
    description: String
    reference: Uri
    type: CodeableConcept


@dataclass
class DiagnosticReportReplaces:
    id: String
    value_reference: Reference


@dataclass
class DiagnosticReportSummaryOf:
    id: String
    value_reference: Reference


@dataclass
class DirectedBy:
    id: String
    value: DirectedBy_ValueX


@dataclass
class DirectedBy_ValueX:
    codeable_concept: CodeableConcept
    reference: Reference


@dataclass
class EffectivePeriod:
    id: String
    value_period: Period


@dataclass
class ElementDefinitionAllowedUnits:
    id: String
    value: ElementDefinitionAllowedUnits_ValueX


@dataclass
class ElementDefinitionAllowedUnits_ValueX:
    codeable_concept: CodeableConcept
    canonical: Canonical


@dataclass
class ElementDefinitionBestpractice:
    id: String
    value: ElementDefinitionBestpractice_ValueX


@dataclass
class ElementDefinitionBestpractice_ValueX:
    boolean: Boolean
    codeable_concept: CodeableConcept


@dataclass
class ElementDefinitionBestpracticeExplanation:
    id: String
    value_markdown: Markdown


@dataclass
class ElementDefinitionBindingName:
    id: String
    value_string: String


@dataclass
class ElementDefinitionDisplayHint:
    id: String
    value_string: String


@dataclass
class ElementDefinitionEquivalence:
    id: String
    value_code: ElementDefinitionEquivalence_ValueCode


@dataclass
class ElementDefinitionEquivalence_ValueCode:
    value: ConceptMapEquivalenceCode_Value
    id: String
    extension: Extension


@dataclass
class ElementDefinitionExplicitTypeName:
    id: String
    value_string: String


@dataclass
class ElementDefinitionFhirType:
    id: String
    value_url: Url


@dataclass
class ElementDefinitionHierarchy:
    id: String
    value_boolean: Boolean


@dataclass
class ElementDefinitionIdentifier:
    id: String
    value_identifier: Identifier


@dataclass
class ElementDefinitionInheritedExtensibleValueSet:
    id: String
    value: ElementDefinitionInheritedExtensibleValueSet_ValueX


@dataclass
class ElementDefinitionInheritedExtensibleValueSet_ValueX:
    uri: Uri
    canonical: Canonical


@dataclass
class ElementDefinitionIsCommonBinding:
    id: String
    value_boolean: Boolean


@dataclass
class ElementDefinitionMaxValueSet:
    id: String
    value: ElementDefinitionMaxValueSet_ValueX


@dataclass
class ElementDefinitionMaxValueSet_ValueX:
    uri: Uri
    canonical: Canonical


@dataclass
class ElementDefinitionMinValueSet:
    id: String
    value: ElementDefinitionMinValueSet_ValueX


@dataclass
class ElementDefinitionMinValueSet_ValueX:
    uri: Uri
    canonical: Canonical


@dataclass
class ElementDefinitionObjectClass:
    id: String
    value_coding: Coding


@dataclass
class ElementDefinitionObjectClassProperty:
    id: String
    value_coding: Coding


@dataclass
class ElementDefinitionProfileElement:
    id: String
    value_string: String


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
class EncounterReasonCancelled:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class EntryFormat:
    id: String
    value_string: String


@dataclass
class EpisodeOfCareExtension:
    id: String
    value_reference: Reference


@dataclass
class EventHistory:
    id: String
    value_reference: Reference


@dataclass
class FamilyMemberHistoryAbatement:
    id: String
    value: FamilyMemberHistoryAbatement_ValueX


@dataclass
class FamilyMemberHistoryAbatement_ValueX:
    date: Date
    age: Age
    boolean: Boolean


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
class FamilyMemberHistoryPatientRecord:
    id: String
    value_reference: Reference


@dataclass
class FamilyMemberHistorySeverity:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class FamilyMemberHistorySibling:
    id: String
    extension: Extension
    type: CodeableConcept
    reference: Reference


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
class Fmm:
    id: String
    value_integer: Integer


@dataclass
class GoalAcceptance:
    id: String
    extension: Extension
    individual: Reference
    status: GoalAcceptance_StatusCode
    priority: CodeableConcept


@dataclass
class GoalAcceptance_StatusCode:
    value: GoalAcceptanceStatusCode_Value
    id: String
    extension: Extension


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
class HumanLanguage:
    id: String
    value_code: Code


@dataclass
class HumanNameAssemblyOrder:
    id: String
    value_code: HumanNameAssemblyOrder_ValueCode


@dataclass
class HumanNameAssemblyOrder_ValueCode:
    value: HumanNameAssemblyOrderValueSet_Value
    id: String
    extension: Extension


@dataclass
class HumanNameENQualifier:
    id: String
    value_code: HumanNameENQualifier_ValueCode


@dataclass
class HumanNameENQualifier_ValueCode:
    value: EntityNamePartQualifierValueSet_Value
    id: String
    extension: Extension


@dataclass
class HumanNameENRepresentation:
    id: String
    value_code: HumanNameENRepresentation_ValueCode


@dataclass
class HumanNameENRepresentation_ValueCode:
    value: NameRepresentationUseValueSet_Value
    id: String
    extension: Extension


@dataclass
class HumanNameENUse:
    id: String
    value_code: HumanNameENUse_ValueCode


@dataclass
class HumanNameENUse_ValueCode:
    value: V3EntityNameUseR2Code_Value
    id: String
    extension: Extension


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
class InitialValue:
    id: String
    value_string: String


@dataclass
class InstantiatesCanonical:
    id: String
    value_canonical: Canonical


@dataclass
class InstantiatesUri:
    id: String
    value_uri: Uri


@dataclass
class LastReviewDate:
    id: String
    value_date: Date


@dataclass
class ListChangeBase:
    id: String
    value_reference: Reference


@dataclass
class LocationBoundaryGeojson:
    id: String
    value_attachment: Attachment


@dataclass
class LocationExtension:
    id: String
    value_reference: Reference


@dataclass
class MaxDecimalPlaces:
    id: String
    value_integer: Integer


@dataclass
class MaxSize:
    id: String
    value_decimal: Decimal


@dataclass
class MeasureInfo:
    id: String
    extension: Extension
    measure: Canonical
    group_id: String
    population_id: String


@dataclass
class MessageHeaderMessageheaderResponseRequest:
    id: String
    value_code: MessageHeaderMessageheaderResponseRequest_ValueCode


@dataclass
class MessageHeaderMessageheaderResponseRequest_ValueCode:
    value: MessageheaderResponseRequestCode_Value
    id: String
    extension: Extension


@dataclass
class MimeType:
    id: String
    value_code: MimeType_ValueCode


@dataclass
class MimeType_ValueCode:
    id: String
    extension: Extension
    value: str


@dataclass
class MinLength:
    id: String
    value_integer: Integer


@dataclass
class Namespace:
    id: String
    value_uri: Uri


@dataclass
class NarrativeLink:
    id: String
    value_url: Url


@dataclass
class NullFlavor:
    id: String
    value_code: NullFlavor_ValueCode


@dataclass
class NullFlavor_ValueCode:
    value: V3NullFlavorCode_Value
    id: String
    extension: Extension


@dataclass
class NutritionOrderAdaptiveFeedingDevice:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class NutritionOrderDoNotPerform:
    id: String
    value_boolean: Boolean


@dataclass
class NutritionOrderInsurance:
    id: String
    value_reference: Reference


@dataclass
class NutritionOrderReplaces:
    id: String
    value_reference: Reference


@dataclass
class ObservationAllele:
    id: String
    extension: Extension
    name: CodeableConcept
    state: CodeableConcept
    frequency: Decimal


@dataclass
class ObservationAminoAcidChange:
    id: String
    extension: Extension
    name: CodeableConcept
    type: CodeableConcept


@dataclass
class ObservationAncestry:
    id: String
    extension: Extension
    name: CodeableConcept
    percentage: Decimal
    source: CodeableConcept


@dataclass
class ObservationCopyNumberEvent:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationDNARegionName:
    id: String
    value_string: String


@dataclass
class ObservationDelta:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationDeviceCode:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationFocusCode:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationGatewayDevice:
    id: String
    value_reference: Reference


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
    extension: Extension
    id_slice: Uri
    molecular_sequence: Reference


@dataclass
class ObservationPrecondition:
    id: String
    value_reference: Reference


@dataclass
class ObservationReagent:
    id: String
    value_reference: Reference


@dataclass
class ObservationReplaces:
    id: String
    value_reference: Reference


@dataclass
class ObservationSecondaryFinding:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationSequelTo:
    id: String
    value_reference: Reference


@dataclass
class ObservationSpecimenCode:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ObservationTimeOffset:
    id: String
    value_integer: Integer


@dataclass
class ObservationVariant:
    id: String
    extension: Extension
    name: CodeableConcept
    id_slice: CodeableConcept
    type: CodeableConcept


@dataclass
class OperationDefinitionAllowedType:
    id: String
    value_uri: Uri


@dataclass
class OperationDefinitionProfile:
    id: String
    value_uri: Uri


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
class OrdinalValue:
    id: String
    value_decimal: Decimal


@dataclass
class OrganizationAffiliationPrimaryInd:
    id: String
    value_boolean: Boolean


@dataclass
class OrganizationPeriod:
    id: String
    value_period: Period


@dataclass
class OrganizationPreferredContact:
    id: String
    value_boolean: Boolean


@dataclass
class OriginalText:
    id: String
    value_string: String


@dataclass
class ParametersFullUrl:
    id: String
    value_uri: Uri


@dataclass
class PartOf:
    id: String
    value_reference: Reference


@dataclass
class PatientAdoptionInfo:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class PatientAnimal:
    id: String
    extension: Extension
    species: CodeableConcept
    breed: CodeableConcept
    gender_status: CodeableConcept


@dataclass
class PatientBirthPlace:
    id: String
    value_address: Address


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
class PatientCongregation:
    id: String
    value_string: String


@dataclass
class PatientDisability:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class PatientGenderIdentity:
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
class PatientPreferenceType:
    id: String
    value_coding: Coding


@dataclass
class PatientProficiency:
    id: String
    extension: Extension
    level: Coding
    type: Coding


@dataclass
class PatientRelatedPerson:
    id: String
    value_reference: Reference


@dataclass
class PatientReligion:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class PerformerFunction:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class PermittedValueConceptmap:
    id: String
    value_canonical: Canonical


@dataclass
class PermittedValueValueset:
    id: String
    value_canonical: Canonical


@dataclass
class PlanDefinitionCdsHooksEndpoint:
    id: String
    value_uri: Uri


@dataclass
class PractitionerRolePrimaryInd:
    id: String
    value_boolean: Boolean


@dataclass
class Preferred:
    id: String
    value_boolean: Boolean


@dataclass
class ProcedureCausedBy:
    id: String
    value_reference: Reference


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
class QuantityPQTranslation:
    id: String
    value_quantity: Quantity


@dataclass
class QuantityUncertainty:
    id: String
    value_decimal: Decimal


@dataclass
class QuantityUncertaintyType:
    id: String
    value_code: QuantityUncertaintyType_ValueCode


@dataclass
class QuantityUncertaintyType_ValueCode:
    value: ProbabilityDistributionTypeValueSet_Value
    id: String
    extension: Extension


@dataclass
class QuestionnaireBaseType:
    id: String
    value_code: QuestionnaireBaseType_ValueCode


@dataclass
class QuestionnaireBaseType_ValueCode:
    value: DataTypeCode_Value
    id: String
    extension: Extension


@dataclass
class QuestionnaireChoiceOrientation:
    id: String
    value_code: QuestionnaireChoiceOrientation_ValueCode


@dataclass
class QuestionnaireChoiceOrientation_ValueCode:
    value: ChoiceListOrientationCode_Value
    id: String
    extension: Extension


@dataclass
class QuestionnaireConstraint:
    id: String
    extension: Extension
    key: Id
    requirements: String
    severity: QuestionnaireConstraint_SeverityCode
    expression: String
    human: String
    location: String


@dataclass
class QuestionnaireConstraint_SeverityCode:
    value: ConstraintSeverityCode_Value
    id: String
    extension: Extension


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
class QuestionnaireMaxOccurs:
    id: String
    value_integer: Integer


@dataclass
class QuestionnaireMaxValue:
    id: String
    value: QuestionnaireMaxValue_ValueX


@dataclass
class QuestionnaireMaxValue_ValueX:
    date: Date
    date_time: DateTime
    time: Time
    instant: Instant
    decimal: Decimal
    integer: Integer


@dataclass
class QuestionnaireMinOccurs:
    id: String
    value_integer: Integer


@dataclass
class QuestionnaireMinValue:
    id: String
    value: QuestionnaireMinValue_ValueX


@dataclass
class QuestionnaireMinValue_ValueX:
    date: Date
    date_time: DateTime
    time: Time
    decimal: Decimal
    integer: Integer


@dataclass
class QuestionnaireOptionExclusive:
    id: String
    value_boolean: Boolean


@dataclass
class QuestionnaireOptionPrefix:
    id: String
    value_string: String


@dataclass
class QuestionnaireReferenceFilter:
    id: String
    value_string: String


@dataclass
class QuestionnaireReferenceProfile:
    id: String
    value_canonical: Canonical


@dataclass
class QuestionnaireReferenceResource:
    id: String
    value_code: QuestionnaireReferenceResource_ValueCode


@dataclass
class QuestionnaireReferenceResource_ValueCode:
    value: ResourceTypeCode_Value
    id: String
    extension: Extension


@dataclass
class QuestionnaireResponseAuthor:
    id: String
    value_reference: Reference


@dataclass
class QuestionnaireResponseCompletionMode:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class QuestionnaireResponseReason:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class QuestionnaireResponseReviewer:
    id: String
    value_reference: Reference


@dataclass
class QuestionnaireResponseSignature:
    id: String
    value_signature: Signature


@dataclass
class QuestionnaireSignatureRequired:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class QuestionnaireSliderStepValue:
    id: String
    value_integer: Integer


@dataclass
class QuestionnaireSupportLink:
    id: String
    value_uri: Uri


@dataclass
class QuestionnaireUnit:
    id: String
    value_coding: Coding


@dataclass
class QuestionnaireUnitOption:
    id: String
    value_coding: Coding


@dataclass
class QuestionnaireUnitValueSet:
    id: String
    value_canonical: Canonical


@dataclass
class QuestionnaireUsageMode:
    id: String
    value_code: QuestionnaireUsageMode_ValueCode


@dataclass
class QuestionnaireUsageMode_ValueCode:
    value: QuestionnaireItemUsageModeCode_Value
    id: String
    extension: Extension


@dataclass
class QuestionnaireVariable:
    id: String
    value_expression: Expression


@dataclass
class ReasonCode:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ReasonReference:
    id: String
    value_reference: Reference


@dataclass
class Regex:
    id: String
    value_string: String


@dataclass
class RelatedArtifactExtension:
    id: String
    value_related_artifact: RelatedArtifact


@dataclass
class RelativeDateCriteria:
    id: String
    extension: Extension
    event: RelativeDateCriteria_EventX
    relationship: RelativeDateCriteria_RelationshipCode
    offset: Duration


@dataclass
class RelativeDateCriteria_EventX:
    reference: Reference
    codeable_concept: CodeableConcept


@dataclass
class RelativeDateCriteria_RelationshipCode:
    value: ActionRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class RelativeDateTime:
    id: String
    extension: Extension
    target: Reference
    target_path: String
    relationship: RelativeDateTime_RelationshipCode
    offset: RelativeDateTime_OffsetX


@dataclass
class RelativeDateTime_RelationshipCode:
    value: ActionRelationshipTypeCode_Value
    id: String
    extension: Extension


@dataclass
class RelativeDateTime_OffsetX:
    duration: Duration
    range: Range


@dataclass
class RelevantHistory:
    id: String
    value_reference: Reference


@dataclass
class RenderedValue:
    id: String
    value_string: String


@dataclass
class Replaces:
    id: String
    value_canonical: Canonical


@dataclass
class ResearchStudyExtension:
    id: String
    value_reference: Reference


@dataclass
class ResourcePertainsToGoal:
    id: String
    value_reference: Reference


@dataclass
class Risk:
    id: String
    value_reference: Reference


@dataclass
class ServiceRequestPerformerOrder:
    id: String
    value_integer: Integer


@dataclass
class ServiceRequestPrecondition:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class ServiceRequestQuestionnaireRequest:
    id: String
    value_reference: Reference


@dataclass
class SpecialStatus:
    id: String
    value_string: String


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
    value: SpecimenProcessingTime_ValueX


@dataclass
class SpecimenProcessingTime_ValueX:
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
class StandardsStatus:
    id: String
    value_code: StandardsStatus_ValueCode


@dataclass
class StandardsStatus_ValueCode:
    value: StandardsStatusCode_Value
    id: String
    extension: Extension


@dataclass
class StatusReason:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class StatusReasonExtension:
    id: String
    value_codeable_concept: CodeableConcept


@dataclass
class StringMarkdown:
    id: String
    value_markdown: Markdown


@dataclass
class StringSCCoding:
    id: String
    value_coding: Coding


@dataclass
class StringXhtml:
    id: String
    value_string: String


@dataclass
class StructureDefinitionAncestor:
    id: String
    value_uri: Uri


@dataclass
class StructureDefinitionApplicableVersion:
    id: String
    value_code: StructureDefinitionApplicableVersion_ValueCode


@dataclass
class StructureDefinitionApplicableVersion_ValueCode:
    value: FHIRVersionCode_Value
    id: String
    extension: Extension


@dataclass
class StructureDefinitionCategory:
    id: String
    value_string: String


@dataclass
class StructureDefinitionCodegenSuper:
    id: String
    value_string: String


@dataclass
class StructureDefinitionDependencies:
    id: String
    value_canonical: Canonical


@dataclass
class StructureDefinitionFmmNoWarnings:
    id: String
    value_integer: Integer


@dataclass
class StructureDefinitionNormativeVersion:
    id: String
    value_code: StructureDefinitionNormativeVersion_ValueCode


@dataclass
class StructureDefinitionNormativeVersion_ValueCode:
    value: FHIRVersionCode_Value
    id: String
    extension: Extension


@dataclass
class StructureDefinitionSecurityCategory:
    id: String
    value_code: StructureDefinitionSecurityCategory_ValueCode


@dataclass
class StructureDefinitionSecurityCategory_ValueCode:
    value: ResourceSecurityCategoryCode_Value
    id: String
    extension: Extension


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
    value_code: StructureDefinitionTemplateStatus_ValueCode


@dataclass
class StructureDefinitionTemplateStatus_ValueCode:
    value: TemplateStatusCodeValueSet_Value
    id: String
    extension: Extension


@dataclass
class StructureDefinitionXmlNoOrder:
    id: String
    value_boolean: Boolean


@dataclass
class Style:
    id: String
    value_string: String


@dataclass
class StyleSensitive:
    id: String
    value_boolean: Boolean


@dataclass
class SupportingInfo:
    id: String
    value_reference: Reference


@dataclass
class TargetBodyStructure:
    id: String
    value_reference: Reference


@dataclass
class TaskCandidateList:
    id: String
    value_reference: Reference


@dataclass
class TaskReplaces:
    id: String
    value_reference: Reference


@dataclass
class TimezoneCode:
    id: String
    value_code: TimezoneCode_ValueCode


@dataclass
class TimezoneCode_ValueCode:
    id: String
    extension: Extension
    value: str


@dataclass
class TimingDayOfMonth:
    id: String
    value_positive_int: PositiveInt


@dataclass
class TimingExact:
    id: String
    value_boolean: Boolean


@dataclass
class Translation:
    id: String
    extension: Extension
    lang: Code
    content: Translation_ContentX


@dataclass
class Translation_ContentX:
    string_value: String
    markdown: Markdown


@dataclass
class UsageContextGroup:
    id: String
    value_string: String


@dataclass
class ValueSetActivityStatusDate:
    id: String
    value_date: Date


@dataclass
class ValueSetAuthor:
    id: String
    value_contact_detail: ContactDetail


@dataclass
class ValueSetAuthoritativeSource:
    id: String
    value_uri: Uri


@dataclass
class ValueSetCaseSensitive:
    id: String
    value_boolean: Boolean


@dataclass
class ValueSetConceptComments:
    id: String
    value_string: String


@dataclass
class ValueSetConceptDefinition:
    id: String
    value_string: String


@dataclass
class ValueSetConceptOrder:
    id: String
    value_integer: Integer


@dataclass
class ValueSetDeprecated:
    id: String
    value_boolean: Boolean


@dataclass
class ValueSetEffectiveDate:
    id: String
    value_date_time: DateTime


@dataclass
class ValueSetExpandGroup:
    id: String
    extension: Extension
    code: Code
    display: String
    member: Code


@dataclass
class ValueSetExpandRules:
    id: String
    value_code: ValueSetExpandRules_ValueCode


@dataclass
class ValueSetExpandRules_ValueCode:
    value: ExpansionProcessingRuleCode_Value
    id: String
    extension: Extension


@dataclass
class ValueSetExpansionSource:
    id: String
    value_uri: Uri


@dataclass
class ValueSetExpirationDate:
    id: String
    value_date: Date


@dataclass
class ValueSetExpression:
    id: String
    value_expression: Expression


@dataclass
class ValueSetExtensible:
    id: String
    value_boolean: Boolean


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
    value_canonical: Canonical


@dataclass
class ValueSetOtherName:
    id: String
    extension: Extension
    name: String
    preferred: Boolean


@dataclass
class ValueSetParameterSource:
    id: String
    value_code: ValueSetParameterSource_ValueCode


@dataclass
class ValueSetParameterSource_ValueCode:
    value: ExpansionParameterSourceCode_Value
    id: String
    extension: Extension


@dataclass
class ValueSetReference:
    id: String
    value_uri: Uri


@dataclass
class ValueSetRulesText:
    id: String
    value_markdown: Markdown


@dataclass
class ValueSetSourceReference:
    id: String
    value_uri: Uri


@dataclass
class ValueSetSteward:
    id: String
    value_contact_detail: ContactDetail


@dataclass
class ValueSetSupplement:
    id: String
    value_canonical: Canonical


@dataclass
class ValueSetSystem:
    id: String
    value_canonical: Canonical


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


@dataclass
class Wg:
    id: String
    value_code: Wg_ValueCode


@dataclass
class Wg_ValueCode:
    value: HL7WorkgroupCode_Value
    id: String
    extension: Extension

