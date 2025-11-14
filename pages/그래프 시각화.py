import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

# 한글 폰트 설정
font_path = os.path.join(os.path.dirname(__file__), '../fonts/NanumGothic-Regular.ttf')
fm.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

st.set_page_config(page_title="그래프 시각화", layout="wide")
st.title("📊 그래프 시각화")
st.write("matplotlib을 활용한 다양한 그래프 예시")

# 1. 선 그래프 (Line Chart)
st.subheader("1️⃣ 선 그래프")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    ax.plot(x, y, linewidth=2, color='blue', label='sin(x)')
    ax.set_xlabel('X 축')
    ax.set_ylabel('Y 축')
    ax.set_title('sin 함수 그래프')
    ax.grid(True, alpha=0.3)
    ax.legend()
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    ax.plot(x, y1, label='sin(x)', linewidth=2)
    ax.plot(x, y2, label='cos(x)', linewidth=2)
    ax.set_xlabel('X 축')
    ax.set_ylabel('Y 축')
    ax.set_title('sin과 cos 함수 비교')
    ax.grid(True, alpha=0.3)
    ax.legend()
    st.pyplot(fig)

# 2. 막대 그래프 (Bar Chart)
st.subheader("2️⃣ 막대 그래프")
fig, ax = plt.subplots(figsize=(10, 5))
categories = ['데이터1', '데이터2', '데이터3', '데이터4', '데이터5']
values = [45, 38, 52, 41, 58]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
bars = ax.bar(categories, values, color=colors, edgecolor='black', linewidth=1.5)
ax.set_ylabel('값')
ax.set_title('카테고리별 데이터 비교')
ax.set_ylim(0, 70)

# 값 표시
for bar, value in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
            str(value), ha='center', va='bottom', fontweight='bold')

st.pyplot(fig)

# 3. 산점도 (Scatter Plot)
st.subheader("3️⃣ 산점도")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(8, 5))
    np.random.seed(42)
    x = np.random.randn(100)
    y = np.random.randn(100)
    colors = np.random.rand(100)
    scatter = ax.scatter(x, y, c=colors, s=100, cmap='viridis', alpha=0.6, edgecolors='black')
    ax.set_xlabel('X 축')
    ax.set_ylabel('Y 축')
    ax.set_title('무작위 데이터 산점도')
    plt.colorbar(scatter, ax=ax)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.linspace(0, 10, 50)
    y = 2 * x + 5 + np.random.normal(0, 3, 50)
    ax.scatter(x, y, s=100, alpha=0.6, color='red', edgecolors='darkred', linewidth=1)
    # 추세선
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    ax.plot(x, p(x), "b--", linewidth=2, label='추세선')
    ax.set_xlabel('X 축')
    ax.set_ylabel('Y 축')
    ax.set_title('선형 추세 분석')
    ax.legend()
    st.pyplot(fig)

# 4. 히스토그램 (Histogram)
st.subheader("4️⃣ 히스토그램")
fig, ax = plt.subplots(figsize=(10, 5))
data = np.random.normal(100, 15, 1000)
ax.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
ax.set_xlabel('값')
ax.set_ylabel('빈도')
ax.set_title('정규분포 데이터 히스토그램')
ax.grid(True, alpha=0.3, axis='y')
st.pyplot(fig)

# 5. 파이 차트 (Pie Chart)
st.subheader("5️⃣ 파이 차트")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(8, 6))
    labels = ['항목A', '항목B', '항목C', '항목D']
    sizes = [30, 25, 20, 25]
    colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.set_title('전체 구성 비율')
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(8, 6))
    labels = ['구매', '환불', '반품', '기타']
    sizes = [60, 20, 15, 5]
    explode = (0.05, 0, 0, 0)
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
    ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=45)
    ax.set_title('거래 현황')
    st.pyplot(fig)

# 6. 박스플롯 (Box Plot)
st.subheader("6️⃣ 박스플롯")
fig, ax = plt.subplots(figsize=(10, 5))
np.random.seed(42)
data_sets = [np.random.normal(100, 20, 100) for _ in range(4)]
bp = ax.boxplot(data_sets, labels=['그룹1', '그룹2', '그룹3', '그룹4'], patch_artist=True)

colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

ax.set_ylabel('값')
ax.set_title('그룹별 데이터 분포')
ax.grid(True, alpha=0.3, axis='y')
st.pyplot(fig)

st.divider()
st.info("💡 Tip: 이 페이지는 matplotlib을 활용한 다양한 그래프 시각화 예시입니다.")
