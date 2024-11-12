*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Register Should Succeed
    
Register With Too Short Username And Valid Password
    Set Username  t
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  testi
    Set Password Confirmation  testi
    Submit Credentials
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
    Set Username  testi
    Set Password  testisalasana
    Set Password Confirmation  testisalasana
    Submit Credentials
    Register Should Fail With Message  Password must not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi124
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  testi123
    Set Password Confirmation  testi123
    Submit Credentials
    Register Should Fail With Message  Username already exsists

Login After Successful Registration
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Credentials
    Navigate To Main Page
    Logout
    Set Username  pekka
    Set Password  pekka123
    Submit Credentials For Login
    Login Should Succeed

Login After Failed Registration
    Set Username  pekka
    Set Password  pekka
    Set Password Confirmation  pekka
    Submit Credentials
    Register Should Fail With Message  Password is too short
    Navigate To Login Page
    Set Username  pekka
    Set Password  pekka
    Submit Credentials For Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Navigate To Main Page
    Click Link  Continue to main page

Logout 
    Click Button  Logout

Navigate To Login Page
    Click Link  Login

Submit Credentials For Login
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
