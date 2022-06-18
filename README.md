## Introduction

This is a Python based app to extract images from set of URLs in a text file and save images in the specified folder

## Prerequisites
Python v3.6.8 and higher
Libraries:  
urllib3 (>=1.26.9)  

### Test Environment 
Has the same prerequistes

## Folder Structure (Overview)
    |-----test/  ~ test scripts for the app
    |-----images/  ~ default folder in which the extracted images are saved
    |-----app.log ~ log file for the application 
    |-----main.py ~ the file to be executed 
    |-----urls.txt ~ the default file contianing the urls

## Usage

Download the app and navigate to the <em>main.py</em> file. Execute the command:
```
python main.py
```
To choose a new text file for the URLs change the contents of the variable
<em>src_file_path</em> in line 119 to the new file location in the <em>main.py</em> file.  
Similarly to change the folder to save the retrieved images modify the 
<em>save_file_path</em> in line 120 to the new folder location in the <em>main.py</em> file.