import pandas as pd
import json

# 先读入 JSON
with open("my_dict.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# 转换成 DataFrame
df = pd.DataFrame(data)

# 转置一下行列（因为通常想要每一行是一个tracker，每一列是一个属性）
df = df.transpose()

# 写入 Excel
df.to_excel("output.xlsx", index=True)
