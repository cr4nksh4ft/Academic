#Dictionary acts as matrix which shows directed links
d_graph={
'A':{'A':0,'B':1,'C':1},
'B':{'A':0,'B':0,'C':1},
'C':{'A':1,'B':0,'C':0,'D':1}
}
node_str=d_graph.keys()
outlink={key:list(d_graph[key].values()).count(1) for key in node_str}
rank={key:[1] for key in node_str}
d=0.85
count=0
convergence=False
print("Iteration",*node_str,sep="    ")
while(not convergence):
    count+=1
    temp_rank=[]
    for node in node_str:
        bkt = [(rank[v][-1])/outlink[v] for v in node_str if d_graph[v][node]!=0]
        r=(1-d) + d*(sum(bkt))
        temp_rank.append(r)
        rank[node].append(r)
    print(count,*temp_rank,sep="      ")
    flag=[rank[n][-1]-rank[n][-2] for n in node_str]
    if(not any(flag)):
        convergence=True
