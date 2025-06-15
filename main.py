import streamlit as st

# Page config
st.set_page_config(page_title="Faisal Sheriff | Portfolio", layout="wide")

# Sidebar Navigation
st.sidebar.title("📂 Portfolio Navigation")
page = st.sidebar.radio("Go to:", [
    "Home",
    "About Me",
    "Skills",
    "Education & Certifications",
    "Experience",
    "Projects",
    "Volunteer Work",
    "Contact"
])

# ---- Home ----
if page == "Home":
    st.markdown("# 👋 Hi There, I'm **Faisal Sheriff**")
    st.markdown("""
    **Master’s Student in Network Engineering**  
    Certified Workflow Specialist | Cybersecurity & Cloud Security Focused  
    ___  
    🔹 Building secure systems, coordinating projects, and enabling tech-driven change.  

    📍 Wyndham Vale, Melbourne  
    📧 faisalssheriff@gmail.com  
    ☎️ +61-0478632666  
    [LinkedIn](https://linkedin.com/in/faisalsheriff) | [GitHub](https://github.com/faisalsherrif)
    """)

# ---- About Me ----
elif page == "About Me":
    st.markdown("## 👤 About Me")
    st.markdown("""
    I’m a master's student in Networking with a Cybersecurity specialization at **Melbourne Institute of Technology**.  
    I bring hands-on experience from ANZ, Mastercard, and Datacom, where I supported IT services, cybersecurity awareness, and threat analysis.

    I thrive at the intersection of:
    - Threat detection and digital forensics
    - Workflow automation and student services coordination
    - Secure network deployment and system administration

    I'm currently expanding into **cloud security and AI-based analysis**, while pursuing AWS and ISC2 certifications.
    """)

# ---- Skills ----
elif page == "Skills":
    st.markdown("## ⚙️ Skills")

    st.markdown("### 🛠️ Technical Skills")
    st.markdown("""
    - **Networking & Security:** TCP/IP, OSI Model, Nmap, Wireshark, Kali Linux  
    - **Digital Forensics:** Autopsy, FTK Imager  
    - **System Admin:** Windows Server 2019, VirtualBox, UTM, Remote Access  
    - **Workflow Tools:** Asana, Jira, MS Project, Confluence  
    - **Programming:** Python, Java (Basic), Google Colab  
    - **Operating Systems:** Kali Linux, Windows, macOS, Ubuntu
    """)

    st.markdown("### 🧠 Soft Skills")
    st.markdown("Analytical Thinking | Problem-Solving | Communication | Leadership | Time Management")

# ---- Education & Certifications ----
elif page == "Education & Certifications":
    st.markdown("## 🎓 Education & Certifications")

    st.markdown("### 📘 Education")
    st.markdown("""
    - **Master’s in Networking (Cybersecurity)**  
      Melbourne Institute of Technology | 2023 – Present

    - **B.Tech in Computer Science Engineering**  
      Dayananda Sagar University | 2018 – 2022
    """)

    st.markdown("### 📜 Certifications")
    st.markdown("""
    - Certified Workflow Specialist – Asana  
    - AWS Certified Cloud Practitioner *(In Progress)*  
    - ISC2 Certified in Cybersecurity (CC) *(In Progress)*
    """)

# ---- Experience ----
elif page == "Experience":
    st.markdown("## 💼 Professional Experience")

    st.markdown("### 🛡️ Capstone Team Lead – Knowledge Management Pty Ltd (Mar 2025 – Present)")
    st.markdown("""
    - Developed AI-powered dashboard for analyzing cyberattacks  
    - Built CSV upload + Streamlit interface + AI assistant for querying incidents
    """)

    st.markdown("### 🖥️ IT Service Desk Intern – Datacom (Sept 2024)")
    st.markdown("""
    - Resolved network outages, applied ITIL for incident tracking  
    - Diagnosed system issues and supported remote access
    """)

    st.markdown("### 🧠 Security Awareness Analyst – Mastercard (Jul 2024)")
    st.markdown("""
    - Created training material and security awareness campaigns  
    - Contributed to internal cybersecurity posture improvements
    """)

    st.markdown("### 🗂️ Student Services Admin – MIT (2025)")
    st.markdown("""
    - Supported enrolment and registration desk  
    - Assisted with documentation, helpdesk, and onboarding
    """)

    st.markdown("### 📊 Project Coordinator – Knowledge Management (Jul – Oct 2024)")
    st.markdown("""
    - Managed QCA-based cyber incident analysis project  
    - Built truth tables, attack vignettes, and final reports
    """)

# ---- Projects ----
elif page == "Projects":
    st.markdown("## 💡 Projects")

    st.markdown("### 🧠 Vignette Signatures of Cyberattacks (Capstone)")
    st.markdown("""
    - Streamlit-based dashboard with AI assistant for querying cyber incidents  
    - CSV input, heatmap/radar visualizations, QCA-based threat analysis
    """)

    st.markdown("### 🔐 Secure File Storage on Cloud")
    st.markdown("- Used cryptographic techniques to secure cloud file transfers")

    st.markdown("### 🧬 Breast Cancer Detection using ML")
    st.markdown("- Built detection models for early diagnosis using ML algorithms")

    st.markdown("### 🍱 Online Food Donation App")
    st.markdown("- Designed Android app to streamline food donations")

# ---- Volunteer ----
elif page == "Volunteer Work":
    st.markdown("## 🤝 Volunteer Experience")

    st.markdown("### 🧑‍🏫 Senior Buddy – MIT (Jul 2023)")
    st.markdown("""
    - Guided new students through enrolment and course selection  
    - Mentored peers and provided academic support
    """)

# ---- Contact ----
elif page == "Contact":
    st.markdown("## 📬 Contact")

    st.markdown("""
    📧 **Email:** faisalssheriff@gmail.com  
    📞 **Phone:** +61-0478632666  
    📍 **Location:** Wyndham Vale, Melbourne  

    🔗 [LinkedIn](https://linkedin.com/in/faisalsheriff)  
    💻 [GitHub](https://github.com/faisalsherrif)  
    🐦 Twitter: *(optional)*  
    """)

    st.success("Thank you for visiting my portfolio!")
