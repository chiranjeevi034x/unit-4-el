import os
 
API_KEY = os.environ.get("API_KEY")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
 
if not API_KEY or not DB_PASSWORD:
    raise SystemExit("Missing API_KEY or DB_PASSWORD: set them in the environment or a .env file")
 
 
def connect():
    # never print secrets; show only that they were loaded
    return f"Connecting with key=****{API_KEY[-4:]} and password loaded: {bool(DB_PASSWORD)}"
 
 
print(connect())
