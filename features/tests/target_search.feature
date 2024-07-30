Feature: Target main page search tests

  Scenario: User can search for a product for tea
    Given Open Target main page
    When Search for coffee
    When Click search button
    Then Verify search results shown for coffee
    Then Verify correct search results URL opens for coffee


  Scenario: User can search for a product for water
    Given Open Target main page
    When Search for water
    When Click search button
    Then Verify search results shown for water
    Then Verify correct search results URL opens for water

  Scenario: User can search for a product for shampoo
    Given Open Target main page
    When Search for shampoo
    When Click search button
    Then Verify search results shown for shampoo
    Then Verify correct search results URL opens for shampoo


#  Scenario Outline: User can search for products
#    Given Open Target main page
#    When search for <product>
#    Then Verify search results shown for <expected_result>
#    Then Verify correct search results URL opens for <expected_result>
#    Examples:
#    |product  |expected_result |
#    |tea  |tea |
#    |water  |water |
#    |shampoo |shampoo |