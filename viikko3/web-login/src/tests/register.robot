*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  galle
    Set Password  galle123
    Set Password Confirmation  galle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ga
    Set Password  galle123
    Set Password Confirmation  galle123
    Submit Credentials
    Register Should Fail With Message  Username should have at least tree characters, and only letters a-z are allowed

Register With Valid Username And Invalid Password
    Set Username  galle
    Set Password  galle12
    Set Password Confirmation  galle12
    Submit Credentials
    Register Should Fail With Message  Password should have at least 8 characters, and at least one character should be other than a-z

Register With Nonmatching Password And Password Confirmation
    Set Username  galle
    Set Password  galle123
    Set Password  galle1234
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    # registration
    Set Username  calle
    Set Password  calle123
    Set Password Confirmation  calle123
    Submit Credentials
    Register Should Succeed

    # logout
    Go To Main page
    Click Logout Button
    
    # login
    Go To Login Page
    Set Username  calle
    Set Password  calle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    # registration
    Set Username  qa
    Set Password  qalle123
    Set Password Confirmation  qalle123
    Submit Credentials
    
    # login
    Go To Login Page
    Set Username  qa
    Set Password  qalle123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Click Logout Button
    Click Button  Logout
    Login Page Should Be Open

Submit Login Credentials
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
