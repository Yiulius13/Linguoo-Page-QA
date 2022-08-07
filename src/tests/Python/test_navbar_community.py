from src.pages.Python.HomePage import HomePage

def test_navbar_community_button(browser,config):
    #GIVEN: Linguoo Homepage.
    #WHEN:  User clicks on "Community" button at the navbar.
    #THEN:  Go to community page.

    homepage=HomePage(browser,config)
    homepage.load()

    communitypage=homepage.click_navbar_community_button()
    url=communitypage.return_url()

    assert url==config["community-url"]