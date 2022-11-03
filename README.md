# Recipes

## Description
This project showcases the different Full-Stack technologies used to display a Full-CRUD using Python, Flask, Flash, Jinja and MySQL/MySQL workbench.

Recipes that can be created and shared with others is a great way to help everyone answer the age old question of what should I eat today.

One key thing I learned in this project was ensuring that everything works before jumping to the next part, so that I don't waste time when an error appears. Addtionally, this was the first project that I submitted to Github using Git, so I have come to appreciate what all the fuss is about with Git.

## Demo
https://youtu.be/4KRd8-BHOQo

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Todo](#todo)

## Prerequisites
- [Python 3.10](https://www.python.org/downloads/) (Mac)
- [Python 3.10](https://www.python.org/downloads/windows/) (Windows)

## Installation 
1. Clone the repo
   ```
   git clone https://github.com/HonarchianMonte/Recipes-Python.git
   ```

2. Install Virtual Environment tool
   Mac:
   ```
   pip3 install pipenv
   ```
   Windows:
   ```
   pip install pipenv
   ```

3. Install Flask
   ```
   pipenv install flask
   ```
   Note: If you receive an error using pipenv, you may need to import it as a module first before it can be run as a script. You can do so using the -m flag as below. You will need to do this every time you use pipenv.
   Mac:
   ```
   python3 -m pipenv
   ```
   Windows:
   ```
   python -m pipenv
   ```

## Usage
1. Activate Virtual Environment
   ```
   pipenv shell
   ```
   Note: To deactivate the Virtual Environment, use 
   ```
   exit
   ```

2. Run the application
   After navigating to the project directory, run the following command. Make sure the Virtual Environment is running already.
   ```
   python server.py
   ```

3. Open a browser and navigate to http://localhost:5000/. 



## Todo
- Implement Bootstrap to give tables and some quick color and life to the appearance of the pages.
- Implement saving recipes functionality to allow users to favorite recipes and save them in their individual accounts.