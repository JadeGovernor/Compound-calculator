# 💰 财富自由模拟器 (Wealth Simulator)

> 一个基于 Python Streamlit 的复利计算与资产可视化工具。

## 📖 项目简介
作为训练项目，我开发了这个工具来帮助用户直观地理解**复利效应**。用户只需输入本金、年化收益率和年限，即可实时看到资产增长的指数曲线。

## 🚀 核心功能
- **参数交互**：通过侧边栏动态调整本金、利率和年限。
- **可视化图表**：实时生成资产增长折线图。
- **数据透明**：支持查看每年的详细本息数据表。

## 🛠️ 技术栈
- **核心语言**: Python 3.11
- **前端框架**: Streamlit
- **数据处理**: Pandas, NumPy

## 💻 如何运行
如果你想在本地运行这个项目：

1. 克隆项目
\`\`\`bash
git clone https://github.com/JadeGovernor/Compound-calculator.git
\`\`\`

2. 安装依赖
\`\`\`bash
pip install streamlit pandas
\`\`\`

3. 启动应用
\`\`\`bash
streamlit run app.py
\`\`\`

## 📝 待办清单 (Roadmap)
- [ ] 增加“每年追加定投”功能
- [ ] 增加“通货膨胀率”调整
- [ ] 部署到 Streamlit Cloud (让手机也能访问)
