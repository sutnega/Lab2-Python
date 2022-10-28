def level2(lst):
    d2 = [ i for i in lst if i % 2 == 0]
    d3 = [ i for i in lst if i % 3 == 0]
    d5 = [ i for i in lst if i % 5 == 0]
    return d2, d3, d5
 
print(level2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))