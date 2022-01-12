# JavaScript-like Minecraft functions

# (JMC)

A compiler for compiling .jmc file (custom language) to minecraft datapack.
The language is _inspired_ from JavaScript. It's not exactly like JavaScript

## Why use JMC

JMC allows you to write minecraft functions in a better language (.jmc) which is more readable and easier to write.
For example, you can declare multiple function in a single file and whitespaces no longer matter which means you can split a single command into multiple line

Normal function from .mcfunction file will not works in JMC, the syntax is almost entirely different.

## Installation

### Released Version

_There's no released version at the moment_

1. [Download jmc.exe]() from github
1. Create a directory for your datapack
1. Put **jmc.exe** file in that directory
1. Create your jmc file with .jmc extension

### Pre-released Version

1. Download ZIP or Clone repository
1. Create a virtual environment for python
1. Install libraries from requirements.txt
1. Run `python compile.py <target jmc file>` with virtual environment

## Usage

Create \<name\>.jmc file and compile it!
[Documentation](docs/index.md) (Soon TM)

## Contributing

**My Discord:** WingedSeal#0795

## Features

- Function declaration (Arrow function does not work)
- ~~Function parameters~~ (Discontinued) 
- Custom variable assignment, incrementation sysntax 
- Importing other .jmc files
- Multiline command
- Build-in functions for basic datapack feature
- Grouping things in a directory using "class" declaration (Note that it's not an actual class)

## License

[MIT](https://choosealicense.com/licenses/mit/)
