from myapp.configs import logger

from myapp.controllers.foo_controller import FooController


fooController = FooController(logger)

__all__ = [
    "fooController"
]