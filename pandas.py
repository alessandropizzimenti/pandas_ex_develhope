import pandas as pd
import numpy as np

data = np.random.randint(1, 100, size=(10, 4))
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

def evidenzia_colonne(x):
    color = {
        'A': 'background-color: yellow',
        'B': 'background-color: lightgreen',
        'C': 'background-color: lightblue',
        'D': 'background-color: lightcoral'
    }
    return [color.get(col, '') for col in x.index]  

styled_df = df.style.apply(evidenzia_colonne, axis=0) 

styled_df