# Sublinput
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/Sigmanificient/pg-sublime-input/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/Sigmanificient/pg-sublime-input/?branch=master)
[![Build Status](https://scrutinizer-ci.com/g/Sigmanificient/pg-sublime-input/badges/build.png?b=master)](https://scrutinizer-ci.com/g/Sigmanificient/pg-sublime-input/build-status/master)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Sigmanificient/pg-sublime-input)
![Lines of code](https://img.shields.io/tokei/lines/github/Sigmanificient/pg-sublime-input)


A sublime pygame ui as alternative to unsupported python input built-in.

## Install

```bash
pip install sublinput
```

or 
```bash
python -m pip install sublinput
```

## Usage

You only needs to input the package then use the default input function as usual !

```py
import sublinput

val = int(input("Enter a number: "))
print(val)
```

When an input function is called, the following windows will appear, with title being the input message.

![](https://raw.githubusercontent.com/Sigmanificient/pg-sublime-input/master/img/windows_empty.png)

Type in the windows as a usual input function.

![](https://raw.githubusercontent.com/Sigmanificient/pg-sublime-input/master/img/windows_42.png)

Then press enter (*not keypad enter*) to submit the value.

An input-like log will be printed.
```cmd
Enter a number : 42
```
Then it will return the submit value as a `str`.

*You only need to remove the *import sublinput* from your code to disable it !*