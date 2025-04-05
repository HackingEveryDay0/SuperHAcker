for i in range(1, 101):
    if i < 2:  
        print(f"{i} Not Prime")
        continue  
    is_prime = True  
    for j in range(2, int(i ** 0.5) + 1): 
        if i % j == 0:  
            is_prime = False  
            break  
    if is_prime:
        print(f"{i} Prime")
    else:
        print(f"{i} Not Prime")