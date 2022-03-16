#!/usr/bin/env python
# Created by "Thieu" at 21:32, 14/03/2022 ----------%                                                                               
#       Email: nguyenthieu2102@gmail.com            %                                                    
#       Github: https://github.com/thieu1995        %                         
# --------------------------------------------------%

import numpy as np
from mealpy.utils.boundary import is_in_bound
from mealpy.utils.logger import Logger


class Validator:
    def __init__(self, **kwargs):
        self.log_to, self.log_file = None, None
        self.__set_keyword_arguments(kwargs)
        self.logger = Logger(self.log_to, log_file=self.log_file).create_logger(name=f"{__name__}.{__class__.__name__}",
            format_str='%(asctime)s, %(levelname)s, %(name)s [line: %(lineno)d]: %(message)s')
        self.logger.propagate = False

    def __set_keyword_arguments(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def check_int(self, name:str, value:int, bound=None):
        if type(value) in [int, float]:
            if bound is None:
                return int(value)
            elif is_in_bound(value, bound):
                return int(value)
        bound = "" if bound is None else f", and valid range is: {bound}"
        self.logger.error(f"'{name}' should be an integer{bound}.")
        exit(0)

    def check_float(self, name: str, value: int, bound=None):
        if type(value) in [int, float]:
            if bound is None:
                return float(value)
            elif is_in_bound(value, bound):
                return float(value)
        bound = "" if bound is None else f", and valid range is: {bound}"
        self.logger.error(f"'{name}' should be a float{bound}.")
        exit(0)

    def check_tuple_int(self, name: str, values: tuple, bounds=None):
        if type(values) in [tuple, list] and len(values) > 1:
            value_flag = [type(item) == int for item in values]
            if np.all(value_flag):
                if bounds is not None and len(bounds) == len(values):
                    value_flag = [is_in_bound(item, bound) for item, bound in zip(values, bounds)]
                    if np.all(value_flag):
                        return values
                else:
                    return values
        bounds = "" if bounds is None else f", and should be in range: {bounds}"
        self.logger.error(f"'{name}' are int values{bounds}.")
        exit(0)

    def check_tuple_float(self, name: str, values: tuple, bounds=None):
        if type(values) in [tuple, list] and len(values) > 1:
            value_flag = [type(item) in [int, float] for item in values]
            if np.all(value_flag):
                if bounds is not None and len(bounds) == len(values):
                    value_flag = [is_in_bound(item, bound) for item, bound in zip(values, bounds)]
                    if np.all(value_flag):
                        return values
                else:
                    return values
        bounds = "" if bounds is None else f", and should be in range: {bounds}"
        self.logger.error(f"'{name}' are float values{bounds}.")
        exit(0)


