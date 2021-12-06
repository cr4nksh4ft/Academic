from random import sample
import numpy as np
vector=[int(input("Element {}:".format(i+1))) for i in range(int(input("No. of items:")))]
k=int(input("No. of clusters:"))
centroids=np.sort(sample(vector,k))
print("\nInitial Centroids:",centroids,sep=" ")
curr_clusters=np.array([])
prev_clusters=np.array([])
print("\nIntermediate clusters:")
while(True):
    temp=[[] for _ in range(k)]
    prev_clusters=curr_clusters
    for item in vector:
        diff=abs(centroids-item)
        index=np.where(diff==min(diff))[0][-1]
        temp[index].append(item)
    else:
        curr_clusters=np.array(temp,dtype=object)
        centroids=np.sort(list(map(lambda x:sum(x)/len(x),temp)))
        print("")
        for i in range(k):
            print("k{}:".format(i+1),curr_clusters[i],sep=" ")
        else:
            if(np.array_equal(curr_clusters,prev_clusters)):
                break
            for i in range(k):
                print("m{}:".format(i+1),centroids[i],sep=" ")
print("\nCluster repetition observed. Therefore, final clusters are:")
print(*curr_clusters,sep="\n")