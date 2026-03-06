class <lambda>(torch.nn.Module):
    def forward(self, arg0_1: "f32[2, 3, 5, 7, 11, 13, 17, 19]"):
        # File: /opt/pytorch/numba-eval/method1.1/run.py:13 in _method1_1_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        view: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.view.default(arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]);  arg0_1 = None

        # File: /opt/pytorch/numba-eval/method1.1/run.py:14 in _method1_1_inner, code: out = F.normalize(out, dim=(i % 4))
        pow_1: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(view, 2.0)
        sum_1: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_1, [0], True);  pow_1 = None
        pow_2: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_1, 0.5);  sum_1 = None
        clamp_min: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_2, 1e-12);  pow_2 = None
        expand: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min = None
        div: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(view, expand);  view = expand = None
        pow_3: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div, 2.0)
        sum_2: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_3, [1], True);  pow_3 = None
        pow_4: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_2, 0.5);  sum_2 = None
        clamp_min_1: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_4, 1e-12);  pow_4 = None
        expand_1: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_1, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_1 = None
        div_1: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div, expand_1);  div = expand_1 = None
        pow_5: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_1, 2.0)
        sum_3: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_5, [2], True);  pow_5 = None
        pow_6: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_3, 0.5);  sum_3 = None
        clamp_min_2: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_6, 1e-12);  pow_6 = None
        expand_2: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_2, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_2 = None
        div_2: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_1, expand_2);  div_1 = expand_2 = None
        pow_7: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_2, 2.0)
        sum_4: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_7, [3], True);  pow_7 = None
        pow_8: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_4, 0.5);  sum_4 = None
        clamp_min_3: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_8, 1e-12);  pow_8 = None
        expand_3: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_3, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_3 = None
        div_3: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_2, expand_3);  div_2 = expand_3 = None
        pow_9: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_3, 2.0)
        sum_5: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_9, [0], True);  pow_9 = None
        pow_10: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_5, 0.5);  sum_5 = None
        clamp_min_4: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_10, 1e-12);  pow_10 = None
        expand_4: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_4, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_4 = None
        div_4: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_3, expand_4);  div_3 = expand_4 = None
        pow_11: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_4, 2.0)
        sum_6: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_11, [1], True);  pow_11 = None
        pow_12: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_6, 0.5);  sum_6 = None
        clamp_min_5: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_12, 1e-12);  pow_12 = None
        expand_5: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_5, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_5 = None
        div_5: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_4, expand_5);  div_4 = expand_5 = None
        pow_13: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_5, 2.0)
        sum_7: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_13, [2], True);  pow_13 = None
        pow_14: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_7, 0.5);  sum_7 = None
        clamp_min_6: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_14, 1e-12);  pow_14 = None
        expand_6: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_6, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_6 = None
        div_6: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_5, expand_6);  div_5 = expand_6 = None
        pow_15: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_6, 2.0)
        sum_8: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_15, [3], True);  pow_15 = None
        pow_16: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_8, 0.5);  sum_8 = None
        clamp_min_7: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_16, 1e-12);  pow_16 = None
        expand_7: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_7, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_7 = None
        div_7: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_6, expand_7);  div_6 = expand_7 = None
        pow_17: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_7, 2.0)
        sum_9: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_17, [0], True);  pow_17 = None
        pow_18: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_9, 0.5);  sum_9 = None
        clamp_min_8: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_18, 1e-12);  pow_18 = None
        expand_8: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_8, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_8 = None
        div_8: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_7, expand_8);  div_7 = expand_8 = None
        pow_19: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_8, 2.0)
        sum_10: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_19, [1], True);  pow_19 = None
        pow_20: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_10, 0.5);  sum_10 = None
        clamp_min_9: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_20, 1e-12);  pow_20 = None
        expand_9: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_9, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_9 = None
        div_9: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_8, expand_9);  div_8 = expand_9 = None
        pow_21: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_9, 2.0)
        sum_11: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_21, [2], True);  pow_21 = None
        pow_22: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_11, 0.5);  sum_11 = None
        clamp_min_10: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_22, 1e-12);  pow_22 = None
        expand_10: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_10, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_10 = None
        div_10: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_9, expand_10);  div_9 = expand_10 = None
        pow_23: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_10, 2.0)
        sum_12: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_23, [3], True);  pow_23 = None
        pow_24: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_12, 0.5);  sum_12 = None
        clamp_min_11: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_24, 1e-12);  pow_24 = None
        expand_11: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_11, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_11 = None
        div_11: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_10, expand_11);  div_10 = expand_11 = None
        pow_25: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_11, 2.0)
        sum_13: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_25, [0], True);  pow_25 = None
        pow_26: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_13, 0.5);  sum_13 = None
        clamp_min_12: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_26, 1e-12);  pow_26 = None
        expand_12: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_12, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_12 = None
        div_12: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_11, expand_12);  div_11 = expand_12 = None
        pow_27: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_12, 2.0)
        sum_14: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_27, [1], True);  pow_27 = None
        pow_28: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_14, 0.5);  sum_14 = None
        clamp_min_13: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_28, 1e-12);  pow_28 = None
        expand_13: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_13, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_13 = None
        div_13: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_12, expand_13);  div_12 = expand_13 = None
        pow_29: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_13, 2.0)
        sum_15: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_29, [2], True);  pow_29 = None
        pow_30: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_15, 0.5);  sum_15 = None
        clamp_min_14: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_30, 1e-12);  pow_30 = None
        expand_14: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_14, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_14 = None
        div_14: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_13, expand_14);  div_13 = expand_14 = None
        pow_31: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_14, 2.0)
        sum_16: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_31, [3], True);  pow_31 = None
        pow_32: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_16, 0.5);  sum_16 = None
        clamp_min_15: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_32, 1e-12);  pow_32 = None
        expand_15: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_15, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_15 = None
        div_15: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_14, expand_15);  div_14 = expand_15 = None
        pow_33: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_15, 2.0)
        sum_17: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_33, [0], True);  pow_33 = None
        pow_34: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_17, 0.5);  sum_17 = None
        clamp_min_16: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_34, 1e-12);  pow_34 = None
        expand_16: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_16, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_16 = None
        div_16: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_15, expand_16);  div_15 = expand_16 = None
        pow_35: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_16, 2.0)
        sum_18: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_35, [1], True);  pow_35 = None
        pow_36: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_18, 0.5);  sum_18 = None
        clamp_min_17: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_36, 1e-12);  pow_36 = None
        expand_17: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_17, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_17 = None
        div_17: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_16, expand_17);  div_16 = expand_17 = None
        pow_37: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_17, 2.0)
        sum_19: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_37, [2], True);  pow_37 = None
        pow_38: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_19, 0.5);  sum_19 = None
        clamp_min_18: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_38, 1e-12);  pow_38 = None
        expand_18: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_18, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_18 = None
        div_18: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_17, expand_18);  div_17 = expand_18 = None
        pow_39: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_18, 2.0)
        sum_20: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_39, [3], True);  pow_39 = None
        pow_40: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_20, 0.5);  sum_20 = None
        clamp_min_19: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_40, 1e-12);  pow_40 = None
        expand_19: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_19, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_19 = None
        div_19: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_18, expand_19);  div_18 = expand_19 = None
        pow_41: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_19, 2.0)
        sum_21: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_41, [0], True);  pow_41 = None
        pow_42: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_21, 0.5);  sum_21 = None
        clamp_min_20: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_42, 1e-12);  pow_42 = None
        expand_20: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_20, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_20 = None
        div_20: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_19, expand_20);  div_19 = expand_20 = None
        pow_43: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_20, 2.0)
        sum_22: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_43, [1], True);  pow_43 = None
        pow_44: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_22, 0.5);  sum_22 = None
        clamp_min_21: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_44, 1e-12);  pow_44 = None
        expand_21: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_21, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_21 = None
        div_21: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_20, expand_21);  div_20 = expand_21 = None
        pow_45: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_21, 2.0)
        sum_23: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_45, [2], True);  pow_45 = None
        pow_46: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_23, 0.5);  sum_23 = None
        clamp_min_22: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_46, 1e-12);  pow_46 = None
        expand_22: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_22, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_22 = None
        div_22: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_21, expand_22);  div_21 = expand_22 = None
        pow_47: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_22, 2.0)
        sum_24: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_47, [3], True);  pow_47 = None
        pow_48: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_24, 0.5);  sum_24 = None
        clamp_min_23: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_48, 1e-12);  pow_48 = None
        expand_23: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_23, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_23 = None
        div_23: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_22, expand_23);  div_22 = expand_23 = None
        pow_49: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_23, 2.0)
        sum_25: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_49, [0], True);  pow_49 = None
        pow_50: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_25, 0.5);  sum_25 = None
        clamp_min_24: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_50, 1e-12);  pow_50 = None
        expand_24: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_24, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_24 = None
        div_24: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_23, expand_24);  div_23 = expand_24 = None
        pow_51: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_24, 2.0)
        sum_26: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_51, [1], True);  pow_51 = None
        pow_52: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_26, 0.5);  sum_26 = None
        clamp_min_25: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_52, 1e-12);  pow_52 = None
        expand_25: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_25, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_25 = None
        div_25: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_24, expand_25);  div_24 = expand_25 = None
        pow_53: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_25, 2.0)
        sum_27: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_53, [2], True);  pow_53 = None
        pow_54: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_27, 0.5);  sum_27 = None
        clamp_min_26: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_54, 1e-12);  pow_54 = None
        expand_26: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_26, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_26 = None
        div_26: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_25, expand_26);  div_25 = expand_26 = None
        pow_55: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_26, 2.0)
        sum_28: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_55, [3], True);  pow_55 = None
        pow_56: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_28, 0.5);  sum_28 = None
        clamp_min_27: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_56, 1e-12);  pow_56 = None
        expand_27: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_27, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_27 = None
        div_27: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_26, expand_27);  div_26 = expand_27 = None
        pow_57: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_27, 2.0)
        sum_29: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_57, [0], True);  pow_57 = None
        pow_58: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_29, 0.5);  sum_29 = None
        clamp_min_28: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_58, 1e-12);  pow_58 = None
        expand_28: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_28, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_28 = None
        div_28: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_27, expand_28);  div_27 = expand_28 = None
        pow_59: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_28, 2.0)
        sum_30: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_59, [1], True);  pow_59 = None
        pow_60: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_30, 0.5);  sum_30 = None
        clamp_min_29: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_60, 1e-12);  pow_60 = None
        expand_29: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_29, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_29 = None
        div_29: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_28, expand_29);  div_28 = expand_29 = None
        pow_61: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_29, 2.0)
        sum_31: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_61, [2], True);  pow_61 = None
        pow_62: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_31, 0.5);  sum_31 = None
        clamp_min_30: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_62, 1e-12);  pow_62 = None
        expand_30: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_30, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_30 = None
        div_30: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_29, expand_30);  div_29 = expand_30 = None
        pow_63: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_30, 2.0)
        sum_32: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_63, [3], True);  pow_63 = None
        pow_64: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_32, 0.5);  sum_32 = None
        clamp_min_31: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_64, 1e-12);  pow_64 = None
        expand_31: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_31, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_31 = None
        div_31: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_30, expand_31);  div_30 = expand_31 = None
        pow_65: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_31, 2.0)
        sum_33: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_65, [0], True);  pow_65 = None
        pow_66: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_33, 0.5);  sum_33 = None
        clamp_min_32: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_66, 1e-12);  pow_66 = None
        expand_32: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_32, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_32 = None
        div_32: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_31, expand_32);  div_31 = expand_32 = None
        pow_67: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_32, 2.0)
        sum_34: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_67, [1], True);  pow_67 = None
        pow_68: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_34, 0.5);  sum_34 = None
        clamp_min_33: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_68, 1e-12);  pow_68 = None
        expand_33: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_33, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_33 = None
        div_33: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_32, expand_33);  div_32 = expand_33 = None
        pow_69: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_33, 2.0)
        sum_35: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_69, [2], True);  pow_69 = None
        pow_70: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_35, 0.5);  sum_35 = None
        clamp_min_34: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_70, 1e-12);  pow_70 = None
        expand_34: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_34, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_34 = None
        div_34: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_33, expand_34);  div_33 = expand_34 = None
        pow_71: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_34, 2.0)
        sum_36: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_71, [3], True);  pow_71 = None
        pow_72: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_36, 0.5);  sum_36 = None
        clamp_min_35: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_72, 1e-12);  pow_72 = None
        expand_35: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_35, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_35 = None
        div_35: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_34, expand_35);  div_34 = expand_35 = None
        pow_73: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_35, 2.0)
        sum_37: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_73, [0], True);  pow_73 = None
        pow_74: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_37, 0.5);  sum_37 = None
        clamp_min_36: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_74, 1e-12);  pow_74 = None
        expand_36: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_36, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_36 = None
        div_36: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_35, expand_36);  div_35 = expand_36 = None
        pow_75: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_36, 2.0)
        sum_38: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_75, [1], True);  pow_75 = None
        pow_76: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_38, 0.5);  sum_38 = None
        clamp_min_37: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_76, 1e-12);  pow_76 = None
        expand_37: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_37, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_37 = None
        div_37: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_36, expand_37);  div_36 = expand_37 = None
        pow_77: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_37, 2.0)
        sum_39: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_77, [2], True);  pow_77 = None
        pow_78: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_39, 0.5);  sum_39 = None
        clamp_min_38: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_78, 1e-12);  pow_78 = None
        expand_38: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_38, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_38 = None
        div_38: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_37, expand_38);  div_37 = expand_38 = None
        pow_79: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_38, 2.0)
        sum_40: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_79, [3], True);  pow_79 = None
        pow_80: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_40, 0.5);  sum_40 = None
        clamp_min_39: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_80, 1e-12);  pow_80 = None
        expand_39: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_39, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_39 = None
        div_39: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_38, expand_39);  div_38 = expand_39 = None
        pow_81: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_39, 2.0)
        sum_41: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_81, [0], True);  pow_81 = None
        pow_82: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_41, 0.5);  sum_41 = None
        clamp_min_40: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_82, 1e-12);  pow_82 = None
        expand_40: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_40, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_40 = None
        div_40: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_39, expand_40);  div_39 = expand_40 = None
        pow_83: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_40, 2.0)
        sum_42: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_83, [1], True);  pow_83 = None
        pow_84: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_42, 0.5);  sum_42 = None
        clamp_min_41: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_84, 1e-12);  pow_84 = None
        expand_41: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_41, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_41 = None
        div_41: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_40, expand_41);  div_40 = expand_41 = None
        pow_85: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_41, 2.0)
        sum_43: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_85, [2], True);  pow_85 = None
        pow_86: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_43, 0.5);  sum_43 = None
        clamp_min_42: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_86, 1e-12);  pow_86 = None
        expand_42: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_42, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_42 = None
        div_42: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_41, expand_42);  div_41 = expand_42 = None
        pow_87: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_42, 2.0)
        sum_44: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_87, [3], True);  pow_87 = None
        pow_88: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_44, 0.5);  sum_44 = None
        clamp_min_43: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_88, 1e-12);  pow_88 = None
        expand_43: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_43, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_43 = None
        div_43: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_42, expand_43);  div_42 = expand_43 = None
        pow_89: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_43, 2.0)
        sum_45: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_89, [0], True);  pow_89 = None
        pow_90: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_45, 0.5);  sum_45 = None
        clamp_min_44: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_90, 1e-12);  pow_90 = None
        expand_44: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_44, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_44 = None
        div_44: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_43, expand_44);  div_43 = expand_44 = None
        pow_91: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_44, 2.0)
        sum_46: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_91, [1], True);  pow_91 = None
        pow_92: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_46, 0.5);  sum_46 = None
        clamp_min_45: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_92, 1e-12);  pow_92 = None
        expand_45: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_45, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_45 = None
        div_45: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_44, expand_45);  div_44 = expand_45 = None
        pow_93: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_45, 2.0)
        sum_47: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_93, [2], True);  pow_93 = None
        pow_94: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_47, 0.5);  sum_47 = None
        clamp_min_46: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_94, 1e-12);  pow_94 = None
        expand_46: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_46, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_46 = None
        div_46: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_45, expand_46);  div_45 = expand_46 = None
        pow_95: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_46, 2.0)
        sum_48: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_95, [3], True);  pow_95 = None
        pow_96: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_48, 0.5);  sum_48 = None
        clamp_min_47: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_96, 1e-12);  pow_96 = None
        expand_47: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_47, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_47 = None
        div_47: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_46, expand_47);  div_46 = expand_47 = None
        pow_97: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_47, 2.0)
        sum_49: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_97, [0], True);  pow_97 = None
        pow_98: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_49, 0.5);  sum_49 = None
        clamp_min_48: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_98, 1e-12);  pow_98 = None
        expand_48: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_48, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_48 = None
        div_48: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_47, expand_48);  div_47 = expand_48 = None
        pow_99: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_48, 2.0)
        sum_50: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_99, [1], True);  pow_99 = None
        pow_100: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_50, 0.5);  sum_50 = None
        clamp_min_49: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_100, 1e-12);  pow_100 = None
        expand_49: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_49, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_49 = None
        div_49: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_48, expand_49);  div_48 = expand_49 = None
        pow_101: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_49, 2.0)
        sum_51: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_101, [2], True);  pow_101 = None
        pow_102: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_51, 0.5);  sum_51 = None
        clamp_min_50: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_102, 1e-12);  pow_102 = None
        expand_50: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_50, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_50 = None
        div_50: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_49, expand_50);  div_49 = expand_50 = None
        pow_103: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_50, 2.0)
        sum_52: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_103, [3], True);  pow_103 = None
        pow_104: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_52, 0.5);  sum_52 = None
        clamp_min_51: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_104, 1e-12);  pow_104 = None
        expand_51: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_51, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_51 = None
        div_51: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_50, expand_51);  div_50 = expand_51 = None
        pow_105: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_51, 2.0)
        sum_53: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_105, [0], True);  pow_105 = None
        pow_106: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_53, 0.5);  sum_53 = None
        clamp_min_52: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_106, 1e-12);  pow_106 = None
        expand_52: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_52, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_52 = None
        div_52: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_51, expand_52);  div_51 = expand_52 = None
        pow_107: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_52, 2.0)
        sum_54: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_107, [1], True);  pow_107 = None
        pow_108: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_54, 0.5);  sum_54 = None
        clamp_min_53: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_108, 1e-12);  pow_108 = None
        expand_53: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_53, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_53 = None
        div_53: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_52, expand_53);  div_52 = expand_53 = None
        pow_109: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_53, 2.0)
        sum_55: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_109, [2], True);  pow_109 = None
        pow_110: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_55, 0.5);  sum_55 = None
        clamp_min_54: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_110, 1e-12);  pow_110 = None
        expand_54: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_54, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_54 = None
        div_54: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_53, expand_54);  div_53 = expand_54 = None
        pow_111: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_54, 2.0)
        sum_56: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_111, [3], True);  pow_111 = None
        pow_112: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_56, 0.5);  sum_56 = None
        clamp_min_55: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_112, 1e-12);  pow_112 = None
        expand_55: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_55, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_55 = None
        div_55: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_54, expand_55);  div_54 = expand_55 = None
        pow_113: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_55, 2.0)
        sum_57: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_113, [0], True);  pow_113 = None
        pow_114: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_57, 0.5);  sum_57 = None
        clamp_min_56: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_114, 1e-12);  pow_114 = None
        expand_56: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_56, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_56 = None
        div_56: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_55, expand_56);  div_55 = expand_56 = None
        pow_115: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_56, 2.0)
        sum_58: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_115, [1], True);  pow_115 = None
        pow_116: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_58, 0.5);  sum_58 = None
        clamp_min_57: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_116, 1e-12);  pow_116 = None
        expand_57: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_57, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_57 = None
        div_57: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_56, expand_57);  div_56 = expand_57 = None
        pow_117: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_57, 2.0)
        sum_59: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_117, [2], True);  pow_117 = None
        pow_118: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_59, 0.5);  sum_59 = None
        clamp_min_58: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_118, 1e-12);  pow_118 = None
        expand_58: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_58, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_58 = None
        div_58: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_57, expand_58);  div_57 = expand_58 = None
        pow_119: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_58, 2.0)
        sum_60: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_119, [3], True);  pow_119 = None
        pow_120: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_60, 0.5);  sum_60 = None
        clamp_min_59: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_120, 1e-12);  pow_120 = None
        expand_59: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_59, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_59 = None
        div_59: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_58, expand_59);  div_58 = expand_59 = None
        pow_121: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_59, 2.0)
        sum_61: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_121, [0], True);  pow_121 = None
        pow_122: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_61, 0.5);  sum_61 = None
        clamp_min_60: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_122, 1e-12);  pow_122 = None
        expand_60: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_60, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_60 = None
        div_60: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_59, expand_60);  div_59 = expand_60 = None
        pow_123: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_60, 2.0)
        sum_62: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_123, [1], True);  pow_123 = None
        pow_124: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_62, 0.5);  sum_62 = None
        clamp_min_61: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_124, 1e-12);  pow_124 = None
        expand_61: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_61, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_61 = None
        div_61: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_60, expand_61);  div_60 = expand_61 = None
        pow_125: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_61, 2.0)
        sum_63: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_125, [2], True);  pow_125 = None
        pow_126: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_63, 0.5);  sum_63 = None
        clamp_min_62: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_126, 1e-12);  pow_126 = None
        expand_62: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_62, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_62 = None
        div_62: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_61, expand_62);  div_61 = expand_62 = None
        pow_127: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_62, 2.0)
        sum_64: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_127, [3], True);  pow_127 = None
        pow_128: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_64, 0.5);  sum_64 = None
        clamp_min_63: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_128, 1e-12);  pow_128 = None
        expand_63: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_63, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_63 = None
        div_63: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_62, expand_63);  div_62 = expand_63 = None
        pow_129: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_63, 2.0)
        sum_65: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_129, [0], True);  pow_129 = None
        pow_130: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_65, 0.5);  sum_65 = None
        clamp_min_64: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_130, 1e-12);  pow_130 = None
        expand_64: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_64, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_64 = None
        div_64: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_63, expand_64);  div_63 = expand_64 = None
        pow_131: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_64, 2.0)
        sum_66: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_131, [1], True);  pow_131 = None
        pow_132: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_66, 0.5);  sum_66 = None
        clamp_min_65: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_132, 1e-12);  pow_132 = None
        expand_65: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_65, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_65 = None
        div_65: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_64, expand_65);  div_64 = expand_65 = None
        pow_133: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_65, 2.0)
        sum_67: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_133, [2], True);  pow_133 = None
        pow_134: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_67, 0.5);  sum_67 = None
        clamp_min_66: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_134, 1e-12);  pow_134 = None
        expand_66: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_66, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_66 = None
        div_66: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_65, expand_66);  div_65 = expand_66 = None
        pow_135: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_66, 2.0)
        sum_68: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_135, [3], True);  pow_135 = None
        pow_136: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_68, 0.5);  sum_68 = None
        clamp_min_67: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_136, 1e-12);  pow_136 = None
        expand_67: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_67, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_67 = None
        div_67: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_66, expand_67);  div_66 = expand_67 = None
        pow_137: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_67, 2.0)
        sum_69: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_137, [0], True);  pow_137 = None
        pow_138: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_69, 0.5);  sum_69 = None
        clamp_min_68: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_138, 1e-12);  pow_138 = None
        expand_68: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_68, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_68 = None
        div_68: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_67, expand_68);  div_67 = expand_68 = None
        pow_139: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_68, 2.0)
        sum_70: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_139, [1], True);  pow_139 = None
        pow_140: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_70, 0.5);  sum_70 = None
        clamp_min_69: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_140, 1e-12);  pow_140 = None
        expand_69: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_69, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_69 = None
        div_69: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_68, expand_69);  div_68 = expand_69 = None
        pow_141: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_69, 2.0)
        sum_71: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_141, [2], True);  pow_141 = None
        pow_142: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_71, 0.5);  sum_71 = None
        clamp_min_70: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_142, 1e-12);  pow_142 = None
        expand_70: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_70, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_70 = None
        div_70: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_69, expand_70);  div_69 = expand_70 = None
        pow_143: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_70, 2.0)
        sum_72: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_143, [3], True);  pow_143 = None
        pow_144: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_72, 0.5);  sum_72 = None
        clamp_min_71: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_144, 1e-12);  pow_144 = None
        expand_71: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_71, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_71 = None
        div_71: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_70, expand_71);  div_70 = expand_71 = None
        pow_145: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_71, 2.0)
        sum_73: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_145, [0], True);  pow_145 = None
        pow_146: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_73, 0.5);  sum_73 = None
        clamp_min_72: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_146, 1e-12);  pow_146 = None
        expand_72: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_72, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_72 = None
        div_72: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_71, expand_72);  div_71 = expand_72 = None
        pow_147: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_72, 2.0)
        sum_74: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_147, [1], True);  pow_147 = None
        pow_148: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_74, 0.5);  sum_74 = None
        clamp_min_73: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_148, 1e-12);  pow_148 = None
        expand_73: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_73, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_73 = None
        div_73: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_72, expand_73);  div_72 = expand_73 = None
        pow_149: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_73, 2.0)
        sum_75: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_149, [2], True);  pow_149 = None
        pow_150: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_75, 0.5);  sum_75 = None
        clamp_min_74: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_150, 1e-12);  pow_150 = None
        expand_74: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_74, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_74 = None
        div_74: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_73, expand_74);  div_73 = expand_74 = None
        pow_151: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_74, 2.0)
        sum_76: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_151, [3], True);  pow_151 = None
        pow_152: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_76, 0.5);  sum_76 = None
        clamp_min_75: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_152, 1e-12);  pow_152 = None
        expand_75: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_75, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_75 = None
        div_75: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_74, expand_75);  div_74 = expand_75 = None
        pow_153: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_75, 2.0)
        sum_77: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_153, [0], True);  pow_153 = None
        pow_154: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_77, 0.5);  sum_77 = None
        clamp_min_76: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_154, 1e-12);  pow_154 = None
        expand_76: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_76, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_76 = None
        div_76: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_75, expand_76);  div_75 = expand_76 = None
        pow_155: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_76, 2.0)
        sum_78: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_155, [1], True);  pow_155 = None
        pow_156: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_78, 0.5);  sum_78 = None
        clamp_min_77: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_156, 1e-12);  pow_156 = None
        expand_77: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_77, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_77 = None
        div_77: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_76, expand_77);  div_76 = expand_77 = None
        pow_157: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_77, 2.0)
        sum_79: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_157, [2], True);  pow_157 = None
        pow_158: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_79, 0.5);  sum_79 = None
        clamp_min_78: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_158, 1e-12);  pow_158 = None
        expand_78: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_78, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_78 = None
        div_78: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_77, expand_78);  div_77 = expand_78 = None
        pow_159: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_78, 2.0)
        sum_80: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_159, [3], True);  pow_159 = None
        pow_160: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_80, 0.5);  sum_80 = None
        clamp_min_79: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_160, 1e-12);  pow_160 = None
        expand_79: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_79, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_79 = None
        div_79: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_78, expand_79);  div_78 = expand_79 = None
        pow_161: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_79, 2.0)
        sum_81: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_161, [0], True);  pow_161 = None
        pow_162: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_81, 0.5);  sum_81 = None
        clamp_min_80: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_162, 1e-12);  pow_162 = None
        expand_80: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_80, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_80 = None
        div_80: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_79, expand_80);  div_79 = expand_80 = None
        pow_163: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_80, 2.0)
        sum_82: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_163, [1], True);  pow_163 = None
        pow_164: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_82, 0.5);  sum_82 = None
        clamp_min_81: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_164, 1e-12);  pow_164 = None
        expand_81: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_81, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_81 = None
        div_81: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_80, expand_81);  div_80 = expand_81 = None
        pow_165: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_81, 2.0)
        sum_83: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_165, [2], True);  pow_165 = None
        pow_166: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_83, 0.5);  sum_83 = None
        clamp_min_82: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_166, 1e-12);  pow_166 = None
        expand_82: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_82, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_82 = None
        div_82: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_81, expand_82);  div_81 = expand_82 = None
        pow_167: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_82, 2.0)
        sum_84: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_167, [3], True);  pow_167 = None
        pow_168: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_84, 0.5);  sum_84 = None
        clamp_min_83: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_168, 1e-12);  pow_168 = None
        expand_83: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_83, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_83 = None
        div_83: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_82, expand_83);  div_82 = expand_83 = None
        pow_169: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_83, 2.0)
        sum_85: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_169, [0], True);  pow_169 = None
        pow_170: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_85, 0.5);  sum_85 = None
        clamp_min_84: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_170, 1e-12);  pow_170 = None
        expand_84: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_84, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_84 = None
        div_84: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_83, expand_84);  div_83 = expand_84 = None
        pow_171: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_84, 2.0)
        sum_86: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_171, [1], True);  pow_171 = None
        pow_172: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_86, 0.5);  sum_86 = None
        clamp_min_85: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_172, 1e-12);  pow_172 = None
        expand_85: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_85, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_85 = None
        div_85: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_84, expand_85);  div_84 = expand_85 = None
        pow_173: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_85, 2.0)
        sum_87: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_173, [2], True);  pow_173 = None
        pow_174: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_87, 0.5);  sum_87 = None
        clamp_min_86: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_174, 1e-12);  pow_174 = None
        expand_86: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_86, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_86 = None
        div_86: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_85, expand_86);  div_85 = expand_86 = None
        pow_175: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_86, 2.0)
        sum_88: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_175, [3], True);  pow_175 = None
        pow_176: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_88, 0.5);  sum_88 = None
        clamp_min_87: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_176, 1e-12);  pow_176 = None
        expand_87: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_87, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_87 = None
        div_87: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_86, expand_87);  div_86 = expand_87 = None
        pow_177: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_87, 2.0)
        sum_89: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_177, [0], True);  pow_177 = None
        pow_178: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_89, 0.5);  sum_89 = None
        clamp_min_88: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_178, 1e-12);  pow_178 = None
        expand_88: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_88, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_88 = None
        div_88: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_87, expand_88);  div_87 = expand_88 = None
        pow_179: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_88, 2.0)
        sum_90: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_179, [1], True);  pow_179 = None
        pow_180: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_90, 0.5);  sum_90 = None
        clamp_min_89: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_180, 1e-12);  pow_180 = None
        expand_89: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_89, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_89 = None
        div_89: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_88, expand_89);  div_88 = expand_89 = None
        pow_181: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_89, 2.0)
        sum_91: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_181, [2], True);  pow_181 = None
        pow_182: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_91, 0.5);  sum_91 = None
        clamp_min_90: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_182, 1e-12);  pow_182 = None
        expand_90: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_90, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_90 = None
        div_90: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_89, expand_90);  div_89 = expand_90 = None
        pow_183: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_90, 2.0)
        sum_92: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_183, [3], True);  pow_183 = None
        pow_184: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_92, 0.5);  sum_92 = None
        clamp_min_91: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_184, 1e-12);  pow_184 = None
        expand_91: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_91, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_91 = None
        div_91: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_90, expand_91);  div_90 = expand_91 = None
        pow_185: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_91, 2.0)
        sum_93: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_185, [0], True);  pow_185 = None
        pow_186: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_93, 0.5);  sum_93 = None
        clamp_min_92: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_186, 1e-12);  pow_186 = None
        expand_92: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_92, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_92 = None
        div_92: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_91, expand_92);  div_91 = expand_92 = None
        pow_187: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_92, 2.0)
        sum_94: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_187, [1], True);  pow_187 = None
        pow_188: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_94, 0.5);  sum_94 = None
        clamp_min_93: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_188, 1e-12);  pow_188 = None
        expand_93: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_93, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_93 = None
        div_93: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_92, expand_93);  div_92 = expand_93 = None
        pow_189: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_93, 2.0)
        sum_95: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_189, [2], True);  pow_189 = None
        pow_190: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_95, 0.5);  sum_95 = None
        clamp_min_94: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_190, 1e-12);  pow_190 = None
        expand_94: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_94, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_94 = None
        div_94: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_93, expand_94);  div_93 = expand_94 = None
        pow_191: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_94, 2.0)
        sum_96: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_191, [3], True);  pow_191 = None
        pow_192: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_96, 0.5);  sum_96 = None
        clamp_min_95: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_192, 1e-12);  pow_192 = None
        expand_95: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_95, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_95 = None
        div_95: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_94, expand_95);  div_94 = expand_95 = None
        pow_193: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_95, 2.0)
        sum_97: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_193, [0], True);  pow_193 = None
        pow_194: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_97, 0.5);  sum_97 = None
        clamp_min_96: "f32[1, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_194, 1e-12);  pow_194 = None
        expand_96: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_96, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_96 = None
        div_96: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_95, expand_96);  div_95 = expand_96 = None
        pow_195: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_96, 2.0)
        sum_98: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_195, [1], True);  pow_195 = None
        pow_196: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_98, 0.5);  sum_98 = None
        clamp_min_97: "f32[19, 1, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_196, 1e-12);  pow_196 = None
        expand_97: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_97, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_97 = None
        div_97: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_96, expand_97);  div_96 = expand_97 = None
        pow_197: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_97, 2.0)
        sum_99: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_197, [2], True);  pow_197 = None
        pow_198: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_99, 0.5);  sum_99 = None
        clamp_min_98: "f32[19, 17, 1, 11, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_198, 1e-12);  pow_198 = None
        expand_98: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_98, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_98 = None
        div_98: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_97, expand_98);  div_97 = expand_98 = None
        pow_199: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(div_98, 2.0)
        sum_100: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.sum.dim_IntList(pow_199, [3], True);  pow_199 = None
        pow_200: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.pow.Tensor_Scalar(sum_100, 0.5);  sum_100 = None
        clamp_min_99: "f32[19, 17, 13, 1, 7, 5, 3, 2]" = torch.ops.aten.clamp_min.default(pow_200, 1e-12);  pow_200 = None
        expand_99: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.expand.default(clamp_min_99, [19, 17, 13, 11, 7, 5, 3, 2]);  clamp_min_99 = None
        div_99: "f32[19, 17, 13, 11, 7, 5, 3, 2]" = torch.ops.aten.div.Tensor(div_98, expand_99);  div_98 = expand_99 = None

        # File: /opt/pytorch/numba-eval/method1.1/run.py:15 in _method1_1_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        view_199: "f32[2, 3, 5, 7, 11, 13, 17, 19]" = torch.ops.aten.view.default(div_99, [2, 3, 5, 7, 11, 13, 17, 19]);  div_99 = None
        return (view_199,)
