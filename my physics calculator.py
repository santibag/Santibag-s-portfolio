print("""Welcome to my physics calculator.
Made by Santibag. August 2016

List of operations:
""")

prefixes = ["P", "T", "G", "M", "k", "" , "m", "mic", "n", "p"]
op_list = ["Gravity Acceleration","Gravitational Force", ]

for op in range(len(op_list)):
    print("{0}-{1}".format(op+1,op_list[op]))
op_type = eval(input("\nPlease choose the operation by\ntyping its number from the list above:"))

while op_type is 1:
    m = eval(input("Please enter the mass:"))
    r = eval(input("Please enter the distance\nfrom gravity center:"))
    g = 6.67408 / 10**11 * m / r**2



    pre = 5
    changed = g
    while changed < 1:
        if pre < 9:
            changed = changed * 1000
            pre = pre +1

    while changed > 1000:
        if pre > 0:
            changed = changed / 1000
            pre = pre -1

    prefix = prefixes[pre]

    res = "{0}{1}m/s^2".format(changed,prefix)

    print (res)
    print ("\nCalculation ended. You can continue to another calculation.\n")
