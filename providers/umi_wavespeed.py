from providers.base import BaseProvider

class UMIWavespeedProvider(BaseProvider):

    name = "UMI-Wavespeed"

    async def authenticate(self):
        print("[UMI-Wavespeed] authenticate")

    async def fetch_quota(self):
        return {
            "remaining": 640
        }

    async def send_prompt(self, prompt):
        return {
            "provider": self.name,
            "response": f"UMI-Wavespeed processed: {prompt}"
        }