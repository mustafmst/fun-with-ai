import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


class Perceptron:
    def __init__(self, input_length, weighs=None):
        if weighs is None:
            self.weights = np.random.random(input_length) * 2 - 1
        else:
            self.weights = weighs
        self.learning_rate = 0.1

    @staticmethod
    def unit_step_function(whole_input):
        if whole_input >= 0:
            return 1
        return 0

    def __call__(self, in_data):
        weighted_inputs = self.weights * in_data
        weighted_sum = weighted_inputs.sum()
        return Perceptron.unit_step_function(weighted_sum)

    def adjust(self, target_result, calculated_result, in_data):
        error = target_result - calculated_result;
        for i in range(len(in_data)):
            correction = error * in_data[i] * self.learning_rate
            self.weights[i] += correction

    def print_weights(self):
        print(self.weights)


def above_line(point, line_func):
    x, y = point
    if y > line_func(x):
        return 1
    else:
        return 0


points = np.random.randint(1, 1000, (100, 2))
p = Perceptron(2)


def line(x):
    return x * 0.5


x = []
y = []

for point in points:
    p.adjust(above_line(point, line), p(point), point)
    x.append(point[0])
    y.append(point[1])

evaluation = Counter()
for point in points:
    if p(point) == above_line(point, line):
        evaluation["correct"] += 1
    else:
        evaluation["wrong"] += 1
print(evaluation.most_common())
p.print_weights()


def colors(x, y):
    cols = []
    for i in range(len(x)):
        if p([x[i], y[i]]) == 1:
            cols.append('green')
        else:
            cols.append('red')
    return cols


plt.plot([0, 1000], [line(0), line(1000)])
plt.scatter(x, y, s=20, c=colors(x, y))
plt.show()
