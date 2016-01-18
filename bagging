#------------
# Bagging
#------------
import glob
import pandas as pd
import csv

#path =r'/home/balazs/Downloads/rossmann' # use appropriate path
#allFiles = glob.glob(path + "/*.csv")
#frame = pd.DataFrame()
#list_ = []
#for file_ in allFiles:
#    df = pd.read_csv(file_,index_col=None, header=0)
#    list_.join(df)
#frame = pd.append(list_)

#df0 = pd.read_csv('rf2.csv')
df1 = pd.read_csv('11884.csv')
df2 = pd.read_csv('12003.csv')
df3 = pd.read_csv('12017.csv')
df4 = pd.read_csv('12300.csv')
df5 = pd.read_csv('12488.csv')
df6 = pd.read_csv('12553.csv')
df7 = pd.read_csv('12628.csv')
df8 = pd.read_csv('12769.csv')
df9 = pd.read_csv('12792.csv')

df10 = pd.read_csv('13235.csv')
df11 = pd.read_csv('13462.csv')
df12 = pd.read_csv('13484.csv')
df13 = pd.read_csv('13491.csv')
df14 = pd.read_csv('13550.csv')
df15 = pd.read_csv('13580.csv')
df16 = pd.read_csv('13913.csv')
df17 = pd.read_csv('13945.csv')
df18 = pd.read_csv('13962.csv')



#results = (df1.Sales * 0.985 + df2.Sales * 0.985 + df3.Sales * 0.985 + \
#            df4.Sales * 0.985 + df5.Sales * 0.985 + df6.Sales * 0.985 + \
#            df7.Sales * 0.985 + df8.Sales * 0.985 + df9.Sales * 0.985) / 9.0
            
#results = (df1.Sales * 0.985 + df2.Sales * 0.985 + df3.Sales * 0.985 + \
#            df4.Sales * 0.985 + df5.Sales * 0.985) / 5.0
            
results = (df1.Sales * 0.985 + df2.Sales * 0.985 + df3.Sales * 0.985 + \
            df4.Sales * 0.985 + df5.Sales * 0.985 + df6.Sales * 0.985 + \
            df7.Sales * 0.985 + df8.Sales * 0.985 + df9.Sales * 0.985 + \
            df10.Sales * 0.985 + df11.Sales * 0.985 + df12.Sales * 0.985 + df13.Sales * 0.985 + \
            df14.Sales * 0.985 + df15.Sales * 0.985 + df16.Sales * 0.985 + \
            df17.Sales * 0.985 + df18.Sales) / 18.0
            
            
results = pd.DataFrame(results)
results.T
results.columns = ['Sales']
results.index += 1
results.to_csv('bagged.csv', index_label='Id')
