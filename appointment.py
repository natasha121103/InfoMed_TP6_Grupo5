from fhir.resources.appointment import Appointment, AppointmentParticipant
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.coding import Coding
from fhir.resources.identifier import Identifier
from fhir.resources.reference import Reference

# Sistema (namespace) de los números de turno de nuestra institución ficticia
TURNO_SYSTEM = "http://hospital-ejemplo.com.ar/fhir/sid/turnos"


# Crear el recurso FHIR Appointment (turno) para un paciente existente
def create_appointment_resource(patient_id, start, end, status="booked",
                                turno_number=None, specialty_code=None, specialty_name=None,
                                practitioner_id=None, practitioner_name=None):

    # participant (1..*): el paciente siempre participa del turno
    participants = [
        AppointmentParticipant(
            actor=Reference(reference=f"Patient/{patient_id}"),
            status="accepted",
        )
    ]

    # Profesional (opcional): se agrega como un segundo participant
    if practitioner_id or practitioner_name:
        practitioner_ref = Reference()
        if practitioner_id:
            # Referencia real a un Practitioner que existe en el servidor
            practitioner_ref.reference = f"Practitioner/{practitioner_id}"
        if practitioner_name:
            # Nombre legible del profesional
            practitioner_ref.display = practitioner_name
        participants.append(
            AppointmentParticipant(actor=practitioner_ref, status="accepted")
        )

    # status (1..1) y participant (1..*) son obligatorios.
    # start y end: en un turno 'booked' tienen que estar los dos.
    appointment = Appointment(
        status=status,
        participant=participants,
        start=start,
        end=end,
    )

    # identifier (0..*): número de turno del sistema de agenda de la institución
    if turno_number:
        identifier = Identifier()
        identifier.use = "official"
        identifier.system = TURNO_SYSTEM
        identifier.value = turno_number
        appointment.identifier = [identifier]

    # specialty (0..*): especialidad requerida, codificada con SNOMED CT
    if specialty_code:
        appointment.specialty = [CodeableConcept(
            coding=[Coding(system="http://snomed.info/sct", code=specialty_code)],
            text=specialty_name,
        )]

    return appointment