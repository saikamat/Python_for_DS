'''
LAMBDA FUNCTIONS
1. aka anonymous expressesions
2. any expression without a function name.
3. add lambda and the expression following 'lambda' is a function definition
4. e.g. >>> lambda x: 3*x+1
        <function <lambda> at 0x01D...F6>
        this however isn't enough. lambda's gotta have a return value. therefore,
5. e.g. >>> g = lambda x: 3*x+1
        >>> g(2)
        7       <---- right answer!

WITH MULTIPLE INPUTS
1. # combine first and last names into a single full name
    >>> full_name = lambda first, last: first.strip().title() + " " + last.strip().title();
    # here strip is used to remove the white space, and title() gives the expression a sentence case.
    >>> full_name("   bruce","Wayne")
    Bruce Wayne

TYPICAL LAMBDA EXPRESSIONS
lambda : "what's up?"
lambda x: 3*x+1;
lambda x, y : (x*y)**0.5 # geometric mean.
lambda x, y, z: 3/(1/x+1/y+1/z);    # harmonic mean
lambda x1, x2, ...., xN : ...

Some function definitions are simple enough that they can be converted to a
lambda function. By doing this, you write less lines of code, which is pretty
awesome and will come in handy, especially when you're writing and maintaining
big programs. In this exercise, you will use what you know about lambda functions
to convert a function that does a simple task into a lambda function. Take a look
at this function definition:
def echo_word(word1, echo):
    """Concatenate echo copies of word1."""
    words = word1 * echo
    return words
The function echo_word takes 2 parameters: a string value, word1 and an integer value,
echo. It returns a string that is a concatenation of echo copies of word1. Your task is
to convert this simple function into a lambda function.
Instructions
-Define the lambda function echo_word using the variables word1 and echo. Replicate what
the original function definition for echo_word() does above.
-Call echo_word() with the string argument 'hey' and the value 5, in that order. Assign
the call to result.
'''
words = lambda word1, echo: word1*echo;

#calling the lambda function
result = words('hi',5);
print(result);
