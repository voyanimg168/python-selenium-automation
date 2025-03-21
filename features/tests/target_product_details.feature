# Created by jackd at 3/18/2025
Feature: Product Page Functionality test cases

  Scenario Outline: Click on color options
    Given Open target <product_id> page
    Then Click on <product_id> for <expected_colors> options
    Examples:
      | product_id | expected_colors                                                       |
      | A-54551690 | Blue Tint, Denim Blue, Marine, Raven                                  |
      | A-91511634 | black/gum, dark khaki, grey, navy/tan, white/navy/red, white/sand/tan |