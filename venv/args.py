"""Just one way to catenate strings and center the text. List comprehension
could be easier. Also writing a 'centered' file."""

def centered_text(*args, sep=" ", end="\n", file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end= end, file= file, flush=flush)

with open("centered", mode="w") as centered_file:
    # Calling the function
    centered_text("text, text and text", file=centered_file)
    centered_text("text, text and text... and more text", file=centered_file)
    fift = "last"
    centered_text("first", "second", 3, 4, fift, sep=";", file=centered_file)