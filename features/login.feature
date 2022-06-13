Feature: login feature
          This describes how login feature will behave

  Scenario: valid login
    Given browser is open
    When we enter actitime.com in address bar
    Then login page should be displayed


  Scenario: valid login2
    Given browser is open
    When we enter google.com in address bar
    Then login page should be displayed