Feature: Error Detection/Input Validation


  Scenario Outline: Makes Sure Input is Valid and Notifies User When Invalid Input is Entered for Birth Year
    Given the user is using the full_retirement_age.py program
    When the user enters <invalid_input> when prompted for their year of birth
    And the user enters any valid input such as 1 for their month of birth
    Then the program should return 'Invalid input. Please try again.'
    
    Examples:
      | invalid_input |
      | 0             |
      | -1            |
      | 1940.2        |
      | 2050          |
      | string        |

  Scenario Outline: Makes Sure Input is Valid and Notifies User When Invalid Input is Entered for Birth Month
    Given the user is using the full_retirement_age.py program
    When the user enters any valid input such as 1980 when prompted for their year of birth
    And the user enters <invalid_input> when prompted for their month of birth
    Then the program should return 'Invalid input. Please try again.'
    
    Examples:
      | invalid_input |
      | 0             |
      | -1            |
      | 10.2          |
      | 8.99          |
      | string        |