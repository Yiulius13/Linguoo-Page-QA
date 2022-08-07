
from src.pages.Python.HomePage import HomePage

def test_contact_info(browser,config):
    #GIVEN: Linguoo homepage
    #WHEN:  User clicks facebook logo button (at the contact section)
    #THEN:  Go to facebook linguoo page

    #GIVEN: Linguoo homepage
    #WHEN:  User clicks twitter logo button (at the contact section)
    #THEN:  Go to twitter linguoo page
    
    #GIVEN: Linguoo homepage
    #WHEN: User clicks on speakers logo button (at the contact section)
    #THEN: Go to login page

    homepage=HomePage(browser,config)
    homepage.load()

    facebookpage=homepage.click_contact_facebook()
    url=facebookpage.return_url()
    assert url==config["facebook-url"]

    homepage.close_new_tab()

    twitterpage=homepage.click_contact_twitter()
    url=twitterpage.return_url()
    assert url==config["twitter-url"]

    homepage.close_new_tab()

    loginpage=homepage.click_contact_headphones()
    url=loginpage.return_url()
    assert url==config["login-url"]

