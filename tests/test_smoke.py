import pytest
import torch

import project_name


def test_package_imports() -> None:
    assert project_name.__name__ == "project_name"


def test_tensor_sum():
    x = torch.ones(2, 3)
    assert x.sum().item() == 6.0


@pytest.mark.gpu
def test_cuda_tensor_sum():
    x = torch.ones(2, 3, device="cuda")
    assert x.sum().item() == 6.0
