# Created by jackd at 3/13/2025
Feature: Cart Test Cases

  Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    When Click on cart icon
    Then Verify 'Your cart is empty' message is shown
