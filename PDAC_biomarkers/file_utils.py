"""
File IO utilities
"""

import pandas as pd
from pathlib import Path


def read_csv(filepath: Path) -> pd.DataFrame:
    return pd.read_csv(filepath)
