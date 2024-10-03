init -5 python:

    from abc import ABC

    # logger = getModuleLogger("Singleton.rpy")

    class Singleton(type, ABC):
        """Prevent multiple instantiations of each item type"""

        # Store single instances of each class
        _instances = {}

        def __call__(cls, *args, **kwargs):
            # If class hasn't been instantiated yet, we may instantiate it and then store it in Singleton.
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            # Otherwise, send a warning that a singleton class attempted to instantiate more than once
            # else:
            #     raise TypeError(f"Attempted to instantiate another instance of {cls}. {cls} has already been instantiated!")
            #     logger.warning(f"Attempted to instantiate another instance of {cls}. {cls} has already been instantiated!")
            #     print(f"Attempted to instantiate another instance of {cls}. {cls} has already been instantiated!")
            # Return the stored class
            return cls._instances[cls]