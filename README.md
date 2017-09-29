# Mini Python course

Dear "Big Questions in Data" student, 

Welcome to this mini Python course. In this course we'll take a small dive into the Python programming language. We'll cover some **basic programming concepts** and briefly delve into **data acquisition** by using API's.

From previous iterations we've distilled that learning the basics isn't the challenge (anymore) due to the abundance of open online courses and interactive online tutorials. **Rather, the question is: how do I craft useful scripts that solve real-world problems?** 

Hence, we'll show you how to **apply your knowledge** to the challenges you'd like to **address day-to-day activities**. Along the way, we'll show you how to solve common Python-related problems, give you tips-and-tricks about finding help and expanding Python's capabilities with external modules.

This course is extremely hands-on: **we don't have slides or extensive lecture notes; we'll only show and execute Python code**. We think we can get away with this approach only because you'll have done the bulk of the learning by the time you join us on Tuesday class. 

Curious? Read on!

## Course overview

- Introduction to Python
- Introduction to debugging
- Getting help: introduction to StackOverflow and online documentation 
- Introduction to API access using the requests module
- Accessing the twitter API using the tweepy module

## Methodology and programme

This course consists of a self-learning part and two hands-on workshops. a short interactive lecture are planned for the mornings while the afternoons are filled with supervised practical assignments.

The program is as follows:
 - self-study: [Python course on Codeacademy](https://www.codecademy.com/learn/python)
 - workshop I:
   - interactive recap of Codeacademy material, introduction to API's and requests
   - practical assignment - using the Amsterdam API, with the requests module
 - workshop II: 
   - recap of workshop I, introduction to Twitter API and tweepy
   - practical assignment - using the Twitter API, with the tweepy module

Each interactive session + practical assignment pair is accompanied by a short manual and some Python scripts, see the [lecture materials](https://github.com/clucas111/gi-minor-python-course#lecture-materials) section below for more information. 

## Self-study: codeacademy.com

To maximize the time available for the hands-on lectures and exercises we kindly ask you to complete a number of Codeacademy Python lessons in advance.
 
 [codeacademy.com](codeacademy.com) is an online learning platform that offers programming courses in a wide range of languages. You learn to program by typing and executing Python commands directly in your browser.
 
 Register for Codeacademy as follows:

1. go to [https://www.codecademy.com/](https://www.codeacademy.com) and register
2. log in and navigate to the [Python course](https://www.codecademy.com/learn/python)
3. click `Start`

Please complete the following exercises before coming to class on the 19th of September. 

- Unit 1 - [Lesson: Python Syntax](https://www.codecademy.com/courses/introduction-to-python-6WeG3/0/1)
- Unit 2 - Lesson: Strings & Console Output
- Unit 3 - Lesson: Conditionals & Control Flow
- Unit 4 - Lesson: Functions
- Unit 5 - Lesson: Python Lists and Dictionaries
- Unit 7 - Lesson: List and functions
- Unit 8 - Lesson: Loops
- (optional) Unit 10 - Lesson: Advanced Topics in Python
- Unit 12 - Lesson: File Input and Output

Practice makes perfect: feel free to complete any of the other lessons and or exercises after you've gone through this list.

## Lecture materials

The lecture notes are split in three chapters. Each chapter contains a short manual and one or more Python scripts. 

- [Chapter 1 - recap](https://github.com/clucas111/gi-minor-python-course/tree/master/1_recap) - recap of the Codeacademy material you studied by yourself.
- [Chapter 2 - Amsterdam API](https://github.com/clucas111/gi-minor-python-course/tree/master/2_AmsterdamAPI) - describes the Amsterdam API assignment + hints/tips/tricks about using an API.
- [Chapter 3 - Twitter API](https://github.com/clucas111/gi-minor-python-course/tree/master/3_TwitterAPI) - describes the Twitter API assignment + hints/tips/tricks about using the Twitter API.

You can download the accompanying Python scripts as follows:

1. scroll to the top of this page
2. click on the green button labelled `Clone or download`
3. click on `Download ZIP`
4. Unzip the file you downloaded and load the `.py` scripts contained in one of the folders in your favourite editor.

## Installing Python (Windows)

You'll need to install Python and a number of external modules on your machine to run the example scripts and perform the exercises. To make it easier we will use a python distribution that already comes with a large number of modules that are useful for scientific computing, called Anaconda. We will use the 2.7 version, since it has better library support and it is the version used by GIS packages like ArcGIS and QGIS. Anaconda also comes with a module manager called Conda, which we will use to install a few modules.

You can install Anaconda and the needed modules as follows: 

- Download and install Anaconda (Python 2.7 version) -> [Download Anaconda](https://www.anaconda.com/download/) and double click it. You can accept the default choices.

- Update Spyder: open a Anaconda prompt (`Start Menu` -> `Anaconda` -> `Anaconda Prompt`) and enter the following commands:

    `conda update qt pyqt`
    
    press `Enter` to execute it.

    `conda update spyder`
    
    press `Enter` to execute it.
    
- Install the `fiona` module: open a Anaconda prompt (`Start Menu` -> `Anaconda` -> `Anaconda Prompt`) and enter the following command:

    `conda install -c conda-forge fiona`

    press `Enter` to execute it.

- Install the `tweepy` module: open a Anaconda prompt (`Start Menu` -> `Anaconda` -> `Anaconda Prompt`) and enter the following command:

    `conda install -c conda-forge tweepy`

    press `Enter` to execute it.

- If you ever want to install other modules just Google `conda *module name*` and look for the result (with `Anaconda Cloud` in the title) with the latest version available for your platform. Copy the text under `To install this package with conda run one of the following:` and enter this command in the Anaconda prompt.

Test if everything works: 
- start the Python editor `Spyder` (`Start Menu` -> `Anaconda` -> `Spyder`)
- copy/paste the following code into the newly opened editor

```python
import fiona
import tweepy

print 'Everything works!'
```
- save the file: `File` -> `Save`
- run the code: `Run` -> `Run`
- do you see `Everything works!` in the ouput screen? Great, you're all set!
- do you see something else? Too bad, something's wrong. Please copy/paste the output in the issue tracker (see below for instructions) and we'll try to assist you.

## Getting help

Please use the [issue tracker](https://github.com/clucas111/gi-minor-python-course/issues) to post questions about the lecture notes, examples, exercises and Python in general or in case you're having difficulties installing Python. 

1. scroll to the top of this page and click on `Issues`
2. click on the green button labelled `New issue`
3. enter a descriptive `Title` and a describe your issue/question in the `Comment` textbox.
 
*Note*: you need a GitHub account to post an issue.
 
We encourage you to use the issue tracker as it 

- the act of verbalizing your problem often times leads you to a solution
- is a nice collaborative learning mechanism: seeing other people's questions is a sure way to learn something new and unexpected
- saves you a lot of time in case someone else has posted your question already
- saves us a lot of time since we don't have to answer each question separately (through mail)
 
 Not convinced? Feel free to send us an email. 

## The team

- Eduardo Dias
- Simeon Nedkov
- Brian de Vogel
- Mark Opmeer
- Chris Lucas
