import streamlit as st 
from resume_analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")

st.markdown("### 🚀 Improve your resume and increase your chances of getting hired")

st.markdown("Analyze your resume and get instant feedback.")

uploaded_file = st.file_uploader("Upload your resume (.txt)", type=["txt"])

resume_text = ""
if uploaded_file:
    resume_text = uploaded_file.read().decode("utf-8")
else:
    resume_text = st.text_area("Paste your resume here:")

if st.button("🚀 Analyze Resume"):
    if not resume_text:
        st.warning("Please paste your resume")
    else:
        with st.spinner("Analyzing...."):
            result = analyze_resume(resume_text)

        st.divider() 
        if result["score"] >= 9:
            st.success(f"🎯 Score: {result['score']} / 12")
        elif result["score"] >= 6:
            st.warning(f"🎯 Score: {result['score']} / 12")
        else:
            st.error(f"🎯 Score: {result['score']} / 12")

        st.subheader("✅ Strengths")
        for s in result["strengths"]:
            st.write(f"✔ {s}")

        st.subheader("⚠️ Areas to Improve")
        for f in result["feedback"]:
            st.write(f"✘ {f}")