from pytest_bdd import scenarios, parsers, given, when, then
import pytest
from .full_retirement_age import main

CONVERTERS = {
    'year': str,
    'month': str,
    'retire_years': str,
    'retire_months': str,
    'retire_year': str,
    'month_name': str
}

scenarios("basic_functionality.feature")

@pytest.fixture
@given("the user is using the full_retirement_age.py program")
def user_inputs():
    return dict(user_birthyear="", user_birthmonth="")

@when(parsers.parse('the user enters {year} when prompted for their year of birth'), converters=CONVERTERS)
def input_year(user_inputs, year):
    user_inputs["user_birthyear"] = year

@when(parsers.parse('the user enters {month} when prompted for their month of birth'), converters=CONVERTERS)
def input_month(user_inputs, month):
    user_inputs["user_birthmonth"] = month


@then(parsers.parse("the text the program returns should include 'Your full retirement age is {retire_years} and {retire_months} months.'"), converters=CONVERTERS)
def check_return_age(user_inputs, retire_years, retire_months):
    assert f'Your full retirement age is {retire_years} and {retire_months} months.' in main(user_inputs["user_birthyear"], user_inputs["user_birthmonth"])

@then(parsers.parse("the text the program returns should include 'This will be in {month_name} of {retire_year}.'"), converters=CONVERTERS)
def check_return_time(user_inputs, retire_year, month_name):
    assert f'This will be in {month_name} of {retire_year}.' in main(user_inputs["user_birthyear"], user_inputs["user_birthmonth"])