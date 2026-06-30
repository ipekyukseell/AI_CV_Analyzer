import streamlit as st
import pdfplumber

st.set_page_config(page_title="AI CV Analyzer", page_icon="🤓")

st.title("🤓 AI CV Analyzer")

uploaded_file = st.file_uploader(
    "CV'nizi yükleyin",
    type=["pdf"]
)

if uploaded_file:

    st.success("CV başarıyla yüklendi! ✅")

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

    st.subheader("📄 CV İçeriği")
    st.text(text)

    lower_text = text.lower()

    score = 0

    st.subheader("🤖 AI Analizi")

    def kontrol(kelime, puan):
        global score
        if kelime in lower_text:
            st.success(f"✅ {kelime.upper()} bulundu.")
            return puan
        else:
            st.error(f"❌ {kelime.upper()} bulunamadı.")
            return 0

    score += kontrol("python",10)
    score += kontrol("c++",10)
    score += kontrol("java",10)
    score += kontrol("sql",10)
    score += kontrol("html",5)
    score += kontrol("css",5)
    score += kontrol("javascript",5)
    score += kontrol("git",5)
    score += kontrol("github",10)
    score += kontrol("api",10)
    score += kontrol("ingilizce",5)
    score += kontrol("sertifika",5)
    score += kontrol("proje",10)

    if score > 100:
        score = 100

    st.subheader("📊 CV Puanı")
    st.metric("Puan", f"{score}/100")

    st.subheader("📌 Öneriler")

    if "github" not in lower_text:
        st.warning("GitHub profilinizi ekleyin.")

    if "linkedin" not in lower_text:
        st.warning("LinkedIn profilinizi ekleyin.")

    if "sql" not in lower_text:
        st.warning("SQL bilginizi ekleyin.")

    if "ingilizce" not in lower_text:
        st.warning("Yabancı dil seviyenizi belirtin.")

    st.subheader("🧠 AI Yorumu")

    if score >= 90:
        st.success("CV'niz oldukça güçlü görünüyor. İş başvuruları için hazır.")

    elif score >= 75:
        st.info("CV'niz iyi durumda. Birkaç küçük geliştirme ile daha güçlü olabilir.")

    elif score >= 50:
        st.warning("CV'nizde eksikler bulunuyor. Daha fazla proje ve teknik beceri ekleyebilirsiniz.")

    else:
        st.error("CV'nüzü önemli ölçüde geliştirmeniz önerilir.")