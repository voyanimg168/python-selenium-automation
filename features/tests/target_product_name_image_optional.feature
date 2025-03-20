# Created by jackd at 3/19/2025
Feature: Optional Test Cases

  Scenario Outline: Verify product name and image on Target search results page
    Given Open target main page
    When Search for <search_word>
    Then Verify every product on <search_word> search results page has name and image
        Examples:
      | search_word | expected_text |
      | sofa        | sofa          |
