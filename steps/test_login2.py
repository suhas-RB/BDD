from pytest_bdd import scenario,given,when,then

@scenario("./../features/login2.feature","valid login")
def test_login():
    pass

@given("login page is displayed")
def enter_un():
    print("Enter admin in username")

@when("enter admin in username")
def enter_pwd():
    print("Enter admin in username")

@when("enter manager in password")
def enter_pwd():
    print("Enter manager in password")

@when("click login")
def click_login():
    print("click login button")

@then("home page should be displayed")
def homepage():
    print("home page is displayed")