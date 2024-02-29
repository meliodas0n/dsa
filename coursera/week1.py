import sys

def a():
  return "Hello, World"

def b():
  return f"Hello {sys.argv[1]} and {sys.argv[2]}\nGoodbye {sys.argv[1]} and {sys.argv[2]}"

def c():
  pass

if __name__ == "__main__":
  print(a())
  if len(sys.argv) != 0: print(b())
  print(c())
