from turtle import home
from src.pages.Python.HomePage import HomePage

def test_testimonial_cards_changes(browser,config):
    #GIVEN: Linguoo homepage.
    #WHEN:  User clicks on testimonial span (under testimonial cards)
    #THEN:  Testimonial cards change

    homepage=HomePage(browser,config)
    homepage.load()

    checks=homepage.change_testimonial_cards()
    for card in checks:
        assert card