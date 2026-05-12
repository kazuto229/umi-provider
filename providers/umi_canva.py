from providers.base import BaseProvider

class UMICanvaProvider(BaseProvider):

    name = "UMI-Canva"

    async def authenticate(self):
        print("[UMI-Canva] authenticate")

    async def fetch_quota(self):
        return {
            "remaining": 850
        }

    async def send_prompt(self, prompt):
        return {
            "provider": self.name,
            "response": f"UMI-Canva processed: {prompt}"
        }