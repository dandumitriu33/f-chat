# f-chat
Simple chat app - API and JS practice  
# Requirements

Features:

1. Create a user table that stores the following data
    1. id
    2. nickname
    3. password
2. Let the users register a new account
3. Create a chat table that stores the following data
    1. id
    2. user_id
    3. message
    4. datetime 
4. Let the users login, using nickname and password
5. While logged in, the user sees a page with the last 30 messages from chat table, ordered by the most recent one.
6. Underneath the chat messages, the user sees an input box and a button. If he writes a message and presses the button, the contents should go into the chat table and the page should refresh
