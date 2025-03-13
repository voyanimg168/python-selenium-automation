# Created by jackd at 3/11/2025
Feature: Target cart empty test case

  Scenario: User sees cart is empty
    Given Open Target main page
    When Click on cart icon
    Then Verify correct message shown