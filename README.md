# TP6 – Interoperabilidad | Grupo 5

**Informática Médica (16.22) – Bioingeniería, ITBA**  
**Estándar:** HL7 FHIR R4  
**Recurso asignado:** Appointment

## Descripción

Este repositorio contiene la resolución en Python de la **Actividad 3 del TP6 de Interoperabilidad**. Partimos del repositorio `FHIR-basics` proporcionado por la cátedra y lo extendimos para crear pacientes identificados mediante DNI, buscarlos por documento y registrar un turno médico asociado a un paciente existente. Para almacenar y recuperar los recursos utilizamos la API REST del servidor público de prueba **HAPI FHIR R4**.

## Actividades implementadas

**3.a – Creación y lectura de Patient**

Modificamos la creación del recurso `Patient` para incorporar el DNI argentino como `identifier`. Utilizamos el código HL7 `NI`, el sistema de identificación de RENAPER y su denominación como entidad emisora. El paciente se envía al servidor mediante POST y posteriormente se recupera por su identificador lógico (`id`).

**3.b – Búsqueda de pacientes por DNI**

Implementamos una función que permite buscar pacientes mediante el parámetro FHIR `identifier`, utilizando una solicitud GET. El servidor devuelve un recurso `Bundle`, del que se extraen los pacientes encontrados.

**3.c – Creación y lectura de Appointment**

Implementamos el recurso `Appointment`, para representar un turno médico. El turno incluye su estado (`booked`), fecha y horario, referencia al paciente, número de turno y especialidad codificada con **SNOMED CT**. También permite incorporar un profesional de forma opcional.

## Estructura del proyecto

| Archivo | Función |
|---|---|
| `patient.py` | Construcción del recurso Patient, incluyendo el DNI. |
| `base.py` | Creación, lectura y búsqueda de recursos mediante la API de HAPI FHIR. |
| `appointment.py` | Construcción del recurso Appointment. |
| `workflow.py` | Ejecución de las actividades 3.a, 3.b y 3.c. |

## Funcionamiento

El programa intenta crear un paciente, lo lee y lo busca por DNI. Si el servidor rechaza la creación por duplicado, puede recuperar el paciente existente mediante la búsqueda. Luego utiliza su identificador para crear un recurso `Appointment`, estableciendo una referencia al paciente. Finalmente, lee el turno creado para comprobar los datos almacenados.

Todas las operaciones se realizan sobre el servidor público de prueba:

https://hapi.fhir.org/baseR4

**Nota:** se utilizan datos ficticios. Los recursos almacenados y los identificadores asignados pueden variar entre ejecuciones.

## Referencias

- [Repositorio base](https://github.com/euberrino/FHIR-basics)
- [HL7 FHIR R4 – Patient](https://hl7.org/fhir/R4/patient.html)
- [HL7 FHIR R4 – Appointment](https://hl7.org/fhir/R4/appointment.html)
