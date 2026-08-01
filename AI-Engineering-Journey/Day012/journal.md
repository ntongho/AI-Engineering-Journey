How do modules make large software projects easier to build and maintain?
Easier navigation: Finding a bug in a 100-line file takes seconds; finding it in a 10,000-line file is a nightmare.
Team collaboration: Multiple developers can work on different files at the same time without code conflicts.
No variable clashes: Functions in different modules can share the same name without breaking each other.
Better performance: Python only loads the specific code your program needs at that moment.


Modules make large software projects manageable by breaking massive codebases into smaller, isolated pieces. 
Module: A single Python file (e.g., calculator.py).
Package: A folder containing multiple modules grouped together (e.g., a math_tools/ directory).



1. Why is splitting code into modules better than writing everything in one file?

    Modules make large software projects manageable by breaking massive codebases into smaller, isolated pieces. 

2. What is the difference between a module and a package?

    Module: A single Python file (e.g., calculator.py).

    Package: A folder containing multiple modules grouped together (e.g., a math_tools/ directory).

    This isolation prevents code conflicts and simplifies troubleshooting

3. Why is the if __name__ == "__main__": pattern important?

    Prevents accidental execution: It stops test code or script logic from running automatically when another file imports your module.

    Enables dual-purpose files: It allows a file to act as a reusable library in one project and a standalone, runnable script in another.