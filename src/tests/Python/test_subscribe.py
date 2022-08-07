from src.pages.Python.HomePage import HomePage

def test_send_subscription(browser,config):
    #GIVEN: Linguoo homepage.
    #WHEN:  User fill info to subscribe (email)
    #THEN:  Click on "subscribe" button.

    homepage=HomePage(browser,config)
    homepage.load()

    check=homepage.send_subscription()
    assert check