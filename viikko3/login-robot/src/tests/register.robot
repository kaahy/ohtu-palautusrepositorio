*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ckalle  ckalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  bkalle  ckalle123
    Output Should Contain  User with username bkalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ck  bkalle123
    Output Should Contain  Invalid username or password

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  bk1  ckalle123
    Output Should Contain  Invalid username or password

Register With Valid Username And Too Short Password
    Input Credentials  cka  ckalle1
    Output Should Contain  Invalid username or password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ckalle  ckalleabc
    Output Should Contain  Invalid username or password

*** Keywords ***
Input New Command And Create User
    Create user  bkalle  bkalle123
    Input New Command
