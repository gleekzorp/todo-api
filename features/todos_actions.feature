Feature: When an action occurs the correct action happens and the correct information is displayed

  Background:
    Given a list of these todos:
      | Title       | Done  |
      | Clean room  | False |
      | Wash Car    | False |
      | Cut Hair    | True  |
      | Code        | True  |

#    Original
  Scenario: Clicking a Todos mark complete button adds the correct styles
    Given The todo has a done value of False
    When I click that todos mark complete button
    Then Its Done value should be changed to True in the database
    And That todos style should have a strike through it

  Scenario: Clicking a Todos mark complete button adds the correct styles
    Given The todo has a done value of True
    When I click that todos mark complete button
    Then Its Done value should be changed to False in the database
    And That todos style should NOT have a strike through it

  Scenario: Clicking a Todos delete button removes the todo
    When I click a Todos delete button
    Then It should be removed from the database
    And The todo should no longer be visible to the user

  Scenario: Clicking the delete all completed button removes the todos with a value of mark complete
    When I click the delete all completed button
    Then It should remove the todos with the value of Done from the database
    And I there should only be 2 Todos visible to the user
    And These Todos should NOT have a strike through style

  Scenario: Filling in the input field and clicking add todo will update the list of todos
    When I fill in the input field with "Buy Milk"
    And Click the add todo button
    Then It should add the todo to the database
    And I should see a new todo with the title of "Buy Milk"
    And It should NOT have a strike through style


#  Refactor
  Scenario: Clicking a Todos mark complete button that isn't complete adds the correct styles
    Given the todo is not complete
    When I click that todos mark complete button
    Then it should have a strike through it

  Scenario: Clicking a Todos mark complete button that is complete adds the correct styles
    Given the todo is complete
    When I click that todos mark complete button
    Then it should NOT have a strike through it

  Scenario: Clicking a Todos delete button removes the todo
    When I click a Todos delete button
    Then The todo should no longer be visible to the user

  Scenario: Clicking the 'delete all completed' button removes the todos that have been marked complete
    When I click the delete all completed button
    Then it should remove all of the todos marked complete
    And there should only be 2 Todos visible to the user

  Scenario: Filling in the text input field and clicking add todo will update the list of todos
    When I fill in the text input field with "Buy Milk"
    And Click the add todo button
    Then I should see a new todo with the title of "Buy Milk"
    And It should NOT have a strike through style