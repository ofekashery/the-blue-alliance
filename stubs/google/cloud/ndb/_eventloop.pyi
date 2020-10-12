from collections import namedtuple
from typing import Any

_Event = namedtuple('_Event', ['when', 'callback', 'args', 'kwargs'])

class EventLoop:
    current: Any = ...
    idlers: Any = ...
    inactive: int = ...
    queue: Any = ...
    rpcs: Any = ...
    rpc_results: Any = ...
    def __init__(self) -> None: ...
    def clear(self) -> None: ...
    def insort_event_right(self, event: Any) -> None: ...
    def call_soon(self, callback: Any, *args: Any, **kwargs: Any) -> None: ...
    def queue_call(self, delay: Any, callback: Any, *args: Any, **kwargs: Any) -> None: ...
    def queue_rpc(self, rpc: Any, callback: Any) -> None: ...
    def add_idle(self, callback: Any, *args: Any, **kwargs: Any) -> None: ...
    def run_idle(self): ...
    def run0(self): ...
    def run1(self): ...
    def run(self) -> None: ...

def get_event_loop(): ...
def add_idle(callback: Any, *args: Any, **kwargs: Any) -> None: ...
def call_soon(callback: Any, *args: Any, **kwargs: Any) -> None: ...
def queue_call(delay: Any, callback: Any, *args: Any, **kwargs: Any) -> None: ...
def queue_rpc(future: Any, rpc: Any) -> None: ...
def run() -> None: ...
def run0() -> None: ...
def run1() -> None: ...