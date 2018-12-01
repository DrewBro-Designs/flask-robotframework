*** Settings ***  
Library  Selenium2Library

*** Variables ***
${SEARCH_ENGINE}  https://www.google.com/
${BROWSER}  chrome
${SEARCH_TERM}  robot framework

*** Test Cases ***
Search on google
    Open Browser  ${SEARCH_ENGINE}  ${BROWSER}
    Input Text  xpath://*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input  ${SEARCH_TERM}
    Submit Form
    Click Link  xpath://*[@id="rso"]/div[1]/div/div[1]/div/div/div[1]/a
    Delete All Cookies
    Close Browser

New test Case
    Open Browser  ${SEARCH_ENGINE}  ${BROWSER}
    Input Text  xpath://*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input  HAHAHAHAHAHAA
    Submit Form
    Click Link  xpath://*[@id="rso"]/div[3]/div/div[1]/div/div/div[1]/a[1]
    Delete All Cookies
    Close Browser