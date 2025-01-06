
export URL=your-cloud-run-service-url
curl -X POST $URL/nutrients -H "Content-Type: application/json" -d '{
    "calories": 3,
    "protein": 70,
    "calcium": 0.8,
    "iron": 12,
    "vitamin_a": 5,
    "vitamin_b1": 1.8,
    "vitamin_b2": 2.7,
    "niacin": 18,
    "vitamin_c": 75
}'