*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ville  vii5vee3
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  vii5vee3
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    input Credentials  vk  kal5lee3
    Output Should Contain  Username is invalid

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kal3le  vii5vee3
    Output Should Contain  Username is invalid
Register With Valid Username And Too Short Password
    Input Credentials  ville  vii5vee
    Output Should Contain  Password is invalid
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  ville  viisvees
    Output Should Contain  Password is invalid

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command