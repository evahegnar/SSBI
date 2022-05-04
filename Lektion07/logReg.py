import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler



#Caveat - vi behöver förstås inkludera fler saker till vår preprocessing för att göra detta till en bra logistic regression modell, nämligen:

# - Balanserad sampling
# - Göra om kategoriska variabler med fler än en kategori till binära kolumner
# - Analysera vilka våra viktigaste predictors är och eventuellt dimensionsreducera/exkludera variabler
# - Ingen metric för hur bra den faktiskt jobbar är gjord! Ansätt en lämplig metric.
# - Cross Validation - testa för olika splits.


# Mycket av detta gås igenom på https://towardsdatascience.com/building-a-logistic-regression-in-python-step-by-step-becd4d56c9c8

dataset = pd.read_csv("HR_file.csv")

#Behöver hantera stringdata, kan använda en LabelEncoder
label_enc = LabelEncoder()
#print(dataset)


#Flera departments - tekniskt sett ett problem, men ingenting som hanterades under lektionen.
print(dataset['Departments '].unique())
print(dataset['salary'].unique())
dataset['Departments '] = label_enc.fit_transform(dataset['Departments '])
dataset['salary'] = label_enc.fit_transform(dataset['salary'])

#Obalanserat - tekniskt sett också ett problem! Vill helst ha detta så balanserat som möjligt.
#Kan lösas med vad undersampling, oversampling, i vissa fall viktad backpropagation.
quitters = list(dataset['Quit the Company'])
print(f'Proportion of quitters: {sum(quitters)/len(quitters)}')


#Dela upp datan till X och Y:

features = list(filter(lambda x: x != 'Quit the Company', dataset.columns))


X = dataset[features]

y = dataset['Quit the Company']



#Normalisera data för att göra den lättare att jobba med
scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X,y)


#Skapa en LogisticRegressionmodell
log = LogisticRegression()

log.fit(X_train, y_train)
print(vars(log))

y_pred = log.predict(X)

y_prob = log.predict_proba(X)[:,1]

dataset['predictions'] = y_pred
dataset['probabilites'] = y_prob

