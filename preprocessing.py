import pandas as pd

# 'data_final_vol1.csv' là file 'data_final.csv' đã được xử lý sơ qua bằng công cụ excel
df = pd.read_csv('data_final_vol1.csv')

# #lowercase toàn bộ cột text
df['text'] = df['text'].apply(lambda x: x.lower() if isinstance(x,str) else x)

# #thêm dấu chấm vào những câu ko có dấu kết thúc câu
df['text'] = df['text'].apply(lambda x: x +'.' if isinstance(x,str) and not (x.endswith(".") or x.endswith("?") or x.endswith("!")) else x)

df.to_csv('data_final_vol2.csv', encoding='utf-8-sig')