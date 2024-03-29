from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/" \
           "catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    main_page = MainPage(browser, link)
    login_page = LoginPage(browser, browser.current_url)
    main_page.open()
    main_page.go_to_login_page()
    login_page.should_be_login_url()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/" \
           "catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_be_login_link()
