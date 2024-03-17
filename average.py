def average(numbers):
    """
    Calculate the arithmetic mean (average) for a list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    float: The arithmetic mean (average) of the numbers.
    """
  #  if not numbers:
  #      return None
  #  return sum(numbers) / len(numbers)

# Test the function
numbers = [1, 2, 3, 4, 5]
print("Average of", numbers, ":", average(numbers))

numbers2 = [10, 20, 30, 40, 50]
print("Average of", numbers2, ":", average(numbers2))

numbers3 = [-1, 0, 1]
print("Average of", numbers3, ":", average(numbers3))


