from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec


class OptionsSetter:

    @staticmethod
    def configure_options():
        options = webdriver.ChromeOptions()
        options.add_argument('--allow-profiles-outside-user-dir')
        options.add_argument('--enable-profile-shortcut-manager')
        options.add_argument(r'user-data-dir=/home/newuser/wa-sender/profiles')
        options.add_argument('--profile-directory=Profile 1')
        options.add_argument('--profiling-flush=n')
        options.add_argument('--enable-aggressive-domstorage-flushing')

        return options


class WaSender:
    def __init__(self):
        self.options = OptionsSetter().configure_options()

    def login_qr(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        wait = WebDriverWait(driver, 30)

        url = "https://web.whatsapp.com/"
        driver.get(url)
        sleep(60)

    def send_message(self):
        numbers = ['+77004808765', '+79227288984']
        text = 'hello+world'

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        wait = WebDriverWait(driver, 30)

        for number in numbers:
            url = f"https://web.whatsapp.com/send?phone={number}&text={text}"
            driver.get(url)
            wait.until(ec.element_to_be_clickable(
                (By.XPATH, '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')))
            driver.find_element(By.XPATH,
                                '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
            sleep(5)


w = WaSender()
w.send_message()