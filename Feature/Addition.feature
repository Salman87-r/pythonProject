Feature: Addition

  Scenario: Check addition functionality of addition
    Given Launch the Application
    When  click first number for addition
    And   click add
    And   click second number for addition
    Then  Verify the result
    And   Close application



