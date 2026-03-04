TRACED GRAPH
 ===== __compiled_fn_2_a6effe82_fe44_473b_9d9e_b4a45ebc78a0 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_tensor_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_tensor_ = L_tensor_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_tensor_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_tensor_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_6_3daefe7a_ecdb_474e_89eb_1137eab49eda =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_10_01476dd2_435e_456f_b345_1e14739093fc =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_14_335a604f_7841_4215_a19b_0259c4e40f6d =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_18_0ef9509f_1146_4792_8757_24d4fce71ebe =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_22_483527ea_c02b_4c94_aba7_006cb83c3104 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_26_9748d311_9010_4873_be3f_e2008bdcf0bb =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_30_b680d7e8_d095_4344_a605_17b19084e66f =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_34_d7155409_e0ce_46dc_8fb7_19610f429e41 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_38_f323f632_ad37_4eb8_99d7_b18e432b0b5b =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_42_b08472b9_d600_448e_a605_5add2ef6594d =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_46_e1b7aa0f_6fcf_49a4_96e0_ac9cc578908f =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_50_0909607b_da53_4e6f_a16b_0936782c09d2 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_54_e2cfe9c5_66e0_4f45_a4ad_e367e01d97ec =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_58_fafa410c_540f_407c_92bd_288cf68a4b75 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_62_bf774dd5_e489_44d1_8147_c4fe86832d4d =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_66_15d7a449_37ba_488f_9711_7a5f60240f72 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_70_d6fb0894_2143_404d_994d_8ab32577bd6b =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_74_3d32dd97_21b3_42ff_9547_8a92c0750da2 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_78_9540d3fe_8a0d_4f40_b50f_1debb91e85d4 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_82_82432a82_d063_40fd_b56a_4169fe656c23 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_86_24b84b8f_d04c_4926_b1f0_aa4d1ddfad31 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_90_b6993d58_de94_4f5f_b3e0_1782468c8a8f =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_94_cce6f135_0033_4120_b6c8_f95ad0af19e3 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_98_1c84d49d_3c1c_40b3_aa6e_b40c2711bc4f =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_102_d20f0cac_0e15_47d8_b61a_de11689c082c =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_106_0429a007_c233_4b09_b734_83b74a8f8507 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_110_a4d94517_35b1_4cd1_92dd_94bec3c65fb7 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_114_fb577b16_e8be_48f1_808f_24a03c41f66b =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_118_4753e82c_6c65_49fc_9e2c_c5f04a8c047a =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_122_2c03419f_cabb_411f_840c_6f85e18295ce =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_126_4cfa503e_5b10_4d42_8c16_f55e2e212fe2 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_130_8250a2e8_2b45_4dd2_9687_3b5197bec423 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_134_a757aca2_836d_45aa_a4b0_b226b9093afb =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_138_e2e62928_550d_48ab_b8fa_9dcf5098bb96 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_142_88c935a0_56ba_4437_bea5_b3947ac34aea =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_146_d626170e_d36f_4863_97da_f09209895fbc =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_150_8149bded_5a32_494c_8050_4e0976a424c7 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_154_14377bf3_1a2c_49e0_9da3_3546e82ae07f =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_158_a4e02890_2bc0_4eab_b250_06f8a54223ae =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_162_a8657aa3_9511_493d_97e4_26f54452c168 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_166_df52ba2d_1c32_4782_a4de_a66c185bd47e =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_170_81980c9a_8d50_49e8_9af9_bbb00a0b47cc =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_174_9c5cae72_e2d2_4acd_a96d_896f00cd5ebc =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_178_42fb2533_32d5_4116_82c8_0da41e94df5c =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_182_1b5d310f_08e8_4dc4_a294_d5b36225a4e9 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_186_f1964be5_bd20_45eb_ab68_1c48f24c541c =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_190_cdf87bc0_c264_4e46_8a39_4cb3e7833335 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_194_e4312565_73fd_4271_8450_74e3d83dad85 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_198_9bb8cd48_a685_4501_a422_202868010831 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_202_1a73a68a_ce0d_4dab_8ed1_7faea4001689 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_206_fbe1fa4d_70ec_4026_8063_7c568fea5f5f =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_210_238255e0_49bc_4daf_af21_5f611f680724 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_214_15bac0ff_1a63_40cb_817f_12fdf20ec8b4 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_218_5fabaa85_50fc_4ff3_b4a2_ad53bc61e5f6 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_222_0f61e200_0745_419b_868f_b638f80e5f79 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_226_018164e0_0174_4868_99ee_3edf4243700e =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_230_033f3c20_b9bb_4690_875e_05416b75c675 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_234_bf6221d5_1905_4a4f_8f31_9443cf23823e =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_238_1b67820f_e17a_42a3_b486_1e230bd41baa =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_242_2b7c346b_d921_450e_9e6e_0038f28eed53 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_246_dcee09ae_c712_48a0_a20d_38d609dffd40 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_250_50bbabe7_5800_4f55_9664_35a2880a671f =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_254_aa9c2402_e721_49c7_9c1a_95adb42650dc =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_258_986c54fd_961b_4b2a_b4fd_247d16039ee1 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_262_a5626f76_a324_49d6_ba65_5aa7ada99b0e =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_266_d8a71cee_93b9_4d41_aeab_a2ed1e9930c5 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_270_a0082bc6_050f_4859_87a9_dd9e3402ffa2 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_274_1cf1d6ee_e682_4d66_a90f_86a3e02de6eb =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_278_2fb8778a_903d_4441_a888_b73e99fb5b40 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_282_9e2e4b98_0123_4daa_9ac5_e6f27de1fcaa =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_286_9427265c_8653_4db1_b871_4190af0b12d1 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_290_abe65075_7d83_4022_8c33_a9c2ead16bcd =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_294_3bd79d98_eafb_4737_94b1_8dd90859130c =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_298_30c6eb19_c6d2_45a4_ab7c_adf291d000da =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_302_6c355e8e_c5fe_487c_aecd_642d3773dbff =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_306_f00c7cfd_7c09_4c83_8888_be3a70e9bb24 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_310_dcd771fd_a1dc_440c_b148_187bcf6d18d4 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_314_6e58b51e_1ece_46f2_81b1_eba127861d5b =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_318_fae24b52_a0fa_45a2_be18_3b50d57791c5 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_322_a5cda41b_67a8_406e_9b36_cebdbf7e57f1 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_326_bf9f6176_ffde_48c6_a245_a9b389193260 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_330_772fa2e8_1464_45a8_97f4_c10641de2b2e =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_334_07da75b6_30ee_4c96_a57f_4ff35c26db8f =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_338_a0ac5aff_6693_479e_ade3_125e3584ff60 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_342_83c5b10d_6af6_4d2d_b9fb_880f61b3f95c =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_346_4817d4ec_444d_4106_b9e9_5906a3ba3b1d =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_350_8a76b6a4_fe30_4961_9999_c74f7cb7dce6 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_354_2d3ce152_1412_47dd_a9a0_ecbb4bfeae1f =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_358_3689bc71_f065_49bd_ab7a_a48cc84f3cfc =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_362_20a3c874_b68f_4248_a624_34dfc5b000f8 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_366_10ed7329_6e23_4965_b88a_1ecf933a020a =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_370_e93627c0_9800_45f1_99b8_16ecfcee278d =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_374_12973fb0_66bb_4c56_9dc5_a129a78c3b0e =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_378_9e258241_2b35_4dff_add5_7a2d3924ee94 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_382_64af26b2_6181_4f27_849f_a1ca7056f124 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_386_81880a86_93d5_4d51_b3f7_a1d2e165c876 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_390_67a7f0f1_6ef8_4fec_a450_f2c9257f4f77 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_394_9fdfe296_773b_4126_b3c8_29fc818f6c71 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


TRACED GRAPH
 ===== __compiled_fn_398_758484fe_b239_467d_b043_e6970df6d4e8 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class GraphModule(torch.nn.Module):
    def forward(self, L_out_: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        l_out_ = L_out_

        # No stacktrace found for following nodes
        out: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = l_out_.reshape(19, 17, 13, 11, 7, 5, 3, 2);  l_out_ = None
        out_1: "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0" = out.add(0);  out = None
        out_2: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = out_1.reshape(2, 3, 5, 7, 11, 13, 17, 19);  out_1 = None
        return (out_2,)


