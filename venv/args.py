# Just one way to catenate strings and center the text.
# List comprehension could be easier.

def centre_text(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# Calling the function
centre_text("text, text and text")
centre_text("text, text and text... and more text")
fift = "last"
centre_text("first", "second", 3, 4, fift)