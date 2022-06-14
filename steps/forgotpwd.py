from pytest_bdd import scenario, given, when, then, parsers


@scenario("./../features/forgotpwd.feature", "valid pwd recovery")
def test_valid_pwd_recovery():
    pass


@scenario("./../features/forgotpwd.feature", "invalid pwd recovery")
def test_invalid_pwd_recovery():
    pass


@when("click on forgot password link")
def forgot_pwd_link():
    print("click forgot pwd link")


@when(parsers.parse("enter {id} email id"))
def enter_mail_id(id):
    print("enter {} mail id".format(id))



@when("click request button")
def click_request_button():
    print("click request button")


@then(parsers.parse("{msg} msg should be displayed"))
def msg_displayed(msg):
    print("{} msg is displayed".format(msg))



