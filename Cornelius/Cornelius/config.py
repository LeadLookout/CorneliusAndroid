class Config:
    def __init__(self):
        self.settings = {
            "learning_rate": 0.01,
            "modules_path": "./modules",
            # ...existing code...
        }
        self.validate_settings()

    def get_setting(self, key):
        return self.settings.get(key, None)

    def validate_settings(self):
        if not isinstance(self.settings.get("learning_rate"), (int, float)):
            raise ValueError("Invalid learning_rate in configuration")
        if not isinstance(self.settings.get("modules_path"), str):
            raise ValueError("Invalid modules_path in configuration")
