from providers.base import BaseProvider

class UMIKiroProvider(BaseProvider):

    name = "UMI-Kiro"

    async def authenticate(self):
        print("[UMI-Kiro] authenticate")

    async def fetch_quota(self):
        return {
            "remaining": 1200
        }

    async def send_prompt(self, prompt):
        return {
            "provider": self.name,
            "response": f"UMI-Kiro processed: {prompt}"
        }