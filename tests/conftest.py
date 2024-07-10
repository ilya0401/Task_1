import logging
import os

import pytest
from _pytest.fixtures import FixtureRequest
from py_selenium_auto.browsers.browser_services import BrowserServices

from py_selenium_auto_core.logging.logger import Logger
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

from resources.browsers.custom_startup import CustomStartup


@pytest.fixture(scope="session", autouse=True)
def setup_session(request):
    # TODO: workaround to set calling root path, because pytest runs from the root dir
    # conftest.py should be in the tests folder. If it is moved to another level,
    # then you need to set os.chdir(work_dir) differently without RootPathHelper.current_root_path(__file__)
    work_dir = RootPathHelper.current_root_path(__file__)
    os.chdir(work_dir)
    Logger.info(f'Setting work_dir: {work_dir}')

    for log_name in [
        "selenium.webdriver.remote.remote_connection",
        "selenium.webdriver.common.selenium_manager",
        "urllib3.connectionpool",
    ]:
        logger = logging.getLogger(log_name)
        logger.disabled = True

    Logger.info("Setup startup config")
    BrowserServices.Instance.set_startup(CustomStartup())
    yield


@pytest.fixture(scope="function", autouse=True)
def setup_function(request: FixtureRequest):
    BrowserServices.Instance.browser.maximize()
    yield
    if BrowserServices.Instance.is_browser_started:
        Logger.info("Closing browser")
        BrowserServices.Instance.browser.quit()
