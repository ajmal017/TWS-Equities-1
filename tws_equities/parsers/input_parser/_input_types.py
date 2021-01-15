from argparse import ArgumentTypeError
from datetime import datetime as dt
from os import getcwd
from os.path import isfile
from os.path import join
from os.path import sep


class _EndDate:

    def __call__(self, end_date):
        _err = 'Expected a date-like string, format: "YYYYMMDD" (Ex: "20210101")'
        # all characters must be digits
        # there must be 8 digits in total (YYYYMMDD)
        if not(end_date.isdigit()) or len(end_date) != 8:
            raise ArgumentTypeError(_err)
        try:
            dt.strptime(end_date, '%Y%m%d')
        except:
            raise ArgumentTypeError(_err)
        return end_date


class _EndTime:

    def __call__(self, end_time):
        _err = 'Expected a time-like string in 24-hour format: "HH:MM:SS (Ex: "15:01:00")"'
        try:
            dt.strptime(end_time, '%H:%M:%S')
        except:
            raise ArgumentTypeError(_err)
        return end_time


class _Duration:

    def __call__(self, duration):
        _err = 'Expected a string containing a digit and a unit separated by whitespace (Ex: "1 D").'
        valid_units = ['S', 'D', 'W', 'M', 'Y']
        try:
            digit, unit = duration.split()
            assert digit.isdigit()
            assert unit in valid_units
        except:
            raise ArgumentTypeError(_err)
        return duration


class _BarSize:

    def __call__(self, bar_size):
        _err = 'Expected a string containing a digit and a valid unit for bar size (Ex: "1 min").'
        valid_bar_sizes = {
            'secs': [1, 5, 10, 15, 30],
            'min': [1, 2, 3, 5, 10, 15, 20, 30],
            'hour': [1, 2, 3, 4, 8],
            'day': [1],
            'week': [1],
            'month': [1]
        }
        try:
            digit, unit = bar_size.split()
            assert digit.isdigit(), f'{_err}'
            assert unit in list(valid_bar_sizes), f'{_err}\n'\
                                                  f'Acceptable units are: {list(valid_bar_sizes.keys())}'
            assert int(digit) in valid_bar_sizes[unit], f'{_err}\n'\
                                                        f'Acceptable values for given unit({unit}) are: '\
                                                        f'{valid_bar_sizes[unit]}'
        except Exception as e:
            raise ArgumentTypeError(f'{e}')
        return bar_size


class _TickersList:

    def __call__(self, value):
        _err = f'User should specify a list of ticker ID(s) separated by whitespace.'
        try:
            raise NotImplementedError(f'Tickers list is not implemented yet.')
        except Exception as e:
            raise ArgumentTypeError(f'{e}')
        # return value


class _File:

    def __call__(self, file):
        _err = f'Expected a valid file-path, file({file}) does not exist.'
        _supproted_file_types = ['csv']
        _special_keywords = ['test', 'default']
        try:
            if file not in _special_keywords:
                # make sure user passes file in supported formats
                file_type = file.split(sep)[-1].split('.')[-1]
                assert file_type in _supproted_file_types, f'Given file type is not supported yet, ' \
                                                           f'please choose from: {_supproted_file_types}'

                # support relative paths
                if not(isfile(file)):
                    file = join(getcwd(), file)

                # check if file actually exists
                assert isfile(file), _err
        except Exception as e:
            raise ArgumentTypeError(f'{e}')
        return file


class _URL:

    def __call__(self, url):
        try:
            raise NotImplementedError('URL parsing is not supported yet!')
        except Exception as e:
            raise ArgumentTypeError(f'{e}')


INPUT_TYPES = {
                    'end_date': _EndDate(),
                    'end_time': _EndTime(),
                    'duration': _Duration(),
                    'bar_size': _BarSize(),
                    'file': _File(),
                    'url': _URL(),
                    'list': _TickersList()
              }
