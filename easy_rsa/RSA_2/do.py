def cube_root(x):
  lo, hi = 0, x
  while lo < hi:
    mid  = (lo + hi) // 2
    cube_of_mid = mid ** 3
    if cube_of_mid == x:
      return mid
    if cube_of_mid > x:
      hi = mid
    else:
      lo = mid + 1

if __name__ == "__main__":
  c = int(input())
  m = cube_root(c)
  print(m.to_bytes(m.bit_length() + 1, byteorder="big").decode('utf-8'))