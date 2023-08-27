import dotenv
import os

dotenv.load_dotenv()

key         = os.getenv("PRIVATE_KEY")
sepolia_url = os.getenv("SEPOLIA_URL")
mumbai_url  = os.getenv("MUMBAI_URL")

