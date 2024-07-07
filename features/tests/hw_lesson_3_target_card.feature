
Feature: Target cart field

  Scenario: Verify that cart field is empty
    Given Open Target main page
    When Click on cart button
    Then Verify cart is empty


  Scenario: Verify Sign in
    Given Open Target main page
    When Click on Sign in button
    When Click on right Sign in button
    Then Verify Sign in page