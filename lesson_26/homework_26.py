from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

frame_secrets = {
    "frame1": "Frame1_Secret",
    "frame2": "Frame2_Secret"
}

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get("http://localhost:8000/dz.html")
    time.sleep(2)

    for frame_id, secret in frame_secrets.items():

        driver.switch_to.frame(driver.find_element(By.ID, frame_id))

        input_elem = driver.find_element(By.TAG_NAME, "input")
        input_elem.clear()
        input_elem.send_keys(secret)

        driver.find_element(By.TAG_NAME, "button").click()

        time.sleep(1)
        alert = Alert(driver)
        assert alert.text == "Верифікація пройшла успішно!", f"Помилка у {frame_id}: {alert.text}"
        print(f"[OK] {frame_id}: {alert.text}")
        alert.accept()

        driver.switch_to.default_content()

    print("Успішно пройдено всі фрейми")

finally:
    time.sleep(2)
    driver.quit()