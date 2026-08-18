# Day 019 - Concept Check

## Question 1

What is a list comprehension?

**Answer:**
A concise, one-line syntax in Python used to create a new list by iterating over an existing iterable.

---

## Question 2

What is the basic structure of a list comprehension?

**Answer:**
[expression for item in iterable] (Optionally followed by an if condition: [expression for item in iterable if condition]).

---

## Question 3

What is a dictionary comprehension?

**Answer:**
A concise syntax to create a new dictionary from an iterable, structured as {key_expression: value_expression for item in iterable}.

---

## Question 4

What is a set comprehension?

**Answer:**

 A concise syntax to create a new set (automatically removing duplicates), structured as {expression for item in iterable}.
---

## Question 5

What does `map()` do?

**Answer:**
It applies a specified function to every item in an iterable and returns an iterator yielding the results.

---

## Question 6

What does `filter()` do?

**Answer:**
It tests every element in an iterable with a function (which returns True or False) and returns an iterator containing only the items that returned True.

---

## Question 7

What is a lambda function?

**Answer:**
A small, anonymous, single-expression function defined without a name using the lambda keyword.

---

## Question 8

What is the difference between `map()` and `filter()`?

**Answer:**

map() changes the value of every item in the collection, while filter() changes the number of items by selecting a subset based on a condition.
---

## Question 9

Why do we use `list()` with `map()` and `filter()` in many examples?

**Answer:**
Both map() and filter() return lazy iterators to save memory; wrapping them in list() forces evaluation and converts the result into a viewable list.

---

## Question 10

Which would you prefer for simple transformations: a list comprehension or `map()`? Why?

**Answer:**

 A list comprehension. It is widely considered more "Pythonic," easier to read, and faster because it avoids the overhead of function calls (especially when paired with lambda)

---

## Question 11

What happens when a condition in a list comprehension is false?

**Answer:**

The current item is skipped entirely and is not included in the final list.

---

## Question 12

Give a real-world example of where filtering data would be useful in an AI system.

**Answer:**
Removing low-confidence object detections (e.g., bounding boxes with a confidence score under 70%) from a computer vision camera stream before passing the data to an autonomous driving system.