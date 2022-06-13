"""login feature feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)


@scenario('./../features/login3.feature', 'validate login page')
def test_validate_login_page():
    pass


@given('browser is ready')
def browser_is_ready():
    print("browser is ready")


@when(parsers.parse('we enter {url} in address bar'))
def we_enter_url_in_address_bar(url):
    print("Enter {} in address bar".format(url))


@then(parsers.parse('{page} page should be displayed'))
def page_page_should_be_displayed(page):
    print("{} page should be displayed".format(page))

