
Feature: Tests for Help pages

  Scenario: User can select Help topic Gift Cards
    Given Open Help pages for Returns
    Then Verify Help Returns page opened
    When Select Help topic Gift Cards
    Then Verify Help Target GiftCard balance page opened