# Python Programming Essentials - Control Structures

## Outline
- If/else/elif
- For Loops
- While Loops
- More on Iterables

## If/else/elif

There are times in our program that we want some certain behavior based on some defined conditions. Suppose we want to customize a response based on the age entered by the user, then we will use the `if/else` statement to do this:

```python
age = input("What is your age?")
# customize responce based on value of age
if age > 18:
    print("Wow, you are older than I expected. Awesome!")
else:
    print("Wow, you are younger than I expected, Fabulous!")
```

Notice that the block of code that is execute in each `if` statement is indented. This is very important as only codes indented under the statement is considered under that condition. If no block of code is indented under the `if` statement, an error will occur because this is the expected syntax by python language. We can also have a standalone `if` statement.

```python
# do some
```

## For Loops

## While Loops

## More on Iterables

- How to use iterables
- Functions to manipulate iterables
- Pros and cons of each class

## Useful Resources and Bibliography

1. https://www.pythonlikeyoumeanit.com/index.html
2. John M. Zelle, Python Programming: An Introduction to Computer Science. Franklin, Beedle & Associates, Inc., 2004
