from src.pages.Python.HomePage import HomePage

def test_send_comments(browser,config):
    #GIVEN: Linguoo homepage.
    #WHEN:  User fill info in the entrys (at the comment section)
    #THEN:  Send comment.

    homepage=HomePage(browser,config)
    homepage.load()

    check=homepage.send_comment()
    assert check