#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)

```python
    # This is O(1)
    a = 0
    # This loop will run O(n) times
    while (a < n * n * n)
      # a is incremented by n**2 each loop
      # multiplication, addition and assignment is O(1)
      a = a + n * n
    # Total time complexity is O(1 + n + 1) --> O(n)
```

b)

```python
    # This is O(1)
    sum = 0
    # The outer loop runs in O(n) * the complexity of the inner loop
    for i in range(n):
      # This is O(1)
      j = 1
      # j doubles in each iteration, so this loop will run in O(log n)
      while j < n:
        # this is O(1)
        j *= 2
        # This is O(1)
        sum += 1

    # The total time complexity is O(1) + O(n) * (O(log n) * O( 1 + 1))
    #                           == O(1) + O(n) * O(log n)
    #                           == O(n log n)
```

c)

```python
    def bunnyEars(bunnies):
      # This is O(1)
      if bunnies == 0:
        return 0

      # The state of 'bunnies' decreases by 1 on each recursion
      # so bunnyEars will recurse n times
      return 2 + bunnyEars(bunnies-1)

      # The total time complexity is O(1) + O(n)
      #                              == O(n)
```

## Exercise II

If we think of the building floors as a sorted array, this reminds me of binary
search.

0. Initialize the min floor to 1
   0a. Initilize the max floor to n
1. Set 'f' as (min floor + max floor ) / 2 -- round down if not an
   integer
2. Go to 'f' floor
3. Throw an egg
4. If the egg breaks:
   4a. Go one floor below and throw an egg
   4b. If the egg does not break, return f
   4c. If the egg does break, we're too high. Set the max = f
   4d. Go back to step 1
5. If the egg doesn't break:
   5a. Go up one floor and throw an egg
   5b. If the egg breaks, return f
   5c. If the egg doesn't break, we're too low. Set the min = f+1
   5d. Go back to step 1
