##########################################################################
# NSAp - Copyright (C) CEA, 2021
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
This module defines the CSV dataset loader.
"""

# Third party import
import pandas as pd

# Package import
from .loader_base import LoaderBase


class CSV(LoaderBase):
    """ Define the CSV loader.
    """
    allowed_extensions = [".csv"]

    def load(self, path, separator=",", header_type="infer", nrows=None,
             skiprows=None, usecols=None):
        """ A method that load the table data.

        Parameters
        ----------
        path: str
            the path to the CSV file to load.
        **kwargs: see pd.read_csv.

        Returns
        -------
        data: pandas DataFrame
            the loaded table.
        """

        return pd.read_csv(path, header=header_type, sep=separator,
                usecols=usecols, nrows=nrows, skiprows=skiprows)

    def save(self, data, path):
        """ A method that save the table.

        Parameters
        ----------
        data: pandas DataFrame
            the table to be saved.
        path: str
            the path to the CSV file to save the table into.
        """
        data.to_csv(path)
