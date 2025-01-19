import json

import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'): #scope: to run only once per session for all the test suites
    # Read the file
    with open("config.json") as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Safari', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # return config so it can be used
    return config

@pytest.fixture
def browser(config):
    # Initialize the webdriver instance
    if config['browser'] == "Chrome":
        b = selenium.webdriver.Chrome()
    elif config['browser'] == "Safari":
        b = selenium.webdriver.Safari()
    elif config['browser'] == "Headless Chrome":
        opt = selenium.webdriver.ChromeOptions()
        opt.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opt)
    else:
        raise Exception(f'browser "{config['browser']}" is not supported')

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config['implicit_wait'])

    # return the webdriver instance for the setup - till here all of the above are setup steps for each test
    yield b

    # Quit the driver instance for the cleanup
    b.quit()
