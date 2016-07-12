from eecom.point import Point
import pandas as pd

data = pd.read_csv('./data_point_21.csv', header=None, names=['dt', 'value'])

s1 = data.iloc[:, 1]
s1.index = data['dt']
p1 = Point(s1)
print p1
