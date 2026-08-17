1. What is an iterator?
    An iterator is an object that lets you go through a collection of items one at a time using a state to remember where it is.

2. What does next() do?
The next() function tells an iterator to give you the very next item in its list.

3. What is a generator?
    A generator is a special kind of function that creates an iterator easily using the yield keyword.

4. What is the difference between return and yield?
    return sends back a value and ends the function completely, while yield pauses the function, sends back a value, and lets the function wake up later to continue.

5. Why can generators be useful when processing large datasets?
    Generators handle large datasets well because they create and load only one item into memory at a time instead of storing the whole list

6. What does "lazy" mean in the context of generators?
    "Lazy" means a generator waits to do work or create data until you actually ask for it.
7. What is the relationship between a generator and an iterator?
    Every generator is automatically an iterator, because a generator builds the iterator behavior for you behind the scenes.




If I have 10 million AI training records, why might I prefer a generator over creating a list containing all 10 million records?
Ans:
    You prefer a generator because a list loads all 10 million training records into RAM at once, which can crash your system with an out-of-memory error. A generator uses lazy evaluation, yielding one record at a time on the fly, saving massive amounts of memory