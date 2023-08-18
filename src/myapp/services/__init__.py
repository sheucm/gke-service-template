import os
from abc import abstractmethod
from typing import Dict, Any
from myapp.configs import app_config
from myapp.configs import logger

class ServiceBase:
    required_envs = {}
  
    def __init__(self) -> None:
        self._config = app_config.get(self.service_name, {})
        self._logger = logger
    
    @property
    @abstractmethod
    def service_name(self) -> str:
        raise NotImplementedError
    
    @classmethod
    def _get_params(cls) -> Dict[str, Any]:
        params = {}
        for env_name, name in cls.required_envs.items():
            value = os.getenv(env_name)
            if value is None:
                raise AssertionError(f"Required {env_name} is not defined")
            params[name] = value
        return params