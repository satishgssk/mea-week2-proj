Feature: Testing the REST application

    Scenario Outline: User adding a new item successfully
        Given That a user is on the url "http://localhost:8080/index.html"
        When The user enters the item name "<name>", description "<description>", and price "<price>" into the CREATE section
        And The user clicks the POST button
        Then The READ ALL section will populate with JSON containing _id "<_id>", name "<name>", description "<description>", and price "<price>"
        Examples:
            | name |  description | price | _id |
            | Test Name | Test Description | 9.99 | 1 |
