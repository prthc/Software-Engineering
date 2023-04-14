```Code

import sys


class Hello1:
    def __init__(self, earth):
        self.HelloEarth = earth

    def output(self):
        print(self.HelloEarth)


class HelloWorld():
    x = Hello1("Hello World")
    try:
        if sys.argv[1] == "--help":
            print("UP2036098")
    except IndexError:
        x.output()
```
