# Created by jackd at 3/18/2025
Feature: Help Page UI Test Case

  Scenario: Verify 6 UI element on the Target Help page
    Given Open target help page
    Then Verify 6 UI elements on the Target Help page

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page
    And Click on View Current Promotions
    And Verify Help - Current Promotions page opens
    When Select Browse Help dropdown topic Promotions & Coupons
    Then Verify Help Current Promotions page opened

   Scenario: User can select Help topic Target Circle
     Given Open Help page
     And Click on View Current Promotions
     And Verify Help - Current Promotions page opens
     When Select Browse Help dropdown topic Target Circle
     Then Verify Help About Target Circle page opened