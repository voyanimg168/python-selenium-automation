# Created by jackd at 3/18/2025
Feature: Help Page UI Test Case

  Scenario: Verify 6 UI element on the Target Help page
    Given Open Help page
    Then Verify 6 UI elements on the Target Help page

  Scenario Outline: User can select Help topic page
    Given Open Help Returns page
    When Select Browse Help topic <option_value>
    Then Verify Help topic <header> page opens
    Examples:
    |option_value         |header                               |
    |Promotions & Coupons |Current promotions                   |
    |Target Circle™       |About Target Circle                  |
    |Registries & Lists   |Create & manage registry & wish list |

