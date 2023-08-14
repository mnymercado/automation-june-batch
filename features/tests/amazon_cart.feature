Feature: Tests for the amazon Cart

  Scenario: Verify that the Cart is Empty
    Given Open Amazon page
    When Click cart icon
    Then Verify cart is empty

  Scenario: Add product to cart
    Given Open Amazon page
    When Search for table
    And Click result
    And Click add to cart btn
    And Click go to cart btn
    Then Verify cart not empty