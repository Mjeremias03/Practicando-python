def sum_numeros(numeros, target):
    def find_combinations(remaining, current_combination):
        if sum(current_combination) == target:
            print(current_combination)
            result.append(current_combination)
        elif sum(current_combination) < target:
            for i, num in range(i, len(remaining)):
                # print(i,num)
                find_combinations(remaining[i + 1:], current_combination + [num])

    result = []
    find_combinations(numeros, [])
    return result

resultado = sum_numeros([1, 5, 3, 2], 6)
print(resultado)

# def find_sum (numeros:list,target:int) -> list:
#     def sum_num (start,combination):
#      return
#     result = []
#     sum_num(0,[])
# print(find_sum([1,5,2,3],6))