import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import time

from shipment_generator import generate_shipments, get_kpis, predict_delay
from utils import display_kpi_metrics, prepare_map_data, prepare_delay_chart_data, format_shipment_details

# Page configuration
st.set_page_config(
    page_title="PortScope - Logistics Dashboard",
    page_icon="🚢",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stButton>button {
        width: 100%;
    }
    .shipment-card {
        padding: 15px;
        border-radius: 10px;
        background-color: #f8f9fa;
        margin-bottom: 10px;
        border-left: 5px solid #4e79a7;
    }
    .delayed {
        border-left-color: #e74c3c !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for shipments if not exists
if 'shipments' not in st.session_state:
    st.session_state.shipments = generate_shipments(15)

# Track last update time
if 'last_update' not in st.session_state:
    st.session_state.last_update = datetime.now()

def refresh_data():
    """Refresh the shipment data."""
    st.session_state.shipments = generate_shipments(15)
    st.session_state.last_update = datetime.now()
    st.rerun()

# Sidebar
with st.sidebar:
    st.title("PortScope")
    st.caption("Houston Port Logistics Dashboard")
    
    st.divider()
    
    # Refresh button
    if st.button("🔄 Refresh Data"):
        with st.spinner("Updating shipment data..."):
            refresh_data()
    
    st.caption(f"Last updated: {st.session_state.last_update.strftime('%Y-%m-%d %H:%M:%S')}")
    
    st.divider()
    
    # Search functionality
    st.subheader("🔍 Shipment Lookup")
    search_id = st.text_input("Enter Shipment ID (e.g., SH1001):")
    
    if search_id:
        found = next((s for s in st.session_state.shipments if s['shipment_id'].lower() == search_id.lower().strip()), None)
        if found:
            st.success(f"Found: {found['vessel_name']} ({found['shipment_id']})")
            
            # Show prediction
            prediction = predict_delay(found)
            if prediction['will_be_delayed']:
                st.error("⚠️ Potential Delay Predicted")
                st.write("Risk Factors:")
                for factor in prediction['risk_factors']:
                    st.write(f"- {factor}")
                st.write(f"Confidence: {prediction['confidence']}%")
            else:
                st.success("✅ On-time delivery expected")
            
            # Show details
            st.markdown("### Shipment Details")
            st.markdown(format_shipment_details(found), unsafe_allow_html=True)
        else:
            st.error("Shipment not found. Please check the ID and try again.")

# Main content
st.title("🚢 PortScope - Houston Port Operations")

# Display KPIs
kpis = get_kpis(st.session_state.shipments)
display_kpi_metrics(kpis)

# Tabs for different views
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📍 Vessel Map", "📈 Delay Trends"])

with tab1:
    st.subheader("Shipment Overview")
    
    # Display shipments in cards
    for shipment in st.session_state.shipments:
        card_class = "shipment-card"
        if shipment['is_delayed']:
            card_class += " delayed"
            
        with st.container():
            st.markdown(f"<div class='{card_class}'>" + 
                       f"<b>{shipment['vessel_name']}</b> ({shipment['shipment_id']})<br>" +
                       f"Status: {shipment['status']} | " +
                       f"ETA: {datetime.fromisoformat(shipment['eta']).strftime('%b %d, %Y')}" +
                       (f"<br>⚠️ <span style='color:#e74c3c'>Delayed: {shipment['delay_minutes']} min</span>" if shipment['is_delayed'] else "") +
                       f"</div>", unsafe_allow_html=True)

with tab2:
    st.subheader("Vessel Locations")
    map_data = prepare_map_data(st.session_state.shipments)
    if not map_data.empty:
        st.map(map_data, 
              latitude='lat',
              longitude='lon',
              size=20,
              color='#FF4B4B',
              use_container_width=True)
    else:
        st.warning("No vessel data available for mapping.")

with tab3:
    st.subheader("Delay Trends")
    delay_data = prepare_delay_chart_data(st.session_state.shipments)
    
    if not delay_data.empty:
        # Calculate 3-day moving average for smoother trend
        delay_data['moving_avg'] = delay_data['delay_minutes'].rolling(3, min_periods=1).mean()
        
        st.line_chart(
            delay_data.set_index('date')['moving_avg'],
            use_container_width=True,
            height=400
        )
        
        # Show recent delays
        st.write("### Recent Delays")
        recent_delays = [s for s in st.session_state.shipments if s['is_delayed']]
        recent_delays.sort(key=lambda x: x['delay_minutes'], reverse=True)
        
        if recent_delays:
            for delay in recent_delays[:5]:  # Show top 5
                st.write(f"- {delay['vessel_name']}: {delay['delay_minutes']} min delay ({delay['delay_reason']})")
        else:
            st.info("No recent delays to report.")
    else:
        st.warning("Insufficient data to display delay trends.")

# Footer
st.divider()
st.caption("PortScope - A logistics monitoring dashboard | Data is simulated and refreshed on demand")
