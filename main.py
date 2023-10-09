import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラム')

expnder1 = st.expander('問い合わせ１')
expnder1.write('問い合わせ１の回答')

expnder2 = st.expander('問い合わせ2')
expnder2.write('問い合わせ2の回答')

expnder3 = st.expander('問い合わせ3')
expnder3.write('問い合わせ3の回答')

# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの好きな趣味:', text
# 'コンディション:', condition




# if st.checkbox('Shew Image'):
#     img = Image.open('sample.jpg')
#     st.image(img,caption='kuro',use_column_width=True)

