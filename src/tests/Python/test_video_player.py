from src.pages.Python.HomePage import HomePage
import time
def test_video_player(browser,config):
    #GIVEN: Linguoo homepage.
    
    #WHEN:  User clicks the "play" button (at the "What is Linguoo?" section)
    #THEN:  YouTube video player displays-

    #WHEN:  User starts the video.
    #THEN:  The video plays.
    
    #WHEN:  User clicks the "x" button to close the video player.
    #THEN:  The video player closes.

    homepage=HomePage(browser,config)
    homepage.load()

    
    player_displayed=homepage.click_play_video()
    assert player_displayed

    current_video_time=homepage.videoplayer_click_play()
    assert current_video_time != "0:00"

    homepage.switch_default_frame()

    player_not_displayed=homepage.videoplayer_click_close()
    assert player_not_displayed
