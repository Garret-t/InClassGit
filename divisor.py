def divisors(a):
    div_list = []
    for i in range(1, a+1):
        if a % i == 0:
            div_list.append(i)
    return div_list

print(divisors(int(input("Divisors for: "))))