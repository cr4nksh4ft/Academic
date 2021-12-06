import numpy as np
from math import sqrt
from operator import itemgetter
n = int(input("Enter the no. of nodes:"))
adj_matrix = []
for _ in range(n):
    adj_matrix.append(list(map(int,input().split())))
transpose_adj_matrix = list(zip(*adj_matrix))
transpose_adj_matrix = np.array(transpose_adj_matrix)
u = np.array([[1]*n])
v = np.matmul(transpose_adj_matrix,u.T)
u = np.matmul(adj_matrix,v)
u=list(u.flatten())
v=list(v.flatten())
table = [[i,u[i],v[i]] for i in range(n)]
hub = [[item[0],item[1]] for item in table]
authority = [[item[0],item[2]] for item in table]
print("Iteration 1")
print("Node Hub Authority")
print(*table,sep="\n")
print("Hub Rank(Descending): ",*sorted(hub,key=itemgetter(1),reverse=True),sep=" ")
print("Authority Rank(Descending): ",*sorted(authority,key=itemgetter(1),reverse=True),sep=" ")
count=2
while(True):
    print(f'\nIteration {count}')
    temp1=[item[1]**2 for item in hub]
    temp2=[item[1]**2 for item in authority]
    sum_hub = round(sqrt(sum(temp1)),3)
    sum_auth = round(sqrt(sum(temp2)),3)
    new_hub = [[i,round(hub[i][1]/sum_hub,3)] for i in range(n)]
    new_authority = [[i,round(authority[i][1]/sum_auth,3)] for i in range(n)]
    table=[[i,new_hub[i][1],new_authority[i][1]] for i in range(n)]
    print("Node Hub Authority")
    print(*table,sep="\n")
    print("Hub Rank(Descending): ",*sorted(new_hub,key=itemgetter(1),reverse=True),sep=" ")
    print("Authority Rank(Descending): ",*sorted(new_authority,key=itemgetter(1),reverse=True),sep=" ")
    if(new_hub==hub and new_authority==authority):
        print("\nVALUES HAVE CONVERGED")
        break
    hub = new_hub
    authority = new_authority
    count+=1
print("\nFINAL HUB & AUTHORITY RANKS:\n")
print("Node Hub Authority")
print(*table,sep="\n")
print("Hub Rank(Descending): ",*sorted(new_hub,key=itemgetter(1),reverse=True),sep=" ")
print("Authority Rank(Descending): ",*sorted(new_authority,key=itemgetter(1),reverse=True),sep=" ")
