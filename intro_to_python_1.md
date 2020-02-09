# Introduction to Programming using Python

Introduction to Programming using Python

## Outline

- Writing simple programs (introduction to elements of a python program)
  - Printing
  - Strings
  - Variables
  - Comments
  - Arithmetic Operations
  - Booleans
- Iterables
  - list
  - tuples
  - strings as iterables
- Control Structures
  - If/else/elif
  - For Loops
  - While Loops
- Data Structures Introduction (Dictionaries)
- Using Functions


<!-- page break -->
<div style="page-break-after: always;"></div>

## Part 1

### Printing

To print to the terminal in python is as simple as 

```python
print("whatever you want")
```

It is necessary at this point to introduce a variable type called `strings`. This is a kind of variable that stores alphanumeric values such as `"Names"` and `"Places"`. So if we would like to print out a message with a string variable, it is a simple as;

```python
full_name = "Joshua Owoyemi"
# print out the message with the name
print("Full Name: ", full_name)
```

You will notice that a line was started with `#`. This is to tell python program to ignore that line. Therefore anything written on that line is ignored and will not be `compiled`. It is called a `comment`. So if we do something like;

```python
full_name = "Joshua Owoyemi"
#print("Full Name: ", full_name)
```

Nothing will be printed to the terminal because the line has been commented out. `Comments` are useful to add human readable information to our code so we can easily remember or understand what we are trying to do in that part of the code. Please use comments as much as possible.

In python, other variables can also be printed in the already introduced manner. For example a variable storing a number can be printed as such;

```python
number = 7800000000
print("World Population = ", number)

# this is also possible
number = 7.8
print("There are, ", 7.8, "billion people in the world right now")
```

The print statement can be used in more various ways. More of this will be introduced in future sections.

### Strings

One class of variable that deserves to be treated separately is `strings`. This section will focus on `string` manipulation as it has been introduced earlier. Two major manipulation for python strings are `concatenation` and `slicing`. `Concatenation` allows two or more string sequences to be combined into one, such as;

```python
first_name = "Joshua"
last_name = "Owoyemi"
full_name = first_name + " " + last_name
```

Notice that a space (`" "`) is added in the middle as will be expected in a full name.

On the other hand, `slicing` allows us to split a single string variable to smaller pieces as such;

```python
full_name = "Joshua Owoyemi"
first_name = full_name[:7]
last_name = full_name[7:]
```

What happened here is that we give an `index` of the point where we want the string variable to be split. This idea can be applied to some other variable types. We will talk about them in later sections.



<!-- page break -->
<div style="page-break-after: always;"></div>

## Useful Resources and Bibliography

https://www.pythonlikeyoumeanit.com/index.html