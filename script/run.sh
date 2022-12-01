#!/bin/bash


# using Allure and generate report

cd ApiTesting

#run positive test case
pytest -m positive


#run negative test case
pytest -m negative

#create Allure test report
pytest --alluredir=allure_reports

#Show generated report in browser:
allure serve allure_reports



