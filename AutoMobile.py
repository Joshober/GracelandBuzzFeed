try:
    import subprocess


    def install_library(library_name):
        try:
            __import__(library_name)
        except ImportError:
            print(f"The '{library_name}' library is not installed. Installing...")
            subprocess.check_call(["pip", "install", library_name])
            print(f"The '{library_name}' library has been installed.")


    # Usage:
    install_library("threading")
    install_library("time")
    install_library("urllib.request")
    install_library("datetime")
    install_library("requests")
    install_library("webdriver-manager")
    install_library("selenium")
    install_library("pyautogui")
    import time
    import threading

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service

    from webdriver_manager.chrome import ChromeDriverManager

    from selenium.webdriver.common.by import By

    from selenium.webdriver.common.keys import Keys
    from datetime import datetime, timedelta

    import pyautogui

    import requests


    def addEvents(browser, Event):
        # Download the image from the URL    try:

        time.sleep(10)
        try:
            browser.get(
                "https://manage.wix.com/dashboard/fbbad089-2c01-471d-a369-84d7d986ec43/events/new?referralInfo=events")
            time.sleep(10)

            browser.find_element(By.XPATH,
                                 '//*[@id="root"]/div/div/div/div/div[2]/main/span/div/div[2]/div[1]/div/div/span/span/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[2]/div/div/label/div/div/div[2]').click()
        except Exception as e:
            print("Error in clicking rsvp", e)

        try:
            browser.find_element(By.XPATH, '//*[@id="eventName"]').click()

            browser.find_element(By.XPATH, '//*[@id="eventName"]').send_keys(Event.title)
        except Exception as e:
            print("Error in finding and sending keys to 'title' element:", e)

        try:
            browser.find_element(By.XPATH,
                                 '//*[@id="root"]/div/div/div/div/div[2]/main/span/div/div[2]/div[1]/div/div/span/span/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[1]/div/div[3]/div/div[2]/div/div/div/div[1]/div/div/span/div[2]/div/input').send_keys(
                Event.tag)
            print(Event.tag)
        except Exception as e:
            print("Error in entering category:", e)
        try:
            time.sleep(4)
            photo = {'f31894_f91bfb87a14544c082a4d747e33f7ba2~mv2.png': 2,
                     'f31894_cb9bc732e1204dcbb11ccce7f953f90d~mv2.jpg': 1,
                     'rganization-photos/6daa785c-d747-431e-ade3-4149ac459e18/036bf836-1173-4c20-af11-781d21751c10.png': 0}
            try:
                image_name = photo[Event.imageLink[35:]]
            except Exception as e:
                image_name = 0

            browser.find_element(By.XPATH,
                                 '//div[@class="wds_1_38_0_AddItem__contentContainer wds_1_38_0_AddItem---theme-5-image wds_1_38_0_AddItem---size-4-tiny wds_1_38_0_AddItem---alignItems-6-center"]').click()
            time.sleep(4)
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('enter')
            time.sleep(5)

            for x in range(image_name + 1):
                pyautogui.press('right')
            pyautogui.press('enter')

            print("Ran")

        except Exception as e:
            print(Event.imageLink[35:])
            print("Error in clicking the image:", e)
        time.sleep(2)
        try:
            browser.find_element(By.XPATH,
                                 '//*[@id="react-collapsed-panel-1"]/div/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/div/input').send_keys(
                Events.startDate.strftime("%m/%d/%Y") + Keys.LEFT * (
                            len(Events.startDate.strftime("%m/%d/%Y")) + 1) + Keys.BACKSPACE * 20)

            browser.find_element(By.XPATH,
                                 '//*[@id="react-collapsed-panel-1"]/div/div/div[1]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/div/input').send_keys(
                Keys.DELETE + Keys.TAB)
            time.sleep(2)
            browser.find_element(By.XPATH,
                                 '//*[@id="react-collapsed-panel-1"]/div/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/input').send_keys(
                Events.startDate.strftime("%H:%M") + Keys.BACKSPACE + Keys.TAB)
            browser.find_element(By.XPATH,
                                 '//*[@id="react-collapsed-panel-1"]/div/div/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div/div/div/div/input').send_keys(
                Keys.TAB)


        except Exception as e:
            print("Error in entering event date: ", e)

        try:
            tba = browser.find_elements(By.CSS_SELECTOR,'.wds_1_38_0_ToggleSwitchCore__input')
            tba[1].click()

            time.sleep(1)
            browser.find_element(By.XPATH,'//*[@id="tbdMessage"]').send_keys(Keys.BACKSPACE*20)
            browser.find_element(By.XPATH,'//*[@id="tbdMessage"]').send_keys(Event.location)

            # browser.find_element(By.XPATH,
            #                      '//*[@id="root"]/div/div/div/div/div[2]/main/span/div/div[2]/div[1]/div/div/span/span/div[2]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/input').send_keys(Event.location+Keys.ARROW_DOWN)
            # time.sleep(3)
            # browser.find_element(By.XPATH,
            #                      '//*[@id="root"]/div/div/div/div/div[2]/main/span/div/div[2]/div[1]/div/div/span/span/div[2]/div/div/div/div[2]/div/div/div/div[4]/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/div/div/input').send_keys(Keys.UP+ Keys.TAB)



        except Exception as e:
            print("Error in entering the location:", e)

        try:
            browser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div/div/div/div[2]/main/span/div/div[2]/div[1]/div/div/span/span/div[2]/div/div/div/div[2]/div/div/div/div[5]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div/div/div/div').send_keys(
                Event.description + Keys.ENTER + "Link: " + Event.link + Keys.TAB)
        except Exception as e:
            print("Error in entering description", e)


        try:
            browser.find_element(By.XPATH,
                                 '//button[@data-hook="header-primary-action"]').click()
            time.sleep(10)

            pyautogui.press('esc')

            browser.execute_script("window.scrollTo(document.body.scrollWidth, 0);")
            time.sleep(1)
            browser.find_element(By.XPATH,
                                 '//*[@id="root"]/div/div/div/div/div[2]/main/span/div/div[2]/div[1]/div/div/span/span/div[2]/div/div[1]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/button').click()


            print("Sucess")


        except Exception as e:

            print("fail")


    class Event:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)
            if not hasattr(Event, 'contactName'):
                # Code to be executed if 'attribute3' doesn't exist
                setattr(self, "contactName", "Graceland Library")
            if not hasattr(Event, 'contactEmail'):
                # Code to be executed if 'attribute3' doesn't exist
                setattr(self, "contactEmail", "jacobstarks@gmail.com")

                if not hasattr(Event, 'Location'):
                    # Code to be executed if 'attribute3' doesn't exist
                    setattr(self, "Location", "Graceland University Lamoni Iowa")

        def print_values(self):
            for attr_name, attr_value in vars(self).items():
                print(f"{attr_name}: {attr_value}")



    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Replace with your actual endpoint URL
    endpoint_url = "https://www.gracelandlibraries.org/_functions/Events/"

    headers = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        }

    response = requests.get(endpoint_url, headers=headers)
    if response.status_code == 200:
            data = response.json()
            items = data["items"]

            try:

                driver.get(
                    "https://manage.wix.com/dashboard/fbbad089-2c01-471d-a369-84d7d986ec43/events/new?referralInfo=events")
                pyautogui.press('f11')

                driver.find_element(By.TAG_NAME, "input").send_keys(
                    "email" + Keys.ENTER)  # You can adjust the XPath expression to match your requirements
                time.sleep(6)
                driver.find_element(By.TAG_NAME, "input").send_keys(
                    Keys.TAB + "password" + Keys.ENTER)  # You can adjust the XPath expression to match your requirements
                time.sleep(4)


            except Exception as e:
                print("Error in browser signin:", e)
                time.sleep(5)
            # Process the items as needed
            for item in items:

                print(item["startDate"])
                Events = Event(**item)
                Events.startDate = datetime.fromisoformat((item["startDate"])[:-1])
                if Events.startDate.strftime("%H") == "00":
                    Events.startDate = datetime.fromisoformat((item["startDate"])[:-1])
                else:

                    Events.startDate = datetime.fromisoformat((item["startDate"])[:-1])-timedelta(hours=5)



                # Events = Event(item ["title"],item ["description"],item ["startDate"],item ["endDate"],item ["tag"])
                addEventThread = threading.Thread(target=addEvents(driver, Events))
                # addEvents(driver, Events)

                addEventThread.start()
                # Access individual fields within each item
                # Process the fields further or perform desired operations

    else:
        print("API request failed:", response.text)
        driver.quit()
        # driver.quit()

except Exception as e:
            print("An error occurred:", e)
            input("Press Enter to exit...")
            driver.quit()
driver.quit()
