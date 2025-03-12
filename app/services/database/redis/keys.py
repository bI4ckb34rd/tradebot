from app.utils.key_builder import StorageKey


class UserKey(StorageKey, prefix="users"):
    key: str
