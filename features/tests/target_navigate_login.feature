# Created by jackd at 3/12/2025
Feature: Navigate Target Main Page to Sign In page test case

  Scenario: User navigate to Sign In page on Target
    Given Open Target Main Page
    When Click on Sign In Icon on Main Page
    And Click on Sign In icon on Navigation Page
    Then Verify Sign In Form Opens
