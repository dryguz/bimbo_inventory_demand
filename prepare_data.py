import pandas as pd


data = {
"train" : pd.read_csv("data/train.csv", iterator=True),
"town_state" : pd.read_csv("data/town_state.csv"),
"producto_tabla" : pd.read_csv("data/producto_tabla.csv"),
"cliente_tabla" : pd.read_csv("data/cliente_tabla.csv")
}

train = data["train"].get_chunk(1000)



# data["train"] = pd.read_csv("data/train.csv")
ext_train = pd.merge(train, data['producto_tabla'], how='left', on='Producto_ID')
ext_train = pd.merge(ext_train, data['cliente_tabla'], how='left', on='Cliente_ID')
ext_train = pd.merge(ext_train, data['town_state'], how='left', on='Agencia_ID')

