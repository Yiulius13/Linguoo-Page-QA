from src.pages.Python.HomePage import HomePage

def test_downloads_android(browser,config):
    #GIVEN: Linguoo homepage.
    #WHEN:  User clicks "Android" button (at the headder)
    #THEN:  Go to playstore, linguoo app.

    #WHEN:  User clicks on "Play Store" button (at the downloads section)
    #THEN:  Go to plastore, linguoo app.

    homepage=HomePage(browser,config)
    homepage.load()

    playstorepage=homepage.click_android_button()
    url=playstorepage.return_url()

    assert url==config["playstore-url"]

    homepage.load()

    url=homepage.click_playstore_button()

    assert url==config["playstore-url"]
    