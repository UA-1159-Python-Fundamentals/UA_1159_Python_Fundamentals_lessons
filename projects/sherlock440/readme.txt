!!! All paths in the app were made for macOS/Linux, so in Windows there should be some other slashes. I could use
something like "import platform" to make different paths depending on the OS, but I guess it's an overengineering in
terms of the project

The app is for replacing some words on pictures to others.

User decides which words to replace and by what words, of course pictures can be any (but a third-party OCR library
handles with limited number of fonts).

Pictures for editing should be placed on /"Жалкие пародии" folder.
For demonstrating I prepared 2 of them, the proper font size is place in the end of each file name.

The app can handle mistakes of input by a user, so it can be tested. Somewhere I also write "try-except" blocks for
situations like having no permissions to make a folder, but frankly I did not pay much attention to it, because it's
not a real project.

There is one "problem" that I don't know how to solve — I guess it's because of library PIL and troubles with fonts.
The problem is that a theoretical height of fonts don't always equal to an actual one, and there is no way to calculate
it inside a program for putting a word literally in the vertical center of an area for putting. So I had to crate a dict
with prepared appropriate values to each font — if there is no value (because of appearing of new fonts, for example),
the app takes a default value.

I could make every py-module work also separately by adding if __name__ = "__main__", but I guess that the current
functional is also enough. But it would be quite easy.