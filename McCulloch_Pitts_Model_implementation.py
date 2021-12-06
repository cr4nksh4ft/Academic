import itertools
#INPUT
no_of_inputs = int(input('Enter no. of inputs:'))
b = [0]*no_of_inputs+[1]*no_of_inputs
possible_weights = set(itertools.permutations([1]*no_of_inputs+[-1]*no_of_inputs,no_of_inputs))
t = 0
rules = []
print('\t'.join([f'x{i}' for i in range(no_of_inputs)])+'\ty')
for inp in set(itertools.permutations(b,no_of_inputs)):
    y = int(input('\t'.join(map(str,inp))+'\t'))
    if(not any(inp) and y==0):
        t = 1
    rules.append((*inp,y))

#ANALYZE CONDITIONS
conditions=[]
for rule in rules:
    terms = tuple(itertools.compress([f'w{i}' for i in range(no_of_inputs)],rule[:-1]))
    if(terms):
        term_sum = '+'.join(terms)
        if(rule[-1]==1):
            conditions.append(term_sum+'>=t')
            continue
        else:
            conditions.append(term_sum+'<t')
#conditions generated so far
print('\nCONDITIONS: ',*conditions,sep="\n")

#FIND WEIGHTS AND t
def evaluate(weight_dict,condition_list,t):
    for key,val in weight_dict.items():
        exec(key + '=val')
    print('\nWEIGHTS ',weight_dict)
    for condition in condition_list:
        if(eval(condition)==False):
            print('\tDID NOT SATISFY',condition,'HENCE SKIPPED')
            return False
        print('\tSATISFIED',condition)
    return True
        
i = 1 if t>0 else -1
threshold_found = False
while(not threshold_found):
    print(f'\n\n------- FOR t = {t} -------')
    for candidate in possible_weights:
        weight_dict = {f'w{i}':val for i,val in enumerate(candidate)}
        if(evaluate(weight_dict,conditions,t)):
            print('\nWEIGHTS',weight_dict,'SATISFY ALL CONDITIONS FOR THRESHOLD',t)
            print('\nANSWER')
            print('\t->THRESHOLD = ',t)
            print('\t->WEIGHTS = ',weight_dict)
            threshold_found = True
            break
    t = t + i
