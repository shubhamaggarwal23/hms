from pytest import fixture
from selenium import webdriver

from pom.adminpage import Adminpage
from pom.doctorpage import Doctorpage
from pom.loginpage import Loginpage


def pytest_addoption(parser):
    parser.addoption("--browser",action = "store", default = "chrome", dest = "browser")
    parser.addoption("--env", action = "store", default = "test", dest = "env")
    parser.addoption("--headless", action = "store_true", default = False, dest = "--headless")


# @fixture
# def _config(request):
#     env = request.config.option.env
#
#     class Test_config:
#         url ="http://49.249.28.218:8081/AppServer/Hospital_Management_System/index.html"
#         admin_user_name = "admin"
#         admin_password = "Test@12345"
#
#     class Stage_config:
#         url = "http://49.249.28.218:8081/AppServer/Hospital_Management_System/index.html"
#         admin_user_name = "admin"
#         admin_password = "Test@12345"
#
#     return Test_config()

@fixture()
def driver(request):
    browser = request.config.option.browser
    #headless = request.config.option.headless

    if browser.upper() == "CHROME":
        _driver = webdriver.Chrome()
    elif browser.upper() == "FIREFOX":
        _driver = webdriver.Firefox()
    elif browser.upper() == "EDGE":
        _driver = webdriver.Edge()
    else:
        print("invalid browse")

    _driver.maximize_window()
    _driver.get("http://49.249.28.218:8081/AppServer/Hospital_Management_System/index.html")
    yield _driver
    _driver.quit()

@fixture()
def pages(driver):
    class Pages:
        loginpage = Loginpage(driver)
        adminpage = Adminpage(driver)
        doctorpage = Doctorpage(driver)

    return Pages()
