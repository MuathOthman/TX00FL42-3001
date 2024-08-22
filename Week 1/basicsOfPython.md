# 🐍 Lecture 1: Introduction to Python Programming 📐

## What is Python? 🤔

Python is a powerful, easy-to-learn programming language that’s used by professionals across a wide range of industries—from web development and data science to automation and engineering. Its simplicity and versatility make it the perfect tool for beginners and experts alike. Whether you're looking to automate repetitive tasks, analyze data, or develop complex applications, Python has got you covered! 💻

## Why Python? 🎯

Here’s why Python is an excellent choice, especially in the field of civil engineering:

### 1. **Easy to Learn and Use** 🧑‍🎓
Python’s clean and straightforward syntax means you can focus on solving problems without getting bogged down by complex code. This makes it a great starting point for anyone new to programming, especially when you’re more interested in solving engineering challenges than writing intricate code.

### 2. **Vast Libraries and Tools** 📚
Python has a rich ecosystem of libraries that can help you with everything from numerical analysis (using **NumPy** and **SciPy**) to data visualization (with **Matplotlib** and **Plotly**). This means you don’t have to reinvent the wheel—you can leverage existing tools to get your work done faster and more efficiently.

### 3. **Automation and Efficiency** ⚙️
In civil engineering, repetitive tasks like data entry, calculations, and report generation can eat up a lot of your time. Python allows you to automate these tasks, freeing up your time for more critical thinking and problem-solving. Imagine writing a script that automatically calculates and logs the load-bearing capacity of various structures—sounds like a time-saver, right? ⏱️

### 4. **Data Analysis and Visualization** 📊
Civil engineers deal with massive amounts of data, whether it’s soil analysis, traffic patterns, or material properties. Python can help you organize, analyze, and visualize this data effectively. You can create graphs, charts, and even 3D models to better understand and present your findings.

### 5. **Interoperability** 🔄
Python can easily integrate with other software and systems you might already be using in your civil engineering projects, such as AutoCAD or BIM tools. This means you can enhance your existing workflows with the power of Python without starting from scratch.

---
# How to Get Started with Python 🚀

Ready to start your Python journey? Here’s what you need to do:
First, we install the Python interpreter. The Python interpreter is a program that translates the Python language
statements in a program one at a time into instructions
accepted by the computer's central processing unit (CPU).

The installation of the Python interpreter proceeds as follows:

1. Navigate to https://www.python.org/downloads/ with your browser.
2. Select **Downloads / All releases**.
3. Scroll to the section titled **Looking for a specific release?**.
   Click Download for the version of your choice (any version between 3.7.X and 3.9.X should do). The minor revision number
   X can be any number.
4. Download the Python interpreter by clicking the link *Windows installer (64-bit)* at the bottom of the page.
   The wizard will guide you in the installation process. It is recommended to use the default folder for the installation.

**Important:** The guided installation process provides the opportunity to add
the Python interpreter to the `PATH` environment variable in the Windows operating
system. This environment variable contains a list of directories that the operating
system automatically searches for executable programs. Adding Python to the `PATH`
is recommended because it allows you to use the `python` command from any directory
in the command prompt, and the Python interpreter will be found automatically.
(This is beneficial for the upcoming Hardware 1 and 2 courses, where Python is also used.)

The following image shows the checkbox from which the addition is made:

![Updating the PATH environmental variable](../img/path_envvar.png)

## Installation of the IDE

Next, we install the development environment (IDE), which is short for *Integrated Development Environment*.
IDEs are professional software tools used for writing, executing, and testing program code.

On this course we are using the JetBrains PyCharm IDE. Please follow these instructions to install PyCharm:
1. Navigate to https://www.jetbrains.com/
2. Select **Developer tools / PyCharm** ja click **Download**.
3. Select the Professional version to download.
4. To use PyCharm, you must create a JetBrains account with your Metropolia email to acquire a free student license. The student license is active for one year at a time. The installation tool helps you register your account. To acquire the software license, click the shopping cart icon at the top of the JetBrains website and select **Special offers / For students and teachers**. **Remember to use your Metropolia email**, and complete the registration by following the instructions in the activation email. When your license is about to expire after the first year, you will automatically receive instructions to your email on how to renew your license.

Once your installation is finished, you can open PyCharm by clicking at the PyCharm icon on your computer.

## Creating a new project and a Python source file

Before you can start writing programs, you must create a new project. A project is a bit like a suitcase where you can store
programs focused on the same topic. For example, you can create a new project called 'Learning Python' for your first Python programs.
The name of the project is written at the end of the file path.

![Creating a new project](../img/new_project.png)

By default, a new project is created under a virtual environment (venv). Virtual environments help the management and version control of software packages required by programs.

When you select **Create**, the IDE prompts you whether you want to open the new project in a new window. You can select either option.

A project tree opens on the left side of the screen, showing you all the files that belong to the project.

![Project tree](../img/project_tree.png)

Each program is written in a file under the project's directory. For the first program, you can create a new file by right-clicking the project name under the project tree.
Then select **New / Python file** and write the name for the new file in the popup window. You can name the first file `hello`. A new file with the name `hello.py` is now
seen is the project tree. File extension `.py` is characteristic of Python program files.

## Writing, saving and running a program

A program, or Python source code, is written in the editor field:

![First program](../img/first_program.png)

You can execute, or run, a program by right-clicking the editor field and selecting **Run 'hello'**.

Output will be shown in the console window at the bottom of the screen.

```python
Hello, world!
```

If there are errors in your program, don't worry! You will get an error message that helps you find the source for the error.
You can edit the program as many times as you need and run it over and over again.

Making errors is part of programming. It has been estimated that 80% of the work time of a professional programmer is used
for troubleshooting and fixing errors. Making errors also helps you learn. Every time you run into an error, find it, and fix it,
you have become a bit better at programming.
