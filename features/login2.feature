Feature: login feature

  Scenario: valid login
    Given login page is displayed
    When enter admin in username
    And enter manager in password
    And click login
    Then home page should be displayed


  Scenario: invalid login
    Given login page is displayed
    When enter abc in username
    And enter xyz in password
    And click login
    Then err msg should be displayed
