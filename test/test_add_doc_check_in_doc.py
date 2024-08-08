from pytest import mark

from generic_utility.excel_lib import read_headers, read_data


login_headers = read_headers("admin_data", "admin_login")
login_data = read_data("admin_data", "admin_login")

admin_header = read_headers("admin_data","admin_add_doctor")
admin_data = read_data("admin_data","admin_add_doctor")

doc_login_header = read_headers("doc_data", "doctor_login")
doc_login_data = read_data("doc_data", "doctor_login")


@mark.parametrize(login_headers,login_data)
@mark.parametrize(admin_header,admin_data)
@mark.parametrize(doc_login_header,doc_login_data)
def test_add_doc_check_in_doc(pages, username, password, specilization, name, address, fees, contactNo, doc_password, confirmpassword,
                              doc_username,doctor_password):

    pages.loginpage.login_admin(username,password)
    pages.adminpage.create_doctor(specilization,name,address,fees,contactNo,doc_password,confirmpassword)
    pages.loginpage.login_doctor(doc_username,doctor_password)
    pages.docpage.doctor_logout()