import os
import time
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import tenacity
import pyperclip

def send_message(message: str, hook: str) -> None:
    """메시지를 디스코드로 보낸다."""
    requests.post(
        hook,
        data={"content": message},
    )

class TicketCrawler:
    def __init__(self) -> None:
        self.driver = self._get_driver()
        self.wait = WebDriverWait(self.driver, 30)

    def _get_driver(self) -> webdriver.Chrome:
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--no-sandbox")
        # chrome_options.add_argument("--disable-dev-shm-usage")
        return webdriver.Chrome(options=chrome_options)

    def run(self) -> None:
        self.create_longblack_ticket()
        # self.create_ep9_ticket()
        self.driver.quit()

    def create_longblack_ticket(self) -> None:
        self.driver.get("https://www.longblack.co/login")


        kakao_login_button = self.driver.find_element(By.CSS_SELECTOR, ".auth-service.kakao")
        time.sleep(1)
        kakao_login_button.click()

        username = self.driver.find_element(By.ID, "loginId--1")
        time.sleep(1)
        username.send_keys("drekali@naver.com")
        password = self.driver.find_element(By.ID, "password--2")
        time.sleep(1)
        password.send_keys("Rhakdhkd#1")
        time.sleep(1)
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".btn_g.highlight.submit")
        time.sleep(1)
        login_button.click()


        agree_button = WebDriverWait(self.driver, 300).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn_agree"))
)
        time.sleep(1)
        agree_button.click()
        time.sleep(2)

        self.driver.get("https://www.longblack.co/note")
        time.sleep(1)
        
        self.driver.find_element(By.CSS_SELECTOR, ".mygrid .mycell").click()
        time.sleep(1)

        element = self.driver.find_element(By.CSS_SELECTOR, ".share")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

        ticket = self.driver.find_element(By.ID, "re-clipboard").get_attribute("value")
        send_message(ticket, hook="https://discord.com/api/webhooks/1224926412117512254/aELQx4elDn-sp5hyvartNNDWtSJCAc6jFNCeXpmHdT_4Sni7iV3a48L_cXXFWB54XCfL")


    def create_ep9_ticket(self) -> None:
        self.driver.get("https://www.ep9.co/login")

        kakao_login_button = self.driver.find_element(By.CSS_SELECTOR, "[class^='page_kakaoBtn__']")
        kakao_login_button.click()
        time.sleep(1)

        username = self.driver.find_element(By.ID, "loginId--1")
        username.send_keys("drekali@naver.com")
        time.sleep(1)
        password = self.driver.find_element(By.ID, "password--2")
        password.send_keys("Rhakdhkd#1")
        time.sleep(1)
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".btn_g.highlight.submit")
        login_button.click()

        agree_button = WebDriverWait(self.driver, 300).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn_agree"))
        )
        agree_button.click()
        time.sleep(2)

        self.driver.get("https://www.ep9.co")
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, "[class^='Today_todayRecord__']").click()
        time.sleep(1)

        share_button =  WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[class^='shareBtn_textBtn__']"))
        )
        share_button.click()
        time.sleep(2)

        element = self.driver.find_element(By.CSS_SELECTOR, "button.css-7qh9s5")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

        # 클립보드에서 링크 가져오기
        copied_link = pyperclip.paste()
        send_message(copied_link, hook="https://discord.com/api/webhooks/1224929265972150282/OcHw5uY7NN4X23VHXRo-6Rpd8qQWM1Cdt-7H1Q1LaOPqziOO0gf1SvUV9l9XRYGHf7js")




if __name__ == "__main__":
    TicketCrawler().run()