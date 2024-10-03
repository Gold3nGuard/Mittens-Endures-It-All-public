init -4 python:

    # Initialize logging
    import os
    from pathlib import Path
    import logging 
    from logging import Logger

    def getModuleLogger(name: str) -> Logger:
        logger = logging.getLogger(name)
        logfile: str = f"{os.getcwd()}/logs/{name}.log"
        logdir: str = logfile.rsplit('/', 1)[0]
        Path(logdir).mkdir(parents=True, exist_ok=True)
        if not os.path.exists(logfile):
            with open(logfile, "w"):
                pass
        logging.basicConfig(filename=logfile, level=logging.INFO, format="[%(asctime)s] %(levelname)s: %(name)s %(message)s")
        return logger