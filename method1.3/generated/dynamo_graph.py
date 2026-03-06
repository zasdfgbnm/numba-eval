TRACED GRAPH
 ===== __compiled_fn_1_7de92bcd_14be_4503_a1f8_38c8c83ea38a =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_tensor_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_tensor_ = L_tensor_

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_tensor_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_tensor_ = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_1: "f32[][]cuda:0" = out.sum()
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out + sum_1;  out = sum_1 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_3: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_2.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_2 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_2: "f32[][]cuda:0" = out_3.sum()
        out_4: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_3 + sum_2;  out_3 = sum_2 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_5: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_4.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_4 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_6: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_5.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_5 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_3: "f32[][]cuda:0" = out_6.sum()
        out_7: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_6 + sum_3;  out_6 = sum_3 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_8: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_7.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_7 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_9: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_8.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_8 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_4: "f32[][]cuda:0" = out_9.sum()
        out_10: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_9 + sum_4;  out_9 = sum_4 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_11: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_10.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_10 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_12: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_11.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_11 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_5: "f32[][]cuda:0" = out_12.sum()
        out_13: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_12 + sum_5;  out_12 = sum_5 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_14: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_13.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_13 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_15: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_14.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_14 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_6: "f32[][]cuda:0" = out_15.sum()
        out_16: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_15 + sum_6;  out_15 = sum_6 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_17: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_16.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_16 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_18: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_17.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_17 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_7: "f32[][]cuda:0" = out_18.sum()
        out_19: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_18 + sum_7;  out_18 = sum_7 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_20: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_19.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_19 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_21: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_20.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_20 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_8: "f32[][]cuda:0" = out_21.sum()
        out_22: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_21 + sum_8;  out_21 = sum_8 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_23: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_22.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_22 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_24: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_23.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_23 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_9: "f32[][]cuda:0" = out_24.sum()
        out_25: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_24 + sum_9;  out_24 = sum_9 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_26: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_25.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_25 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_27: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_26.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_26 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_10: "f32[][]cuda:0" = out_27.sum()
        out_28: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_27 + sum_10;  out_27 = sum_10 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_29: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_28.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_28 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_30: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_29.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_29 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_11: "f32[][]cuda:0" = out_30.sum()
        out_31: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_30 + sum_11;  out_30 = sum_11 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_32: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_31.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_31 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_33: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_32.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_32 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_12: "f32[][]cuda:0" = out_33.sum()
        out_34: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_33 + sum_12;  out_33 = sum_12 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_35: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_34.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_34 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_36: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_35.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_35 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_13: "f32[][]cuda:0" = out_36.sum()
        out_37: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_36 + sum_13;  out_36 = sum_13 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_38: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_37.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_37 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_39: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_38.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_38 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_14: "f32[][]cuda:0" = out_39.sum()
        out_40: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_39 + sum_14;  out_39 = sum_14 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_41: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_40.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_40 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_42: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_41.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_41 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_15: "f32[][]cuda:0" = out_42.sum()
        out_43: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_42 + sum_15;  out_42 = sum_15 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_44: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_43.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_43 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_45: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_44.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_44 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_16: "f32[][]cuda:0" = out_45.sum()
        out_46: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_45 + sum_16;  out_45 = sum_16 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_47: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_46.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_46 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_48: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_47.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_47 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_17: "f32[][]cuda:0" = out_48.sum()
        out_49: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_48 + sum_17;  out_48 = sum_17 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_50: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_49.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_49 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_51: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_50.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_50 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_18: "f32[][]cuda:0" = out_51.sum()
        out_52: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_51 + sum_18;  out_51 = sum_18 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_53: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_52.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_52 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_54: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_53.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_53 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_19: "f32[][]cuda:0" = out_54.sum()
        out_55: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_54 + sum_19;  out_54 = sum_19 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_56: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_55.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_55 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_57: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_56.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_56 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_20: "f32[][]cuda:0" = out_57.sum()
        out_58: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_57 + sum_20;  out_57 = sum_20 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_59: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_58.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_58 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_60: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_59.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_59 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_21: "f32[][]cuda:0" = out_60.sum()
        out_61: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_60 + sum_21;  out_60 = sum_21 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_62: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_61.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_61 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_63: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_62.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_62 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_22: "f32[][]cuda:0" = out_63.sum()
        out_64: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_63 + sum_22;  out_63 = sum_22 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_65: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_64.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_64 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_66: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_65.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_65 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_23: "f32[][]cuda:0" = out_66.sum()
        out_67: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_66 + sum_23;  out_66 = sum_23 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_68: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_67.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_67 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_69: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_68.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_68 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_24: "f32[][]cuda:0" = out_69.sum()
        out_70: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_69 + sum_24;  out_69 = sum_24 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_71: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_70.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_70 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_72: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_71.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_71 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_25: "f32[][]cuda:0" = out_72.sum()
        out_73: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_72 + sum_25;  out_72 = sum_25 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_74: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_73.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_73 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_75: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_74.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_74 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_26: "f32[][]cuda:0" = out_75.sum()
        out_76: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_75 + sum_26;  out_75 = sum_26 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_77: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_76.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_76 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_78: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_77.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_77 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_27: "f32[][]cuda:0" = out_78.sum()
        out_79: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_78 + sum_27;  out_78 = sum_27 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_80: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_79.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_79 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_81: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_80.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_80 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_28: "f32[][]cuda:0" = out_81.sum()
        out_82: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_81 + sum_28;  out_81 = sum_28 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_83: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_82.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_82 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_84: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_83.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_83 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_29: "f32[][]cuda:0" = out_84.sum()
        out_85: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_84 + sum_29;  out_84 = sum_29 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_86: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_85.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_85 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_87: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_86.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_86 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_30: "f32[][]cuda:0" = out_87.sum()
        out_88: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_87 + sum_30;  out_87 = sum_30 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_89: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_88.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_88 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_90: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_89.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_89 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_31: "f32[][]cuda:0" = out_90.sum()
        out_91: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_90 + sum_31;  out_90 = sum_31 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_92: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_91.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_91 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_93: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_92.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_92 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_32: "f32[][]cuda:0" = out_93.sum()
        out_94: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_93 + sum_32;  out_93 = sum_32 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_95: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_94.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_94 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_96: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_95.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_95 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_33: "f32[][]cuda:0" = out_96.sum()
        out_97: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_96 + sum_33;  out_96 = sum_33 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_98: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_97.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_97 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_99: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_98.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_98 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_34: "f32[][]cuda:0" = out_99.sum()
        out_100: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_99 + sum_34;  out_99 = sum_34 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_101: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_100.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_100 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_102: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_101.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_101 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_35: "f32[][]cuda:0" = out_102.sum()
        out_103: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_102 + sum_35;  out_102 = sum_35 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_104: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_103.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_103 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_105: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_104.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_104 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_36: "f32[][]cuda:0" = out_105.sum()
        out_106: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_105 + sum_36;  out_105 = sum_36 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_107: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_106.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_106 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_108: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_107.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_107 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_37: "f32[][]cuda:0" = out_108.sum()
        out_109: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_108 + sum_37;  out_108 = sum_37 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_110: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_109.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_109 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_111: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_110.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_110 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_38: "f32[][]cuda:0" = out_111.sum()
        out_112: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_111 + sum_38;  out_111 = sum_38 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_113: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_112.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_112 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_114: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_113.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_113 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_39: "f32[][]cuda:0" = out_114.sum()
        out_115: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_114 + sum_39;  out_114 = sum_39 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_116: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_115.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_115 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_117: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_116.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_116 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_40: "f32[][]cuda:0" = out_117.sum()
        out_118: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_117 + sum_40;  out_117 = sum_40 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_119: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_118.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_118 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_120: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_119.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_119 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_41: "f32[][]cuda:0" = out_120.sum()
        out_121: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_120 + sum_41;  out_120 = sum_41 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_122: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_121.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_121 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_123: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_122.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_122 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_42: "f32[][]cuda:0" = out_123.sum()
        out_124: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_123 + sum_42;  out_123 = sum_42 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_125: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_124.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_124 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_126: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_125.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_125 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_43: "f32[][]cuda:0" = out_126.sum()
        out_127: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_126 + sum_43;  out_126 = sum_43 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_128: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_127.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_127 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_129: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_128.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_128 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_44: "f32[][]cuda:0" = out_129.sum()
        out_130: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_129 + sum_44;  out_129 = sum_44 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_131: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_130.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_130 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_132: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_131.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_131 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_45: "f32[][]cuda:0" = out_132.sum()
        out_133: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_132 + sum_45;  out_132 = sum_45 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_134: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_133.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_133 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_135: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_134.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_134 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_46: "f32[][]cuda:0" = out_135.sum()
        out_136: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_135 + sum_46;  out_135 = sum_46 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_137: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_136.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_136 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_138: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_137.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_137 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_47: "f32[][]cuda:0" = out_138.sum()
        out_139: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_138 + sum_47;  out_138 = sum_47 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_140: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_139.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_139 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_141: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_140.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_140 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_48: "f32[][]cuda:0" = out_141.sum()
        out_142: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_141 + sum_48;  out_141 = sum_48 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_143: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_142.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_142 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_144: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_143.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_143 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_49: "f32[][]cuda:0" = out_144.sum()
        out_145: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_144 + sum_49;  out_144 = sum_49 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_146: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_145.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_145 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_147: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_146.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_146 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_50: "f32[][]cuda:0" = out_147.sum()
        out_148: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_147 + sum_50;  out_147 = sum_50 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_149: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_148.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_148 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_150: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_149.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_149 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_51: "f32[][]cuda:0" = out_150.sum()
        out_151: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_150 + sum_51;  out_150 = sum_51 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_152: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_151.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_151 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_153: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_152.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_152 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_52: "f32[][]cuda:0" = out_153.sum()
        out_154: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_153 + sum_52;  out_153 = sum_52 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_155: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_154.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_154 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_156: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_155.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_155 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_53: "f32[][]cuda:0" = out_156.sum()
        out_157: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_156 + sum_53;  out_156 = sum_53 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_158: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_157.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_157 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_159: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_158.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_158 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_54: "f32[][]cuda:0" = out_159.sum()
        out_160: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_159 + sum_54;  out_159 = sum_54 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_161: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_160.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_160 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_162: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_161.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_161 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_55: "f32[][]cuda:0" = out_162.sum()
        out_163: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_162 + sum_55;  out_162 = sum_55 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_164: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_163.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_163 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_165: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_164.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_164 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_56: "f32[][]cuda:0" = out_165.sum()
        out_166: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_165 + sum_56;  out_165 = sum_56 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_167: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_166.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_166 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_168: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_167.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_167 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_57: "f32[][]cuda:0" = out_168.sum()
        out_169: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_168 + sum_57;  out_168 = sum_57 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_170: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_169.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_169 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_171: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_170.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_170 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_58: "f32[][]cuda:0" = out_171.sum()
        out_172: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_171 + sum_58;  out_171 = sum_58 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_173: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_172.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_172 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_174: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_173.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_173 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_59: "f32[][]cuda:0" = out_174.sum()
        out_175: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_174 + sum_59;  out_174 = sum_59 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_176: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_175.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_175 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_177: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_176.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_176 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_60: "f32[][]cuda:0" = out_177.sum()
        out_178: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_177 + sum_60;  out_177 = sum_60 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_179: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_178.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_178 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_180: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_179.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_179 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_61: "f32[][]cuda:0" = out_180.sum()
        out_181: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_180 + sum_61;  out_180 = sum_61 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_182: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_181.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_181 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_183: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_182.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_182 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_62: "f32[][]cuda:0" = out_183.sum()
        out_184: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_183 + sum_62;  out_183 = sum_62 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_185: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_184.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_184 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_186: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_185.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_185 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_63: "f32[][]cuda:0" = out_186.sum()
        out_187: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_186 + sum_63;  out_186 = sum_63 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_188: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_187.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_187 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_189: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_188.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_188 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_64: "f32[][]cuda:0" = out_189.sum()
        out_190: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_189 + sum_64;  out_189 = sum_64 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_191: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_190.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_190 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_192: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_191.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_191 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_65: "f32[][]cuda:0" = out_192.sum()
        out_193: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_192 + sum_65;  out_192 = sum_65 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_194: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_193.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_193 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_195: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_194.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_194 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_66: "f32[][]cuda:0" = out_195.sum()
        out_196: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_195 + sum_66;  out_195 = sum_66 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_197: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_196.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_196 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_198: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_197.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_197 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_67: "f32[][]cuda:0" = out_198.sum()
        out_199: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_198 + sum_67;  out_198 = sum_67 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_200: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_199.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_199 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_201: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_200.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_200 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_68: "f32[][]cuda:0" = out_201.sum()
        out_202: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_201 + sum_68;  out_201 = sum_68 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_203: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_202.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_202 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_204: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_203.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_203 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_69: "f32[][]cuda:0" = out_204.sum()
        out_205: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_204 + sum_69;  out_204 = sum_69 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_206: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_205.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_205 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_207: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_206.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_206 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_70: "f32[][]cuda:0" = out_207.sum()
        out_208: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_207 + sum_70;  out_207 = sum_70 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_209: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_208.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_208 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_210: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_209.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_209 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_71: "f32[][]cuda:0" = out_210.sum()
        out_211: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_210 + sum_71;  out_210 = sum_71 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_212: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_211.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_211 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_213: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_212.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_212 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_72: "f32[][]cuda:0" = out_213.sum()
        out_214: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_213 + sum_72;  out_213 = sum_72 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_215: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_214.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_214 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_216: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_215.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_215 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_73: "f32[][]cuda:0" = out_216.sum()
        out_217: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_216 + sum_73;  out_216 = sum_73 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_218: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_217.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_217 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_219: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_218.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_218 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_74: "f32[][]cuda:0" = out_219.sum()
        out_220: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_219 + sum_74;  out_219 = sum_74 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_221: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_220.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_220 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_222: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_221.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_221 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_75: "f32[][]cuda:0" = out_222.sum()
        out_223: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_222 + sum_75;  out_222 = sum_75 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_224: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_223.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_223 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_225: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_224.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_224 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_76: "f32[][]cuda:0" = out_225.sum()
        out_226: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_225 + sum_76;  out_225 = sum_76 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_227: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_226.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_226 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_228: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_227.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_227 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_77: "f32[][]cuda:0" = out_228.sum()
        out_229: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_228 + sum_77;  out_228 = sum_77 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_230: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_229.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_229 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_231: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_230.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_230 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_78: "f32[][]cuda:0" = out_231.sum()
        out_232: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_231 + sum_78;  out_231 = sum_78 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_233: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_232.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_232 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_234: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_233.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_233 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_79: "f32[][]cuda:0" = out_234.sum()
        out_235: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_234 + sum_79;  out_234 = sum_79 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_236: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_235.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_235 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_237: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_236.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_236 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_80: "f32[][]cuda:0" = out_237.sum()
        out_238: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_237 + sum_80;  out_237 = sum_80 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_239: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_238.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_238 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_240: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_239.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_239 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_81: "f32[][]cuda:0" = out_240.sum()
        out_241: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_240 + sum_81;  out_240 = sum_81 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_242: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_241.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_241 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_243: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_242.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_242 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_82: "f32[][]cuda:0" = out_243.sum()
        out_244: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_243 + sum_82;  out_243 = sum_82 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_245: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_244.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_244 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_246: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_245.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_245 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_83: "f32[][]cuda:0" = out_246.sum()
        out_247: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_246 + sum_83;  out_246 = sum_83 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_248: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_247.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_247 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_249: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_248.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_248 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_84: "f32[][]cuda:0" = out_249.sum()
        out_250: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_249 + sum_84;  out_249 = sum_84 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_251: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_250.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_250 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_252: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_251.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_251 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_85: "f32[][]cuda:0" = out_252.sum()
        out_253: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_252 + sum_85;  out_252 = sum_85 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_254: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_253.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_253 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_255: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_254.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_254 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_86: "f32[][]cuda:0" = out_255.sum()
        out_256: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_255 + sum_86;  out_255 = sum_86 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_257: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_256.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_256 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_258: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_257.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_257 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_87: "f32[][]cuda:0" = out_258.sum()
        out_259: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_258 + sum_87;  out_258 = sum_87 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_260: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_259.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_259 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_261: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_260.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_260 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_88: "f32[][]cuda:0" = out_261.sum()
        out_262: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_261 + sum_88;  out_261 = sum_88 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_263: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_262.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_262 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_264: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_263.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_263 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_89: "f32[][]cuda:0" = out_264.sum()
        out_265: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_264 + sum_89;  out_264 = sum_89 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_266: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_265.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_265 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_267: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_266.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_266 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_90: "f32[][]cuda:0" = out_267.sum()
        out_268: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_267 + sum_90;  out_267 = sum_90 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_269: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_268.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_268 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_270: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_269.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_269 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_91: "f32[][]cuda:0" = out_270.sum()
        out_271: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_270 + sum_91;  out_270 = sum_91 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_272: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_271.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_271 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_273: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_272.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_272 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_92: "f32[][]cuda:0" = out_273.sum()
        out_274: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_273 + sum_92;  out_273 = sum_92 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_275: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_274.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_274 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_276: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_275.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_275 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_93: "f32[][]cuda:0" = out_276.sum()
        out_277: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_276 + sum_93;  out_276 = sum_93 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_278: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_277.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_277 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_279: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_278.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_278 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_94: "f32[][]cuda:0" = out_279.sum()
        out_280: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_279 + sum_94;  out_279 = sum_94 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_281: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_280.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_280 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_282: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_281.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_281 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_95: "f32[][]cuda:0" = out_282.sum()
        out_283: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_282 + sum_95;  out_282 = sum_95 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_284: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_283.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_283 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_285: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_284.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_284 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_96: "f32[][]cuda:0" = out_285.sum()
        out_286: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_285 + sum_96;  out_285 = sum_96 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_287: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_286.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_286 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_288: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_287.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_287 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_97: "f32[][]cuda:0" = out_288.sum()
        out_289: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_288 + sum_97;  out_288 = sum_97 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_290: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_289.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_289 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_291: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_290.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_290 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_98: "f32[][]cuda:0" = out_291.sum()
        out_292: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_291 + sum_98;  out_291 = sum_98 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_293: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_292.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_292 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_294: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_293.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_293 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_99: "f32[][]cuda:0" = out_294.sum()
        out_295: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_294 + sum_99;  out_294 = sum_99 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_296: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_295.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_295 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:12 in _method1_3_inner, code: out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)
        out_297: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_296.reshape(19, 17, 13, 11, 7, 5, 3, 2);  out_296 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:13 in _method1_3_inner, code: out = out + out.sum()
        sum_100: "f32[][]cuda:0" = out_297.sum()
        out_298: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out_297 + sum_100;  out_297 = sum_100 = None

        # File: /opt/pytorch/numba-eval/method1.3/run.py:14 in _method1_3_inner, code: out = out.reshape(2, 3, 5, 7, 11, 13, 17, 19)
        out_299: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_298.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_298 = None
        return (out_299,)


