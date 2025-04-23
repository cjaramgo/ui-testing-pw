import logging
import time

import pytest
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger()


# Setup browser
@pytest.fixture(scope="session", autouse=True)
def setup(browser, base_url):
    initial_msg = " Running a new automated test "
    logger.info(initial_msg.center(100, "*"))
    context = browser.new_context(base_url=base_url)
    yield context
    context.close()
    browser.close()
    final_msg = " Finished UI Automation Test "
    logger.info(final_msg.center(100, "*"))


# Setup page
@pytest.fixture()
def page(setup, request, pytestconfig):
    initial_msg = "Setup new page - this is a change in the Main branch"
    logger.info(initial_msg.center(100, "*"))
    page = setup.new_page()
    page.set_default_timeout(60000)
    yield page
    page.close()


def pytest_bdd_before_scenario(request, feature, scenario):
    running_scenario_msg = f" Running Scenario: {scenario.name} "
    logger.info(running_scenario_msg.center(100, "*"))


def pytest_bdd_after_scenario(request, feature, scenario):
    if not scenario.failed:
        logger.info(f"The Scenario: '{scenario.name}' has Passed \n")
    else:
        logger.error(f"The Scenario: '{scenario.name}' has Failed")


def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    scenario.failed = step.failed
    logger.info(f"{step.type.capitalize()} {step.name}")
    if step.type == 'then':
        if "login_page" in step_func_args:
            current_time = time.strftime("%Y%m%d%H%M%S")
            page = step_func_args['login_page']
            page.capture_screenshot(f"{scenario.name}-{current_time}")


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    scenario.failed = step.failed
    current_time = time.strftime("%Y%m%d%H%M%S")
    logger.error(f"The step: '{step.type.capitalize()} {step.name}' has failed")
    if "login_page" in step_func_args:
        page = step_func_args['login_page']
        page.capture_screenshot(f"FAILED-{scenario.name}-{current_time}")
