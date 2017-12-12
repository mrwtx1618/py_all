#encoding:utf8
import pandas as pd
import numpy as np
transactions2 = pd.read_excel('C:/Users/Administrator/Desktop/transactions2.xlsx')
# print(transactions2)
# print(type(transactions2))
accounts_unique = transactions2['account_id'].unique()
# print(accounts_unique)
# print((accounts_unique).shape)
accounts_ids = np.random.choice(accounts_unique,int(0.1*len(accounts_unique)),replace=False)
# print(accounts_ids.shape)
accounts_id_map = dict(zip(accounts_ids,range(len(accounts_ids))))
# print(accounts_id_map)
transactions2 = transactions2.loc[transactions2['account_id'].isin(accounts_ids)]
# print(transactions2)
# print(transactions2.shape)

n_accounts = len(accounts_id_map)
print(n_accounts)
# n_items = len(set(product_maps.values))

x = [accounts_id_map[a] for a in transactions2.account_id.values]
y = transactions2.product_id.values
print(x)
print(len(x))
print('/////////////////////////')
print((y))
Q = np.zeros((n_accounts,100))
print(Q)
global_means = Q.mean()
users_mean = Q.mean(axis=1,keepdims=True)
item_mean = Q.mean(axis=0,keepdims=True)
for u,i in zip(x,y):
    Q[u,i] +=1
print(Q)















