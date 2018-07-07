import pandas as pd

data = {
"train" : pd.read_csv("data/train.csv", iterator=True),
"town_state" : pd.read_csv("data/town_state.csv"),
"producto_tabla" : pd.read_csv("data/producto_tabla.csv"),
"cliente_tabla" : pd.read_csv("data/cliente_tabla.csv")
}

train = data["train"].get_chunk(1000)