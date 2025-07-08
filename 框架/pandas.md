

加载excel 得到DataFrame
```
df = pd.read_excel('data.xlsx')
```

加载第几行  第几列
```
df.iloc[2, 1]  # 第3行、第2列
batch_df = df.iloc[0:20]  #0-20行
```

获取DataFrame 的行标签（默认是 0, 1, 2...）
```
print(df.index)
# 输出: RangeIndex(start=0, stop=100, step=1)
```

获取 DataFrame 所有列名
```
print(df.columns)
# 输出: Index(['index', '问题', '描述'], dtype='object')
```

逐行遍历 DataFrame，返回每一行的索引和对应的 Series（即一行数据）
```
for idx, row in df.iterrows():
    print(row['问题'])
```

将DataFrame保存为excel
```
result_df.to_excel('processed_data.xlsx', index=False)  #不保存自动生成的索引列
```

判断表格是不是为空值 not nan     与isna()相反
```
s = pd.Series([1, np.nan, 3, None])
print(pd.notna(s))
输出：
0     True
1    False
2     True
3    False
dtype: bool
```