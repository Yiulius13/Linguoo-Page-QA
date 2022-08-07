import time
from src.pages.Python.HomePage import HomePage

def test_scroll_up_button(browser,config):
    #GIVEN: Linguoo homepage.
    #WHEN:  User scrolls down (to the botton)
    #WHEN:  User clicks on "scroll up" button.
    #THEN:  Auto scroll to the top.

    homepage=HomePage(browser,config)
    homepage.load()

    top_height=homepage.get_scroll_height()
    homepage.auto_scroll_down()
    bottom_height=homepage.get_scroll_height()

    assert top_height != bottom_height

    homepage.click_scroll_up_button()

    time.sleep(2)
    new_height=homepage.get_scroll_height()
    assert top_height==new_height