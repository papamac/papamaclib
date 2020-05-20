"""
 PACKAGE:  papamac's common module library (papamaclib)
  MODULE:  nbi.py
   TITLE:  non-blocking command line input (nbi)
FUNCTION:  nbi provides a class and methods to incorporate non-blocking command
           line input into main programs.
   USAGE:  nbi is imported and used within main programs (e.g., msg-c and
           msg-s).  It is compatible with Python 2.7.16 and all versions of
           Python 3.x.
  AUTHOR:  papamac
 VERSION:  1.0.2
    DATE:  May 20, 2020


MIT LICENSE:

Copyright (c) 2018-2020 David A. Krause, aka papamac

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


DESCRIPTION:

****************************** needs work *************************************

DEPENDENCIES/LIMITATIONS:

****************************** needs work *************************************

"""

__author__ = 'papamac'
__version__ = '1.0.2'
__date__ = 'May 20, 2020'

from queue import Queue, Empty
from threading import Thread


class NBI(Thread):
    """
    **************************** needs work ***********************************
    """

    _queue = Queue()

    # Private method:

    @classmethod
    def _run(cls):
        while True:
            cls._queue.put(input())

    # Public methods:

    @classmethod
    def start(cls):
        _nbi = Thread(name='nbi', target=cls._run, daemon=True)
        _nbi.start()

    @classmethod
    def get_input(cls):
        try:
            data = cls._queue.get(timeout=1)
        except Empty:
            data = None
        return data
