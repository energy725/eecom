import pandas as pd
from pandas import Series
from pandas.tseries.index import DatetimeIndex


class Point(object):
    """
    The basic representation unit of energy data, usually refers to monitoring
    or measurement point of meters or sensors.
    """

    def __init__(self, data, p_name=None, p_type='cumulative'):
        """
        :param data: the input energy data
        :param p_name: the name tag for the point
        :param p_type: the type of energy data (cumulative, gap, instant)
        """

        if data is None:
            data = {}

        if isinstance(data, Series):

            if not isinstance(data.index, DatetimeIndex):
                try:
                    data.index = pd.to_datetime(data.index)
                except ValueError:
                    raise ValueError('invalid index value when importing from Series')

            if p_name is None:
                p_name = data.name
        elif isinstance(data, dict):
            try:
                data = Series(data)
                data.name = p_name
                data.index = pd.to_datetime(data.index)
            except ValueError:
                raise ValueError('input dict must be with timestamp key')
        else:
            raise ValueError('input data type unaccepted')

        if p_type not in [None, 'cumulative', 'gap', 'instant']:
            raise ValueError('unexpected value of p_type')

        self.data = data.sort_index()
        self.p_name = p_name
        self.p_type = p_type

        self.type_check()

    def __str__(self):
        return 'Point object \n' \
               'name: %s\n' \
               'type: %s\n' \
               'data: \n%s' % \
               (self.p_name, self.p_type, self.data)
    __repr__ = __str__

    def type_check(self):
        """
        check whether the input data violates the type
        """

        values = self.data.values
        if self.p_type == 'cumulative':
            if not all(values[i] >= values[i-1] for i in range(1, len(values))):
                raise ValueError("energy data does not match the type 'cumulative'")
        elif self.p_type == 'gap':
            return True
        elif self.p_type == 'instant':
            return False

    def time_min(self):
        return self.data.index.min()

    def time_max(self):
        return self.data.index.max()

    def time_len(self):
        return self.data.index.max() - self.data.index.min()

    def intervals(self):
        dts = sorted(self.data.index)
        return [dts[i] - dts[i-1] for i in range(1, len(dts))]

    def interval_fixed(self):
        if set(self.intervals()) > 1:
            return False
        return True

