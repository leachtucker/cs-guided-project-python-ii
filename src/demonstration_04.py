"""
Challenge #4:

Create a function that changes specific words into emoticons. Given a sentence
as a string, replace the words `smile`, `grin`, `sad`, and `mad` with their
corresponding emoticons.

word -> emoticon
---
smile -> :D
grin -> :)
sad -> :(
mad	-> :P

Examples:
- emotify("Make me smile") ➞ "Make me :D"
- emotify("Make me grin") ➞ "Make me :)"
- emotify("Make me sad") ➞ "Make me :("

Notes:
- The sentence always starts with "Make me".
- Try to solve this without using conditional statements like if/else.
"""


def emotify(txt):
    words = txt.split()

    i = 0
    while i < len(words):
        if (words[i].lower() == "smile"):
            words[i] = ":D"
        elif (words[i].lower() == "grin"):
            words[i] = ":)"
        elif (words[i].lower() == "sad"):
            words[i] = ":("
        i += 1

    return words

print(emotify("Make me smile"))
print(emotify("Make me grin"))
print(emotify("Make me sad"))


