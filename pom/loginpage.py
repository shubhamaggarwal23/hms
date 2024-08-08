from generic_utility.lib_methods import SeleniumWrapper
from generic_utility.excel_lib import attach_locator


@attach_locator("loginpage")
class Loginpage:

    def __init__(self,driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(driver)

    def login_admin(self,username,password):
        self.wrapper.pagedown()
        self.wrapper.click_element(self.click_admin)
        self.wrapper.enter_text(self.txt_admin_username, value=username)
        self.wrapper.enter_text(self.txt_admin_password, value=password)
        self.wrapper.click_element(self.btn_admin_login)
        self.wrapper.takescreenshot()

    def login_doctor(self,doc_username,doctor_password):
        self.wrapper.pagedown()
        self.wrapper.click_element(self.click_doctor)
        self.wrapper.enter_text(self.txt_doctor_username, value = doc_username)
        self.wrapper.enter_text(self.txt_doctor_password, value = doctor_password)
        self.wrapper.click_element(self.btn_doctor_login)


    def login_pateint(self,pateint_username, patient_password):
        self.wrapper.pagedown()
        self.wrapper.click_element(self.click_patient)
        self.wrapper.enter_text(self.txt_patient_usernme, value = pateint_username)
        self.wrapper.enter_text(self.txt_patient_password, value = patient_password)
        self.wrapper.click_element()