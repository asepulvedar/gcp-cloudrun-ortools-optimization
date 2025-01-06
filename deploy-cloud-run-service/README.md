# Nutrients API Documentation

## Endpoint: `/nutrients`
**Method:** `POST`

**Description:** This endpoint receives nutrient data in JSON format, processes it, and returns the optimal annual cost for foods and the daily nutrient amounts.

### Input Parameters:
The request body should be a JSON object with the following structure:
```json
{
    "calories": 3,
    "protein": 70,
    "calcium": 0.8,
    "iron": 12,
    "vitamin_a": 5,
    "vitamin_b1": 1.8,
    "vitamin_b2": 2.7,
    "niacin": 18,
    "vitamin_c": 75
}
```

### Example request
```bash
curl -X POST http://127.0.0.1:5000/nutrients -H "Content-Type: application/json" -d '{
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
```

### Response:
The response will be a JSON object containing two keys: `foods` and `nutrients`. Each key will contain a JSON string representing a list of records.

**Example Response:**
```json
{
  "foods": "[{\"Food\":\"Wheat Flour (Enriched)\",\"Annual Cost\":10.7744575119},{\"Food\":\"Liver (Beef)\",\"Annual Cost\":0.6907834111},{\"Food\":\"Cabbage\",\"Annual Cost\":4.0932688648},{\"Food\":\"Spinach\",\"Annual Cost\":1.8277960704},{\"Food\":\"Navy Beans, Dried\",\"Annual Cost\":22.2754256872}]",
  "nutrients": "[{\"Nutrient\":\"Calories (kcal)\",\"Amount\":3.0,\"Minimum\":3.0},{\"Nutrient\":\"Protein (g)\",\"Amount\":147.4135349422,\"Minimum\":70.0},{\"Nutrient\":\"Calcium (g)\",\"Amount\":0.8,\"Minimum\":0.8},{\"Nutrient\":\"Iron (mg)\",\"Amount\":60.4669221017,\"Minimum\":12.0},{\"Nutrient\":\"Vitamin A (KIU)\",\"Amount\":5.0,\"Minimum\":5.0},{\"Nutrient\":\"Vitamin B1 (mg)\",\"Amount\":4.1204388048,\"Minimum\":1.8},{\"Nutrient\":\"Vitamin B2 (mg)\",\"Amount\":2.7,\"Minimum\":2.7},{\"Nutrient\":\"Niacin (mg)\",\"Amount\":27.3159807003,\"Minimum\":18.0},{\"Nutrient\":\"Vitamin C (mg)\",\"Amount\":75.0,\"Minimum\":75.0}]"
}
```

### Explanation of Response Fields:
- `foods`: A JSON string representing a list of foods with their respective annual costs.
  - `Food`: The name of the food.
  - `Annual Cost`: The annual cost of the food.

- `nutrients`: A JSON string representing a list of nutrients with their respective amounts and minimum required amounts.
  - `Nutrient`: The name of the nutrient.
  - `Amount`: The amount of the nutrient.
  - `Minimum`: The minimum required amount of the nutrient.
```