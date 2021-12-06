import csv
def parseFile(filename):
    #parse data from file
    with open(filename,'r') as csvfile:
        csvreader=csv.reader(csvfile)
        #Omit first row. Column headings.
        next(csvreader)
        #create list of tuples
        records=list(map(tuple,csvreader))
    return records

def calcProb(test_tuple):
    try:
        #filter yes & no tuples
        y_tup=list(filter(lambda x:x[-1]=="Y",records))
        n_tup=list(filter(lambda x:x[-1]=="N",records))
        #CALCULATE PROBABILITY
        prob_y,prob_n=len(y_tup)/len(records),len(n_tup)/len(records)
        print("P(yes)",prob_y,sep=":")
        print("P(no)",prob_n,sep=":")
        prob_ty,prob_tn=1,1
        for value in test_tuple:
            prob_ty*=(sum(x.count(value) for x in y_tup)/len(y_tup))
            prob_tn*=(sum(x.count(value) for x in n_tup)/len(n_tup))
        print("P(t|yes)",prob_ty,sep=":")
        print("P(t|no)",prob_tn,sep=":")
        prob_t=(prob_ty*prob_y)+(prob_tn*prob_n)
        print("P(t)",prob_t,sep=":")
        prob_yt=(prob_ty*prob_y)/prob_t
        prob_nt=(prob_tn*prob_n)/prob_t
        print("P(yes|t)",prob_yt,sep=":")
        print("P(no|t)",prob_nt,sep=":")
        return "Yes" if prob_yt>prob_nt else "No"
    except Exception as e:
        print("Naive Bayes algorithm failed!")
        print("Reason:",e,sep=" ")
        return "Not Defined"

#Input & Output
fpath=input("Enter csv file path: ")
records=parseFile(fpath)
for i in range(int(input("No. of test records: "))):
    inp=input("Enter test record[{}]: ".format(i+1)).split(",")
    test_tuple=tuple(map(lambda x:x.strip(),inp))
    #test_tuple=tuple(input("Enter test record[{}]: ".format(i)).split(","))
    print("Classified as:",calcProb(test_tuple),sep=" ")
