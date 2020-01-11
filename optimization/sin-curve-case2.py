import sys
import math
import matplotlib.pyplot as g

GAMMA = 1e-3
EPSILON = 1e-3


def f(x):
  return math.sin(math.pi * x / 180)


def df(x):
  return math.cos(math.pi * x / 180)


def point_generator(x_max):
  X = []
  Y = []
  for x in range(-x_max, x_max):
    X.append(x)
    Y.append(f(x))

  return X, Y


def gradient_descent(start):
  x = start
  print("df(x) = {}".format(df(x)))
  while df(x) > EPSILON or df(x) < -EPSILON:
    x = x - GAMMA*df(x)
    print("df(x) = {}".format(df(x)))

  return x


def x_axis(x_max):
  X = []
  Y = []
  for x in range(-x_max, x_max):
    X.append(x)
    Y.append(0)

  return X, Y


def main():
  x_max = 360
  X0, Y0 = x_axis(x_max)
  g.plot(X0, Y0)

  X, Y = point_generator(x_max)
  start_x = 150

  critical_x = gradient_descent(start_x)
  print("Critical x = {}".format(critical_x))

  g.plot(X, Y)
  g.plot([start_x], [f(start_x)], marker='o', markersize=10, color="blue")
  g.plot([critical_x], [f(critical_x)], marker='o', markersize=10, color="red")
  g.xlabel("X")
  g.ylabel("Y")
  g.show()

if __name__ == "__main__":
  main()
