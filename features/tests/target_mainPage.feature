# Created by jackd at 3/17/2025
Feature: Main Page UI Test Case

  Scenario: Verify header links has at least 1 link
    Given Open target main page
    Then Verify at least 1 link shown
  @smoke
  Scenario: Verify all header links are shown
    Given Open target main page
    Then Verify 6 header links are shown