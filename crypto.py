from flask import Flask, request, render_template

app = Flask(__name__)

# CryptoBuddy logic
crypto_db = {  
    "Bitcoin": {"price_trend": "rising", "market_cap": "high", "energy_use": "high", "sustainability_score": 3},  
    "Ethereum": {"price_trend": "stable", "market_cap": "high", "energy_use": "medium", "sustainability_score": 6},  
    "Cardano": {"price_trend": "rising", "market_cap": "medium", "energy_use": "low", "sustainability_score": 8}  
}

def crypto_buddy_response(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"I recommend {recommend}! 🌱 It's eco-friendly and has long-term potential!"

    elif "trending" in user_query or "rising" in user_query:
        trending = [name for name, data in crypto_db.items() if data["price_trend"] == "rising"]
        return f"These coins are trending 📈: {', '.join(trending)}"

    elif "long-term" in user_query or "growth" in user_query:
        for name, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] >= 7:
                return f"{name} is trending up and has a top-tier sustainability score! 🚀"
        return "Hmm, no perfect match for long-term growth right now."

    elif "profitable" in user_query or "best investment" in user_query:
        profitable = [name for name, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if profitable:
            return f"For profit, consider: {', '.join(profitable)} 💸"
        return "No high-profit coins found at the moment."

    else:
        return "I'm not sure about that 🤔 Ask me about sustainability, trends, or long-term growth."


@app.route("/", methods=["GET", "POST"])
def chat():
    reply = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        reply = crypto_buddy_response(user_input)
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
