def simple_map(function, values):
    return (function(value) for value in values)

values = [1, 3, 1, 5, 7]
operation = lambda x: x + 5

result = simple_map(operation, values)
print(*result)

#The code defines a function named simple_map, which performs a simplified version
# of the map operation in Python. The map function is used to apply a given function
# to each element of an iterable and returns an iterator with the results.

#  def simple_map(function, values):
       #This line defines the function simple_map that takes two arguments:
            #function: A function that will be applied to each element of values.
            #values: An iterable (e.g., list, tuple) containing the values on which the function will be applied.

  #return (function(value) for value in values)
        #This line uses a generator expression to apply the function to each element in values. It creates a new
        # generator that yields the results of applying the function to each element.

 #values: A list of integers [1, 3, 1, 5, 7].
 #operation: A lambda function that takes an argument x and returns x + 5. This function will be applied to each element in values.
 #result: It will store the result of calling simple_map(operation, values).

#print(*result)
    #This line unpacks the result generator and prints its elements. 
        # The * operator before result is used to unpack the generator into separate arguments for the print function.
