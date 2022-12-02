#Reddit Test Cases
*** Settings ***
Documentation       Test suite to validate reddit.com
Resource            ../Keywords/RedditKeywords.resource

*** Test Cases ***
Create A New Post On Reddit.com
    [Documentation]         This test case verifies that the user can successfully create a new post on reddit.com
    Create New Post In Reddit
    Verify That New Post Is Created
    Add Comment In Post

Delete A Post On Reddit.com
    [Documentation]         This test case verifies that a user can successfully delete a post on reddit.com
    Delete Post In Reddit
    Verify That Post Is Deleted
