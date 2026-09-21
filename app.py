import os
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Z-SURVIVAL // 좀비 아포칼립스 생존 가이드",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        .stApp {
            background-color: #0a0a0c;
        }
        /* Remove default streamlit padding to maximize embedded html view */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### ☣️ DEFCON 1 PROTOCOL")
    st.markdown("---")
    st.markdown("**배포 정보**")
    st.info("이 애플리케이션은 GitHub에 저장된 `htmls/index.html` 파일을 로드하여 Streamlit 환경에서 실행합니다.")
    
    st.markdown("---")
    st.markdown("**시스템 관리**")
    if st.button("🔄 가이드 새로고침"):
        st.rerun()
        
    st.markdown("---")
    st.caption("Z-SURVIVAL WEB SYSTEM v3.4")

html_file_path = os.path.join("htmls", "index.html")

if os.path.exists(html_file_path):
    try:
        with open(html_file_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        # Using a large height with scrolling enabled to ensure the entire web page fits seamlessly.
        components.html(html_content, height=1200, scrolling=True)
        
    except Exception as e:
        st.error(f"❌ HTML 파일을 읽는 중 오류가 발생했습니다: {e}")
else:
    st.error(f"🚨 오류: `{html_file_path}` 경로에서 파일을 찾을 수 없습니다.")
    st.warning("GitHub 저장소의 `htmls` 폴더 안에 `index.html` 파일이 정상적으로 위치해 있는지 확인해주세요.")
