"""
 PACKAGE:  papamac's common module library (papamaclib)
  MODULE:  argsandlogs.py
   TITLE:  command line argument and and logging (argsandlogs)
FUNCTION:  argsandlogs provides generalized definition and parsing of
           command line arguments and setup of both print and file logging for
           main programs.  It uses the standard Python argparse and logging
           modules.
   USAGE:  Import argsandlogs in main programs as needed.  It is compatible
           with all versions of Python 3.x.  It is incompatible with Python 2.7
           because of its use of the pathlib package and also because it uses
           the reserved function name print as a variable.
  AUTHOR:  papamac
 VERSION:  1.0.5
    DATE:  April 7, 2020


MIT LICENSE:

Copyright (c) 2019-2020 David A. Krause, aka papamac

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
__version__ = '1.0.5'
__date__ = 'April 7, 2020'


from argparse import ArgumentParser
import logging
from logging import addLevelName, Formatter, StreamHandler
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from . import colortext
from .colortext import DATA, THREAD_DEBUG


# Global constant.

LOG = colortext.getLogger('Plugin')


class AL:
    """
    """
    _log = logging.getLogger('Plugin')
    parser = ArgumentParser()
    name = parser.prog.replace('.py', '')
    args = None

    @classmethod
    def start(cls, version=''):
        """
        Parse command line arguments, initialize printing/logging and log main
        program starting message.
        """
        cls.parser.add_argument('-p', '--print', choices=['THREAD_DEBUG',
                    'DEBUG', 'DATA', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    help='optional printing to sys.stdout and printing level')
        cls.parser.add_argument('-l', '--log', choices=['THREAD_DEBUG',
                    'DEBUG', 'DATA', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                    help='optional file logging and logging level')
        cls.parser.add_argument('-L', '--log_directory',
                    default='/var/local/log',
                    help='top-level log directory (full pathname or relative)')
        cls.args = cls.parser.parse_args()

        addLevelName(THREAD_DEBUG, 'THREAD_DEBUG')
        addLevelName(DATA, 'DATA')
        cls._log.setLevel(THREAD_DEBUG)

        if cls.args.print:
            print_handler = StreamHandler()
            print_handler.setLevel(cls.args.print)
            print_formatter = Formatter('%(message)s')
            print_handler.setFormatter(print_formatter)
            cls._log.addHandler(print_handler)

        if cls.args.log:
            dir_path = Path(cls.args.log_directory)
            log_path = dir_path / Path(cls.name.lower() + '.log')
            try:
                dir_path.mkdir(parents=True, exist_ok=True)
                log_handler = TimedRotatingFileHandler(log_path,
                                                       when='midnight')
            except OSError as err:
                warning = ('open error %s "%s" %s; log option ignored'
                           % (err.errno, log_path, err.strerror))
                LOG.warning(warning)
                cls.args.log = None
            else:
                log_handler.setLevel(cls.args.log)
                log_formatter = Formatter(
                    '%(asctime)s %(levelname)s %(message)s')
                log_handler.setFormatter(log_formatter)
                cls._log.addHandler(log_handler)

        if version:
            version = ' v' + version
        LOG.blue('starting %s%s with the following arguments/defaults:'
                 % (cls.name, version))
        LOG.blue('%s' % str(cls.args).split('(')[1][:-1])

    @classmethod
    def stop(cls):

        # Log main program stopping message.

        LOG.blue('stopping %s' % cls.name)
