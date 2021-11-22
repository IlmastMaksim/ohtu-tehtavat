*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input New Command

Register With Already Taken Username And Valid Password
    Run Keyword and Expect Error  User with username kissa already exists  Create User  kissa  kalle123123

Register With Too Short Username And Valid Password
    Run Keyword and Expect Error  UserInputError: Invalid username  Create User  k  kalle123

Register With Valid Username And Too Short Password
    Run Keyword and Expect Error  UserInputError: Invalid password  Create User  kassa  mk123

Register With Valid Username And Long Enough Password Containing Only Letters
    Run Keyword and Expect Error  UserInputError: Invalid password  Create User  kassa  jndsfkndskfjdsjfn

*** Keywords ***
Input New Command And Create User
    Input   new
    Create User  kissa  kalle123
