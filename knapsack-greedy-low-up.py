# upper-lower-bound
# Mohammad Mehdi Khosravi

import numpy as np
import pandas as pd

# Data & Parameters
n = 7
b = 50
w = [10, 12, 7, 6, 14, 7, 8]
v = [20, 12, 70, 30, 28, 28, 24]

# Define a range
nr = np.arange(0,7)
t  = np.arange(0,7)

# Make a Vi/Wi column

A =[]  
for j in nr:
    t[j] = v[j]/w[j]
    A.append(t[j])
        

# Make a Dataframe using Pandas
df = pd.DataFrame({
    'I':nr,
    'W':w,
    'V':v,
  'V/W':A
                 })

# Sort The Values by 'Vi/Wi'
dfs = df.sort_values(by='V/W',ascending=False)

############ Show The initial result:
print('initial table: ')
print(df)
print('#####################')
print('Sorted table: ')
print(dfs)
print('#####################')


Nd = dfs.to_numpy()


count_w = 0
count_v = 0
Result = []

#up
count_w_up = 0
count_v_up = 0
Result_up = []

#flag
flag1=True

# Main Algorithm
for i in nr:
        if (count_w+Nd[i][1]) <= b:
            
            count_w = count_w + Nd[i][1]
            #print(count_w)
            
            Result.append(Nd[i][0])
            #print(Result)
            Result_up.append(Nd[i][0])  # for upper
            
            count_v = count_v+Nd[i][2]
            #print(count_v)
        else:
            # upper bound
            if flag1 == True:
                Zarib = ((b - count_w) / Nd[i][1] ) * Nd[i][2]
                count_w_up = b
                count_v_up = count_v + Zarib
                
                if Zarib != 0:
                    Result_up.append(str(Nd[i][0])+' Relaxed')
                
                print('')
                print('upper-bound results')
                print(Result_up)
                print('W : ', count_w_up)
                print('V up: ', count_v_up)

                flag1 = False
            
        

# Show the final result

print('')
print('lower-bound results')
print(Result)
print('W : ', count_w)
print('V low: ', count_v)