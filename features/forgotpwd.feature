Feature: login feature

  Background:
    Given open the browser
    When enter the url


  Scenario: valid pwd recovery
    Given login page is displayed
    When click on forgot password link
    And enter valid email id
    And click request button
    Then success msg should be displayed


  Scenario: invalid pwd recovery
    Given login page is displayed
    When click on forgot password link
    And enter invalid email id
    And click request button
    Then error msg should be displayed
