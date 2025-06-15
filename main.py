import streamlit as st
from PIL import Image
from streamlit_extras.mention import mention

# Page config
st.set_page_config(page_title="Faisal Sheriff | Portfolio", layout="wide")

# Custom CSS for style (optional enhancement)
st.markdown("""
<style>
    .main {
        background-color: #f9f9f9;
    }
    .big-font {
        font-size: 48px !important;
        font-weight: 700;
    }
    .highlight {
        color: #fca311;
    }
    .small-tagline {
        font-size: 20px;
        font-weight: 500;
        color: #e63946;
    }
    .button-style {
        background-color: #14213d;
        color: white;
        border-radius: 12px;
        padding: 0.5rem 1rem;
        text-decoration: none;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# Columns for layout
left, right = st.columns([2, 1])

with left:
    st.markdown('<div class="big-font">Hi There,<br>I\'m <span class="highlight">Faisal Sheriff</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="small-tagline">I specialize in Cybersecurity, Digital Forensics, and Network Engineering.</div>', unsafe_allow_html=True)
    
    st.markdown("### ")
    st.link_button("🔎 About Me", "#about-me")

    st.markdown("### ")
    st.markdown("#### Connect with Me")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("[![LinkedIn](https://img.icons8.com/ios-filled/40/000000/linkedin.png)](https://linkedin.com/in/faisalsherrif)")
    with col2:
        st.markdown("[![GitHub](https://img.icons8.com/ios-glyphs/40/000000/github.png)](https://github.com/faisalsherrif)")
    with col3:
        st.markdown("[![Email](https://img.icons8.com/ios-filled/40/000000/new-post.png)](mailto:faisal@example.com)")
    with col4:
        st.markdown("[![Twitter](https://img.icons8.com/ios-filled/40/000000/twitter--v1.png)](https://twitter.com/yourhandle)")

with right:
    profile_pic = Image.open("avatar.png")  # Replace with your actual avatar image
    st.image(profile_pic, width=300)

