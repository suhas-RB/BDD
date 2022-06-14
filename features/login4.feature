Feature: login feature

  Background:
    Given open the browser
    When enter the url


  Scenario: valid login
    Given login page is displayed
    When enter admin in username
    And enter manager in password
    And click login
    Then home page should be displayed


  Scenario Outline: invalid login
    Given login page is displayed
    When enter <un> in username
    And enter <pw> in password
    And click login
    Then err msg should be displayed
    Examples:
      | un   | pw  |  
      | abc  | xyz |
      | asds |add  |
