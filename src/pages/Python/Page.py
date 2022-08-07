class Page:
    def __init__(self,browser):
        self.browser=browser
    def return_url(self):
        return self.browser.current_url
    def close_new_tab(self):
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])
    def load(self):
        self.browser.get(self.url)
    def switch_default_frame(self):
        self.browser.switch_to.default_content()
    def auto_scroll_down(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    def get_scroll_height(self):
        totalScrolledHeight = self.browser.execute_script("return window.pageYOffset + window.innerHeight")
        return totalScrolledHeight