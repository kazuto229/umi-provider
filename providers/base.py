class BaseProvider:

    name = "base"

    async def authenticate(self):
        pass

    async def fetch_quota(self):
        return {}

    async def send_prompt(self, prompt):
        raise NotImplementedError

    async def refresh_token(self):
        pass

    def available(self):
        return True