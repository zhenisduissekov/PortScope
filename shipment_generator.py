import random
from datetime import datetime, timedelta
from typing import List, Dict, Any
import numpy as np

# Houston port coordinates (approximate)
HOUSTON_PORT = (29.6081, -95.0218)

# Sample data for generation
VESSEL_NAMES = [
    "MSC Isabella", "Maersk Houston", "CMA CGM Brazil", "Ever Given", "Cosco Shipping",
    "MOL Treasure", "APL Charleston", "HMM Rotterdam", "ONE Innovation", "Yang Ming Unity"
]

STATUSES = [
    "At Port", "In Transit", "Anchored", "Docked", "Underway"
]

ROUTES = [
    "Asia - Houston", "Europe - Houston", "South America - Houston",
    "West Coast - Houston", "Gulf - Houston"
]

DELAY_REASONS = [
    "Port Congestion", "Weather Conditions", "Mechanical Issues",
    "Crew Change", "Customs Delay", "None"
]

def generate_shipment(shipment_id: int) -> Dict[str, Any]:
    """Generate a single shipment record with realistic data."""
    vessel_name = random.choice(VESSEL_NAMES)
    status = random.choice(STATUSES)
    route = random.choice(ROUTES)
    
    # Generate random timestamps
    days_ago = random.randint(1, 30)
    eta_days = random.randint(1, 10)
    
    created_at = datetime.now() - timedelta(days=days_ago)
    eta = datetime.now() + timedelta(days=eta_days)
    
    # Determine if delayed (30% chance of delay)
    is_delayed = random.random() < 0.3
    delay_minutes = random.randint(60, 720) if is_delayed else 0
    delay_reason = random.choice(DELAY_REASONS) if is_delayed else "None"
    
    # Generate position near Houston with some randomness
    lat = HOUSTON_PORT[0] + random.uniform(-2, 2)
    lon = HOUSTON_PORT[1] + random.uniform(-2, 2)
    
    return {
        "shipment_id": f"SH{1000 + shipment_id}",
        "vessel_name": vessel_name,
        "status": status,
        "route": route,
        "created_at": created_at.isoformat(),
        "eta": eta.isoformat(),
        "is_delayed": is_delayed,
        "delay_minutes": delay_minutes,
        "delay_reason": delay_reason,
        "current_lat": lat,
        "current_lon": lon,
        "containers_count": random.randint(100, 5000),
        "weight_kg": random.randint(50000, 1000000)
    }

def generate_shipments(count: int = 15) -> List[Dict[str, Any]]:
    """Generate multiple shipment records."""
    return [generate_shipment(i) for i in range(1, count + 1)]

def get_kpis(shipments: List[Dict[str, Any]]) -> Dict[str, float]:
    """Calculate KPIs from shipments data."""
    if not shipments:
        return {
            "avg_delay": 0,
            "success_rate": 100,
            "active_shipments": 0
        }
    
    delayed = sum(1 for s in shipments if s["is_delayed"])
    total = len(shipments)
    avg_delay = sum(s["delay_minutes"] for s in shipments) / total
    success_rate = ((total - delayed) / total) * 100
    
    return {
        "avg_delay": round(avg_delay, 1),
        "success_rate": round(success_rate, 1),
        "active_shipments": total
    }

def predict_delay(shipment: Dict[str, Any]) -> Dict[str, Any]:
    """Predict if a shipment will be delayed (simple rule-based prediction)."""
    # Simple rules for prediction
    risk_factors = []
    
    # Check if ETA is too tight (less than 2 days)
    eta = datetime.fromisoformat(shipment["eta"])
    days_until_eta = (eta - datetime.now()).days
    
    if days_until_eta < 2:
        risk_factors.append("ETA too tight")
    
    # Check if route is known for delays
    if "Asia" in shipment["route"] and random.random() > 0.6:
        risk_factors.append("Route congestion")
    
    # Check if vessel is frequently delayed (simplified)
    if hash(shipment["vessel_name"]) % 5 == 0:
        risk_factors.append("Vessel history of delays")
    
    # Make prediction based on risk factors
    will_be_delayed = len(risk_factors) > 1 or (len(risk_factors) == 1 and random.random() > 0.5)
    
    return {
        "will_be_delayed": will_be_delayed,
        "risk_factors": risk_factors if will_be_delayed else ["No significant risks identified"],
        "confidence": min(90, len(risk_factors) * 30)  # Simple confidence score
    }
