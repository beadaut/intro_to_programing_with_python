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

Notice that the block of code that is execute in each `if` statement is indented. This is very important as only codes indented under the statement is considered under that condition. If no block of code is indented under the `if` statement, an error will occur because this is the expected syntax by python programmin language. We can also have a standalone `if` statement.

```python
# do some computation
...
# this part only executes if the condition is satisfied
if answer < 0:
    answer = 0

# the program continues running
...
```

We can also specify multiple conditions that the we want to satisfy. This is done by adding the `elif` keyword at every new condition. A typical example is giving student grades based on the scores. Also note the use of boolean operations and the combination of multiple comparisons using the `and` keyword.

```python
# get the score
score = input("Enter a score")

if score < 50:
    print("Your grade is D")
elif score >= 50 and score < 60:
    print("Your grade is C")
elif score >= 60 and score < 70:
    print("Your grade is B")
else: # the final condition can be specified implicitly. That is, score >= 70
    print("Your grade is A")
```

Basically, the interpreter goes through every condition one after the other and once a condition is satisfied, it leaves the control structure and continues running the rest of the program. If none of the conditions are satisfied, it runs the final `else` statement. We may also have a multiple condition control structure that does not use the else statement, hence nothing is done if no condition is satisfied.

## For Loops

## While Loops

## More on Iterables

- How to use iterables
- Functions to manipulate iterables
- Pros and cons of each class

## Useful Resources and Bibliography

1. https://www.pythonlikeyoumeanit.com/index.html
2. John M. Zelle, Python Programming: An Introduction to Computer Science. Franklin, Beedle & Associates, Inc., 2004
