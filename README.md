
# Multi‑Location Dining Advisor 🌍🍽️

**A multi-city foodie planner that:**
- Retrieves real-time weather via OpenWeatherMap  
- Recommends indoor or outdoor dining  
- Lists 3 iconic dishes per city with top restaurant suggestions  
- Crafts a weather-aware, one-day “foodie tour” (breakfast, lunch, dinner narratives)  

---

## 🧠 Workflow Overview

1. **Input**  
   The task accepts a JSON input:
   ```json
   {
     "locations": ["New York", "London", "Paris", "Tokyo", "Sydney"]
   }

2. **Weather Fetch**
   For each city, the Julep `weather` integration retrieves current conditions.

3. **Pairing Data**
   City names are paired with their weather reports using an `evaluate` step.

4. **Parallel Prompting**
   For each pair, a system prompt (via YAML `map` and `parallelism`) instructs the model to:

   * Decide indoor vs outdoor dining
   * List 3 iconic dishes
   * Recommend a restaurant per dish
   * **Create a weather-aware “foodie tour”**: breakfast, lunch, dinner narratives

5. **Aggregating Results**
   Individual outputs are joined in one final string via a concluding `evaluate` + `return` step.

6. **Python Orchestration**
   A simple `run.py` script:

   * Creates the agent and task
   * Executes with the provided cities
   * Polls until completion
   * Prints formatted itinerary outputs for each city

---

## 🛠️ Usage

```bash
pip install -r requirements.txt
python run.py
```

Output for each city includes:

* Indoor/outdoor recommendation
* 3 dishes + restaurants
* Full-day, weather-conscious itineraries

---

## 📁 Repository Structure

```
📦multi-location-dining-advisor
 ┣ 📄dinning_suggestion.yaml    # Julep task definition
 ┣ 📄run.py                    # Python orchestration script
 ┣ 📄requirements.txt           # Required packages
 ┗ 📄.env                        # API keys (not included in repo)
```

---

## ✨ Customization Tips

* Add or remove cities in `run.py`
* Adjust itinerary detail or phrasing in the YAML prompt
* Swap `parallelism` to other values in YAML for throttling

---

## 🤝 Contributing

PRs are welcome! Whether it's adding new city support, improving prompts, or enhancing tests, feel free to contribute.

---

## 📄 License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

