#from pom.loginpage import Loginpage
from pytest import mark

from generic_utility.excel_lib import read_headers, read_data


login_headers = read_headers("admin_data", "admin_login")
login_data = read_data("admin_data", "admin_login")

admin_header = read_headers("admin_data","admin_add_doctor")
admin_data = read_data("admin_data","admin_add_doctor")

@mark.parametrize(login_headers, login_data)
@mark.parametrize(admin_header,admin_data)
def test_create_doctor(driver,pages,username,password, specilization,name,address,fees,contactNo,doc_password,confirmpassword):

    # loginpage = Loginpage(driver)
    pages.loginpage.login_admin(username,password)
    pages.adminpage.create_doctor(specilization,name,address,fees,contactNo,doc_password,confirmpassword)
