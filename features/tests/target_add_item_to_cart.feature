Feature: Add item to Target cart

  Scenario: Verify an item in Target cart
    Given Open Target main page
    When Search for mug
    When Add the item to cart
    Then Click on right add to cart button
    When Click on view cart button
    Then Verify the item in the cart