Feature: Target circle benefit cells

  Scenario: Count benefit cells
    Given Open Target main page
    When Click Target circle  button
    When Find benefit cells shown
    Then Verify benefit has 10 links