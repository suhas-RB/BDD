from pytest_bdd import scenario, given, when, then, parsers


@scenario("./../features/login4.feature", "valid login")
def test_validlogin():
    pass


@scenario("./../features/login4.feature", "invalid login")
def test_invalidlogin():
    pass


@given("open the browser")
def open_the_browser():
    print("\nopen the browser")

@when("enter the url")
def enter_the_url():
    print("enter the url")


@given("login page is displayed")
def login_page():
    print("login page is displayed")


@when(parsers.parse("enter {un} in username"))
def enter_un(un):
    print("Enter {} in username".format(un))


@when(parsers.parse("enter {pw} in password"))
def enter_pwd(pw):
    print("Enter {} in password".format(pw))


@when("click login")
def click_login():
    print("click login button")


@then("home page should be displayed")
def homepage():
    print("home page is displayed")


@then("err msg should be displayed")
def err_msg():
    print("Error message is displayed")
