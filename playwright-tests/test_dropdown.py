from playwright.sync_api import Page

def test_select_option_1(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.select_option("#dropdown", label="Option 1")
    assert page.locator("#dropdown").input_value() == "1"

def test_select_option_2(page: Page):
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.select_option("#dropdown", label="Option 2")
    assert page.locator("#dropdown").input_value() == "2"
