import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import joblib
from sklearn.datasets import load_iris

# ตั้งค่าหน้าเพจ
st.set_page_config(
    page_title="Iris Flower Classifier - Pink Edition",
    page_icon="🌸",
    layout="wide"
)

# ตกแต่ง CSS เพิ่มเติมสำหรับธีมสีชมพูพาสเทลและความละมุนของหน้าเว็บ
st.markdown("""
    <style>
    .stApp {
        background-color: #fff1f2;
    }
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #fce7f3;
    }
    .stButton button {
        background: linear-gradient(135deg, #ec4899, #f43f5e);
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        box-shadow: 0 4px 10px rgba(244, 63, 94, 0.3);
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #db2777, #e11d48);
        color: white;
        box-shadow: 0 6px 15px rgba(225, 29, 72, 0.4);
    }
    h1, h2, h3, h4, p, label {
        color: #475569 !important;
    }
    </style>
""", unsafe_allow_html=True)

# โหลดข้อมูล Iris Dataset เพื่อเอาค่าเฉลี่ยมาเปรียบเทียบ
iris = load_iris()
feature_names = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
species_names = iris.target_names

# คำนวณค่าเฉลี่ยของ Dataset แต่ละ Feature
df_iris = pd.DataFrame(iris.data, columns=feature_names)
dataset_averages = df_iris.mean().values

# โหลดโมเดลที่เทรนไว้ (หากไม่มีไฟล์โมเดล ให้สร้างโมเดลตัวอย่างชั่วคราว)
@st.cache_resource
def load_model():
    try:
        model = joblib.load('iris_model.pkl')
    except Exception:
        from sklearn.ensemble import RandomForestClassifier
        model = RandomForestClassifier(random_state=42)
        model.fit(iris.data, iris.target)
    return model

model = load_model()

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("### 🌸 Control Panel")
    st.caption("Adjust the sliders to input flower measurements:")
    
    sepal_length = st.slider("📏 Sepal Length (cm)", min_value=4.0, max_value=8.0, value=7.10, step=0.01)
    sepal_width = st.slider("📏 Sepal Width (cm)", min_value=2.0, max_value=4.5, value=3.40, step=0.01)
    petal_length = st.slider("📏 Petal Length (cm)", min_value=1.0, max_value=7.0, value=3.80, step=0.01)
    petal_width = st.slider("📏 Petal Width (cm)", min_value=0.1, max_value=2.5, value=1.30, step=0.01)
    
    st.markdown("<br>", unsafe_allow_html=True)
    predict_btn = st.button("✨ Predict Species", use_container_width=True)

# ==================== MAIN CONTENT ====================
st.title("🌸 Iris Flower Classifier Lab")
st.markdown("<p style='color: #64748b; font-size: 16px;'>Explore and predict the species of Iris flowers using Machine Learning in a vibrant pink pastel theme.</p>", unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #fbcfe8;'>", unsafe_allow_html=True)

# คำนวณการทำนาย
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = model.predict(input_data)[0]
probabilities = model.predict_proba(input_data)[0]

predicted_species = species_names[prediction].capitalize()
confidence = probabilities[prediction] * 100

col1, col2 = st.columns([1.1, 1], gap="large")

# ----------------- COLUMN 1: INPUT VISUALIZATION -----------------
with col1:
    st.markdown("### 📈 Input Visualization")
    st.caption("Your Input vs Dataset Average")
    
    fig_bar = go.Figure()
    
    # แท่งแสดงค่า Input ของผู้ใช้ (โทนสีชมพู-โรส)
    fig_bar.add_trace(go.Bar(
        x=feature_names,
        y=[sepal_length, sepal_width, petal_length, petal_width],
        name='Your Input',
        marker_color='#ec4899',
        text=[f"{sepal_length:.1f}", f"{sepal_width:.1f}", f"{petal_length:.1f}", f"{petal_width:.1f}"],
        textposition='auto',
        textfont=dict(color='white', weight='bold')
    ))
    
    # แท่งแสดงค่าเฉลี่ยของ Dataset (โทนสีชมพูอ่อนพาสเทล)
    fig_bar.add_trace(go.Bar(
        x=feature_names,
        y=dataset_averages,
        name='Dataset Average',
        marker_color='#fbcfe8',
        text=[f"{v:.2f}" for v in dataset_averages],
        textposition='auto',
        textfont=dict(color='#831843', weight='bold')
    ))
    
    fig_bar.update_layout(
        barmode='group',
        height=380,
        margin=dict(l=20, r=20, t=20, b=40),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        xaxis_title="Features",
        yaxis_title="Value (cm)",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#475569')
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ----------------- COLUMN 2: PREDICTION RESULT -----------------
with col2:
    st.markdown("### 🎯 Prediction Result")
    
    # การ์ดแสดงผลคำนายโทนสีชมพูพาสเทลไล่ระดับหรูหรา
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(135deg, #ec4899, #f43f5e);
            color: white;
            padding: 30px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0px 8px 20px rgba(236, 72, 153, 0.3);
            margin-bottom: 25px;
        ">
            <h3 style="margin: 0; font-size: 18px; font-weight: 500; color: #fce7f3 !important; opacity: 0.9;">Predicted Species</h3>
            <h1 style="margin: 15px 0; font-size: 42px; font-weight: 700; color: white !important;">{predicted_species}</h1>
            <p style="margin: 0; font-size: 16px; color: #fce7f3 !important; opacity: 0.9;">Confidence: {confidence:.1f}%</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("##### Probability Distribution")
    
    # กราฟแท่ง Probabilities ธีมชมพู
    fig_prob = go.Figure()
    
    # ปรับสีให้สอดรับกับธีมพาสเทล (ไฮไลต์ตัวที่เลือกเป็นสีเข้ม)
    colors = ['#fda4af' if i != prediction else '#be185d' for i in range(3)]
    
    fig_prob.add_trace(go.Bar(
        x=[s.capitalize() for s in species_names],
        y=probabilities * 100,
        marker_color=colors,
        text=[f"{p*100:.1f}%" for p in probabilities],
        textposition='outside',
        textfont=dict(color='#475569', weight='bold')
    ))
    
    fig_prob.update_layout(
        height=220,
        margin=dict(l=20, r=20, t=10, b=40),
        yaxis=dict(title="Probability (%)", range=[0, 115]),
        xaxis_title="Species",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#475569')
    )
    st.plotly_chart(fig_prob, use_container_width=True)