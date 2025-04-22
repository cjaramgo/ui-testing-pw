# Technical Test: UI Test Automation Challenge

This tutorial explains how to set up a Python test automation project with pytest and Playwright.

## What is Playwright?

Playwright is a framework for Web Testing and Automation. It allows testing [Chromium](https://www.chromium.org/Home), [Firefox](https://www.mozilla.org/en-US/firefox/new/) and [WebKit](https://webkit.org/) with a single API. Playwright is built to enable cross-browser web automation that is **ever-green**, **capable**, **reliable** and **fast**.

Playwright was created specifically to accommodate the needs of end-to-end testing. Playwright supports all modern rendering engines including Chromium, WebKit, and Firefox. Test on Windows, Linux, and macOS, locally or on CI, headless or headed with native mobile emulation.

For a more thorough list of advantages, check out
[Why Playwright?](https://playwright.dev/python/docs/why-playwright/)
from the docs.

## Getting started

### Prerequisites

1. Install pyenv(https://github.com/pyenv/pyenv#installation)

2. Install Python 3.10 or higher. Make sure you have previously installed the python version in this case 3.10.0. you can use the following command:

```bash
$ pyenv versions
```

3. In case you don't have the specific version you can install it using

```bash
$ pyenv install 3.10.0
```

### Test Project Setup

Let's set up the test project! For this tutorial
1. Create a directory named `ui-testing-pw` for the project or the name you prefer:

```bash
$ mkdir <project name>
$ cd <project name>
```

2. Set up the virtual environment ( it is recommended to use pyenv-virtualenv for this)

```bash
$ pyenv virtualenv 3.10.0 <virtualenv name>
```

**Note**: you can use `venv` or the name you want

3. After creating a virtual environment, you must "activate" it.
On macOS or Linux, use the following command:

```bash
$ pyenv activate <virtualenv name>
```

4. To install necessary packages you have to execute the command on the root to install the dependencies

```bash
$ pip install -r requirements.txt
```

6. Install the required browsers. Running the command without arguments will install the default browsers.

```bash
$ playwright install
```

You can also install specific browsers by providing an argument:

```bash
$ playwright install webkit
```

### Run tests

1. Running all the tests in headless mode

```bash
$ pytest
```

2. Running all the tests in headed mode

```bash
$ pytest --headed
```

3. Running tests using other browsers

```bash
$ pyenv --browser chromium
$ pyenv --browser firefox
$ pyenv --browser webkit
```

4. Running tests against multiple browsers at the same time

```bash
$ pytest <tests> --browser chromium --browser firefox --browser webkit --verbose
```
**Note**: The extra `--verbose` option is not necessary, but adding it will make pytest list each test result with its browser, so you can see the parameterization.

5. Running tests slowly to see the behavior in the browser

```bash
$ pytest --headed --slowmo <milisec>
```

For all file names we use snake case which refers to the style of writing in which each space is replaced by an underscore (_) character, and the first letter of each word written in lowercase.

### Run Reports

Test reports can be generated using Allure Report, this contains the result of each test including the log and a screenshot of each test, to generate the reports you can use the following command

```bash
$ allure serve AllureReport
```

To install Allure reports locally, you can follow the following guide [Allure Reports](https://allurereport.org/docs/install/)

## Implement Page Objects

A page object is an abstraction of a web page using a programming language. The intention is to represent all the page within code to take action against specific elements.

Each page should be modeled by its own class. Page object classes should be located in a directory `pages` so that they can be imported by tests.

A page object class typically has three main parts:

1. Dependency injection of the browser automator through a constructor
2. Locators and any other data stored as variables
3. Interaction methods that use the browser automator and the selectors

Let's add these one at a time.
Inside `pages/file_page.py`, import Playwright's `Page` class:

```python
from playwright.sync_api import Page
```

Define the class constructor, calling the Object `Page`

```python
def __init__(self, page: Page):
    self.page = page
```

Inside the constructor add all required locators

```python
    self.locator_name1 = page.locator('locator')
    self.locator_name2 = page.get_by_role('role_name', name='visible name')
```

These locators are created once and can be used anywhere. We can use them to make interactions. for more information about locator please see [Playwright Locators](https://playwright.dev/python/docs/locators)

And interaction is a method that performs an atomic action like clicking on an element or entering text in an input or selecting an option. An  interaction looks like this:

```python
    def click_on_buton(self):
        self.locator_n.click()
```


### Page object fixtures

In pytest, shared fixtures belong in a module under the `steps`. Example

```python
import pytest

from pages.page_object import ClassNamePage
from playwright.sync_api import Page

@pytest.fixture
def my_page_object(page: Page) -> ClassNamePage:
    return ClassNamePage(page)
```

Now the new fixture `my_page_object` calls the Playwright `page` fixture and use it to construct a page object.

With this new fixture we can use it in the step definition

```python
@when("my step")
def step_definition(my_page_object):
    my_page_object.function
```

Notice the following:

The `my_page_object` fixture is declared as arguments for the step function.
The step function no longer explicitly constructs page objects.

### Project structure

```
├── Questions.md
├── README.md
├── automation.log
├── conftest.py
├── features
│   ├── __init__.py
│   └── login.feature
├── pages
│   ├── __init__.py
│   └── login_page.py
├── pytest.ini
├── requirements.txt
└── steps
    ├── __init__.py
    └── login_steps.py
   ```