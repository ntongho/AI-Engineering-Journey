Exceptions:
This helps handle error 

try:
This is the code block where you run risky codes

except:
This checks the risky code and points out any error the try block encounters

finally:
This runs the code regardless of whether an error happens or not

Raising Exceptions:
This involves  intentionally triggering an error in a program

What is the difference between a bug and an exception?
Bug: A flaw created by the programmer. The code runs without crashing, but it produces the wrong results.
Exception: An unexpected condition that occurs while the program is running, often caused by external factors. The logic may be perfect, but an outside resource failed.

Why should you avoid using a bare except: in most programs?
it hides typo, traps system exit command and makes debugging impossible 

Give a real-world example where exception handling improves the user experience.
Imagine you are checking your bank balance from an ATM machine with your card and they happen to be loss in connection between the machine and the bank database, the atm is not suppose to completely crash.