import logging


class ControllerBase:
    def __init__(self, logger: logging.Logger) -> None:
        self._logger = logger
      
    def exec(self, name: str):
        raise NotImplementedError()

        
    