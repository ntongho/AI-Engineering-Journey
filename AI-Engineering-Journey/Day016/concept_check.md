# Day 016 - Concept Check

## Question 1
What is polymorphism?
**Answer:**
Polymorphism means "many forms." It allows different objects to respond to the exact same method call in their own unique way
---

## Question 2
Why is polymorphism useful?
**Answer:**
It eliminates complex if/else checks, makes code highly reusable, and lets you add new object types without modifying existing logic.
---

## Question 3
How is polymorphism related to inheritance?
**Answer:**
In strictly-typed languages, inheritance is the mechanism used to achieve polymorphism. A child class inherits a parent's method structure but changes its behavior.
---

## Question 4
What is method overriding?
Method overriding occurs when a child class provides its own specific implementation of a method that is already defined in its parent class
---


## Question 5
What is duck typing?

**Answer:**
 A dynamic approach to polymorphism where an object's suitability is determined solely by its methods and behaviors, rather than its explicit class type or inheritance.
---

## Question 6
Why doesn't Python require interfaces like some other languages?
**Answer:**
 Python relies on Duck Typing. It checks for the existence of required methods at runtime rather than enforcing strict compile-time type contracts.

## Question 7
What happens when different objects implement the same method?
**Answer:**
They can be stored in the same collection and invoked interchangeably inside a single loop using dynamic dispatch.

## Question 8
Give a real-world example of polymorphism.
**Answer:**
An audio player running a .play() method on a list containing an MP3File, a WAVFile, and a FLACFile. Each decompresses differently, but the player triggers them all the same way.

## Question 9
Why is polymorphism important in large software systems?
**Answer:**
It creates plug-and-play architecture. Teams can build and integrate new modules seamlessly without breaking or rewiring the core codebase.