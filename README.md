# Task 4 - Infinite Loop Detection

## Objective
To develop a Python-based educational tool
that analyzes loops in Python programs.

## Features
- Detects while loops
- Identifies while True patterns
- Identifies conditional loops
- Detects for loops
- Displays line numbers
- Includes Turing Machine simulation
- Includes unit testing

## Technologies
- Python
- Abstract Syntax Tree (AST)
- Unittest
- VS Code

## Execution

Run the project:

python main.py

Run tests:

python -m unittest discover -s tests -v

## Limitation
The tool uses static pattern analysis.
It cannot decide whether every arbitrary
program will terminate. This is related
to the undecidability of the Halting Problem.