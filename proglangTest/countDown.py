# : Basic Countdown Simulator (Recursion) INTERMEDIATE
# Recursion Base Case Write a simple recursive function that counts down from a number to 1.
# def countdown(n): # Base case: if n is 0, print "Blastoff!" and stop # Recursive
# case: print n, then call countdown(n - 1) pass
# Implement the base case when n == 0.
# In the recursive step, print the current number n and call countdown(n - 1).
# Test the function by calling countdown(5

def countDown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countDown(n-1)

countDown(5)