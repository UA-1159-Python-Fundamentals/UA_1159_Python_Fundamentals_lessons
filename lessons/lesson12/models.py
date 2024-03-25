class User:
    def __init__(self, user_id, username, email):
        self.id = user_id
        self.username = username
        self.email = email

    def __repr__(self):
        return (
            f"User(user_id={self.id}, username='{self.username}', email='{self.email}')"
        )

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }

    def update(self, username=None, email=None):
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
