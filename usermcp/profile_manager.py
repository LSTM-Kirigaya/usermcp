import os
import yaml
from typing import Dict, Any

class ProfileManager:
    def __init__(self, profiles_dir: str = None):
        # 如果没有指定路径，就默认 ~/.usermcp/profiles
        if profiles_dir is None:
            home_dir = os.path.expanduser("~")
            profiles_dir = os.path.join(home_dir, ".usermcp", "profiles")
        
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
        return dict(self.default_profile)  # 返回副本，避免修改默认值

    def insert_profile(self, user_id: str, profile_data: Dict[str, Any]) -> Dict[str, Any]:
        user_file = self._get_user_file(user_id)
        if os.path.exists(user_file):
            existing = self._load_yaml(user_file)
            existing.update(profile_data)
            self._save_yaml(user_file, existing)
            return existing
        else:
            new_data = dict(self.default_profile)  # 拷贝默认配置
            new_data.update(profile_data)
            self._save_yaml(user_file, new_data)
            return new_data

    def delete_profile(self, user_id: str) -> bool:
        user_file = self._get_user_file(user_id)
        if os.path.exists(user_file):
            os.remove(user_file)
            return True
        return False
