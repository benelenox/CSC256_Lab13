from pytest_bdd import scenarios, parsers, given, when, then
import pytest
from .full_retirement_age import main

CONVERTERS = {
    'invalid_input': str
}

scenarios("error_detection.feature")

@pytest.fixture
@given("the user is using the full_retirement_age.py program")
def user_inputs():
    return dict(user_birthyear="", user_birthmonth="")


@when("the user enters any valid input such as 1980 when prompted for their year of birth")
def valid_year(user_inputs):
    user_inputs["user_birthyear"] = "1980" # the main function expects string inputs as one would get from the input function


@when(parsers.parse('the user enters {invalid_input} when prompted for their year of birth'), converters=CONVERTERS)
def invalid_year(user_inputs, invalid_input):
    user_inputs["user_birthyear"] = invalid_input


@when("the user enters any valid input such as 1 for their month of birth")
def valid_month(user_inputs):
    user_inputs["user_birthmonth"] = "1" # the main function expects string inputs as one would get from the input function


@when(parsers.parse('the user enters {invalid_input} when prompted for their month of birth'), converters=CONVERTERS)
def invalid_month(user_inputs, invalid_input):
    user_inputs["user_birthmonth"] = invalid_input


@then("the program should return 'Invalid input. Please try again.'")
def check_return(user_inputs):
    assert main(user_inputs["user_birthyear"], user_inputs["user_birthmonth"]) == 'Invalid input. Please try again.'

