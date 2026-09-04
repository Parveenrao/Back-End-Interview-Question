# Concrete Observer 



from abc import ABC, abstractmethod


class Observer(ABC):
    """Interface that every observer must implement."""

    @abstractmethod
    def update(self, temperature: float) -> None:
        """Receive updated temperature."""
        pass