# Copyright (C) 2016-2021 by the multiphenics authors
#
# This file is part of multiphenics.
#
# multiphenics is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# multiphenics is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with multiphenics. If not, see <http://www.gnu.org/licenses/>.
#

import dolfin as df
import multiphenics as mp
from .multiscale_formulation import MultiscaleFormulation


class FormulationLinear(MultiscaleFormulation):
    def bcs(self):
        onBoundary = df.CompiledSubDomain("on_boundary")
        uD = self.others["uD"] if "uD" in self.others else df.Constant((0, 0))

        bc1 = mp.DirichletBC(self.W.sub(0), uD, onBoundary)
        return [mp.BlockDirichletBC([bc1])]
