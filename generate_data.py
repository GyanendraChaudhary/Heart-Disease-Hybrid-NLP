import os
import random
import pandas as pd

os.makedirs("data", exist_ok=True)

rows = []

symptoms_high = [
    "chest pain shortness of breath fatigue dizziness",
    "severe chest pressure sweating breathing difficulty",
    "irregular heartbeat chest discomfort weakness",
    "pain in chest during exercise tiredness",
]

symptoms_low = [
    "normal breathing no chest pain active lifestyle",
    "mild fatigue no major symptoms",
    "healthy condition normal heart rate",
    "no chest pain good activity level",
]

for i in range(1000):
    age = random.randint(25, 85)
    sex = random.randint(0, 1)
    cp = random.randint(0, 3)
    trestbps = random.randint(90, 190)
    chol = random.randint(140, 380)
    thalach = random.randint(85, 205)

    risk_score = 0
    if age > 55: risk_score += 1
    if trestbps > 140: risk_score += 1
    if chol > 240: risk_score += 1
    if thalach < 120: risk_score += 1
    if cp in [2, 3]: risk_score += 1

    target = 1 if risk_score >= 3 else 0
    symptom_text = random.choice(symptoms_high if target == 1 else symptoms_low)

    rows.append([age, sex, cp, trestbps, chol, thalach, symptom_text, target])

df = pd.DataFrame(rows, columns=[
    "age", "sex", "cp", "trestbps", "chol", "thalach", "symptoms", "target"
])

df.to_csv("data/heart.csv", index=False)

print("✅ 1000 rows dataset generated successfully at data/heart.csv")