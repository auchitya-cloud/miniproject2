import random

products = {'p1': 10, 'p2': 15, 'p3': 20, 'p4': 25, 'p5': 30, 'p6': 35, 'p7': 50,
            'p8': 40, 'p9': 55, 'p10': 60, 'p11': 65, 'p12': 75, 'p13': 70,
            'p14': 45}

minlim = 290
maxlim = 310
result_list = set()  
iterations = 500    

def combinations(iterations, product_list, lb, ub):
    for int in range(iterations):
        combo_size = random.randint(2, len(product_list) - 1)
        combo_list = random.sample(list(product_list.keys()), combo_size)
        combo_sum = sum([product_list[i] for i in combo_list])
        
        if lb <= combo_sum <= ub:
            result_list.add(tuple(combo_list))

combinations(iterations, products, minlim, maxlim)

for r in result_list:
    print(r)

print("\nTotal Sets:", len(result_list), "\n")
