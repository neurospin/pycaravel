##########################################################################
# NSAp - Copyright (C) CEA, 2019
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

"""
This module defines the CSV dataset loader.
"""

# Third party import
import vcfpy

# Package import
from .loader_base import LoaderBase


class VCF(LoaderBase):
    """ Define the TSV loader.
    """
    allowed_extensions = [".vcf"]

    def load(self, path):
        """ A method that load the table data.

        Parameters
        ----------
        path: str
            the path to the table to be loaded.

        Returns
        -------
        data: Ordered dict
            the loaded table.
        """

        return vcfpy.Reader.from_path(path)
