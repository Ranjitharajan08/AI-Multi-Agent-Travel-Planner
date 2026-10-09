import streamlit as st
import streamlit.components.v1 as components
from travel_orchestrator import run_travel_pipeline

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="🌍",
    layout="wide"
)

# ---------------- CLEAN HEADER ----------------
st.markdown("""
    <style>
        .title {
            font-size: 42px;
            font-weight: bold;
            text-align: center;
            color: #1f4e79;
            margin-bottom: 10px;
        }

        .subtitle {
            text-align: center;
            color: #666;
            font-size: 18px;
            margin-bottom: 30px;
        }

        .card {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🌍 AI Multi-Agent Travel Planner</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Plan your perfect trip using AI agents ✈️</div>", unsafe_allow_html=True)

# ---------------- LAYOUT ----------------
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📍 Trip Configuration")

    # Optional browser GPS display (visual only)
    components.html("""
        <script>
        navigator.geolocation.getCurrentPosition(function(position) {
            document.body.innerHTML =
            "<b>Detected Location:</b><br>" +
            "Lat: " + position.coords.latitude + "<br>" +
            "Lng: " + position.coords.longitude;
        });
        </script>
    """, height=80)

    # MAIN origin input (used in backend)
    origin = st.text_input("Enter your current location", "Chennai, India")

    st.subheader("✈ Trip Configuration")

    destination = st.text_input("Destination", "Kerala")
    budget = st.text_input("Budget", "50000 INR")
    days = st.slider("Days", 1, 100, 5)

    travel_style = st.selectbox(
        "Travel Style",
        ["Adventure", "Relaxation", "Cultural", "Luxury", "Budget"]
    )

    run = st.button("🚀 Generate Travel Plan")

with col2:
    st.subheader("📍 Live Preview")
    st.info("Your travel plan will appear here after generation.")

# ---------------- RUN PIPELINE ----------------
if run:
    with st.spinner("🧠 AI Agents are planning your trip..."):

        result = run_travel_pipeline(
            destination,
            budget,
            days,
            travel_style
        )

    st.success("✨ Travel Plan Ready!")

    st.markdown("## 🌍 Final Travel Plan")

    st.markdown(f"""
    <div class='card'>
        {result['final_plan']}
    </div>
    """, unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.markdown("### 📍 Destination")
        st.markdown(f"<div class='card'>{result['destination_info']}</div>", unsafe_allow_html=True)

        st.markdown("### 🍜 Local Guide")
        st.markdown(f"<div class='card'>{result['local_guide']}</div>", unsafe_allow_html=True)

    with col4:
        st.markdown("### 💰 Budget")
        st.markdown(f"<div class='card'>{result['budget_info']}</div>", unsafe_allow_html=True)

        st.markdown("### 📅 Itinerary")
        st.markdown(f"<div class='card'>{result['itinerary']}</div>", unsafe_allow_html=True)

    # ---------------- DOWNLOAD ----------------
    st.download_button(
        label="📥 Download Travel Plan",
        data=result["final_plan"],
        file_name=f"{destination}_travel_plan.txt",
        mime="text/plain"
    )