import pandas as pd
import random
import os

# 👉 确保 data 文件夹存在
os.makedirs("data", exist_ok=True)

data = []

# 正常数据（1000条）
for i in range(1000):
    weight = random.normalvariate(60, 10)
    data.append({"name": f"user_{i}", "weight": round(weight, 2)})

# 异常数据
data.append({"name": "abnormal_1", "weight": 10})
data.append({"name": "abnormal_2", "weight": 250})
data.append({"name": "abnormal_3", "weight": 300})

df = pd.DataFrame(data)

# 保存
df.to_excel("data/sample.xlsx", index=False)

print("数据已生成：data/sample.xlsx")