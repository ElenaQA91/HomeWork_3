
from selene import browser, be, have

def test_open_browser():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_negative_search():
    text = "*_*"
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type(text).press_enter()
    browser.element('[id="search"]').should(have.text('Ответы Mail: *_* что значит?'))