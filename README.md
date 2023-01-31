# About The Project
This project is an interpreter for programming languages which is programmed and initially tested using LOLCODE. It implements the following: 
- lexical analysis
- syntax analysis
- semantic analysis

![Screenshot 2023-01-24 163207](https://user-images.githubusercontent.com/70369183/214249587-b2ded0c8-1c3a-4e0e-98a5-42015595f114.png)

### Specifications
* Once a file is selected, the contents of the file are loaded into the text editor.
* The text editor is editable, and edits done are reflected once the code is run.
* List of Tokens – This is updated every time the Execute/Run button is pressed. This contains all the lexemes detected from the code being ran, and their classification.
* Symbol Table – This is updated every time the Execute/Run button is pressed. This contains all the variables available in the program being ran, and their updated values.
* Execute/Run button – This runs the code from the text editor.
* Console – Input/Output of the program is reflected in the console.
* When a value is updated, the symbol table is also updated.

### Built With
* Python

# Getting Started
To get a local copy up and running, kindly follow these steps.

### Prerequisites
1. Python 3.x
2. Tkinter
3. Regular Expression

### Installation

1. Install Tkinter
```
pip install tkinter
```
2. Install Re (regular expression)
```
pip install re
```
3. Clone the repo
```
git clone https://github.com/r-clarissa/programming-language-interpreter.git
```
4. Find and change your terminal path where the cloned folder on your local directory is found.
5. On your terminal, run the `project.py`.

# Special Note
This is a school project where functionalities are specified by the UPLB - ICS. To prohibit any undesired academic matters, the complete source code is located on another private repository. You may email me at cgrodriguez@up.edu.ph if you have any questions given that the purpose is validated.
