# Complete cryptocurrency dataset
CRYPTO_DB = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3,
        "risk_level": "high",
        "description": "The original cryptocurrency with strong brand recognition but high energy consumption."
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6,
        "risk_level": "medium",
        "description": "A smart contract platform transitioning to more energy-efficient proof-of-stake."
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8,
        "risk_level": "medium",
        "description": "A research-driven blockchain with focus on sustainability and scalability."
    },
    "Solana": {
        "price_trend": "volatile",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 7,
        "risk_level": "high",
        "description": "High-performance blockchain with low fees but has faced network stability issues."
    },
    "Algorand": {
        "price_trend": "stable",
        "market_cap": "low",
        "energy_use": "low",
        "sustainability_score": 9,
        "risk_level": "medium",
        "description": "Pure proof-of-stake blockchain with strong focus on sustainability and decentralization."
    }
}

# Add metadata about the dataset
DATASET_META = {
    "version": "1.0",
    "source": "CoinMarketCap, CryptoCompare",
    "update_frequency": "weekly"
}

def get_all_coins():
    """Return list of all available cryptocurrencies"""
    return list(CRYPTO_DB.keys())

def get_coin_data(coin_name):
    """Get data for specific cryptocurrency"""
    return CRYPTO_DB.get(coin_name, None)