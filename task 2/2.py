import json

# Read JSON from file
with open('ex5.json', 'r') as f:
    ex5 = json.load(f)

# Add batter named "Tea" for donut with name "Old Fashioned"
for donut in ex5['donuts']:
    if donut['name'] == 'Old Fashioned':
        donut['batters']['batter'].append({'id': '1005', 'type': 'Tea'})
        break

# Update JSON file
with open('ex5.json', 'w') as f:
    json.dump(ex5, f, indent=4)

print("Batter named 'Tea' added for donut with name 'Old Fashioned' and ex5.json updated.")

