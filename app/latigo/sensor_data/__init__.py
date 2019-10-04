from dataclasses import dataclass
from datetime import datetime, timedelta
import pandas as pd
import typing


@dataclass
class Task:
    name: str
    from_time: datetime = datetime.now() - +timedelta(0, 20)
    to_time: datetime = datetime.now()


@dataclass
class TimeRange:

    from_time: datetime
    to_time: datetime


@dataclass
class SensorData:

    time_range: TimeRange

    def __str__(self):
        return "PredictionData"


@dataclass
class PredictionData:
    name: str
    time_range: TimeRange
    result: typing.Iterable[typing.Tuple[str, pd.DataFrame, typing.List[str]]]

    def __str__(self):
        return "PredictionData"
