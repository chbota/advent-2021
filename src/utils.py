def read_input(path):
  res = []
  with open(path) as reader:
    line = reader.readline()
    while line != '':
      res.append(int(line))
      line = reader.readline()
  return res
