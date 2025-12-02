import streamlit as st
import pandas as pd

# 1. 标题
st.title('💰 财富自由模拟器 (复利计算)')

# 2. 侧边栏：输入参数
st.sidebar.header('输入你的投资参数')
principal = st.sidebar.number_input('初始本金 (元)', value=10000, step=1000)
rate = st.sidebar.slider('年化收益率 (%)', 1.0, 20.0, 5.0) / 100
years = st.sidebar.slider('投资年限 (年)', 1, 50, 20)

# 3. 核心逻辑：计算复利
data = []
current_amount = principal
for year in range(years + 1):
    data.append([year, current_amount])
    current_amount = current_amount * (1 + rate)

# 4. 数据可视化
df = pd.DataFrame(data, columns=['Year', 'Amount'])

st.subheader(f'{years} 年后的资产总额：')
st.markdown(f"## ¥ {df['Amount'].iloc[-1]:,.2f}") # 格式化金额

# 画折线图
st.line_chart(df.set_index('Year'))

# 展示详细表格
if st.checkbox('显示详细数据表'):
    st.write(df)
