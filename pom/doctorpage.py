from generic_utility.excel_lib import attach_locator
from generic_utility.lib_methods import SeleniumWrapper


@attach_locator("doctorpage")
class Doctorpage:

    def __init__(self,driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)

    def doctor_logout(self):
        self.wrapper.click_element(self.click_doc_dropdown)
        self.wrapper.click_element(self.click_doc_logout)

    def add_patient(self, patientName, patient_contactNo, patient_email, patient_address,patient_age, medical_history):
        self.wrapper.click_element(self.click_patient_expand)
        self.wrapper.click_element(self.click_add_patient)
        self.wrapper.enter_text(self.txt_patient_name, value = patientName)
        self.wrapper.enter_text(self.txt_patient_contactno, value = patient_contactNo)
        self.wrapper.enter_text(self.txt_patient_email, value = patient_email)
        self.wrapper.click_element(self.rdo_patient_gender)
        self.wrapper.enter_text(self.txt_patent_address, value = patient_address)
        self.wrapper.enter_text(self.txt_patient_age, value = patient_age)
        self.wrapper.enter_text(self.txt_patient_mediacal_history, value = medical_history)
        self.wrapper.click_element(self.click_submit)