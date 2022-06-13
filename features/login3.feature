Feature: login feature

 Scenario Outline: validate login page
    Given browser is ready
    When we enter <url> in address bar
    Then <page> page should be displayed
   Examples:
     | url           | page          |  
     | actitime.com  | actitime page |
     | fb.com        | facebook page |
     | google.com    | google page   |

