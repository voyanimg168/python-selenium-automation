# Created by jackd at 3/8/2025
Feature: Target search test cases
  # Enter feature description here

  Scenario: User can search for a product on Target
    Given Open Target Main Page
    When Search for umbrella
    Then Verify correct search results shown