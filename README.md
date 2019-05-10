# Language-Logic Toolkit (LLTK)
LMU Spring 2018 Senior Project

This project is an exploration into the compatibility between language and computation. The goal of the Language-Logic application is to create an application where, when given a sentence can identify prepositional phrases and breakdown its structure in order to output the symbolic logic of the statement. Currently, this program will ony be prepared to tackle simple conditional argument structure.

**Requirements:**
1. Python 2.7, 3.4, or 3.5
2. NLTK (Natural Language ToolKit)
 * Mac/Unix: `sudo pip3 install -U nltk`
 * Windows: [http://pypi.python.org/pypi/nltk](http://pypi.python.org/pypi/nltk)
3. NumPy
 * Mac/Unix: `sudo pip3 install -U numpy`
 * Windows: [http://sourceforge.net/projects/numpy/files/NumPy/](http://sourceforge.net/projects/numpy/files/NumPy/)

[More Information on installing NLTK+Numpy](https://www.nltk.org/install.html)
 
**Documentation**

```$ python3 lltk.py [-options] [sentence]```

```
options:
 	-r	Repeat Input
	-s	Isolate Subject
	-c	Show Conditional Type
	-d	Demo
 ```
```sentence```: Can only be recognized if it includes some sort of if-then or if-and-only-if conditional statement. ex. If I have the time to study then I will get an A.

**Citations:**

Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.
