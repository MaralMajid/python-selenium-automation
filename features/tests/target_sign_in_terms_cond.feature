Feature: Target Sign in page Terms and Conditions test

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target main page
    When Click on Sign in button
    When Click on right Sign in button
    When Store original window
    When Click on Target terms and conditions link
    When Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    Then User can close new window
    Then Switch back to original