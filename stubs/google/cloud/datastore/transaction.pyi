from google.cloud.datastore.batch import Batch as Batch
from google.cloud.datastore_v1.types import TransactionOptions as TransactionOptions
from typing import Any, Optional

class Transaction(Batch):
    def __init__(self, client: Any, read_only: bool = ...) -> None: ...
    @property
    def id(self): ...
    def current(self): ...
    def begin(self, retry: Optional[Any] = ..., timeout: Optional[Any] = ...) -> None: ...
    def rollback(self, retry: Optional[Any] = ..., timeout: Optional[Any] = ...) -> None: ...
    def commit(self, retry: Optional[Any] = ..., timeout: Optional[Any] = ...) -> None: ...
    def put(self, entity: Any) -> None: ...