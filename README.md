# Regex Question

A test for creating a Python regex library

## Overview

Create a deterministic regex engine with a subset of the full Regex features.

- The name of the class should be Regex.

- The constructor for the class should simply take a pattern string. For example: 

```
 regex = Regex('hello.world')
```

 will initialize a new Regex object with the regex pattern 'hello.world'

- The regex object will have a single function: search(matchString). The argument to the function is
  the string that you want to search with the pattern provided in the constructor. The function will return
  a list of matches, as the following example illustrates:

```
  regex("hello|world") = ["hello|world"]
  regex("hello-world helloworld hello,world hello world") = ["hello-world", "hello,world", "hello world"]
```

## Patterns that the Regex class must be able to use


- The complexity of the exercise lies primarily in the features that are implemented in the regex pattern string. At a minimum, the class must respect the following operators:

  - the period ('.') operator: match any character. For example "hell." will match "hello" and "hellp"

  - the question-mark operator: match zero or one instances of the previous character. For example, "hell?o" will match "hello" and "helo". Also, combining the dot and the question mark allows you to make the following expression: "hell?." will match "hello" and "help"


## What we're looking for

- Code should have unit tests.

- Classes and complex methods should have docstrings

- Style: 
  - Functions should have meaningful names. 
  - Code should comply with PEP-8 standards, except a line-length of 120 characters may be used.

