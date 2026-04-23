import streamlit as st 
from resume_analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")

st.markdown("Analyze your resume and get instant feedback.")

resume_text = st.text_area("Paste your resume here:")

if st.button("🚀 Analyze Resume"):
    if not resume_text:
        st.warning("Please paste your resume")
    else:
        with st.spinner("Analyzing...."):
            result = analyze_resume(resume_text)

        st.divider() 
        st.subheader(f"🎯 Score: {result['score']} /12")

        st.subheader("✅ Strengths")
        for s in result["strengths"]:
            st.write(f"✔ {s}")

        st.subheader("⚠️ Areas to Improve")
        for f in result["feedback"]:
            st.write(f"✘ {f}")