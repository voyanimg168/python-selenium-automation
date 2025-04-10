# Created by jackd at 3/14/2025
Feature: Target Search test cases
  @smoke @safari-only @positive
  Scenario: User can search for tea on Target
    Given Open target main page
    When Search for tea
    Then Verify correct search results shown for tea
    And Verify tea in URL

  Scenario Outline: User can search for a product on Target
    Given Open target main page
    When Search for <search_word>
    Then Verify correct search results shown for <expected_text>
    Examples:
      | search_word | expected_text |
      | tea         | tea           |
      | iPhone      | iPhone        |
      | dress       | dress         |

  @smoke
  Scenario: User can add a product to cart
    Given Open target main page
    When Search for coffee
    And Click on Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Store product name
    And Click on View Cart button from side navigation
    Then Verify cart has 1 items
    Then Verify cart has correct product

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image

  Scenario: User can see favorites tooltip for search results
    Given Open target main page
    When Search for tea
    And Hover favorites icon
    Then Verify favorites tooltip is shown