# encoding: utf-8

# (c) 2019 Open Risk, all rights reserved
#
# correlationMatrix is licensed under the Apache 2.0 license a copy of which is included
# in the source distribution of correlationMatrix. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.


"""
Example workflows using correlationMatrix to estimate single factor models from
timeseries data. The datasets are produced in examples/generate_synthetic_data.py

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import correlationMatrix as cm
from correlationMatrix import source_path
from correlationMatrix.utils.converters import datetime_to_float

dataset_path = source_path + "datasets/"

# Example 1: Uniform single factor model
# Example 2: Grouped loadings
# Example 3: Individual loadings

example = 1

# Step 1
# Load the data set into a pandas frame
# Make sure state is read as a string and not as integer
# Second synthetic data example:
# n entities with ~10 observations each, [0,1] state, 50%/50% correlation matrix
print("> Step 1: Load the data set into a pandas frame")
if example == 1:
    data = pd.read_csv(dataset_path + 'synthetic_data1.csv')
    print("> Step 2: Estimate Uniform single factor model")
    myMatrix = cm.FactorCorrelationMatrix()
    myMatrix.fit(data, method='UniformSingleFactor')
    # myMatrix.print()
elif example == 2:
    data = pd.read_csv(dataset_path + 'synthetic_data8.csv', dtype={'State': str})
elif example == 3:
    data = pd.read_csv(dataset_path + 'synthetic_data9.csv', parse_dates=True)
    # convert datetime data to floats, return also the observation window data
    bounds, data = datetime_to_float(data)
    print('Start and End dates', bounds)
