Feature: new project
  Scenario: test 1
    Given launch browser
    When I navigate to home page
    Then make sure the logo is present
    And I search for "moushum"
    When close browser