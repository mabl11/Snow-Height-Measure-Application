from dataclasses import dataclass

@dataclass
class CDataElements:
    """Class to save data
        1. snow depth [float]
        2. temperature [float]
        3. height over sea level [int] """
    snow_depth: float
    temperature: float
    height: int