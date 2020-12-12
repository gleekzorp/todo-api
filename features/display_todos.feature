Feature: Display the todos with the correct information

  Background:
    Given a list of these todos:
      | Title       | Done  |
      | Clean room  | False |
      | Wash Car    | False |
      | Cut Hair    | True  |
      | Code        | True  |

#    Original
  Scenario: Todos have a Title
    When I open the app
    Then I should see 4 todos
    And each todo should have a value for the Title

  Scenario: Todos with a true value for done should have a strike through style
    When I open the app
    Then I should see 2 todos with a strike through it

  Scenario: Todos should have a delete button
    When I open the app
    Then I should see 4 todos
    And Each todo should have a corresponding delete button

  Scenario: Todos should have a mark complete button
    When I open the app
    Then I should see 4 todos
    And Each todo should have a corresponding mark complete button

  Scenario: When I have more than 1 todo marked complete I should see a delete all completed button
    When I open the app
    Then I should see a delete all completed button

  Scenario: The app should have an input field and an add todo button
    When I open the app
    Then I should see a text input field
    And An add todo button


#    Refactor
  Scenario: Todos have a Title
    When I open the app
    Then I should see 4 todos
    And each todo should have a Title

  Scenario: Todos that are complete should have a strike through style
    When I open the app
    Then I should see 2 todos with a strike through it

  Scenario: Todos should have a delete button
    When I open the app
    Then I should see 4 todos
    And Each todo should have a corresponding delete button

  Scenario: Todos should have a mark complete button
    When I open the app
    Then I should see 4 todos
    And Each todo should have a corresponding mark complete button

  Scenario: I should see a 'delete all completed' button when I have more than 1 todo marked complete
    When I open the app
    And there is at least 2 todos marked complete
    Then I should see a delete all completed button

  Scenario: The app should have an input field and an add todo button
    When I open the app
    Then I should see a text input field
    And An add todo button