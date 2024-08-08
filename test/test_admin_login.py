from pytest import mark

from generic_utility.excel_lib import read_headers, read_data
from pom.loginpage import Loginpage


login_headers = read_headers("admin_data", "admin_login")
login_data = read_data("admin_data", "admin_login")

@mark.parametrize(login_headers, login_data)
def test_adminlogin(driver, pages,username,password):
    #adminlogin = Loginpage(driver)
    pages.loginpage.login_admin(username, password)


