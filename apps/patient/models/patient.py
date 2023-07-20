from typing import Any
from prisma.models import Patient


class PatientModel(Patient):
    def __init_subclass__(
        cls, *args: Any, warn_subclass: bool | None = None, **kwargs: Any
    ) -> None:
        return super().__init_subclass__(*args, warn_subclass=warn_subclass, **kwargs)
