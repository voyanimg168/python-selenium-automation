# Created by jackd at 3/18/2025
Feature: Target Circle page test cases

  Scenario: Verify all benefit cells on Target Circle page
    Given Open Target Circle page
    When Click on Target Circle benefit cell
    Then Verify 15 benefit cells show on Target Circle page
    ##minimum 10 benefit cells
