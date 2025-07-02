import time
import yaml
from julep import Julep
from dotenv import load_dotenv

client = Julep(api_key=os.getenv("JULEP_API_KEY"))

# 1. Create agent
agent = client.agents.create(
    name="MultiCityDiningAgent",
    model="claude-3.5-sonnet",
    about="Provides indoor/outdoor dining advice based on weather"
)

# 2. Load and create task
task_def = yaml.safe_load(open("dinning_sugestion.yaml"))
task = client.tasks.create(agent_id=agent.id, **task_def)
print("✅ Created task:", task.id)

# 3. Run task with multiple locations
locations = ["New York", "London", "Paris", "Tokyo", "Sydney"]
execution = client.executions.create(task_id=task.id, input={"locations": locations})
print("🚀 Executing task…", execution.id)

# 4. Poll for result
while True:
    res = client.executions.get(execution.id)
    print("⏱️ Status:", res.status)
    if res.status in ["succeeded", "failed", "cancelled"]:
        break
    time.sleep(2)

# ... after polling finishes
if res.status == "succeeded":
    # Add this line to inspect the raw structure:
    print("🔍 Raw output items:", res.output)

    print("\n✅ Dining Suggestions:")
    # Then parse based on what the structure actually is
    for i, item in enumerate(res.output):
        city = locations[i]
        # Example if the item is a simple string
        advice = item if isinstance(item, str) else item.get("choices", [{}])[0].get("message", {}).get("content", "")
        print(f"📍 {city}: {advice}\n")
else:
    print("❌ Task failed:", res.error)
