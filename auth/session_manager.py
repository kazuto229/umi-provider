class SessionManager:

    def load_session(self):
        return {}

    def save_session(self, provider, session):
        print(f"Saved session for {provider}")