# Created by jackd at 3/18/2025
Feature: Product Page Functionality test cases

  Scenario Outline: Click on <product_id> color options
    Given Open target <product_id> page
    When Click on <product_id> color options
    Then <product_id> color should change
    Examples:
    |product_id|
    |A-54551690 |
    |A-91511634 |