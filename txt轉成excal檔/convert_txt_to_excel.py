import pandas as pd

# 輸入txt文件名
input_file = "ABC.txt"

# 讀取txt文件
df = pd.read_csv(input_file, delimiter="\t", header=None)

# 將DataFrame保存為Excel文件
output_file = "測試.xlsx"
df.to_excel(output_file, index=False, header=False)
