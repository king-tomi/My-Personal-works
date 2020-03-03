def count_l(word):
    """A program that counts the number of letters and digits in a string
       
       input: 'word' a string

       output: a tuple containing the number of digits and letters
       """
    num_letters = 0
    num_digits = 0
    for l in word:
        if l.isdecimal():
            num_digits += 1
        elif l.isalpha():
            num_letters += 1
        else:
            continue
    return f"number of letters is {num_letters} and number of digits is {num_digits}"


# def express(equalities):
#     """A program that solves a given formula by using the values gotten from the array
       
#        input: 'equalities' a list of equality expressions

#        output: a string containing the result of the expressions
#     """
#     expression = ""
#     operand = ""
#     letter = ""
#     result = ""
#     for i in equalities:
#         expression += i
#         for j in expression:
#             if not j.isalpha():
#                 operand += j


def sum_even(start,n):
    """sums all even numbers from start up to n provided start is 0 """
    if start > n:
        return 0
    else:
        return start + sum_even(start+2,n)

print(sum_even(0,6))       