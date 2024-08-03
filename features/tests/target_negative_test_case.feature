
Feature: Target incorrect verifies test

  Scenario: Verify message shown
    Given Open Target main page
    When Click on Sign in button
    When Click on right Sign in button
    When Input wrong email address
    And Input wrong password
    Then Click login button
    Then Verifies that error message is shown