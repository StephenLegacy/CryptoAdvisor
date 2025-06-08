from typing import Dict, List, Tuple
from data.crypto_db import CRYPTO_DB

def analyze_profitability(coin_data: Dict) -> float:
    """Calculate profitability score (0-10)"""
    score = 0
    if coin_data["price_trend"] == "rising":
        score += 6
    elif coin_data["price_trend"] == "stable":
        score += 4
    if coin_data["market_cap"] == "high":
        score += 3
    elif coin_data["market_cap"] == "medium":
        score += 2
    return min(10, score)

def analyze_sustainability(coin_data: Dict) -> float:
    """Calculate sustainability score (0-10)"""
    score = coin_data["sustainability_score"]
    if coin_data["energy_use"] == "low":
        score += 2
    elif coin_data["energy_use"] == "medium":
        score += 1
    return min(10, score)

def generate_recommendation() -> Tuple[str, Dict]:
    """Generate investment recommendation"""
    scored_coins = []
    for name, data in CRYPTO_DB.items():
        profit_score = analyze_profitability(data)
        sustain_score = analyze_sustainability(data)
        total_score = (profit_score * 0.6) + (sustain_score * 0.4)  # Weighted
        scored_coins.append((name, total_score, data))
    
    # Sort by total score descending
    scored_coins.sort(key=lambda x: x[1], reverse=True)
    return scored_coins[0]  # (name, score, data)
