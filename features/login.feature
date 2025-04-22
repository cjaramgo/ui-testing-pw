# Created by Carlos Jaramillo at 4/1/25
Feature: Login

  Background: Login Page
    Given the user is on the Login Page


  Scenario: Successful Login
    When the user enters valid credentials
    Then the system should display a success message

  Scenario: Login with Invalid Password
    When the user enters an invalid password
    Then the system should display an error message

  Scenario: Login with Empty Fields
    When the user leaves both fields empty
    Then the system should display an error message

  Scenario: Login with username field empty
    When the user leaves the username empty
    Then the system should display an error message

  Scenario: Login with password field empty
    When the user leaves the password empty
    Then the system should display an error message

  Scenario: Logout After Successful Login
    Given the user has logged in
    When the user logged out
    Then the system should display a logout message

  Scenario: New scenario
    Given this is given
    When this is when