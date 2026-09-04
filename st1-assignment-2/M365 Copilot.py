# No database
# No GUI

# Normal Appointment
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)
    print("Appointment booked successfully!")

# Example bookings
book_appointment("Alice Smith", "Dr John Doe", "2024-07-20 10:00AM")
book_appointment("Bob Johnson", "Dr Jane Roe", "2024-07-20 11:30AM")

# Display all appointments
for appointment in appointments:
    print(
        f"Patient: {appointment['patient']} | "
        f"Practitioner: {appointment['practitioner']} | "
        f"Time: {appointment['time']}"
    )

    # No database
    # No GUI

# Blank Appointment name
    appointments = []


    def book_appointment(patient_name, practitioner_name, appointment_time):
        appointment = {
            "patient": patient_name,
            "practitioner": practitioner_name,
            "time": appointment_time
        }

        appointments.append(appointment)
        print("Appointment booked successfully!")


    # Example bookings
    book_appointment(" ", "Dr John Doe", "2024-07-20 10:00AM")
    book_appointment(" ", "Dr Jane Roe", "2024-07-20 11:30AM")

    # Display all appointments
    for appointment in appointments:
        print(
            f"Patient: {appointment['patient']} | "
            f"Practitioner: {appointment['practitioner']} | "
            f"Time: {appointment['time']}"
        )

# Two Appointments for the same practictioner/time
# No database
# No GUI

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)
    print("Appointment booked successfully!")

# Example bookings
book_appointment("Alice Smith", "Dr John Doe", "2024-07-20 10:00AM")
book_appointment("Bob Johnson", "Dr John Doe", "2024-07-20 10:00AM")

# Display all appointments
for appointment in appointments:
    print(
        f"Patient: {appointment['patient']} | "
        f"Practitioner: {appointment['practitioner']} | "
        f"Time: {appointment['time']}"
    )

# Strange Input
# No database
# No GUI

appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)
    print("Appointment booked successfully!")

# Example bookings
book_appointment("None", "Dr John Doe", "None")
book_appointment("None", "Dr Jane Roe", "None")

# Display all appointments
for appointment in appointments:
    print(
        f"Patient: {appointment['patient']} | "
        f"Practitioner: {appointment['practitioner']} | "
        f"Time: {appointment['time']}"
    )