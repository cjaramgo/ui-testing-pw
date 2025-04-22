import logging

import allure
from playwright.sync_api import Page, expect


class Login:

    def __init__(self, page: Page):
        self.logger = logging.getLogger()
        self.page = page
        self.username_input = page.locator('input[name="UserName"]')
        self.password_input = page.locator('input[name="Password"]')
        self.login_button = page.get_by_role("button", name="Log In")
        self.logout_button = page.get_by_role("button", name="Log Out")
        self.login_status = page.locator('#loginstatus')

    # New line added
    def enter_username(self, username):
        self.logger.info(f"Enter username {username} in the field {self.username_input}")
        self.username_input.fill(username)

    def enter_password(self, password):
        self.logger.info(f"Enter password {password} in the field {self.password_input}")
        self.password_input.fill(password)

    def click_on_login(self):
        self.logger.info(f"Click on the button {self.login_button}")
        self.login_button.click()

    def click_on_logout(self):
        self.logger.info(f"Click on the button {self.logout_button}")
        self.logout_button.click()

    def validate_message(self, status, username):
        message = {"success": f"Welcome, {username}!",
                   "error": "Invalid username/password",
                   "logout": "User logged out."}
        expect(self.login_status).to_contain_text(message[status])

    def capture_screenshot(self, image_name):
        allure.attach(self.page.screenshot(), name=image_name, attachment_type=allure.attachment_type.PNG)

