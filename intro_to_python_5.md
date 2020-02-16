# Solving Programing Problems with Python (LeetCode 3)

<brief>

## Outline (use a sample problem)

- writing psuedocodes
- create a simple program structure from the psuedocode
- write the code
  - use functions as much as possible
- Sample problem solution

This a topic which is best explain through an example. Here we are going to use a popular problem from leetcode.com. This is a problem you need to be familiar with if you ever want to get a job as a software engineer. Here, we are going to solve the problem with the Python language. The problem is called [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/).

## Writing Psuedocodes

A psuedocode is 'false' code. This means the code or set of instructions is written in a way that does not follow any particular programming language. It helps us to understand the steps necessary to solve a particular problem without thinking about the syntax of the programming language. Suppose we want to write the psuedocode for checking the largest of two numbers `a` and `b`, we might write something like;

```txt
1. Get a and b
2. check a>b
3. if 2 is true, then a is largest
4. else(if 2. is not true) then b is largest
5. return largest
```

This is not a real code but it shows the steps someone might take to solve the problem. It turns out that this step is very important and it helps many programmers to save a lot of time in solving the problem. Without this step, it is easy to run into problems while writing the code and spending a lot of time to fix bugs and logic of the problem solution. Now let us use this idea to solve our problem. Here is a possible psuedocode for the `Longest Substring Without Repeating Characters` problem;

```txt
1. For each letter s in the string
2. If s did not appear before, store s and index of s somewhere
3. If s appeared before, calculate the lenght between index of now and index of before
4. compare lenght if it is the largest
5. Output largest lenght
```


## Bibliography

