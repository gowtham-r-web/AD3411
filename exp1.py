import pandas as pd
data = {&quot;calories&quot;: [420, 380, 390], &quot;
duration&quot;: [50, 40,45]}
#load data into a DataFrame object: df =
pd.DataFrame(data)
print (df.loc[0])
