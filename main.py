# Scenario
# Do you know what a palindrome is?

# It's a word which look the same when read forward and backward. For example, "kayak" is a palindrome, while "loyal" is not.

# Your task is to write a program which:

# asks the user for some text;
# checks whether the entered text is a palindrome, and prints result.
# Note:

# - assume that an empty string isn't a palindrome;
# - treat upper- and lower-case letters as equal;
# - spaces are not taken into account during the check - treat them as non-existent;
# - there are more than a few correct solutions - try to find more than one.

# ######################################################################################################################

# Test your code using the data we've provided.

# Test data
# Sample input:

# Ten animals I slam in a net

# Sample output:

# It's a palindrome


# Sample input:

# Eleven animals I slam in a net

# Sample output:

# It's not a palindrome

# ######################################################################################################################


def isPal(txt1):
    y = 0
    txt1 = txt1.replace(" ", "").lower()
    for i in range(len(txt1) - 1, -1, -1):
        if txt1[i] != txt1[y]:
            return 0
        y += 1
    return 1

txt = input("Please enter the text:\n")
val = isPal(txt)
if val:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
