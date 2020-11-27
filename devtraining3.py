import requests
import sys
import pandas as pd
import json

apiKey = '41e69395fab584f609bdbd830038841d'
secretKey = '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'
password = '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'

r = requests.get("https://41e69395fab584f609bdbd830038841d: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@anhvu2103.myshopify.com/admin/api/2020-10/customers.json")
# print(r.json())
df = pd.DataFrame(r)
df.to_csv(r'/Users/duyanh2103/desktop/python/export.csv', index = False, header = True)
print(df)
