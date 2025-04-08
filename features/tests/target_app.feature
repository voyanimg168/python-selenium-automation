# Created by jackd at 3/27/2025
Feature: Tests for Target App page

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    When Click Privacy Policy Link
    And Switch to new window
    Then Verify Privacy Policy page opens
    And Close current page
    And Return to original window
