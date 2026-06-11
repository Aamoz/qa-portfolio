from playwright.sync_api import Page

def test_checkbox_states(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = page.locator("input[type='checkbox']")
    
    assert not checkboxes.nth(0).is_checked()
    assert checkboxes.nth(1).is_checked()

def test_checkbox_can_be_checked(page: Page):
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    checkbox1 = page.locator("input[type='checkbox']").nth(0)
    
    checkbox1.click()
    
    assert checkbox1.is_checked()
