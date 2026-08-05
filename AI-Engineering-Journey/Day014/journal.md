How does encapsulation help make software safer and easier to maintain?
Ans:Encapsulation makes software safer and easier to maintain by creating clear boundaries between how an object works inside and how other parts of the program interact with it.
For example:
A BankAccount object should not allow another part of the program to change the balance directly. Instead, it should require the deposit() and withdraw() methods.

Interview:

Answer these after completing today's work:

1) What is the difference between an instance method, a class method, and a static method?
Instance Method (self): The standard method. It takes self as the first argument, giving it full access to a specific object's unique data and attributes.

Class Method (cls): Marked with @classmethod. It takes cls as the first argument, giving it access to class-level data shared by all objects, but it cannot see individual object data.

Static Method: Marked with @staticmethod. It takes no special first argument (self or cls). It behaves exactly like a regular function, but is nested inside the class purely for organization because it relates to the class's theme.




2) Why would you use a class variable instead of an instance variable?
You use a class variable when data needs to be shared universally across every single object created from that class, rather than unique to each one.


3) What problem does encapsulation solve?
Encapsulation solves The Chaos of Uncontrolled Access.Without encapsulation, any random piece of code in a massive project can reach deep into an object, change its internal variables directly, and accidentally break its logic