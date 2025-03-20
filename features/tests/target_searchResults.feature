# Created by jackd at 3/14/2025
Feature: Target Search test cases

  Scenario: User can search for tea on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results shown for tea

  Scenario: User can search for iPhone on Target
    Given Open target main page
    When Search for iPhone
    Then Verify correct search results shown for iPhone

  Scenario: User can search for dress on Target
    Given Open target main page
    When Search for dress
    Then Verify correct search results shown for dress

  Scenario Outline: User can search for a product on Target
    Given Open target main page
    When Search for <search_word>
    Then Verify correct search results shown for <expected_text>
    Examples:
      | search_word | expected_text |
      | tea         | tea           |
      | iPhone      | iPhone        |
      | dress       | dress         |

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for coffee
    And Click on Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Store product name
    And Click on View Cart button from side navigation
    Then Verify cart has 1 items
    Then Verify cart has correct product