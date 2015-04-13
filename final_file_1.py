"""
Recursion: A way of coding a problem in such a manner that the function calls itself
repeatedly. This programming technique will be suitable for problems that can be broken
down into smaller problems that need the same steps to be solved.
Run the following demonstration of a recursion problem and see what it prints.

"""
s = "Hello"
b = s
def string_eater(string, length, other_string, other_length):
    eater = length
    ruminator = other_length

    if string is None or other_string is None:
        print(TypeError, "No input entered")

    if eater >= 1:
        print(string[:eater])
        string_eater(string, eater - 1, other_string, ruminator)

    elif ruminator <= len(other_string):
        print(other_string[:ruminator])
        string_eater(string, eater, other_string, ruminator + 1)

string_eater(s, len(s), b, 0)
"""
1. YOUR QUESTION: Who ate my Jell-O?
Write a recursive code that prints Jell-O, ell-O, ll-O, l-O, -O, O
and then O, -O, l-O, ll-O, ell-O, Jell-O
"""


"""
Also remember the factorial problem that we discussed in the class to understand
test driven development and recursion?
5! is 5*4*3*2*1 4! is 4*3*2*1 and so on.... That is 5! is 5*(5-1)!, 4 is 4*(4-1)!..
We can see that the recursive call to solve this problem is (n-1). (N is repeatedly
multiplied by (n-1))
Remember, just like the while loop, in a recursive function, there has to be a base
case that will end the recursive call and unfold the entire function for us. In the
following function, it is n <= 2. What was the base case in the function above?
"""

def factorial(n):
    if n <= 2:
        return n
    else:
        return n * factorial(n-1)

answer = factorial(6)
print(answer)
"""

2. YOUR QUESTION: ITERATE THIS.
When we write a for-loop or a while loop, we're actually iterating over a list or
range. Try the code above and enter 2000 as a value in the function. You'll exceed
runtime limit. Since recursion stores output in a stack before the entire function
is executed, it can exceed runtime limit when we scale up the input.
An iterative loop will work better in such cases.
Write the above function using iteration.
"""

"""
3. YOUR QUESTION: Crap! Winning at this coded game of CRAPS is as hard as the real deal in Vegas!
Build a game of craps.
Rules:
1) We need two six-sided dice.
2) Come Out stage: Roll them at the same time. That is, randomly generate two numbers
between 1-6. Add them.
3) If the come out roll is 2, 3, 12, you lose.
4) If the come out roll is 7 or 11, you are riding your luck. Now you can actually go and celebrate in Vegas ;)
5) However, if you get any other sum, you enter another phase of this game called the Point Phase
6) The sum that you just got becomes "The Point".
7) You roll the dice again and again till you get this Point number of 7. If you get
the point number, you win, if you get 7, you lose. For any other number, you keep rolling
till you get the Point number or 7

1) You can build this game simply using a while loop.
2) However, it'd be really neat if you can build it using functions, have a score, bet
amount and a game state that allows you to restart the game and continue winning or losing
money.
3) To make it a bit more challenging, for the dice values, you can print "*", "**", "***",
"**\n**"... just like they appear on real dice :)
If you build a complete game using all these features, it's worthy of a project that you
can proudly display and share with others to play.
"""
