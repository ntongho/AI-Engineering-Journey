File:
A file is just a place in ones computer where information is stored

File Modes:
This are specifiers passed to the open() to determine the operation you want to execute on a file

Reading Files:
This are specifiers that helps you view the content of a file. represented as "r" e. with open("file_name","r") as file

Writing Files
This means putting a new data to a file. This overwrites the original content of the file

Append Files:
This means adding a new data to the end of an existing file without overwriting its original content e.g with open("file_name","a") as file

with open()
This is the standard and safest way to handle files. It automatically closes the file once the code block finish executing


Why can't variables replace files?
Variables only exist while a program is running. Files store data permanently, so the information is still available after the program ends.


Explain the difference between write mode and append mode.
write mode ('w') erases any existing content in the file before writing, whereas append mode ('a') preserves the existing content and adds new data to the end of the file

Why do professional Python programmers prefer with open()?
Professional Python programmers prefer with open() because it automatically closes files, prevents resource leaks, and handles errors safely without needing manual close()