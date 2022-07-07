Feature: Equalt is Start
    Scenario: Authorization and Registration
        Given Start Equalt
        When Authorization Equalt
        When Set Login and Password
        Then Logout
        Then Registration Page
        Then Finish