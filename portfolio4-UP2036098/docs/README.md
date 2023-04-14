# Hello GitHub Pages

## Overview

| Description | Example Usage | Expected Output |
|---|---|---|
|This code is a simple python code that would print out "Hello Portfolio 4"|By typing python3 HelloWorld.py the code will be executed|Hello Portfolio 4|
|Class Hello1 has two constructor|```def __init__(self, earth)``` and ```def output(self):```| - |
| In class HelloPortfolio():, x will take the argument from and use the constructor from Hello1 class|```x = Hello1("Hello Portfolio 4") x.output()```| - |

## Code

```Code

class Hello1:
    def __init__(self, earth):
        self.HelloEarth = earth

    def output(self):
        print(self.HelloEarth)

class HelloPortfolio():
    x = Hello1("Hello Portfolio 4")
    x.output()
```

## Table example

| Description | Image 1 (width=200px)| Image 2 (width=150px)|
|:---:|:----:|:---:|
|This is a screenshot of Github Pages on my website|![GitHub Pages website](GithubPages.png){width=200px}| ![GitHub Pages website](GithubPages.png){width=150px}|

## Resize example

![This image is width = 250px](GithubPages.png){width=250px}

![This image is width = 290px](GithubPages.png){width=290px}

![This image is width = 310px](GithubPages.png){width=310px}
