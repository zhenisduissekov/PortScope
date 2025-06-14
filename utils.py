from typing import Dict, Any, List
import pandas as pd
import streamlit as st
from datetime import datetime

def display_kpi_metrics(kpis: Dict[str, float]) -> None:
    """Display KPI metrics in a 3-column layout."""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Average Delay (min)", kpis["avg_delay"])
    with col2:
        st.metric("Success Rate", f"{kpis['success_rate']}%")
    with col3:
        st.metric("Active Shipments", kpis["active_shipments"])

def prepare_map_data(shipments: List[Dict[str, Any]]) -> pd.DataFrame:
    """Prepare shipment data for mapping."""
    map_data = []
    for shipment in shipments:
        map_data.append({
            'lat': [shipment['current_lat']],
            'lon': [shipment['current_lon']],
            'vessel': [shipment['vessel_name']],
            'status': [shipment['status']]
        })
    
    if not map_data:
        return pd.DataFrame(columns=['lat', 'lon', 'vessel', 'status'])
    
    return pd.concat([pd.DataFrame(data) for data in map_data], ignore_index=True)

def prepare_delay_chart_data(shipments: List[Dict[str, Any]]) -> pd.DataFrame:
    """Prepare data for delay trend chart."""
    if not shipments:
        return pd.DataFrame()
        
    # Group by date and calculate average delay
    df = pd.DataFrame(shipments)
    df['date'] = pd.to_datetime(df['eta']).dt.date
    
    # Calculate daily average delay
    delay_data = df.groupby('date')['delay_minutes'].mean().reset_index()
    
    return delay_data

def format_shipment_details(shipment: Dict[str, Any]) -> str:
    """Format shipment details for display."""
    details = f"""
    ### 🚢 Vessel: {shipment['vessel_name']}
    - **Shipment ID**: {shipment['shipment_id']}
    - **Status**: {shipment['status']}
    - **Route**: {shipment['route']}
    - **Containers**: {shipment['containers_count']:,}
    - **Weight**: {shipment['weight_kg']:,} kg
    - **Created**: {datetime.fromisoformat(shipment['created_at']).strftime('%Y-%m-%d %H:%M')}
    - **ETA**: {datetime.fromisoformat(shipment['eta']).strftime('%Y-%m-%d %H:%M')}
    """
    
    if shipment['is_delayed']:
        details += f"- **⚠️ Delay**: {shipment['delay_minutes']} minutes\n"
        details += f"- **Reason**: {shipment['delay_reason']}\n"
    
    return details
