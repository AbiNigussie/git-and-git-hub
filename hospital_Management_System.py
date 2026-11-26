
import json
import os
from datetime import datetime

# ==========================================
#       HOSPITAL MANAGEMENT SYSTEM
# ==========================================

PATIENT_FILE = "patients.json"
DOCTOR_FILE = "doctors.json"
APPOINTMENT_FILE = "appointments.json"


# ==========================================
#           FILE HANDLING
# ==========================================

def load_data(filename):
    """Load records from a JSON file."""
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print(f"Warning: Could not read {filename}.")
        return []


def save_data(filename, data):
    """Save records permanently to a JSON file."""
    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError:
        print("Error: Unable to save data.")
        return False


# ==========================================
#           INPUT VALIDATION
# ==========================================

def get_integer(message):
    while True:
        try:
            number = int(input(message))
            if number > 0:
                return number
            print("Enter a positive number.")
        except ValueError:
            print("Invalid input! Enter a number.")


def get_text(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This field cannot be empty.")


# ==========================================
#           PATIENT MANAGEMENT
# ==========================================

def register_patient():
    patients = load_data(PATIENT_FILE)

    patient_id = get_integer("Enter Patient ID: ")

    if any(p["id"] == patient_id for p in patients):
        print("Patient ID already exists!")
        return

    name = get_text("Enter Patient Name: ")
    age = get_integer("Enter Patient Age: ")
    gender = get_text("Enter Gender: ")
    phone = get_text("Enter Phone Number: ")
    address = get_text("Enter Address: ")
    disease = get_text("Enter Medical Condition: ")

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "address": address,
        "disease": disease,
        "registration_date": datetime.now().strftime("%Y-%m-%d")
    }

    patients.append(patient)

    if save_data(PATIENT_FILE, patients):
        print("\nPatient registered successfully!")


def view_patients():
    patients = load_data(PATIENT_FILE)

    if not patients:
        print("\nNo patient records found.")
        return

    print("\n========== PATIENT RECORDS ==========")

    for patient in patients:
        print("-" * 40)
        print(f"Patient ID : {patient['id']}")
        print(f"Name       : {patient['name']}")
        print(f"Age        : {patient['age']}")
        print(f"Gender     : {patient['gender']}")
        print(f"Phone      : {patient['phone']}")
        print(f"Address    : {patient['address']}")
        print(f"Condition  : {patient['disease']}")
        print(f"Registered : {patient['registration_date']}")


def search_patient():
    patients = load_data(PATIENT_FILE)

    patient_id = get_integer("Enter Patient ID to search: ")

    for patient in patients:
        if patient["id"] == patient_id:
            print("\nPatient Found!")
            print(json.dumps(patient, indent=4))
            return

    print("Patient not found!")


def update_patient():
    patients = load_data(PATIENT_FILE)

    patient_id = get_integer("Enter Patient ID to update: ")

    for patient in patients:
        if patient["id"] == patient_id:
            print("\nLeave a field blank to keep its current value.")

            name = input("New Name: ").strip()
            age = input("New Age: ").strip()
            phone = input("New Phone: ").strip()
            address = input("New Address: ").strip()
            disease = input("New Medical Condition: ").strip()

            if name:
                patient["name"] = name

            if age:
                try:
                    new_age = int(age)
                    if new_age <= 0:
                        print("Invalid age. Keeping old age.")
                    else:
                        patient["age"] = new_age
                except ValueError:
                    print("Invalid age. Keeping old age.")

            if phone:
                patient["phone"] = phone

            if address:
                patient["address"] = address

            if disease:
                patient["disease"] = disease

            if save_data(PATIENT_FILE, patients):
                print("Patient information updated!")
            return

    print("Patient not found!")


def delete_patient():
    patients = load_data(PATIENT_FILE)

    patient_id = get_integer("Enter Patient ID to delete: ")

    for patient in patients:
        if patient["id"] == patient_id:
            confirm = input(
                "Are you sure you want to delete? (yes/no): "
            ).lower()

            if confirm == "yes":
                patients.remove(patient)
                if save_data(PATIENT_FILE, patients):
                    print("Patient deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print("Patient not found!")


# ==========================================
#           DOCTOR MANAGEMENT
# ==========================================

def add_doctor():
    doctors = load_data(DOCTOR_FILE)

    doctor_id = get_integer("Enter Doctor ID: ")

    if any(d["id"] == doctor_id for d in doctors):
        print("Doctor ID already exists!")
        return

    name = get_text("Enter Doctor Name: ")
    specialization = get_text("Enter Specialization: ")
    phone = get_text("Enter Phone Number: ")

    doctor = {
        "id": doctor_id,
        "name": name,
        "specialization": specialization,
        "phone": phone
    }

    doctors.append(doctor)

    if save_data(DOCTOR_FILE, doctors):
        print("Doctor added successfully!")


def view_doctors():
    doctors = load_data(DOCTOR_FILE)

    if not doctors:
        print("No doctors registered.")
        return

    print("\n========== DOCTOR LIST ==========")

    for doctor in doctors:
        print("-" * 35)
        print(f"Doctor ID       : {doctor['id']}")
        print(f"Name            : {doctor['name']}")
        print(f"Specialization  : {doctor['specialization']}")
        print(f"Phone           : {doctor['phone']}")


# ==========================================
#        APPOINTMENT MANAGEMENT
# ==========================================

def book_appointment():
    appointments = load_data(APPOINTMENT_FILE)
    patients = load_data(PATIENT_FILE)
    doctors = load_data(DOCTOR_FILE)

    if not patients:
        print("Register a patient first.")
        return

    if not doctors:
        print("Add a doctor first.")
        return

    appointment_id = get_integer("Enter Appointment ID: ")

    if any(a["id"] == appointment_id for a in appointments):
        print("Appointment ID already exists!")
        return

    patient_id = get_integer("Enter Patient ID: ")
    doctor_id = get_integer("Enter Doctor ID: ")

    patient = next(
        (p for p in patients if p["id"] == patient_id), None
    )
    doctor = next(
        (d for d in doctors if d["id"] == doctor_id), None
    )

    if not patient:
        print("Patient not found!")
        return

    if not doctor:
        print("Doctor not found!")
        return

    date = get_text("Enter Appointment Date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format!")
        return

    appointment = {
        "id": appointment_id,
        "patient_id": patient_id,
        "patient_name": patient["name"],
        "doctor_id": doctor_id,
        "doctor_name": doctor["name"],
        "date": date,
        "status": "Scheduled"
    }

    appointments.append(appointment)

    if save_data(APPOINTMENT_FILE, appointments):
        print("Appointment booked successfully!")


def view_appointments():
    appointments = load_data(APPOINTMENT_FILE)

    if not appointments:
        print("No appointments found.")
        return

    print("\n========== APPOINTMENT LIST ==========")

    for appointment in appointments:
        print("-" * 40)
        print(f"Appointment ID : {appointment['id']}")
        print(f"Patient Name   : {appointment['patient_name']}")
        print(f"Doctor Name    : {appointment['doctor_name']}")
        print(f"Date           : {appointment['date']}")
        print(f"Status         : {appointment['status']}")


# ==========================================
#           HOSPITAL DASHBOARD
# ==========================================

def dashboard():
    patients = load_data(PATIENT_FILE)
    doctors = load_data(DOCTOR_FILE)
    appointments = load_data(APPOINTMENT_FILE)

    print("\n========== HOSPITAL DASHBOARD ==========")
    print(f"Total Patients      : {len(patients)}")
    print(f"Total Doctors       : {len(doctors)}")
    print(f"Total Appointments  : {len(appointments)}")
    print("========================================")


# ==========================================
#              MAIN MENU
# ==========================================

def main():

    while True:

        print("\n")
        print("=" * 48)
        print("          HOSPITAL MANAGEMENT SYSTEM")
        print("=" * 48)

        print("1.  Register Patient")
        print("2.  View All Patients")
        print("3.  Search Patient")
        print("4.  Update Patient")
        print("5.  Delete Patient")
        print("6.  Add Doctor")
        print("7.  View Doctors")
        print("8.  Book Appointment")
        print("9.  View Appointments")
        print("10. Hospital Dashboard")
        print("0.  Exit")

        print("=" * 48)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            update_patient()

        elif choice == "5":
            delete_patient()

        elif choice == "6":
            add_doctor()

        elif choice == "7":
            view_doctors()

        elif choice == "8":
            book_appointment()

        elif choice == "9":
            view_appointments()

        elif choice == "10":
            dashboard()

        elif choice == "0":
            print("\nThank you for using Hospital Management System.")
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


# ==========================================
#          PROGRAM EXECUTION
# ==========================================

if __name__ == "__main__":
    main()
