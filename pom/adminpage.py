from ast import literal_eval

from generic_utility.lib_methods import SeleniumWrapper
from generic_utility.excel_lib import attach_locator
from pom.loginpage import Loginpage
from random import randrange
from time import sleep


@attach_locator("adminpage")
class Adminpage:

    def __init__(self,driver):
        self.driver = driver
        self.wrapper = SeleniumWrapper(self.driver)
        #self.login = Loginpage(self.driver)

    def create_doctor(self,specilization,name,address,fees,contactNo,password,confirmpassword):
        # print(self.__class__.__dict__.items())
        #self.login.login_admin("admin","Test@12345")
        self.wrapper.click_element(self.click_expand_doctor)
        self.wrapper.click_element(self.click_add_doctor)
        self.wrapper.select_element(self.txt_doc_specilization,item =specilization)
        self.wrapper.enter_text(self.txt_doc_name,value =name)
        self.wrapper.enter_text(self.txt_doc_clinic_address,value =address)
        self.wrapper.enter_text(self.txt_doc_fees,value =fees)
        self.wrapper.enter_text(self.txt_doc_contact_no, value =contactNo)
        self.wrapper.enter_text(self.txt_doc_email,value =f"{name}{randrange(1,1000)}@gmail.com")
        self.wrapper.enter_text(self.txt_doc_password,value = password)
        self.wrapper.enter_text(self.txt_doc_confirmpassword, value =confirmpassword)
        self.wrapper.click_element(self.click_doc_submit)
        #sleep(10)
        text = "Doctor info added Successfully"
        assert text == self.wrapper.alert_text(),"doctor is not created"

        self.wrapper.click_element(self.click_admin_dropdown)
        self.wrapper.click_element(self.click_admin_logout)

    def update_doctor(self, name, contactNo):
        self.wrapper.click_element(self.click_expand_doctor)
        self.wrapper.click_element(self.click_manage_doctors)
        self.wrapper.pagedown()
        loc_value = str(self.click_edit_pencil)
        l_value = loc_value.replace("{doc_name}",name)
        self.wrapper.click_element(literal_eval(l_value))
        self.wrapper.enter_text(self.txt_doc_contact_no, value = contactNo)
        self.wrapper.click_element(self.click_doc_update)
        text = "Doctor Details updated Successfully"
        assert text == self.wrapper.get_text(self.txt_update_res),"doctor is not updated"

        self.wrapper.click_element(self.click_admin_dropdown)
        self.wrapper.click_element(self.click_admin_logout)
