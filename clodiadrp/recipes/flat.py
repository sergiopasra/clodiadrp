

from numina.core import Product, Requirement
from numina.core import DataFrameType
from numina.types.obsresult import ObservationResultType
from numina.core.recipes import BaseRecipe


class Flat(BaseRecipe):

    obresult = Requirement(ObservationResultType, "Observation Result")
    master_bias = Requirement(DataFrameType, "Master Bias")
    master_flat = Product(DataFrameType)

    def run(self, rinput):

        # Here the raw images are processed
        # and a final image myframe is created
        myframe = None
        #

        result = self.create_result(master_flat=myframe)  (4)
        return result