# plumber_data.py
# Mock data source for plumbers

plumbers = [
    {
        "name": "John's Plumbing Services",
        "pincode": "560001",
        "rating": 4.8,
        "reviews": 120
    },
    {
        "name": "AquaFix Plumbers",
        "pincode": "560001",
        "rating": 4.5,
        "reviews": 98
    },
    {
        "name": "PipeMasters",
        "pincode": "560002",
        "rating": 4.9,
        "reviews": 150
    },
    {
        "name": "QuickFlow Plumbing",
        "pincode": "560001",
        "rating": 4.2,
        "reviews": 75
    },
    {
        "name": "Urban Plumbers",
        "pincode": "560003",
        "rating": 4.7,
        "reviews": 110
    },
]

def get_plumbers_by_pincode(pincode):
    return [p for p in plumbers if p["pincode"] == pincode] 