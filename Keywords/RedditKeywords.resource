#RedditKeywords
*** Settings ***
Library             ../Library/RedditPostLibrary.py
Library             ../Library/LogMessage.py
Variables           ../Library/Variables.py

*** Keywords ***
Create New Community In Reddit
    Create Community
    Log                     A new community has been created

Create New Post In Reddit
    ${post}=                Create Post
    Set Suite Variable      ${post}

Verify That New Post Is Created
    ${check}                Post Availability Check     ${post[0]}
    Should Be True          ${check}
    ${message}=             Post Message                ${post[1]}
    Log                     ${message}

Add Comment In Post
    Create Comment          ${post[0]}
    ${message}=             Comment Message             ${COMMENT_TEXT}
    Log                     ${message}

Delete Post In Reddit
    Delete Post             ${post[0]}

Verify That Post Is Deleted
    ${check}                Post Availability Check     ${post[0]}
    Should Not Be True      ${check}
    ${message}=             Delete Post Message         ${post[1]}
    Log                     ${message}
