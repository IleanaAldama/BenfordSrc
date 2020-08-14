Script for plotting Benford distribution of lines of code in a programming project

### Dependencies
 - [python-tabulate](https://pypi.org/project/tabulate/)
 - [aciiplotlib](https://pypi.org/project/asciiplotlib/)

### Usage
#### positional arguments:
  directory            Directory

#### arguments:
  -h, --help           show this help message and exit
  --ext EXT [EXT ...]  List of extentions to look for: .c .h
### Example
`python main.py ~/Dev/linux --ext .c .h  `
```


  Digit    Freq    Predicted
-------  ------  -----------
      1   15139        15198
      2    9212         8890
      3    6505         6307
      4    4888         4892
      5    3849         3997
      6    3250         3379
      7    2880         2927
      8    2486         2582
      9    2278         2310


Plot

  16000 +-------------------------------------------------------------------+
        |                                                                   |
        |*                                                                  |
  14000 | *                                                                 |
        |  *                                                                |
        |   *                                                               |
  12000 |    *                                                              |
        |     *                                                             |
        |      *                                                            |
  10000 |       *                                                           |
        |        ***                                                        |
        |           **                                                      |
   8000 |             **                                                    |
        |               *                                                   |
        |                *****                                              |
   6000 |                     ***                                           |
        |                        *                                          |
        |                         ********                                  |
   4000 |                                 *********                         |
        |                                          ********                 |
        |                                                  *****************|
   2000 +-------------------------------------------------------------------+
        1        2       3        4       5        6       7        8       9
```
