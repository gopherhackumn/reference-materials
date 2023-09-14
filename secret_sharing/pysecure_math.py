import math
from functools import reduce

def polynomial(x, coefficients, mod):
  """Evaluate a polynomial with given coefficients at x, mod mod"""
  x_to_the_i, result = 1, 0
  for coefficient in coefficients:
    result += coefficient * x_to_the_i
    x_to_the_i *= x
    result %= mod
  return result

def pair(int1, int2):
  """Return unique integer corresponding to argument pair"""
  added = int1 + int2
  return int2 + (added*(added + 1)) // 2

def unpair(num):
  """Return unique integer pair corresponding to argument pair"""
  w = (math.isqrt(8*num + 1) - 1) // 2
  t = (w**2 + w) // 2
  y = num - t
  x = w - y
  return x, y

def x_gcd(a, b):
    """
    Division in integers modulus p means finding the inverse of the
    denominator modulo p and then multiplying the numerator by this
    inverse (Note: inverse of A is B such that A*B % p == 1) this can
    be computed via extended Euclidean algorithm
    http://en.wikipedia.org/wiki/Modular_multiplicative_inverse#Computation
    """
    x, last_x = 0, 1
    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, last_x = last_x - quot * x, x
    return last_x

def interpolate(points, mod, x = 0):
  """Interpolate polynomial with given points over finite field corresponding to prime mod and evaluate at x """
  PI = lambda vals: reduce(lambda x, y: x*y, vals)
  mod_div = lambda num, den: num * x_gcd(den, mod)
  # mod_div finds num / den modulo prime p
  # return satisfies: den * _divmod(num, den, p) % p == num
  x_arr, y_arr = zip(*points)
  nums = []  # avoid inexact division
  dens = []
  for idx, cur in enumerate(x_arr):
      others = [num for i, num in enumerate(x_arr) if idx != i]
      nums.append(PI(x - other for other in others))
      dens.append(PI(cur - other for other in others))
  den = PI(dens)
  num = sum([mod_div(nums[i] * den * y % mod, dens[i]) for i, y in enumerate(y_arr)])
  return (mod_div(num, den) + mod) % mod

def encode_str(key_str):
  """Map string to unique integer"""
  return int.from_bytes(key_str.encode(), "little")

def decode_int(key):
  """Recover string from its unique integer"""
  num_bytes = (key.bit_length() + 7) // 8
  return key.to_bytes(num_bytes, "little").decode()