lst = [1, 2, 3, 4, 5]
lst_1 = [2*x for x in lst]
print("[2*x for x in lst]")
print(lst_1)
lst_2 = [2*x for x in lst if x > 3]
print("[2*x for x in lst if x > 3]")
print(lst_2)
lst_3 = [2*x for x in lst if x <= 2]
print("[2*x for x in lst if x <= 2]")
print(lst_3)
lst_4 = [[x, x**2] for x in lst]
print("[[x, x**2] for x in lst]")
print(lst_4)

a = (x*x for x in range(5))
for i in range(5):
    print(next(a))