from turtle import home
from src.pages.Python.HomePage import HomePage

def test_navbar_home_button(browser,config):
    #GIVEN: Linguoo Home page.
    #WHEN:  User clicks on home button, at the navbar.
    #THEN:  Go to homepage.
    
    homepage=HomePage(browser,config)
    homepage.load()

    url=homepage.click_navbar_home_button()
    assert url==config["url"]