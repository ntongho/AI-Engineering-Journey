# Day 017 - Concept Check

## Question 1
What is abstraction?
**Answer:**
Simply means Hiding complex internal implementation details and exposing only a simple, essential interface to the user.

## Question 2
Why is abstraction useful?
**Answer:**
It reduces mental complexity for developers, isolates code changes to prevent ripple effects, and enforces consistent software design.


## Question 3
What is an abstract class?
**Answer:**
A restricted, incomplete code template that cannot be made into an object directly; it exists solely to be inherited by other classes


## Question 4
What does ABC stand for?
Abstract Base Class (the module used in Python to create and enforce abstract structures).
abc is Python's module for defining Abstract Base Classes, while ABC is a base class provided by that module.

## Question 5
What does @abstractmethod do?
**Answer:**
It marks a function as a mandatory placeholder inside an abstract class, forcing any child class to write the actual code for it or face a system crash.


## Question 6
Abstract classes vs concrete classes
**Answer:**
Abstract Class: Incomplete blueprint; cannot create objects directly; contains placeholder methods.
Concrete Class: Complete blueprint; can create objects directly; contains fully written, actionable methods

## Question 7
Abstraction vs encapsulation
**Answer:**
Abstraction: Focuses on hiding complexity (what an object does at a high level, ignoring how it does it).
Encapsulation: Focuses on hiding data and inner workings (bundling variables and methods safely inside a class to prevent outside tampering).

## Question 8
How abstraction works with inheritance
**Answer:**
Abstraction uses inheritance as its delivery system. An abstract parent class establishes the mandatory rules and structure, and child classes use inheritance to adopt those rules and flesh out the actual code.


## Question 9
How abstraction works with polymorphism
**Answer:**
Abstraction defines a uniform interface, which allows polymorphism to trigger different concrete behaviors using the exact same command (e.g., calling .make_sound() triggers a bark or a meow depending on the object hidden behind the abstract interface).

## Question 10
Real-world examples
**Answer:**
TV Remote: You press the "Power" button (abstract interface) to turn it on, without knowing the electrical circuitry or frequency modulation happening inside (hidden details).
ATM: You press "Withdraw Cash" (abstract interface) without knowing how the machine connects to bank databases, updates ledgers, and counts physical bills internally.
