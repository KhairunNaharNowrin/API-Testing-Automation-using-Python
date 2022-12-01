#!/bin/bash

# using pytest and generate report

#But first install Pytest-HTML by writing the following command on Terminal
#pip3 install pytest-html


cd ApiTesting


#To run a test, you can simply write the following command on Terminal:\
pytest

#To run and get details of all the executed test, you can simply write the following command on Terminal:
pytest -rA



#Then write the following command on Terminal
pytest --html=Result/Test_Result.html


#run shell file
#sh script/run.sh