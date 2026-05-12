class ProviderRouter:

    def __init__(self, providers):
        self.providers = providers

    async def route_prompt(self, prompt):

        for provider in self.providers:

            quota = await provider.fetch_quota()

            if quota.get("remaining", 0) > 0:
                return await provider.send_prompt(prompt)

        return {
            "error": "No provider available"
        }