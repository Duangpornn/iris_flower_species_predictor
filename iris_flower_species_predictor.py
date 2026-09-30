import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# ตั้งค่าหน้าเว็บ Streamlit
st.set_page_config(
    page_title="Iris Flower Species Predictor - Pink Edition",
    page_icon="🌸",
    layout="wide"
)

# โหลดข้อมูลและเทรนโมเดล KNN (k=5)
iris = load_iris()
X, y = iris.data, iris.target
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X, y)

# คำนวณค่าเฉลี่ยของ Dataset แต่ละฟีเจอร์
dataset_means = X.mean(axis=0)

# ตกแต่ง CSS ธีมชมพูพาสเทล
st.markdown("""
    <style>
    .main {
        background-color: #fff1f2;
    }
    .stSidebar {
        background-color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# ส่วน Sidebar สำหรับรับค่า Input
st.sidebar.markdown("### 🎛️ Settings & Inputs")
st.sidebar.text("Tune the measurements")

sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.0, 0.1)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.5, 0.1)
petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 3.1, 0.1)
petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.6, 0.1)

st.sidebar.markdown("---")
st.sidebar.text("Model: KNN (k=5)")

# ทำนายผลลัพธ์ด้วย KNN
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
prediction = model.predict(input_data)
probabilities = model.predict_proba(input_data)[0]
predicted_species = iris.target_names[prediction[0]]
confidence = probabilities[prediction[0]] * 100

# ส่วนหัวข้อหน้าหลัก
st.markdown("### 🌸 Iris Species Classification Lab")
st.title("Iris Flower Species Predictor 🌸")
st.write("An interactive ML dashboard to predict and compare flower dimensions in a vibrant pink pastel theme.")
st.markdown("---")

# แบ่งหน้าจอเป็น 2 คอลัมน์หลัก (ซ้าย: ผลทำนายและความน่าจะเป็น, ขวา: กราฟเปรียบเทียบ)
left_col, right_col = st.columns(2)

with left_col:
    st.markdown("#### 🎯 Prediction Result")
    # กล่องแสดงผลลัพธ์การทำนายโทนสีชมพู
    st.markdown(f"""
        <div style="background: linear-gradient(to right, #ec4899, #f43f5e, #ec4899); padding: 20px; border-radius: 15px; color: white; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <p style="margin: 0; font-size: 12px; font-weight: bold; text-transform: uppercase;">Predicted Species</p>
            <h2 style="margin: 5px 0; font-size: 32px; font-weight: 900;">{predicted_species.capitalize()}</h2>
            <div style="background: rgba(0,0,0,0.15); display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold;">
                ✅ Confidence: {confidence:.1f}%
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### Model Probability by Class")
    species_list = ['Setosa', 'Versicolor', 'Virginica']
    for i, species in enumerate(species_list):
        prob = probabilities[i] * 100
        st.write(f"**{species}**: {prob:.1f}%")
        st.progress(int(prob))

with right_col:
    st.markdown("#### 📊 Your Inputs vs Dataset Mean")
    st.write("Comparison of your configured flower dimensions against the overall Iris dataset mean.")
    
    # สร้าง DataFrame สำหรับแสดงกราฟเปรียบเทียบ
    chart_data = pd.DataFrame({
        'Feature': ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'],
        'Your Values': [sepal_length, sepal_width, petal_length, petal_width],
        'Dataset Average': dataset_means
    })
    
    # แสดง Bar Chart เปรียบเทียบ
    st.bar_chart(chart_data.set_index('Feature'))
