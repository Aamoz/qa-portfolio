import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_checkbox_checked(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    assert not checkboxes[0].is_selected()
    assert checkboxes[1].is_selected()

def test_checkbox_can_be_checked(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    checkbox1 = checkboxes[0]
    checkbox1.click()
    assert checkbox1.is_selected()
