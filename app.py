import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="My Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CSS STYLING ---
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5; 
        /* Ideally use streamlit's theming, but this is a subtle background touch if theme is light */
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
    }
    .stExpander {
        border: none;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        background-color: white;
        border-radius: 10px;
    }
    .stExpander * {
        color: #333333 !important;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("me.png", caption="Aspiring Developer", use_container_width=True)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Portfolio", "Skills", "Contact"])

st.sidebar.markdown("---")
st.sidebar.info("Connect with me on [LinkedIn](#) or [GitHub](#)")

# --- HOME SECTION ---
def show_home():
    col1, col2 = st.columns([1, 2])
    with col1:
        try:
            image = Image.open('me.png')
            st.image(image, use_container_width=True)
        except Exception:
            st.warning("Profile image not found.")
            
    with col2:
        st.title("Hello, I'm Clarence Kirk Macapobre! 👋")
        st.subheader("A very good programmer yesss.")
        st.write("""
        Welcome to my digital portfolio! I am very passionate about lots of stuff especially eating and sleeping like a lot a lot.""")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Download Resume 📄"):
                st.toast("Resume download started! (Simulated)")
               
        with c2:
            if st.button("Contact Me 📧"):
                st.switch_page("app.py") 

    st.markdown("---")
    
   
    st.header("Quick Stats")
    m1, m2, m3 = st.columns(3)
    m1.metric("Projects Completed", "12", "+2 this month")
    m2.metric("Years of Experience", "1.1111", "Learning everyday")
    m3.metric("Coffee Consumed", "∞", "Cups")

# --- ABOUT ME SECTION ---
def show_about():
    st.title("About Me 👤")
    
    tab1, tab2, tab3 = st.tabs(["Biography", "Education", "Experience"])
    
    with tab1:
        st.write("""
        ### My Story
        I started my coding journey on january 20, 1967. yess good programmer...
        
        I love everything especially eating and sleeping. yes yes
        """)
        st.image("aboutme.png", caption="Coding workspace", use_container_width=True)

    with tab2:
        st.write("### Education Path")
        st.info("**Bachelor of Science in Information Technology**  \n*Cebu Institute of Technology* | 2021 - present")
        st.write("Specialized in sleeping and vibe coding.")

    with tab3:
        st.write("### Professional Experience")
        with st.expander("Bantay Tindahan (2015-Present)", expanded=True):
            st.write("""
            - I bantay.
            - I also steal.
            """)
        
        with st.expander("Intern at appletreefarm"):
            st.write("""
            - Assisted in getting apples.
            - I sometimes steal apples.
            """)

# --- PORTFOLIO SECTION ---
def show_portfolio():
    st.title("My Portfolio 📂")
    st.write("Here are some of the projects I've worked on.")
    
    # Filter
    category = st.select_slider("Filter by Category", options=["All", "Data Science", "Web Dev", "Automation"])
    
    projects = [
        {"title": "Stock Price Predictor", "cat": "Data Science", "desc": "Predicted stock prices using LSTM.", "img": "https://via.placeholder.com/300"},
        {"title": "E-commerce Website", "cat": "Web Dev", "desc": "Full-stack shop built with React & Node.", "img": "https://via.placeholder.com/300"},
        {"title": "Will email your job mates about random cat facts everyday", "cat": "Automation", "desc": "Automated weekly reporting emails.", "img": "https://via.placeholder.com/300"},
        {"title": "Customer Segmentation", "cat": "Data Science", "desc": "Clustering customers based on behavior.", "img": "https://via.placeholder.com/300"},
    ]
    
    filtered_projects = [p for p in projects if category == "All" or p["cat"] == category]
    
    cols = st.columns(2)
    for i, project in enumerate(filtered_projects):
        with cols[i % 2]:
            st.markdown(f"### {project['title']}")
            st.caption(project['cat'])
            # st.image(project['img']) # Using placeholder
            st.info(project['desc'])
            st.button(f"View Code for {project['title']}", key=f"btn_{i}")

    st.markdown("---")
    st.subheader("RANDOM DATA FOR cool looking reasons")
    
    
    data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])
    st.dataframe(data)
    
    chart_type = st.selectbox("Select Chart Type", ["Line", "Bar", "Area"])
    if chart_type == "Line":
        st.line_chart(data)
    elif chart_type == "Bar":
        st.bar_chart(data)
    elif chart_type == "Area":
        st.area_chart(data)

# --- SKILLS SECTION ---
def show_skills():
    st.title("My Skills 🛠️")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Technical Proficiency")
        skills = {
            "Python": 90,
            "SQL": 75,
            "Machine Learning": 60,
            "Web Development": 80,
            "Cloud (AWS)": 40
        }
        
        # Radar Chart using Plotly
        df_skills = pd.DataFrame(dict(
            r=list(skills.values()),
            theta=list(skills.keys())
        ))
        fig = px.line_polar(df_skills, r='r', theta='theta', line_close=True)
        fig.update_traces(fill='toself')
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.subheader("Tools & Technologies")
        st.write("Using `st.progress` to visualize expertise:")
        for skill, level in skills.items():
            st.write(f"{skill}")
            st.progress(level)
            
    st.subheader("Where I'm Based")
    # Random coordinates for demo (e.g. roughly NY)
    map_data = pd.DataFrame([{'lat': 11.1761, 'lon': 119.3891}])
    st.map(map_data, zoom=10)

# --- CONTACT SECTION ---
def show_contact():
    st.title("Get In Touch 📬")
    
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        
        submitted = st.form_submit_button("Send Message 🚀")
        
        if submitted:
            if name and email and message:
                st.success("Message sent! I'll get back to you soon.")
                st.balloons()
            else:
                st.error("Please fill in all fields.")

# --- MAIN ROUTING ---
if page == "Home":
    show_home()
elif page == "About Me":
    show_about()
elif page == "Portfolio":
    show_portfolio()
elif page == "Skills":
    show_skills()
elif page == "Contact":
    show_contact()

# Footer
st.markdown("---")
st.markdown("Created by the dude himself")
