from turtle import home
from src.pages.Python.HomePage import HomePage

def test_navbar_login_button(browser,config):
    #GIVEN: Linguoo homepage.
    #WHEN:  User clicks on "Begin to listen" button, at the navbar.
    #THEN:  Go to login page.

    homepage=HomePage(browser,config)
    homepage.load()

    loginpage=homepage.click_navbar_login_button()
    url=loginpage.return_url()
    
    assert url==config["login-url"]