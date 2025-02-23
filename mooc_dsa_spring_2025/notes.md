# Introduction

What is an algorithm?
    An algorithm is a method for solving some computational problem.

- Any algorithm implemented for a computation can be executed on a computer
- In Python an algorithm can be implemented as a function, and then typically the input is given as the function parameters and the output is the return value

Consider the following problem, count even numbers,
    - In a given list of numbers, count the total number of numbers where that number is even

```python
def count_even(numbers):
    result = 0
    for i in numbers:
        if i % 2 == 0:
            result += 1
    return result
```

The function can be tested like so,

```python
print(count_even([1, 2, 3])) # 1
print(count_even([1, 2, 3, 4, 5])) # 2
print(count_even([2, 4, 100, 12873, 100819232])) # 4
```

Upon testing, the answers will be as follows

```python
1
2
4
```

What is a data structure?
    A data strcuture is a way of storing data within a program.

- Basic data structure in python is list.
- The choice of data structures defined the designing part of an algorithm and its efficiency

Implementing an algorithm
    Any algorithm can be implemented with a few basic programming constructs.
    In python, these basic constructs are:
        - variables
        - operators (+, = etc.)
        - conditionals (if)
        - loops (for, while)
        - lists
        - functions
        - classes
    In addition to these, programming languages have amy other features that can help shorten the code,
    but do not affect the fundamental operation logic of the code.

For example:

```python
def count_even(numbers):
    result = 0
    for i in numbers:
        if i % 2 == 0:
            result += 1
    return result
```

Above count_even algorithm, can also be written in a more compact form using the generator expression

```python
def count_even(numbers): return sum(x % 2 == 0 for x in numbers)
```

Here the `sum` function encloses a generator expression that computes the value of the expresssion
`x % 2 == 0` for each element `x` of the list, the possible values are `True` and `False` which are treated as `1` and `0`, which sums up to the count of even numbers in the list.

The advantage of the first function is that the it is easy to explain to someone who is not familiar with python contructs and can be easily converted to other languages for example javascrit.

```javascript
function countEven(numbers) {
    let result = 0;
    for (let x of numbers) {
        if (x % 2 == 0) result++;
    }
    return result;
}
```

The advantage of second function is that is more concise and perhaps more in the style of python programming, afterall the language is supposed to make your life easy by writing less code `:)`.

Efficiency of algorithms

The same task can be solved by different algorithms, and there can be big differences in their efficiencies.
Often the goal is to find the efficient algorithm that solves the task quickly

Let us consider a task, where we are given a list of numbers, and the goal is to find the
largest difference between any two numbers,

Sample input `[3, 2, 6, 5, 8, 5]`, the answer will be 6, which is the largest diff amoong the
numbers 2-8.

This can be written in 3 ways

`Algorithm1`

```python
def max_diff(numbers)
    result = 0
    for x in numbers:
        for y in numbers
        result = max(result, abs(x - y))
    return result
```

`Algorithm2`

```python
def max_diff(numbers):
    numbers = sorted(numbers)
    return numbers[-1] = numbers[0]
```

`Algorithm3`

```python
def max_diff(numbers): return max(numbers) - min(numbers)
```
