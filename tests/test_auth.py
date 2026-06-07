from auth import AuthSystem

auth = AuthSystem()

# Register user
auth.register("kriti", "securepassword123")

# Correct login
auth.login("kriti", "securepassword123")

# Wrong password attempts
auth.login("kriti", "wrong1")
auth.login("kriti", "wrong2")
auth.login("kriti", "wrong3")

# Should block now
auth.login("kriti", "securepassword123")