# Python - Almost a circle
---
## Background Context
In this project, you will review everything about Python:

* Import
* Exceptions
* Class
* Private attribute
* Getter/Setter
* Class method
* Static method
* Inheritance
* Unittest
* Read/Write file

You will also learn about:

* <span style="color:red">args</span> and <span style="color:red">kwargs</span>

* Serialization/Deserialization
* JSON

## Step by step


* Write the first class Base
* Write the class Rectangle that inherits from Base
* Update the class Rectangle by adding validation of all setter methods and instantiation (id excluded)
* Update the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance
* Update the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y here
* Update the class Rectangle by overriding the str method so that it returns [Rectangle] instance
* Update the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
* Update the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute
* Update the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, kwargs) that assigns a key/value argument to attributes
* Write the class Square that inherits from Rectangle
* Update the class Square by adding the public getter and setter size
* Update the class Square by adding the public method def update(self, *args, kwargs) that assigns attributes
* Update the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
* Update the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square
* Update the class Base by adding the class method def savetofile(cls, listobjs): that writes the JSON string representation of listobjs to a file
* Update the class Base by adding the static method def fromjsonstring(jsonstring): that returns the list of the JSON string representation jsonstring
* Update the class Base by adding the class method def create(cls, dictionary): that returns an instance with all attributes already set
* Update the class Base by adding the class method def loadfromfile(cls): that returns a list of instances

[README.md by https://github.com/PereDeMacron]: #

## Resources
##### Read or watch:
[args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
[JSON encoder and decoder](https://docs.python.org/3/library/json.html)
[unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
[Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Learning Objectives
At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

#### General

* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* What is <span style="color:red">*args</span> and how to use it
* What is <span style="color:red">**kwargs</span> and how to use it
* How to handle named arguments in a function

## Requirements
#### Python Scripts

* Allowed editors: <span style="color:red">vi</span>, <span style="color:red">vim</span>, <span style="color:red">emacs</span>
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly <span style="color:red">#!/usr/bin/python3</span>
* A <span style="color:red">README.md</span> file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using <span style="color:red">wc</span>
* All your modules should be documented: <span style="color:red">python3 -c 'print(\__import__("my_module").\__doc__)'</span>
* All your classes should be documented: <span style="color:red">python3 -c 'print(\__import__("my_module").MyClass.\__doc__)'</span>
* All your functions (inside and outside a class) should be documented: <span style="color:red">python3 -c 'print(\__import__("my_module").my_function.\__doc__)'</span> and <span style="color:red">python3 -c 'print(\__import__("my_module").MyClass.my_function.\__doc__)'</span>
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#### Python Unit Tests

* Allowed editors: <span style="color:red">vi</span>, <span style="color:red">vim</span>, <span style="color:red">emacs</span>
* All your files should end with a new line
* All your test files should be inside a folder <span style="color:red">tests</span>
* You have to use the unittest module
* All your test files should be python files (extension: <span style="color:red">.py</span>)
* All your test files and folders should start with <span style="color:red">test_</span>
* Your file organization in the tests folder should be the same as your project: ex: for <span style="color:red">models/base.py</span>, unit tests must be in: <span style="color:red">tests/test_models/test_base.py</span>
* All your tests should be executed by using this command: <span style="color:red">python3 -m unittest discover tests</span>
* You can also test file by file by using this command: <span style="color:red">python3 -m unittest tests/test_models/test_base.py</span>
* We strongly encourage you to work together on test cases so that you don’t miss any edge case
