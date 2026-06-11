import pytest
from playwright.sync_api import Page

def test_successful_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    page.click("button[type='submit']")
    assert "You logged into a secure area!" in page.locator(".flash.success").inner_text()

def test_failed_login(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("#username", "wronguser")
    page.fill("#password", "wrongpassword")
    page.click("button[type='submit']")
    assert "Your username is invalid!" in page.locator(".flash.error").inner_text()
