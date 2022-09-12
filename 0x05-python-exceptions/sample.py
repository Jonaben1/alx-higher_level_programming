def saw(lin = [], x = 0):
    return (lin[:x])


x  = [1,2,3, 4, 5, 6]
y = saw(x, 2)
print(y)
print(saw(x, 5))
