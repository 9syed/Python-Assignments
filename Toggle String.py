input_string = input()
print (''.join(c.lower() if c.isupper() else c.upper() for c in input_string))