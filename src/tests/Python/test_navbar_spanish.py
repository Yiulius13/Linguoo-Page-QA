from src.pages.Python.HomePage import HomePage

def test_navbar_spanish_button(browser,config):
    #GIVEN: Linguoo homepage.
    #WHEN:  User clicks on "Linguoo Español" button at the navbar
    #THEN:  Go to translated homepage.

    homepage=HomePage(browser,config)
    homepage.load()

    spanish_homepage=homepage.click_navbar_spanish_button()
    url=spanish_homepage.return_url()
    assert url==config["spanish-url"]


    