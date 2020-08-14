from os import walk, path
from tabulate import tabulate
from math import log10
import argparse
import asciiplotlib as apl

def walkfiles(callback, dir= '.', ext=''):
  [callback(path.join(root, file)) for root, dirs, files in walk(dir)
                                   for file in files
                                   if file.endswith(ext)]

def countlines(acc, file):
  count = 0
  with open(file) as f:
    try:
     for line in f:
       count += 1
    except:
      print(f'failed to open: {file}')
      print('skiping...')
  acc.append(count)

def predicted(digit, total):
  factor = log10(1.0 + 1.0/float(digit))
  return int(total * factor)


def benford(numbers):
  total = len(numbers)
  freqs = [0] * 9
  for number in numbers:
    digit = int(str(number)[0])
    freqs[digit - 1] += 1
  result = [(index + 1, value, predicted(index + 1, total))
            for index, value in enumerate(freqs)]
  return result

def benfordtable(table):
  print(tabulate(table, headers=['Digit', 'Freq', 'Predicted']))

def benfordplot(table):
  fig = apl.figure()
  fig.plot((t[0] for t in table), (t[1] for t in table))
  fig.show()

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
      description='Calulates the Benford distribution on lines of code of a project')
  parser.add_argument('--ext', required=True, nargs='+',
                      type=str, help="List of extentions to look for: .c .h")
  parser.add_argument('directory', type=str, help="Directory")
  args = parser.parse_args()
  acc = []
  callback = lambda file: countlines(acc, file)
  walkfiles(callback, args.directory, tuple(args.ext))
  res = benford(acc)
  print('\n\n\n')
  benfordtable(res)
  print('\n\nPlot\n')
  benfordplot(res)
