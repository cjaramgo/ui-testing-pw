import os

import pytest
from playwright.sync_api import Page
from pytest_bdd import scenarios, given, when, then, parsers

from pages.login_page import Login

scenarios('login.feature')
valid_username = os.getenv('VALID_USERNAME')
valid_password = os.getenv('VALID_PASSWORD')
invalid_password = os.getenv('INVALID_PASSWORD')


@pytest.fixture
def login_page(page: Page) -> Login:
    return Login(page)


@given("the user is on the Login Page")
def goto_login(page):
    page.goto("sampleapp")


@when("the user enters valid credentials")
def login_valid_credentials(login_page):
    """ This step authorize a valid user"""
    login_page.enter_username(valid_username)
    login_page.enter_password(valid_password)
    login_page.click_on_login()


@when("the user enters an invalid password")
def invalid_password_field(login_page):
    login_page.enter_username(valid_username)
    login_page.enter_password(invalid_password)
    login_page.click_on_login()


@when("the user leaves both fields empty")
def leave_empty_fields(login_page):
    login_page.click_on_login()


@when("the user leaves the username empty")
def leave_username_empty(login_page):
    login_page.enter_password(valid_password)
    login_page.click_on_login()


@when("the user leaves the password empty")
def leave_password_empty(login_page):
    login_page.enter_username(valid_username)
    login_page.click_on_login()


@given("the user has logged in")
def logged_in(login_page):
    login_valid_credentials(login_page)


@when("the user logged out")
def logged_out(login_page):
    login_page.click_on_logout()


@then(parsers.re("the system should display \\w+ (?P<status>[a-zA-Z]*) message"))
def display_success_message(login_page, status):
    login_page.validate_message(status, valid_username)
    return login_page.get_time()
