N = 10_000_000
import random
from functools import reduce

def polynomial(coefficients, x):
  result = 0
  for coefficient in coefficients:
    result *= x
    result += coefficient
  return result

def make_polynomial(y_intercept, num_coefficients):
  coefficients = []
  for _ in range(num_coefficients - 1):
    coefficients.append(random.randint(1, N))
  coefficients.append(y_intercept)
  return coefficients

def generate_shares(m, k=3):
  coefficients = make_polynomial(m, k)
  x_values = set()
  for _ in range(k):
    num = random.randint(1, N)
    while num in x_values:
      num = random.randint(1, N)
    x_values.add(num)
  # we have k random x values in range [1, N - 1]
  shares = [(x, polynomial(coefficients, x)) for x in x_values]
  return shares

def interpolate(points, x=0):
  xs = []
  ys = []
  for x_i, y_i in points:
    xs.append(x_i)
    ys.append(y_i)
  nums = []
  dens = []
  for i, x_i in enumerate(xs):
    other_x = xs[:i] + xs[i+1:]
    multiply = lambda a, b: a * b
    numerator = reduce(multiply, other_x)
    nums.append(numerator)
    denominator = reduce(multiply, [x_j - x_i for x_j in other_x])
    dens.append(denominator)
  result = 0
  for i, y_i in enumerate(ys):
    result += y_i * nums[i] // dens[i]
  return result
    
    
  