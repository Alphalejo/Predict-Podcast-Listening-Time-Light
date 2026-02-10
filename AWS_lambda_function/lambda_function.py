import json
import random
import math

data = {
  "features": {
    "Episode_Title": 65,
    "Episode_Length_minutes": 35,
    "Host_Popularity_percentage": 60,
    "Guest_Popularity_percentage": 52.51,
    "Number_of_Ads": 1,
    "Episode_Sentiment": 1,
    "Guest_Popularity_missing": 1,
    "Genre_encoded": 44.37182458341537,
    "Time_sin": 0,
    "Time_cos": 1,
    "Day_sin": 1,
    "Day_cos": 0,
    "Podcast_Encoded": 46.723734650096695
  }
}


FEATURE_WEIGHTS = {
    "Episode_Title": 0.035,
    "Episode_Length_minutes": 0.776,
    "Host_Popularity_percentage": 0.047,
    "Guest_Popularity_percentage": 0.039,
    "Number_of_Ads": -0.010,
    "Episode_Sentiment": 0.008,
    "Guest_Popularity_missing": -0.002,
    "Genre_encoded": 0.015,
    "Time_sin": 0.008,
    "Time_cos": 0.005,
    "Day_sin": 0.013,
    "Day_cos": 0.008,
    "Podcast_Encoded": 0.034
}

def normalize(value, min_val, max_val):
    if max_val == min_val:
        return 0
    return (value - min_val) / (max_val - min_val)

def fake_listening_time_prediction(features: dict) -> float:
    score = 0.0

    episode_length = features.get("Episode_Length_minutes", 30)

    for feature, weight in FEATURE_WEIGHTS.items():
        value = features.get(feature, 0)

        if feature == "Episode_Length_minutes":
            value = normalize(value, 5, 180)

        elif "Popularity" in feature:
            value = normalize(value, 0, 100)

        elif feature == "Number_of_Ads":
            value = normalize(value, 0, 10)

        elif feature == "Episode_Sentiment":
            value = normalize(value, -1, 1)

        elif feature in ["Genre_encoded", "Podcast_Encoded"]:
            value = normalize(value, 0, 100)

        else:
            value = normalize(value, 0, 1)

        

        score += value * weight
    
    # listening ratio
    ratio = 1 / (1 + math.exp(-score))
    ratio += random.uniform(-0.03, 0.03)
    ratio = min(max(ratio, 0.05), 1)

    print("score:", score)
    print("ratio:", ratio)


    # Minutes lisntened
    listening_time = ratio * episode_length

    return round(listening_time, 2)

def lambda_handler(event, context):
    features = event.get("features", {})

    prediction = fake_listening_time_prediction(features)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "predicted_listening_time_minutes": prediction,
        })
    }

if __name__ == "__main__":
    print (lambda_handler(data, None))