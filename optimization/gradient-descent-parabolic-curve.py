import matplotlib.pyplot as g
import sys

GAMMA = 1e-6
EPSILON = 1e-6

def f(x):
  return x**2

def df(x):
  return 2*x

def point_generator(x_max):
  X = []
  Y = []
  for x in range(-x_max, x_max):
    X.append(x)
    Y.append(f(x))

  return X, Y

def gradient_descent(start):
  x = start
  while df(x) > EPSILON or df(x) < -EPSILON:
    x = x - GAMMA*df(x)

  return x

def main():
  X, Y = point_generator(100)
  start_x = -64

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
