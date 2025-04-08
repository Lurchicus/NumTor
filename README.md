# NumTor

Number Torture for Python (pick a number between 1 and 100, with a twist).

## Imports

- colorama
- random

## Changes

- Dan Rhea - Tue Aug 13 18:53:39 2024 -0400 - Initial commit
- Dan Rhea - Tue Aug 13 19:18:12 2024 -0400 - Add files via upload, Initial program
- Dan Rhea - Tue Aug 13 20:57:07 2024 -0400 - Switched the foreground text to white to make it easier to read
- Dan Rhea - Tue Aug 13 23:28:37 2024 -0400 - Added a "hidden" debug command (-1) and a debug toggle to show several values
- Dan Rhea - Wed Aug 14 00:22:36 2024 -0400 - Ran through pylint and fixed all but "from random import randint", not sure why it's showing a no docstring error unless it's something in the library
- Dan Rhea - Wed Aug 14 10:01:32 2024 -0400 - Changed naming in the info() procedure, updated the debug toggle comment and added imports to readme.
- Dan Rhea - Wed Aug 14 10:06:33 2024 -0400 - Changed info() to use snake case for parameter names
- Dan Rhea - Wed Aug 14 10:24:03 2024 -0400 - Added change history to README.md
- Dan Rhea - Thu Aug 15 02:09:14 2024 -0400 - Added f"" formatting to the info() procedure, and improved docstring. Also added a docstring to the program (pylint seemed to like it)
- Dan Rhea -  - Changed input to a function that error checks the input first. Fixed a few things pylint didn't like.
- Dan Rhea - Tue Dec 24 16:51:30 2024 -0400 - Updated the copyright for the first year NumTor (Number Torture for 8-bit Atari BASIC).
- Dan Rhea - Thu Apr 03 02:09:11 2025 -0400 - Implemented f"{foo}" strings. Changed variable names to lower case (though pylint still thinks some of my variables are constants). Added type hints.
- Dan Rhea - Mon Apr 08 00:27:14 2025 -0400 - Added return types to functions, move the main part of the program into 'main()' and added code to call it.
