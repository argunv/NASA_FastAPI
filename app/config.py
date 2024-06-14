from os import getenv
from dotenv import load_dotenv

load_dotenv()

# URL базы данных
DATABASE_URL = (
    f"postgresql://{getenv('POSTGRES_USER')}:{getenv('POSTGRES_PASSWORD')}"
    f"@{getenv('POSTGRES_HOST')}:{getenv('POSTGRES_PORT')}/{getenv('POSTGRES_DB')}"
)

if getenv("TESTING"):
    DATABASE_URL = "sqlite:///./test.db"

# NASA_API_URL = "https://api.nasa.gov/EPIC/api/natural"
NEO_URL = "https://api.nasa.gov/neo/rest/v1/feed"
DONKI_URL = "https://api.nasa.gov/DONKI/FLR"
TLE_URL = "https://tle.ivanstanojevic.me/api/tle"
# EARTH_API_URL = "https://api.nasa.gov/planetary/earth/imagery" # Does not work

# Ключ API NASA
NASA_API_KEY = getenv("TOKEN", "DEMO_KEY")
BASE_URL = "http://localhost:8000"
