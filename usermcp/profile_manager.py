import os
import yaml
from typing import Dict, Any

class ProfileManager:
    def __init__(self, profiles_dir: str = "profiles"):
        self.profiles_dir = profiles_dir
        self.default_profile = {
            'theme': 'light',
            'language': 'en-US',
            'notifications': True
        }
        os.makedirs(self.profiles_dir, exist_ok=True)

    def _get_user_file(self, user_id: str) -> str:
        return os.path.join(self.profiles_dir, f"{user_id}.yaml")

    def _load_yaml(self, file_path: str) -> Dict[str, Any]:
        if not os.path.exists(file_path):
            return {}
        with open(file_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}

    def _save_yaml(self, file_path: str, data: Dict[str, Any]) -> None:
        with open(file_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(data, f, allow_unicode=True)

    def get_profile(self, user_id: str) -> Dict[str, Any]:
        user_file = self._get_user_file(user_id)
        if os.path.exists(user_file):
            return self._load_yaml(user_file)
        return self.default_profile

    def insert_profile(self, user_id: str, profile_data: Dict[str, Any]) -> Dict[str, Any]:
        user_file = self._get_user_file(user_id)
        if os.path.exists(user_file):
            existing = self._load_yaml(user_file)
            existing.update(profile_data)
            self._save_yaml(user_file, existing)
            return existing
        else:
            default_data = self.default_profile
            default_data.update(profile_data)
            self._save_yaml(user_file, default_data)
            return default_data

    def delete_profile(self, user_id: str) -> bool:
        user_file = self._get_user_file(user_id)
        if os.path.exists(user_file):
            os.remove(user_file)
            return True
        return False
