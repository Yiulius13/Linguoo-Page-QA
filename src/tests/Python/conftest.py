import pytest
import selenium.webdriver
import json
#from selenium.webdriver.chrome.options import Options



@pytest.fixture
def browser(browser_config):
    if browser_config["browser"]=="Firefox":
        b=selenium.webdriver.Firefox()
    elif browser_config["browser"]=="Chrome":
        b=selenium.webdriver.Chrome()
    elif browser_config["browser"]=="Headless Chrome":        
        opts=selenium.webdriver.ChromeOptions()
        opts.add_argument("--headless")
        b=selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception("Browser {} no es soportado".format(config["browser"]))
    
    if type(browser_config["wait"])=="int()":
        b.implicitly_wait(browser_config["wait"])
    else:
        b.implicitly_wait(5)
    
    if browser_config["maximize"]=="True":
        b.maximize_window()
    else:
        pass

    yield b
    
    b.quit()


@pytest.fixture
def browser_config(scope="session"):
    with open("src/config/JSON/browser.json") as f:
        config=json.load(f)
    return config
@pytest.fixture
def config(scope="session"):
    with open("src/config/JSON/config.json") as f:
        config=json.load(f)
    return config
