![image](https://github.com/user-attachments/assets/68e4f43e-077a-478e-a5f2-eb506f48cd00)# WEEK-1-AI-4-SE-
CRYPTO AI
# 🤖 CryptoBuddy: Your Friendly Crypto Advisor Bot

# 1. Personality
print("👋 Hello! I'm CryptoBuddy — your friendly crypto advisor!")
print("Ask me about crypto trends, sustainability, or what to invest in. 💰🌱")
print("Type 'exit' to leave the chat.\n")

# 2. Crypto Data
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8  
    }  
}

# 3. Main Chat Loop
while True:
    user_query = input("You: ").lower()
    
    if user_query in ["exit", "quit", "bye"]:
        print("CryptoBuddy: Catch you later! 🚀 Remember, crypto is risky — always DYOR! 📉📈")
        break

    # 4. Logic Rules

    # --- Sustainability Query
    elif "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: I recommend {recommend}! 🌱 It's eco-friendly and has long-term potential!")

    # --- Trending or Rising
    elif "trending" in user_query or "rising" in user_query:
        trending_coins = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        print(f"CryptoBuddy: These coins are on the rise 📈: {', '.join(trending_coins)}")

    # --- Long-term growth
    elif "long-term" in user_query or "growth" in user_query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                print(f"CryptoBuddy: {name} is trending up and has a top-tier sustainability score! 🚀")
                break
        else:
            print("CryptoBuddy: Hmm, no perfect match right now. Keep researching!")

    # --- Most profitable
    elif "profitable" in user_query or "best investment" in user_query:
        profitable_coins = [name for name, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if profitable_coins:
            print(f"CryptoBuddy: For profit, go with: {', '.join(profitable_coins)} 💸")
        else:
            print("CryptoBuddy: I don’t see any high-profit coins at the moment.")

    # --- Fallback
    else:
        print("CryptoBuddy: I’m not sure about that 🤔 Try asking about sustainability, trends, or long-term growth!")


