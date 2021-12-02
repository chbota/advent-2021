def read_input(path, process = lambda x: x):
  res = []
  with open(path) as reader:
    line = reader.readline()
    while line != '':
      res.append(process(line))
      line = reader.readline()
  return res
