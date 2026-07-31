# Day 011 - Concept Check

## Question 1
What is an exception?
**Answer:**
An exception is an error or unexpected event that occurs while a program is running.
---

## Question 2
Why is exception handling important?
**Answer:**
It does not make sense for a code to crash just because one error that can easily be handled 
---

## Question 3
What does try do?
**Answer:**
 This is the code block where you run risky codes
---

## Question 4
What does except do?
**Answer:**
except catches and handles an exception raised in the try block.
---

## Question 5
What does finally do?

**Answer:**
This runs the code regardless of whether an error happens or not
---

## Question 6
When would a ValueError occur?
**Answer:**
This occurs when a function receives an argument that is different from what it is expecting. Mainly difference in data type



## Question 7
When would a ZeroDivisionError occur?
**Answer:**
Triggers when you attempt to divide a number by zero

## Question 8
Why is using except ValueError: better than just except:?
**Answer:**
except ValueError helps focus more on the argument being received making sure it triggers if there is different datatype being passed

## Question 9
What does raise do?
**Answer:**
raise is used to intentionally trigger an error