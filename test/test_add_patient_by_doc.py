from pytest import mark

from generic_utility.excel_lib import read_headers, read_data

doc_headers = read_headers("doc_data", "doctor_login")
doc_data = read_data("doc_data", "doctor_login")

patient_headers = read_headers("doc_data", "doctor_add_patient")
patient_data = read_data("doc_data", "doctor_add_patient")

@mark.parametrize(patient_headers,patient_data)
@mark.parametrize(doc_headers,doc_data)
def test_add_patient(pages,doc_username, doctor_password, patientName, patient_contactNo, patient_email, patient_address,patient_age,medical_history  ):
    pages.loginpage.login_doctor(doc_username, doctor_password)
    pages.doctorpage.add_patient(patientName,patient_contactNo, patient_email,patient_address,patient_age, medical_history )

