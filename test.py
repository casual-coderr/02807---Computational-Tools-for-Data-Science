"""
Calculate actual cycling distances for bike-sharing routes using OpenRouteService API
"""

import requests
import time
import pandas as pd

# Free OpenRouteService API - Sign up at https://openrouteservice.org/dev/#/signup
# Replace with your API key
API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6Ijc3NmZmY2ExNzc5YjQzMjZhYThiMTk3ZWQwODAyNjgwIiwiaCI6Im11cm11cjY0In0="  # Get free key from openrouteservice.org

# Top 10 routes from your table
routes = [
    {"rank": 1, "route": "2006→2006", "lat1": 40.7659, "lon1": -73.9763, "lat2": 40.7659, "lon2": -73.9763, "table_dist": 0.00},
    {"rank": 2, "route": "432→3263", "lat1": 40.7262, "lon1": -73.9838, "lat2": 40.7295, "lon2": -73.9908, "table_dist": 0.70},
    {"rank": 3, "route": "281→281", "lat1": 40.7644, "lon1": -73.9737, "lat2": 40.7644, "lon2": -73.9737, "table_dist": 0.00},
    {"rank": 4, "route": "2006→3282", "lat1": 40.7659, "lon1": -73.9763, "lat2": 40.7831, "lon2": -73.9594, "table_dist": 2.39},
    {"rank": 5, "route": "460→3093", "lat1": 40.7129, "lon1": -73.9659, "lat2": 40.7175, "lon2": -73.9585, "table_dist": 0.81},
    {"rank": 6, "route": "3093→460", "lat1": 40.7175, "lon1": -73.9585, "lat2": 40.7129, "lon2": -73.9659, "table_dist": 0.81},
    {"rank": 7, "route": "435→509", "lat1": 40.7417, "lon1": -73.9942, "lat2": 40.7455, "lon2": -74.0020, "table_dist": 0.78},
    {"rank": 8, "route": "519→492", "lat1": 40.7519, "lon1": -73.9777, "lat2": 40.7502, "lon2": -73.9909, "table_dist": 1.14},
    {"rank": 9, "route": "519→498", "lat1": 40.7519, "lon1": -73.9777, "lat2": 40.7485, "lon2": -73.9881, "table_dist": 0.96},
    {"rank": 10, "route": "387→387", "lat1": 40.7127, "lon1": -74.0046, "lat2": 40.7127, "lon2": -74.0046, "table_dist": 0.00},
]


def get_cycling_distance(lon1, lat1, lon2, lat2, api_key):
    """
    Get actual cycling distance using OpenRouteService API
    Returns distance in km
    """
    if lat1 == lat2 and lon1 == lon2:
        return 0.0  # Same station
    
    url = "https://api.openrouteservice.org/v2/directions/cycling-regular"
    
    headers = {
        'Authorization': api_key,
        'Content-Type': 'application/json'
    }
    
    body = {
        "coordinates": [[lon1, lat1], [lon2, lat2]],
        "format": "json"
    }
    
    try:
        response = requests.post(url, json=body, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        # Distance is in meters, convert to km
        distance_m = data['routes'][0]['summary']['distance']
        return distance_m / 1000.0
    except Exception as e:
        print(f"Error fetching route: {e}")
        return None


def main():
    print("=" * 50)
    print("CYCLING DISTANCE CALCULATOR")
    print("=" * 50)
    print()
    
    if API_KEY == "YOUR_API_KEY_HERE":
        print("⚠️  Please set your OpenRouteService API key!")
        print()
        print("Steps to get a free API key:")
        print("1. Go to https://openrouteservice.org/dev/#/signup")
        print("2. Sign up for a free account")
        print("3. Copy your API key")
        print("4. Replace 'YOUR_API_KEY_HERE' in this script with your key")
        print()
        print("Free tier includes: 2,000 requests/day, 40 requests/minute")
        return
    
    results = []
    
    print(f"{'Rank':<6} {'Route':<15} {'Cycling Distance (km)':<25}")
    print("-" * 50)
    
    for route in routes:
        cycling_dist = get_cycling_distance(
            route['lon1'], route['lat1'],
            route['lon2'], route['lat2'],
            API_KEY
        )
        
        if cycling_dist is not None:
            print(f"{route['rank']:<6} {route['route']:<15} {cycling_dist:<25.2f}")
            
            results.append({
                'rank': route['rank'],
                'route': route['route'],
                'cycling_distance_km': cycling_dist
            })
        else:
            print(f"{route['rank']:<6} {route['route']:<15} {'ERROR':<25}")
        
        # Rate limiting - free tier: 40 req/min
        time.sleep(1.5)
    
    print()
    print("=" * 50)
    print("SUMMARY")
    print("=" * 50)
    
    if results:
        df = pd.DataFrame(results)
        
        # Save to CSV
        df.to_csv('cycling_distances.csv', index=False)
        print(f"\n✓ Results saved to cycling_distances.csv")
        print(f"✓ Total routes processed: {len(results)}")



if __name__ == "__main__":
    main()
