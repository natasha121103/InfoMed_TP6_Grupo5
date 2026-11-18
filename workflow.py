from patient import create_patient_resource
from appointment import create_appointment_resource
from base import send_resource_to_hapi_fhir, get_resource_from_hapi_fhir, search_patient_by_dni

if __name__ == "__main__":
    # ---------------- Datos del paciente ----------------
    family_name = "Martinez"
    given_name = "María"
    birth_date = "1971-05-25"
    gender = "female"
    phone = "+54 9 11 5678 5678"
    dni = "22123458"

    # 3a) Crear el paciente con DNI como identifier
    print("--- 3a) Creación del paciente ---")
    patient = create_patient_resource(family_name, given_name, birth_date, gender, phone, dni)
    patient_id = send_resource_to_hapi_fhir(patient, 'Patient')
    print(f"ID asignado por el servidor: {patient_id}")

    # 3a) Leer el paciente creado
    if patient_id:
        print("\n--- 3a) Lectura del paciente ---")
        get_resource_from_hapi_fhir(patient_id, 'Patient')

    # 3b) Buscar el paciente por DNI
    print("\n--- 3b) Búsqueda por DNI ---")
    encontrados = search_patient_by_dni(dni)

    # Si el create falló (por ejemplo, paciente duplicado), usamos el encontrado por DNI
    if not patient_id and encontrados:
        patient_id = encontrados[0]["id"]

    # 3c) Crear un turno (Appointment) para el paciente
    if patient_id:
        print("\n--- 3c) Creación del turno (Appointment) ---")
        appointment = create_appointment_resource(
            patient_id=patient_id,
            start="2026-11-25T10:00:00-03:00",
            end="2026-11-25T10:30:00-03:00",
            turno_number="T-2026-000125",
            specialty_code="394802001",
            specialty_name="Medicina general",
            practitioner_name="Dr. Mauro Martinez",   # opcional: borrar esta línea para un turno sin profesional
        )
        appointment_id = send_resource_to_hapi_fhir(appointment, 'Appointment')
        print(f"ID del turno: {appointment_id}")

        # 3c) Leer el turno creado
        if appointment_id:
            print("\n--- 3c) Lectura del turno ---")
            get_resource_from_hapi_fhir(appointment_id, 'Appointment')
    else:
        print("No se pudo obtener un paciente: no se crea el turno.")
