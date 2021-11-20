Feature: Shows Retirement Age and Time
  A user will be able to enter their birth year and month,
  and get back a string of text printed to the console
  that tells them their retirement age as well as the
  year and month that they will retire


  Scenario Outline: Verify Correct Returns for Retirement Age
    Given the user is using the full_retirement_age.py program
    When the user enters <year> when prompted for their year of birth
    And the user enters <month> when prompted for their month of birth
    Then the text the program returns should include 'Your full retirement age is <retire_years> and <retire_months> months.'
    
    # month should not effect the output of retirement age (but should for retirement time)
    Examples:
      | year | month | retire_years | retire_months |
      | 1943 | 7     | 66           | 0             |
      | 1954 | 12    | 66           | 0             |
      | 1942 | 6     | 65           | 10            |
      | 1920 | 4     | 62           | 2             |
      | 1900 | 8     | 58           | 10            |
      | 1955 | 9     | 66           | 2             |
      | 1980 | 1     | 70           | 4             |
      | 2021 | 11    | 77           | 2             |
    
  Scenario Outline: Verify Correct Returns for Retirement Time
    Given the user is using the full_retirement_age.py program
    When the user enters <year> when prompted for their year of birth
    And the user enters <month> when prompted for their month of birth
    Then the text the program returns should include 'This will be in <month_name> of <retire_year>.'
    
    # In order for these examples to return the correct date, the last scenario
    # must work in its entirety as this scenario depends on the function the
    # last scenario was testing
    Examples:
      | year | month | month_name | retire_year |
      | 1943 | 7     | July       | 2009        |
      | 1954 | 12    | December   | 2020        |
      | 1942 | 6     | April      | 2008        |
      | 1920 | 4     | June       | 1982        |
      | 1900 | 8     | June       | 1959        |
      | 1955 | 9     | November   | 2021        |
      | 1980 | 1     | May        | 2050        |
      | 2021 | 11    | January    | 2099        |