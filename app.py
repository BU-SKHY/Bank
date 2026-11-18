
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

# ==========================================
# 1. 페이지 설정
# ==========================================
st.set_page_config(
    page_title="Bank Customer Analysis",
    page_icon="🏦",
    layout="wide"
)

DATA_URL = "https://github.com/BU-SKHY/Bank/raw/main/bank_customer%20(1).xlsx"

st.title("🏦 Bank Customer Data Analysis")
st.markdown(
    "은행 고객 데이터를 활용한 데이터 탐색 및 시각화 대시보드"
)

# ==========================================
# 2. 데이터 불러오기
# ==========================================
@st.cache_data
def load_data():
    return pd.read_excel(DATA_URL)

uploaded_file = st.sidebar.file_uploader(
    "Upload Excel File",
    type=["xlsx", "xls"]
)

try:
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
    else:
        df = load_data()

    st.sidebar.success("데이터 로드 완료!")

except Exception as e:
    st.error(f"데이터를 불러올 수 없습니다: {e}")
    st.info("Excel 파일을 직접 업로드해 주세요.")
    st.stop()

# ==========================================
# 3. 데이터 전처리
# ==========================================
df.columns = df.columns.astype(str).str.strip()

numeric_cols = df.select_dtypes(
    include=["number"]
).columns.tolist()

categorical_cols = df.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

# ==========================================
# 4. 사이드바 필터
# ==========================================
st.sidebar.header("🔎 Data Filter")

filtered_df = df.copy()

if categorical_cols:
    selected_column = st.sidebar.selectbox(
        "Select Category",
        ["All"] + categorical_cols
    )

    if selected_column != "All":
        values = filtered_df[selected_column].dropna().unique()

        selected_values = st.sidebar.multiselect(
            "Select Values",
            options=values,
            default=list(values)
        )

        filtered_df = filtered_df[
            filtered_df[selected_column].isin(selected_values)
        ]

# ==========================================
# 5. KPI 지표
# ==========================================
st.header("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", f"{len(filtered_df):,}")
col2.metric("Total Columns", len(df.columns))
col3.metric(
    "Missing Values",
    f"{filtered_df.isnull().sum().sum():,}"
)
col4.metric(
    "Duplicate Rows",
    f"{filtered_df.duplicated().sum():,}"
)

st.divider()

# ==========================================
# 6. 데이터 미리보기
# ==========================================
st.header("📋 Dataset Preview")

st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)

with st.expander("Dataset Information"):
    st.write("### Data Types")
    st.dataframe(
        df.dtypes.astype(str).rename("Data Type"),
        use_container_width=True
    )

    st.write("### Statistical Summary")
    st.dataframe(
        df.describe(include="all").T,
        use_container_width=True
    )

# ==========================================
# 7. 결측치 분석
# ==========================================
st.header("🧹 Missing Value Analysis")

missing_df = df.isnull().sum().reset_index()
missing_df.columns = ["Column", "Missing Count"]

missing_df["Missing Percentage"] = (
    missing_df["Missing Count"] / len(df) * 100
).round(2)

col1, col2 = st.columns(2)

with col1:
    st.dataframe(
        missing_df,
        use_container_width=True
    )

with col2:
    fig = px.bar(
        missing_df,
        x="Column",
        y="Missing Count",
        title="Missing Values by Column",
        color="Missing Count"
    )
    st.plotly_chart(fig, use_container_width=True)

# ==========================================
# 8. 수치형 데이터 분석
# ==========================================
st.header("📈 Numerical Data Analysis")

if numeric_cols:
    selected_num = st.selectbox(
        "Select Numerical Column",
        numeric_cols
    )

    col1, col2 = st.columns(2)

    with col1:
        fig = px.histogram(
            filtered_df,
            x=selected_num,
            title=f"Distribution of {selected_num}",
            nbins=30,
            marginal="box"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.box(
            filtered_df,
            y=selected_num,
            title=f"Boxplot of {selected_num}"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Numerical Statistics")

    st.dataframe(
        filtered_df[numeric_cols].describe().T,
        use_container_width=True
    )
else:
    st.info("수치형 데이터가 없습니다.")

# ==========================================
# 9. 범주형 데이터 분석
# ==========================================
st.header("👥 Categorical Data Analysis")

if categorical_cols:
    selected_cat = st.selectbox(
        "Select Categorical Column",
        categorical_cols
    )

    category_counts = (
        filtered_df[selected_cat]
        .fillna("Missing")
        .astype(str)
        .value_counts()
        .reset_index()
    )

    category_counts.columns = ["Category", "Count"]

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            category_counts.head(20),
            x="Category",
            y="Count",
            title=f"{selected_cat} Distribution",
            color="Count"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.pie(
            category_counts.head(10),
            names="Category",
            values="Count",
            title=f"{selected_cat} Composition",
            hole=0.4
        )
        st.plotly_chart(fig, use_container_width=True)
else:
    st.info("범주형 데이터가 없습니다.")

# ==========================================
# 10. 상관관계 분석
# ==========================================
st.header("🔥 Correlation Analysis")

if len(numeric_cols) >= 2:
    corr = filtered_df[numeric_cols].corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
        title="Correlation Heatmap"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("상관관계 분석을 위한 수치형 변수가 부족합니다.")

# ==========================================
# 11. 변수 간 관계 분석
# ==========================================
st.header("🔍 Relationship Analysis")

if len(numeric_cols) >= 2:
    col1, col2 = st.columns(2)

    with col1:
        x_axis = st.selectbox(
            "X Axis",
            numeric_cols,
            index=0,
            key="x_axis"
        )

    with col2:
        y_axis = st.selectbox(
            "Y Axis",
            numeric_cols,
            index=1,
            key="y_axis"
        )

    if x_axis != y_axis:
        fig = px.scatter(
            filtered_df,
            x=x_axis,
            y=y_axis,
            title=f"{x_axis} vs {y_axis}",
            trendline="ols" if len(filtered_df) >= 3 else None
        )

        st.plotly_chart(fig, use_container_width=True)

# ==========================================
# 12. 데이터 다운로드
# ==========================================
st.header("📥 Download Data")

csv = filtered_df.to_csv(
    index=False
).encode("utf-8-sig")

st.download_button(
    label="Download Filtered Data (CSV)",
    data=csv,
    file_name="bank_customer_analysis.csv",
    mime="text/csv"
)

st.success("Bank Customer Analysis Dashboard 실행 완료!")

st.caption("Bank Customer Data Analysis | Python & Streamlit")
