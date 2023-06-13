import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

class ML:
    def create_model(self, csv_file):

        data = pd.read_csv(csv_file, delimiter=r"\s+", names=[  'CRIM', 'ZN', 'INDUS',
                                                                'CHAS', 'NOX', 'RM', 'AGE',
                                                                'DIS', 'RAD', 'TAX', 'PTRATIO',
                                                                'B', 'LSTAT', 'TARGET'
                                                                ])
        #Explore data
        data.head()
        data.describe()
        data.info()

        #Get Target
        x = data.loc[:, data.columns != 'TARGET']
        y = data['TARGET']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        # Create a linear regression model
        model = LinearRegression().fit(x_train, y_train)

        scores = model.score(x_test, y_test)

        #print(scores)

        return model, scores
