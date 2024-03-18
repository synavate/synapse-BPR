# A Collection of functions for user related operations

def hash_user(user, topic):
    return str(hash(f"{user}-{topic}"))
