'''Intermediate:  Given a tuple of mixed data types (strings, numbers), create a new tuple containing only the strings.'''

dump = ['hello',82,'world',55,'sum']

og = tuple(element   for element in dump if isinstance(element,str))

print(og)