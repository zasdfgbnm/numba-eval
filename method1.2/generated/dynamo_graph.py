# ===== Subgraph 0 (model__0) =====

class <lambda>(torch.nn.Module):
    def forward(self, arg0_1: "f32[2, 3, 5, 7, 11, 13, 17, 19]"):
        # No stacktrace found for following nodes
        view: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.view.default(arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]);  arg0_1 = None

        # File: /opt/pytorch/numba-eval/method1.2/run.py:4 in _method1_2_inner, code: import torch
        pow_1: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(view, 2.0)
        sum_1: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_1, [0], True);  pow_1 = None
        pow_2: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_1, 0.5);  sum_1 = None
        clamp_min: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_2, 1e-12);  pow_2 = None
        expand: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min = None
        div: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(view, expand);  view = expand = None

        # File: /opt/pytorch/numba-eval/method1.2/run.py:5 in _method1_2_inner, code: import torch.nn.functional as F
        view_1: "f32[2, 3, 5, 7, 11, 13, 17, 19]" = torch.ops.aten.view.default(div, [2, 3, 5, 7, 11, 13, 17, 19]);  div = None
        return (view_1,)


# ===== Subgraph 1 (model__1) =====

class <lambda>(torch.nn.Module):
    def forward(self, arg0_1: "f32[2, 3, 5, 7, 11, 13, 17, 19]"):
        # File: /opt/pytorch/numba-eval/method1.2/run.py:7 in torch_dynamo_resume_in__method1_2_inner_at_6, code: from benchmark import time_cpu  # type: ignore[import-not-found]
        view: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.view.default(arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]);  arg0_1 = None

        # No stacktrace found for following nodes
        pow_1: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(view, 2.0)
        sum_1: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_1, [1], True);  pow_1 = None
        pow_2: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_1, 0.5);  sum_1 = None
        clamp_min: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_2, 1e-12);  pow_2 = None
        expand: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min = None
        div: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(view, expand);  view = expand = None
        view_1: "f32[2, 3, 5, 7, 11, 13, 17, 19]" = torch.ops.aten.view.default(div, [2, 3, 5, 7, 11, 13, 17, 19]);  div = None
        return (view_1,)


# ===== Subgraph 2 (model__2) =====

class <lambda>(torch.nn.Module):
    def forward(self, arg0_1: "f32[2, 3, 5, 7, 11, 13, 17, 19]"):
        # File: /opt/pytorch/numba-eval/method1.2/run.py:11 in torch_dynamo_resume_in__method1_2_inner_at_10, code: # (Dynamo does not support graph_break inside a for/while loop).
        view: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.view.default(arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]);  arg0_1 = None

        # File: /opt/pytorch/numba-eval/method1.2/run.py:12 in torch_dynamo_resume_in__method1_2_inner_at_10, code: _lines = ["def _method1_2_inner(tensor):"]
        pow_1: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(view, 2.0)
        sum_1: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_1, [2], True);  pow_1 = None
        pow_2: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_1, 0.5);  sum_1 = None
        clamp_min: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_2, 1e-12);  pow_2 = None
        expand: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min = None
        div: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(view, expand);  view = expand = None

        # File: /opt/pytorch/numba-eval/method1.2/run.py:13 in torch_dynamo_resume_in__method1_2_inner_at_10, code: _lines.append("    out = tensor")
        view_1: "f32[2, 3, 5, 7, 11, 13, 17, 19]" = torch.ops.aten.view.default(div, [2, 3, 5, 7, 11, 13, 17, 19]);  div = None
        return (view_1,)


# ===== Subgraph 3 (model__3) =====

class <lambda>(torch.nn.Module):
    def forward(self, arg0_1: "f32[2, 3, 5, 7, 11, 13, 17, 19]"):
        # File: /opt/pytorch/numba-eval/method1.2/run.py:15 in torch_dynamo_resume_in__method1_2_inner_at_14, code: _lines.append("    out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)")
        view: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.view.default(arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]);  arg0_1 = None

        # File: /opt/pytorch/numba-eval/method1.2/run.py:16 in torch_dynamo_resume_in__method1_2_inner_at_14, code: _lines.append(f"    out = torch.nn.functional.normalize(out, dim={_i % 4})")
        pow_1: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(view, 2.0)
        sum_1: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_1, [3], True);  pow_1 = None
        pow_2: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_1, 0.5);  sum_1 = None
        clamp_min: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_2, 1e-12);  pow_2 = None
        expand: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min = None
        div: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(view, expand);  view = expand = None

        # File: /opt/pytorch/numba-eval/method1.2/run.py:17 in torch_dynamo_resume_in__method1_2_inner_at_14, code: _lines.append("    out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)")
        view_1: "f32[2, 3, 5, 7, 11, 13, 17, 19]" = torch.ops.aten.view.default(div, [2, 3, 5, 7, 11, 13, 17, 19]);  div = None
        return (view_1,)


