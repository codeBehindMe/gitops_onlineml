# data_simulator.py

# Author : aarontillekeratne
# Date : 2019-06-22

# This file is part of online_to_stream.

# online_to_stream is free software:
# you can redistribute it and/or modify it under the terms of the GNU General
# Public License as published by the Free Software Foundation, either version 3
# of the License, or (at your option) any later version.

# online_to_stream is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with online_to_stream.  
# If not, see <https://www.gnu.org/licenses/>.

"""
Contains the generator function.
"""

import numpy as np
from contextlib import contextmanager
from collections import namedtuple

DSRecord = namedtuple('DSRecord', ['features', 'target'])


@contextmanager
def linear_function_generator(low: int, high: int, *weights: iter):
    """
    Creates a generator whose values are generated using a linear function.

    The generator will generate random values for the 'independent variables'
    and elementwise multiply them with the weights. Then the sum of the results
    is used to compute the 'dependent variable'.

    :param low: Random integer floor.
    :param high: Random integer ceiling.
    :param weights: Weights of the linear function.
    :return:
    """
    w = np.array(weights)

    def gen():
        x = np.array(np.random.randint(low=low, high=high, size=len(weights)))
        return DSRecord(x.tolist(), np.sum(x * w))

    yield gen
