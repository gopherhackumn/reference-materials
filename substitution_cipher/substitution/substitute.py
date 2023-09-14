def substitute(message, sub): # replace each character with its corresponding character in the substitution
    substituted_chars = []
    for char in message:
      substituted_char = char
      if char.lower() in sub:
        substituted_char = sub[char.lower()]
      if char.isupper():
          substituted_char = substituted_char.upper()
      substituted_chars.append(substituted_char)
    return "".join(substituted_chars)