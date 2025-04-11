# Created by jackd at 3/8/2025
Feature: Main Menu test cases

    Scenario: User navigates to Sign In page on Target and opens/closes Terms & Conditions before signing in
        Given Open Target Main Page
        When Click on Sign In Icon in Header
        And Click on Sign In icon on Navigation Page
        And Verify Sign In Form Opens
        And Store original window
        When Input signin email
        And Click continue signin button after email
        And Input signin password
        And Click on Sign In With Password Button
#        And Skip add mobile phone number
#        And Maybe later create passkey
        Then Verify user is logged in

    Scenario: User can open and close Terms and Conditions from sign in page
        Given Open Target Main Page
        When Click on Sign In Icon in Header
        And Click on Sign In icon on Navigation Page
        And Verify Sign In Form Opens
        When Store original window
        When Input signin email
        And Click continue signin button after email
        And Click Terms and Conditions link
        And Switch to new window
        And Verify Terms and Conditions page opens
        And Close current page
        And Return to original window



