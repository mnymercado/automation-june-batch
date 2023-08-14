Feature: test for amazon search

  Scenario: Verify that a user can search
    Given Open Amazon page
    When Search for table
    Then Verify search result is correct

  Scenario: Verify that clicking Orders takes signin
    Given Open Amazon page
    When Click Orders
    Then Verify sign in page opened

