import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_checkbox_checked(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    
    checkbox1 = checkboxes[0]
    checkbox2 = checkboxes[1]
    
    assert not checkbox1.is_selected()
    assert checkbox2.is_selected()

def test_checkbox_can_be_checked(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    
    checkbox1 = checkboxes[0]
    
    checkbox1.click()
    
    assert checkbox1.is_selected()
