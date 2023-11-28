import string
import numpy as np

print("Enter Values: ")
N,Q = map(int, input().split())
alphabet = list(string.ascii_uppercase)

alphabet = alphabet[:N]
points = [0]*N
answer = []
leverage = 0 

def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

def checkOperator(point_list, operator, indice, seen):
    if (operator == ">") :
        point_list[indice[0]] += 1
    elif (operator == "<"):
        point_list[indice[1]] += 1
    elif (operator == "="):
        seen[tuple([indice[0],indice[1]])] = operator
        return
    else :
        print("input is not operator.")

seen = dict()
i = 0
while i < Q:
    if i == 0 : 
        print(f"? {alphabet[i]} {alphabet[i+1]}")
        indice = [0,1]
        operator = input()
        i += 1
    elif allUnique(points):
        result_index = np.argsort(points).tolist()
        break 
    else:
        min_point = min(points)
        indice = [j for j in range(N) if points[j] == min_point+leverage]
        while len(indice) <= 1:
            leverage +=1
            indice = [j for j in range(len(points)) if points[j] == min_point+leverage]
        if tuple([indice[0],indice[1]]) in seen:
            operator = seen[tuple([indice[0],indice[1]])]
            if operator != "=" : checkOperator(points,operator,indice,seen)
        else:
            print(f"? {alphabet[indice[0]]} {alphabet[indice[1]]}")
            operator = input()
            i += 1    
    checkOperator(points,operator,indice,seen)
    if not(tuple([indice[0],indice[1]]) in seen): 
        seen[tuple([indice[0],indice[1]])] = operator

result_index = np.argsort(points).tolist()
sorted_list = [alphabet[index] for index in result_index]

print(f"! {''.join(sorted_list)}")
