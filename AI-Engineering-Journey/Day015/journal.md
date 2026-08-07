How does inheritance reduce duplicate code in software projects?
Ans: Inheritance reduces duplicate code by acting as a central repository for shared attributes and behaviors. Instead of rewriting the same variables and functions across multiple classes, you write them once in a parent class and automatically pass them down to any child classes.


Interview

1) Explain inheritance to someone who has never programmed before.

Think of inheritance like a blueprinting shortcut. Instead of building blueprints for a Truck from scratch, you build a master blueprint called Vehicle with wheels and an engine. The Truck inherit those features automatically, so you only have to write code for what makes them unique (like a truck's cargo bed).


2) What is the difference between overriding a method and adding a new one?

Overriding a Method (Rewriting): The parent already does an action, but the child changes how it is done.
Example: A generic Animal makes a sound. A Dog overrides this to specifically bark.
While 
Adding a Method (Extending): The child learns a brand-new action that the parent cannot do.
Example: A Dog adds a new unique action called wag_tail().

3) Why is super() considered a best practice?
 When a child overrides a parent's method, super() allows the child to reuse the parent's original work instead of throwing it away.
 It is best practice because it prevents code duplication (no copy-pasting parent logic), ensures safety (runs critical background setup from the parent), and handles complex class structures automatically without breaking.   