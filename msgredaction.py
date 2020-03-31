"""
Assignment #3

Program 2 – Message Redaction

Design and write a program that removes all desired letters from any user-entered sentence or phrase.
Your solution should demonstrate an understanding of how to apply list and looping concepts in a 
program that should:
•	Take a sentence or phrase as input,
•	Take a comma-separated list of letters to remove as input,
•	Replace all occurrences of each target letter in the user-entered sentence, regardless of 
case sensitivity, with an underscore (“_”) character.
•	Display the number of letters removed to the user,
•	The program will keep asking the user to enter a new sentence until the user enters the command ‘quit’.

Your solution must contain examples demonstrating your understanding of appropriate use of functions 
and core assignment concepts (loops and lists).


Name..: Cristina Ponay
ID....: W0424195
"""

__AUTHOR__ = "Cristina Ponay <w0424195@nscc.ca>"

def main():
    phrase = ""
    # keep prompting until user inputs "quit"
    while True:
        phrase = input("Type a phrase (or 'quit' to exit program): ").lower()
        if phrase == "quit": # if user inputs "quit"
            break
        else:
            # user must input letters separated by commas
            letters = input("\nType a comma-separated list of letters to redact: ").lower()
            redact = letters.split(",")
            # begin redaction process
            count,newPhrase = redactAMesage(phrase, redact)
            # display redacted message
            print(f"Number of letters redacted: {count}")
            print(f"Redacted phrase: {newPhrase}")

# function that will redact a message
def redactAMesage(in_phrase, in_redactList):
    ctr = 0
    out_phrase = ""
    # iterate through each character in phrase
    for char in in_phrase:
        # check if character is in the redact list
        if char in in_redactList:
            char = "_"
            ctr += 1  # counts the number of characters redacted
        out_phrase += char
    return ctr, out_phrase    # returns the number of characters redacted and the redacted phrase

if __name__ == "__main__":
    main()