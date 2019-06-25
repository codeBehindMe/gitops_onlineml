# test_data_simulator.py

# Author : aarontillekeratne
# Date : 2019-06-25

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


import pytest
from src.simulator.data_simulator import linear_function_generator
from src.simulator.data_simulator import DSRecord


@pytest.fixture(scope='class')
def linear_func_resources():
    with linear_function_generator(0, 10, 3, 4, 5) as f:
        yield f


@pytest.mark.usefixtures("linear_func_resources")
class TestLinearFunctionGenerator:

    def test_returns_callable(self, linear_func_resources: object):
        """
        Checks that the function returns a callable.
        :return:
        """

        assert callable(linear_func_resources)

    def test_inner_returns_dsr(self, linear_func_resources):
        """
        Checks that the internal generator returns a DSRecord object.
        :return:
        """
        assert isinstance(linear_func_resources(), DSRecord)
