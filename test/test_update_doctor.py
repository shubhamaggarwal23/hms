from pytest import mark

from generic_utility.excel_lib import read_headers, read_data


login_headers = read_headers("admin_data", "admin_login")
login_data = read_data("admin_data", "admin_login")

update_doc_header = read_headers("admin_data", "admin_update_doctor")
update_doc_data = read_data("admin_data", "admin_update_doctor")

@mark.parametrize(login_headers,login_data)
@mark.parametrize(update_doc_header,update_doc_data)
def test_update_doc(driver,pages,username,password,name, contactNo):

    pages.loginpage.login_admin(username,password)
    pages.adminpage.update_doctor(name,contactNo)
