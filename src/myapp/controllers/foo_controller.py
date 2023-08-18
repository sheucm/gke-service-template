import logging

from myapp.controllers.controller_base import ControllerBase

class FooController(ControllerBase):
    def __init__(self, logger: logging.Logger):
        super().__init__(logger)

    def exec(self, name: str):
        self._logger.info(f"Hello, {name}. This is Foo.")

