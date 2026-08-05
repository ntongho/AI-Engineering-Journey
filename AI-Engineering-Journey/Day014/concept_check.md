# Day 014 - Concept Check

## Question 1
What is an instance method?
**Answer:**
 A function defined inside a class that operates on a specific object instance and automatically takes self as its first parameter.
---

## Question 2
What is a class variable?
**Answer:**
A variable defined directly inside a class that is shared by all instances of that class.
---

## Question 3
What is the difference between a class variable and an instance variable?
**Answer:**
Class variables are shared across all objects of a class, while instance variables are unique to each specific object.
---

## Question 4
What is a class method?
---
A method bound to the class itself rather than its objects, marked with @classmethod and taking cls as its first parameter.


## Question 5
What does cls represent?

**Answer:**
The class object itself, passed automatically to class methods so you can access or modify class-level attributes.
---

## Question 6
What is a static method?
**Answer:**

Answer: A regular function placed inside a class using @staticmethod that does not access or modify class or instance data.

## Question 7
When would you use a static method?
**Answer:**
When you need a utility or helper function that logically belongs inside a class but does not need to access or modify any class or instance data.

## Question 8
What is encapsulation?
**Answer:**
The practice of bundling data and methods into a single unit (a class) while restricting direct outside access to the internal data.
 

## Question 9
Why do programmers use private attributes?
**Answer:**
To protect internal object data from accidental modification and to hide complex implementation details from the outside user.