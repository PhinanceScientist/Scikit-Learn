import pandas as pd
import sklearn

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

if __name__ =="__main__":
    dataset = pd.read_csv('../Data/whr2017.csv')
    print(dataset.describe())

    x = dataset[['gdp','family','lifexp','freedom', 'corruption', 'generosity', 'dystopia']]
    y = dataset[['score']]

    print(x.shape)
    print(y.shape)

    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25)

    modelLinear = LinearRegression().fit(x_train, y_train)
    y_predict_linear = modelLinear.predict(x_test)


    modelLasso = Lasso(alpha=0.02).fit(x_train, y_train)
    y_predict_lasso = modelLinear.predict(x_test)

    modelRidge = Ridge(alpha=1).fit(x_train, y_train)
    y_predict_Ridge = modelRidge.predict(x_test)

    linear_loss = mean_squared_error(y_test, y_predict_linear)
    print('Linear Loss: ', linear_loss)

    lasso_loss = mean_squared_error(y_test, y_predict_lasso)
    print('Lasso Loss: ', lasso_loss)

    ridge_loss = mean_squared_error(y_test, y_predict_Ridge)
    print('Ridge Loss: ', ridge_loss)

    print ("="*32)
    print ("Coef Lasso")
    print (modelLasso.coef_)

    print ("Coef Ridge")
    print (modelRidge.coef_)





