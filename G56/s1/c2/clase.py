a = [1, 2, 3, 4, 'hola', 8]

print(a[0]) # => 1 (El primer elemento de la lista)
print(a[7]) # => IndexError (No hay un elemento con el índice 7, la lista es mas corta)
print(a[a[0]]) # => 2 (Si evaluamos a[0], esto da 1, entonces sería a[1] => 2)
print(a[4]) # => 'hola' (Es el quinto elemento de la lista)
print(a[-1]) # => 8 (Es el último elemento de la lista!)