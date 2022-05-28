

# Program to read file content and count number of occurrence of words.

def read_file_content(filename):
    with open("./story.txt", "r") as f:
        lines = f.read()
    return lines

def countwords():
    text = read_file_content("./story.txt")
    text_split = text.split()


# Create an empty dictionary.
    count = {}
    for n in text_split:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    return count


print(countwords())
