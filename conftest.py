from pytest_bdd import scenario, given, when, then, parsers


@given("open the browser")
def open_the_browser():
    print("\nopen the browser")

@when("enter the url")
def enter_the_url():
    print("enter the url")

@given("login page is displayed")
def login_page():
    print("login page is displayed")

