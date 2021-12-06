import itertools
from collections import Counter
#Dataset
D=[
{'LED', 'WIRES', 'CAPACITOR'},
{'LED', 'TRANSFORMER'},
{'RESISTANCE'},
{'LED', 'RESISTANCE'},
{'TRANSISTOR', 'CAPACITOR'},
{'WIRES', 'LED'},
{'LED', 'WIRES', 'RESISTANCE'},
{'BATTERY', 'LED', 'WIRES'},
{'FUSE', 'BATTERY', 'CAPACITOR', 'TRANSISTOR'},
{'FUSE', 'LED','WIRES'},
{'FUSE', 'WIRES'},
{'WIRES', 'LED', 'FUSE'},
{'CAPACITOR', 'TRANSISTOR', 'LED'},
{'TRANSFORMER', 'RESISTANCE'},
{'SWITCH', 'LED', 'WIRES'},
{'SWITCH', 'RESISTANCE'},
{'LED', 'TRANSFORMER'},
{'RESISTANCE'},
{'WIRES', 'SWITCH','LED'},
{'FUSE','SWITCH'}
]

L=[]
initial_count=Counter(itertools.chain.from_iterable(D))
#C1
print("::::::C[1]::::::")
[print(key,':',value) for key, value in initial_count.items()]
#minimum support count
supp=2
temp=list(filter(lambda x:x[1]>=supp,initial_count.items()))
L.append([item[0] for item in temp])
#L1
print("\n::::::L[1]::::::")
print(*L[0],sep="\n")
items=L[0]
#Iterate
k=2
while(True):
    #Stopping condition
    if(not L[k-2]):
        print("\nL is empty. Loop Stopped")
        print("\n::::::FREQUENT ITEMSET::::::",*L[k-3],sep="\n")
        break
    #Combinations
    combis=list(itertools.combinations(items,k))
    C={item:0 for item in combis}
    for d in D:
        for combi in combis:
            combi_temp=set(combi)
            if(combi_temp.issubset(d)):
                C[combi]=C[combi]+1
    #Ck
    print("\n::::::C[{}]::::::".format(k))
    [print(key," : ",value) for key, value in C.items()]
    selected_from_C=list(filter(lambda x:x[1]>=supp,C.items()))
    #[print(key," : ",value) for key, value in dict(selected_from_C).items()]
    L.append([item[0] for item in selected_from_C])
    items=list(set(itertools.chain.from_iterable(L[-1])))
    #Lk
    print("\n::::::L[{}]::::::".format(k),*L[-1],sep="\n")
    k+=1
