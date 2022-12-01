**<u>Languages, libraries and tools we used</u>**

- Python3
- pip
- Requests
- JsonPath
- Pytest
- Pycharm

**<u>Setup and installation</u>**

First need to install python3. If python isn't already installed, then go to [python.org](python.org) and download the latest version of python for your OS and run the installer.
Or alternative on mac and have homebrew already installed then you can install python using below command

```
brew install python
```
Let’s test to make sure python is installed and available from the command line

```
python3 --version
```
**<u>Install requests</u>**
Use the command below to install any Python module using Pip. But before that need to install 'pip'. PIP is the package management tool for Python libraries. If we’re using Python on your Mac to create applications, you’ll want to install PIP to easily install and use these libraries and software packages.

Using the Ensurepip Method to Install PIP on Mac for Python 3
If you’re using Python 3.4 or later, you can use the ensurepip command. This is the official method for installing PIP in Python, providing a secure method to install the application (if required).

**<u>To use the get-pip script to install PIP on Mac::</u>**

1. Open the Terminal app via the Launchpad.
2. In the Terminal, type 

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py 
```
and press Enter.
3. Allow curl time to download the script onto Mac.
Once it’s done, type 

```
python3 get-pip.py 
```
and press Enter. Allow time for the installation to complete.

**<u>To check your PIP version on a Mac:</u>**
1. Open the Terminal app.
2. In the Terminal, type 


```
pip –version
```

and it doesn't show the Version, just do

```
pip3 -version
```
and press Enter.

**<u>Install requests</u>**
To install any python module using pip3 you can use below command

```
python3 -m pip install requests 
```
Install requests which we would use to actually make HTTP requests.

We need one more module called jsonpath is installed by executing below.


```
pip3 install jsonpath
```

We can always check the package is installed by executing below.

```
pip3 freeze 
```
Will also use pytest as the test framework of choice.

```
pip3 install pytest 
```

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gm7lxcpqdgjhtjzgntx4.png)



**<u>REST API Testing In Python</u>**
Download [Pycharm](https://www.jetbrains.com/pycharm/)PyCharm Professional Edition. Install Pycharm Open New project.


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/dth223on04fmdxydxmjm.png)

GO to Preference > Python Interpreter and install requests and jsonpath package.

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/pvi5en81hr0v3yvl2ftv.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tfdqwo4e3md33sqnmvx3.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ta2w57wxtp8hlqngkj3e.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/6so3ifk77jka9zppo8v1.png)

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8a8eb06b2hnzqc5e427c.png)



**<u>Create Package</u>**

First create a python package named "api_test". Then create Python File named "get_user"


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/zeiextcd7d5jj1syekkr.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z5y1vdt0wbzvqina55e3.png)


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/kevrwgevo8tk8z16gyqk.png)



To build a Python REST API test suite, you will need to install Python3 first, and below packages (using pytest test framework in this example).

```
pip3 install -U requests Flask pytest pytest-html
```
 
![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/l5ufmby8g7wqajtr7kw6.png)

**<u>Generate Report using Allure</u>**


```
python3 -c "import nltk; nltk.download('all')"
```

```
pytest --alluredir=allure_reports
```

```
allure serve allure_reports
```

**<u>Generate Report using Pytest</u>**

```
pytest
```

```
pytest -rA
```

```
pip3 install pytest-html
```

```
pytest --html=Report/REPORT.html
```
