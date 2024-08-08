from generic_utility.lib_methods import SeleniumWrapper


class Patientpage:

    def __init__(self,driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)


    def create_patient_account(self):
        self.wrapper.click_element(self.)
