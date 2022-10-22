from turtle import width
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
st.title("割り勘")

st.write("明細")

'Start'
latest_iteration =st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)
'Done!!!'

option = st.text_input('趣味')
'あなたの趣味は',option


condition = st.slider('調子',0,100,50)
'コンディション：',condition

left_column,right_column=st.columns(2)
button=left_column.button('右カラムに文字を表示')
if button:
    right_column.write('trueeeeeee')

expander=st.expander('問合せ')
expander.write('問合せ内容を書く')

st.write('Display Image')

option = st.selectbox(
    '好きなもの',
    list(range(1, 10))
)

'あなたの好きな数字は',option,'です。'

if st.checkbox('show image'):
    img = Image.open('sample.jpeg')
    st.image(img, caption='okane', use_column_width=True)


df =pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})
st.write(df)
st.dataframe(df.style.highlight_max(axis=0),width=180,height=180)
st.table(df.style.highlight_max(axis=0))

"""

# あああ

## いいい
``` python
st.write("明細")

df =pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})
st.write(df)
st.dataframe(df.style.highlight_max(axis=0),width=180,height=180)
st.table(df.style.highlight_max(axis=0))
```
### ううう

"""

df2 =pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3 =pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)

st.map(df3)
