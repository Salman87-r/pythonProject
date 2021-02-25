Feature: Scientific Operations
  Background: Launch the application
    When Launch the application
    And  Click Scientic
  Scenario: Check square functionality
    Given Click Number you want square
    And   Click square button
    Then  Verify the  result
    And   Close the application
  Scenario: Check Mode Functionality of mode
    When  Enter first number
    And   ENter mode button
    Then  Enter second number
    And   Close the application


