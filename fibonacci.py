"""
The fibonacci sequence can be generated using different programming techniques.
The following is a sample that will be helpful in understanding certain programming
concepts.
"""
def fib_reg(number):
    """
    Method: Iteration
    :param number: 
    :return: List of fibonacci numbers
    """
    previous_num = 0
    current_num = 1
    fiblist = [previous_num, current_num]
    for i in range(number):
        current_num, previous_num = (current_num + previous_num), current_num
        fiblist.append(current_num)
    return fiblist

print("\nPrinting results for fib_reg, the regular, iterative function")
print(fib_reg(9))

def fib_rec(n):
    """
    Method: Recursion
    :param n: 
    :return: Returns the nth number in fibonacci series
    """
    if n < 0:
        raise ValueError('input can\'t be negative')
    elif not isinstance(n, int):
        raise TypeError('input has to be an int')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

print("\nPrinting results for fib_rec, the recursive function")
check = fib_rec(12)
print(check)
# Use the for loop to generate a series
#for i in range(8):
#    print(fib_rec(i))

def fib_gen():
    """
    Method: Generator
    Yield statement is immediately recognized by the computer
    and it treats this code as a Generator. One cannot have
    return and yield statements in the same function.
    .next() in the for loop is another special call that the
    generator recognizes
    :return:
    """
    first_no = 0
    second_no = 1
    yield first_no
    while True:
        yield second_no
        second_no, first_no = second_no + first_no, second_no

print("\nPrinting results for fib_gen, the generator function that has a yield statement")
gen_ans = fib_gen()
for i in range(6):
    print(gen_ans.next())
