from sklearn import linear_model
import pickle
import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv(r"C:\Users\user\Desktop\LINEAR_REGRESSION_DATA.csv")
mymodel=linear_model.LinearRegression()
mymodel.fit(df[['year']] ,df.pca)
with open('Year_PerCapita_USA_LinearModel','wb') as f:
    pickle.dump(mymodel,f)
plt.scatter(df[['year']],df.pca)
plt.plot(df[['year']],mymodel.predict(df[['year']]))
plt.title('PerCapitaIncome_of_USA')
plt.xlabel('Year')
plt.ylabel('Income in $')
plt.grid()
plt.show()
plt.savefig("YearPerCapitaIncome.png",facecolor='w', edgecolor='w',transparent=True)