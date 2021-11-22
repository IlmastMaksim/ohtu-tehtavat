*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Check It Is Open


*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallen
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  ka
    Set Password Confirmation  ka
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle321
    Submit Credentials
    Register Should Fail With Message  Passwords dont match

Login After Successful Registration
    Set Username  kalles
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed
    Logout From Page
    Go To Login Page And Check It Is Open 
    Set Username  kalles
    Set Password  kalle123
    Login Credentials
    Login Should Succeed


Login After Failed Registration
    Set Username  kalle
    Set Password  ka
    Set Password Confirmation  ka
    Submit Credentials
    Register Should Fail With Message  Invalid password
    Go To Login Page And Check It Is Open
    Set Username  kalle
    Set Password  ka
    Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Go To Register Page And Check It Is Open
    Go To Register Page
    Register Page Should Be Open

Logout From Page
    Go To Ohtu Page
    Click Button  Logout

Go To Login Page And Check It Is Open 
    Go To Login Page
    Login Page Should Be Open