import time

from selenium.webdriver.common.by import By

from src.pages.Python.Page import Page
from src.pages.Python.LoginPage import LoginPage
from src.pages.Python.CommunityPage import CommunityPage
from src.pages.Python.PlayStorePage import PlayStorePage
from src.pages.Python.FacebookPage import FacebookPage
from src.pages.Python.TwitterPage import TwitterPage

class HomePage(Page):
    def __init__(self,browser,config):
        super().__init__(browser)
        self.url=config["url"]
        self.info=config["user-info"]
####################################################################################################################
    def click_navbar_home_button(self):
        home_button=self.browser.find_element(By.ID,"menu-item-191")
        home_button.click()
        return self.browser.current_url
    def click_navbar_login_button(self):
        login_button=self.browser.find_element(By.ID,"menu-item-321")
        login_button.click()
        return LoginPage(self.browser)
    def click_navbar_community_button(self):
        community_button=self.browser.find_element(By.ID,"menu-item-339")
        community_button.click()
        return CommunityPage(self.browser)
    def click_navbar_spanish_button(self):
        spanish_button=self.browser.find_element(By.ID,"menu-item-488")
        spanish_button.click()
        return SpanishHomePage(self.browser)
####################################################################################################################  
    def click_scroll_up_button(self):
        scrollup_button=self.browser.find_element(By.CLASS_NAME,"scrollup")
        scrollup_button.click()
####################################################################################################################  
    def click_android_button(self):
        android_button=self.browser.find_element(By.CLASS_NAME,"btn-white")
        android_button.click()
        return PlayStorePage(self.browser)
    def click_playstore_button(self):
        playstore_button=self.browser.find_element(By.XPATH,"/html/body/div[2]/section[6]/div[2]/div/div[1]/a[2]")
        return playstore_button.get_attribute("href")
####################################################################################################################
    def click_play_video(self):
        play_button=self.browser.find_element(By.CLASS_NAME,"fa-play")
        play_button.click()
        video_player=self.browser.find_element(By.CLASS_NAME,"wrapper-video")
        return video_player.is_displayed()
    def videoplayer_click_play(self):
        self.browser.switch_to.frame(self.browser.find_element(By.CLASS_NAME,"mfp-iframe"))
        play_button=self.browser.find_element(By.CLASS_NAME,"ytp-large-play-button")
        play_button.click()
        time.sleep(5) # perdóname dios
        timmer=self.browser.find_element(By.CLASS_NAME,"ytp-time-current")
        return timmer.text
    def videoplayer_click_close(self):
        close_button=self.browser.find_element(By.CLASS_NAME,"mfp-close")
        close_button.click()
        try:
            check=self.browser.find_element(By.CLASS_NAME,"wrapper-video").is_displayed()
        except:
            check=False
        return check
####################################################################################################################
    def change_testimonial_cards(self):
        cards=self.browser.find_elements(By.CLASS_NAME,"owl-page")
        checks=[]
        for card in cards:
            card.find_element(By.TAG_NAME,"span").click()
            state=card.get_attribute("class")
            if "active" in state:
                checks.append(True)
            else:
                checks.append(False)
        return checks
####################################################################################################################
    def click_contact_facebook(self):
        face_button=self.browser.find_element(By.CLASS_NAME,"fa-facebook")
        face_button.click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        return FacebookPage(self.browser)
    def click_contact_twitter(self):
        twitter_button=self.browser.find_element(By.CLASS_NAME,"fa-twitter")
        twitter_button.click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        return TwitterPage(self.browser)
    def click_contact_headphones(self):
        head_button=self.browser.find_element(By.CLASS_NAME,"fa-headphones")
        head_button.click()
        self.browser.switch_to.window(self.browser.window_handles[1])
        return LoginPage(self.browser)
####################################################################################################################
    def send_comment(self):
        entrys=["name","email","message"]
        datos=[self.info["name"],self.info["email"],self.info["message"]]
        for entry,dato in zip(entrys,datos):
            self.browser.find_element(By.NAME,f"your-{entry}").send_keys(dato)
        send_button=self.browser.find_element(By.CLASS_NAME,"fa-long-arrow-right")
        send_button.click()
        time.sleep(1)
        check=self.browser.find_element(By.CLASS_NAME,"wpcf7-response-output").is_displayed()
        return check
    def send_subscription(self):
        entry=self.browser.find_element(By.NAME,"EMAIL")
        entry.send_keys(self.info["email"])
        button=self.browser.find_element(By.CLASS_NAME,"fa-paper-plane")
        button.click()
        check=self.browser.find_element(By.CLASS_NAME,"mc4wp-alert").is_displayed()
        return check
                


class SpanishHomePage(HomePage):
    def __init__(self,browser):
        self.browser=browser
    def return_text(self):
        text=self.browser.find_element(By.CLASS_NAME,"subheader")
        return text.text