# -*- coding: utf-8 -*-
"""
This is code is used to test envirnonment.
"""

from __future__ import print_function

import torch

# python
print("hello world")

# torch
x = torch.Tensor(5, 3)
print(x)

print(x.size())

y = torch.rand(5, 3)
print(x + y)

z = torch.add(x,y)
print(z)

result = torch.Tensor(5, 3)
torch.add(x, y, out=result)
print(result)
