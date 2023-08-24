import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from code.globals import batch_duration


def start_driver(headless):



    # # after downloading enter the path to the chromedriver here
    # DRIVER_PATH = 'C:/Program Files/chrome driver/chromedriver.exe'
    #
    # # the follwing will configure the scrapper and open a chrome instance that we will use
    # options = Options()
    # options.add_argument("--disable-web-security") #  // don't enforce the same-origin policy
    # options.headless = headless

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280x1696')



    # options.add_argument("--window-size=800,450")
    driver = webdriver.Chrome(options=options) #, executable_path=DRIVER_PATH)
    return driver



def scroll_to_end(driver):
    # Define a function to check if the scroll height has changed
    def get_scroll_height():
        return driver.execute_script("return document.documentElement.scrollHeight")

    # Loop until you've reached the end of the list
    last_height = get_scroll_height()

    while True:
        # Scroll to the bottom of the list
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        # Wait for any potential new content to load
        time.sleep(2) # This may need to be adjusted based on the specific site you're working with

        # Calculate new scroll height and compare with last scroll height
        new_height = get_scroll_height()
        if new_height == last_height:
            break
        last_height = new_height

def get_last_episode_data2(driver):
    try:
        elements = driver.find_elements(By.CLASS_NAME, 'StoryListTile_container__IjFbs')
        last_element = elements[-1]
        time_posted = last_element.find_element(By.CSS_SELECTOR, '.StoryListTile_storyInfo__XnOTC.StoryListTile_oneLineTruncation__llTh3')
        time_posted = time_posted.text
        title = last_element.find_element(By.CSS_SELECTOR, '.StoryListTile_title__uu0Lo.StoryListTile_oneLineTruncation__llTh3')
        title = title.text

        # # Or using WebDriverWait
        # # Wait for the list of elements to be visible
        # elements = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'StoryListTile_container__IjFbs')))
        # last_element = elements[-1]
        # text_element = last_element.find_element(By.CSS_SELECTOR, '.StoryListTile_storyInfo__XnOTC.StoryListTile_oneLineTruncation__llTh3')
        # text = text_element.text
        return title, time_posted
    except IndexError:
        return "", "", ""

def get_last_episode_data(driver, minute='m'):
    try:
        elements = driver.find_elements(By.CLASS_NAME, 'StoryListTile_container__IjFbs')
        last_element = elements[-1]
        time_posted = last_element.find_element(By.CSS_SELECTOR, '.StoryListTile_storyInfo__XnOTC.StoryListTile_oneLineTruncation__llTh3')
        time_posted = time_posted.text
        title = last_element.find_element(By.CSS_SELECTOR, '.StoryListTile_title__uu0Lo.StoryListTile_oneLineTruncation__llTh3')
        title = title.text

        if time_posted[0].isdigit() and int(time_posted[0]) <= batch_duration and time_posted[1] == minute:
            last_element.click()
            time.sleep(2)
            poster = driver.find_element(By.CLASS_NAME, "StoryWebPlayer_videoPlayer__ISmZ6")
            poster = poster.get_attribute("poster")
            return driver.current_url, title, poster, time_posted
        else:
            return "", title, "", time_posted
    except Exception as e:
        print(e)
        return "", "", "", ""