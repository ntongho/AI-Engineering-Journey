Parent vs. Child ClassesParent Class: The original, generic class (e.g., Vehicle) that defines standard properties and behaviors.Child Class: The specific, modified class (e.g., Car) that automatically inherits everything from the parent and adds its own unique features.

Method Overriding:
Method overriding happens when a child class replaces a parent's method with its own version. The child keeps the exact same method name but changes the internal code to perform a task specific to its needs.

super():
super() is a command that lets a child class call and execute methods from its parent class. It allows the child to reuse the parent's established logic while still adding its own custom steps.

Advantages of Inheritance
Code Reusability: You write code once and use it many times.
Time Savings: Developing new features requires less writing and testing.
Easier Maintenance: Fixes made to a parent class automatically update all child classes.
Logical Structure: It mirrors real-world hierarchies, making code easier for humans to understand.