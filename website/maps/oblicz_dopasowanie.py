import numpy as np
import pandas as pd
df = pd.read_excel('./website/maps/dane/Zeszyt1.xlsx')

destination_list = df['destination'].to_list()
column_names_list = df.columns.tolist()
# print('TYP FGH',type(df.iloc[0][4]))
# print(df.iloc[0][4])
def oblicz_dopasowanie(answers):
    lis =[]
    print('TWOJA FUNKCJA', answers)
    for i in range(len(destination_list)):
        b=0
        zero_found = False
        for a in answers:
            s = df.iloc[i][column_names_list.index(a)]
            print(s)
            b += float(s)
            if s == 0:
                zero_found = True
        
        if zero_found:
            lis.append(0)
        else:
            lis.append(b)

    
    return lis

