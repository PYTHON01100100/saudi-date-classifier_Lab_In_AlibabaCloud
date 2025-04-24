import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="Saudi Date Classifier", layout="centered")

st.title("🌴🇸🇦 Saudi Date Classifier")
st.subheader("صنّف تمرك بـذكاء اصطناعي سعودي!")

# Information
st.markdown("""
> 📸 **ارفع صورة للتمرة اللي عندك**  
> 🧠 والنموذج بيعرف نوعها تلقائيًا!

---

🌟 **الأنواع المدعومة:**
- 🟤 **Sokari** - سكري  
- 🟠 **Sagai** - صقعي  
- ⚫ **Ajwa** - عجوة  
- 🟤 **Medjool** - مجدول

🛑 **لأفضل دقة ممكنة:**
- 📷 ارفع صورة فيها **تمرة وحدة فقط**
- ☁️ خل الخلفية نظيفة
- 🚫 تجنب خلط التمر مع فنجان قهوة أو أشياء ثانية

---
Original work By: Abdulrahman Almejna
Linkedin: https://www.linkedin.com/in/abdulrahman-almejna-1786b21b4/
Test On Alibaba cloud ECS : Abdulrahman Almyman
Linkedin: https://www.linkedin.com/in/abdulrahmanalmyman/

""", unsafe_allow_html=True)


API_INTERNAL = "http://backend:8000"
API_EXTERNAL = "http://localhost:8000"

# Load image
uploaded_file = st.file_uploader("📤 ارفع صورة التمرة", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="📷 الصورة اللي رفعتها")

    if st.button("🔎 صنّف التمرة"):
        try:
            files = {"file": uploaded_file.getvalue()}
            response = requests.post(f"{API_INTERNAL}/predict", files=files)

            if response.status_code == 200:
                result = response.json()

                # Translate date from english to arabic
                translations = {
                    "Sokari": "سكري",
                    "Sugaey": "صقعي",
                    "Ajwa": "عجوة",
                    "Medjool": "مجدول"
                }

                predicted_en = result["class"]
                predicted_ar = translations.get(predicted_en, "غير معروف")

                # Display prediction
                st.markdown(f"""
                    <div style='font-size:30px; font-weight:bold; color:#008000;'>
                        🧠 النوع المتوقع: {predicted_ar}
                    </div>
                """, unsafe_allow_html=True)

                # عرض الصورة باستخدام رابط خارجي (المتصفح يفهمه)
                full_image_url = f"{API_EXTERNAL}{result['image_url']}"
                st.image(full_image_url, caption="🔍 الصورة مع التنبؤ")

            else:
                st.error("❌ صار خطأ أثناء التنبؤ")
        except Exception as e:
            st.error(f"⚠️ خطأ غير متوقع: {e}")
