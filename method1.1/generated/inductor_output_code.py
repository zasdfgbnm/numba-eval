Output code: 
# AOT ID: ['0_inference']
from ctypes import c_void_p, c_long, c_int
import torch
import math
import random
import os
import tempfile
from math import inf, nan
from cmath import nanj
from torch._inductor.hooks import run_intermediate_hooks
from torch._inductor.utils import maybe_profile
from torch._inductor.codegen.memory_planning import _align as align
from torch import device, empty_strided
from torch._inductor.async_compile import AsyncCompile
from torch._inductor.select_algorithm import extern_kernels
import triton
import triton.language as tl
from torch._inductor.runtime.triton_heuristics import start_graph, end_graph
from torch._C import _cuda_getCurrentRawStream as get_raw_stream

aten = torch.ops.aten
inductor_ops = torch.ops.inductor
_quantized = torch.ops._quantized
assert_size_stride = torch._C._dynamo.guards.assert_size_stride
assert_alignment = torch._C._dynamo.guards.assert_alignment
empty_strided_cpu = torch._C._dynamo.guards._empty_strided_cpu
empty_strided_cpu_pinned = torch._C._dynamo.guards._empty_strided_cpu_pinned
empty_strided_cuda = torch._C._dynamo.guards._empty_strided_cuda
empty_strided_xpu = torch._C._dynamo.guards._empty_strided_xpu
empty_strided_mtia = torch._C._dynamo.guards._empty_strided_mtia
reinterpret_tensor = torch._C._dynamo.guards._reinterpret_tensor
alloc_from_pool = torch.ops.inductor._alloc_from_pool
async_compile = AsyncCompile()
empty_strided_p2p = torch._C._distributed_c10d._SymmetricMemory.empty_strided_p2p


# kernel path: /tmp/torchinductor_root/6f/c6frgu2jqvxew74qtcsjl243uatexqm74n63otp3wqihctbj2wak.py
# Topologically Sorted Source Nodes: [out, out_1, out_4, out_7, out_10, out_13, out_16, out_19, out_22, out_25, out_28, out_31, out_34, out_37, out_40, out_43, out_46, out_49, out_52, out_55, out_58, out_61, out_64, out_67, out_70, out_73, out_76, out_79, out_82, out_85, out_88, out_91, out_94, out_97, out_100, out_103, out_106, out_109, out_112, out_115, out_118, out_121, out_124, out_127, out_130, out_133, out_136, out_139, out_142, out_145, out_148, out_151, out_154, out_157, out_160, out_163, out_166, out_169, out_172, out_175, out_178, out_181, out_184, out_187, out_190, out_193, out_196, out_199, out_202, out_205, out_208, out_211, out_214, out_217, out_220, out_223, out_226, out_229, out_232, out_235, out_238, out_241, out_244, out_247, out_250, out_253, out_256, out_259, out_262, out_265, out_268, out_271, out_274, out_277, out_280, out_283, out_286, out_289, out_292, out_295, out_298], Original ATen: [aten.view, aten.add]
# Source node to ATen node mapping:
#   out => view
#   out_1 => add
#   out_10 => add_3
#   out_100 => add_33
#   out_103 => add_34
#   out_106 => add_35
#   out_109 => add_36
#   out_112 => add_37
#   out_115 => add_38
#   out_118 => add_39
#   out_121 => add_40
#   out_124 => add_41
#   out_127 => add_42
#   out_13 => add_4
#   out_130 => add_43
#   out_133 => add_44
#   out_136 => add_45
#   out_139 => add_46
#   out_142 => add_47
#   out_145 => add_48
#   out_148 => add_49
#   out_151 => add_50
#   out_154 => add_51
#   out_157 => add_52
#   out_16 => add_5
#   out_160 => add_53
#   out_163 => add_54
#   out_166 => add_55
#   out_169 => add_56
#   out_172 => add_57
#   out_175 => add_58
#   out_178 => add_59
#   out_181 => add_60
#   out_184 => add_61
#   out_187 => add_62
#   out_19 => add_6
#   out_190 => add_63
#   out_193 => add_64
#   out_196 => add_65
#   out_199 => add_66
#   out_202 => add_67
#   out_205 => add_68
#   out_208 => add_69
#   out_211 => add_70
#   out_214 => add_71
#   out_217 => add_72
#   out_22 => add_7
#   out_220 => add_73
#   out_223 => add_74
#   out_226 => add_75
#   out_229 => add_76
#   out_232 => add_77
#   out_235 => add_78
#   out_238 => add_79
#   out_241 => add_80
#   out_244 => add_81
#   out_247 => add_82
#   out_25 => add_8
#   out_250 => add_83
#   out_253 => add_84
#   out_256 => add_85
#   out_259 => add_86
#   out_262 => add_87
#   out_265 => add_88
#   out_268 => add_89
#   out_271 => add_90
#   out_274 => add_91
#   out_277 => add_92
#   out_28 => add_9
#   out_280 => add_93
#   out_283 => add_94
#   out_286 => add_95
#   out_289 => add_96
#   out_292 => add_97
#   out_295 => add_98
#   out_298 => add_99
#   out_31 => add_10
#   out_34 => add_11
#   out_37 => add_12
#   out_4 => add_1
#   out_40 => add_13
#   out_43 => add_14
#   out_46 => add_15
#   out_49 => add_16
#   out_52 => add_17
#   out_55 => add_18
#   out_58 => add_19
#   out_61 => add_20
#   out_64 => add_21
#   out_67 => add_22
#   out_7 => add_2
#   out_70 => add_23
#   out_73 => add_24
#   out_76 => add_25
#   out_79 => add_26
#   out_82 => add_27
#   out_85 => add_28
#   out_88 => add_29
#   out_91 => add_30
#   out_94 => add_31
#   out_97 => add_32
# Graph fragment:
#   %arg0_1 : Tensor "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = PlaceHolder[target=arg0_1]
#   %add_98 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=add_98]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %add : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%view, 0), kwargs = {})
#   %add_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add, 0), kwargs = {})
#   %add_2 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_1, 0), kwargs = {})
#   %add_3 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_2, 0), kwargs = {})
#   %add_4 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_3, 0), kwargs = {})
#   %add_5 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_4, 0), kwargs = {})
#   %add_6 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_5, 0), kwargs = {})
#   %add_7 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_6, 0), kwargs = {})
#   %add_8 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_7, 0), kwargs = {})
#   %add_9 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_8, 0), kwargs = {})
#   %add_10 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_9, 0), kwargs = {})
#   %add_11 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_10, 0), kwargs = {})
#   %add_12 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_11, 0), kwargs = {})
#   %add_13 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_12, 0), kwargs = {})
#   %add_14 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_13, 0), kwargs = {})
#   %add_15 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_14, 0), kwargs = {})
#   %add_16 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_15, 0), kwargs = {})
#   %add_17 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_16, 0), kwargs = {})
#   %add_18 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_17, 0), kwargs = {})
#   %add_19 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_18, 0), kwargs = {})
#   %add_20 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_19, 0), kwargs = {})
#   %add_21 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_20, 0), kwargs = {})
#   %add_22 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_21, 0), kwargs = {})
#   %add_23 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_22, 0), kwargs = {})
#   %add_24 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_23, 0), kwargs = {})
#   %add_25 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_24, 0), kwargs = {})
#   %add_26 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_25, 0), kwargs = {})
#   %add_27 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_26, 0), kwargs = {})
#   %add_28 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_27, 0), kwargs = {})
#   %add_29 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_28, 0), kwargs = {})
#   %add_30 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_29, 0), kwargs = {})
#   %add_31 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_30, 0), kwargs = {})
#   %add_32 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_31, 0), kwargs = {})
#   %add_33 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_32, 0), kwargs = {})
#   %add_34 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_33, 0), kwargs = {})
#   %add_35 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_34, 0), kwargs = {})
#   %add_36 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_35, 0), kwargs = {})
#   %add_37 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_36, 0), kwargs = {})
#   %add_38 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_37, 0), kwargs = {})
#   %add_39 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_38, 0), kwargs = {})
#   %add_40 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_39, 0), kwargs = {})
#   %add_41 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_40, 0), kwargs = {})
#   %add_42 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_41, 0), kwargs = {})
#   %add_43 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_42, 0), kwargs = {})
#   %add_44 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_43, 0), kwargs = {})
#   %add_45 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_44, 0), kwargs = {})
#   %add_46 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_45, 0), kwargs = {})
#   %add_47 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_46, 0), kwargs = {})
#   %add_48 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_47, 0), kwargs = {})
#   %add_49 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_48, 0), kwargs = {})
#   %add_50 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_49, 0), kwargs = {})
#   %add_51 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_50, 0), kwargs = {})
#   %add_52 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_51, 0), kwargs = {})
#   %add_53 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_52, 0), kwargs = {})
#   %add_54 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_53, 0), kwargs = {})
#   %add_55 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_54, 0), kwargs = {})
#   %add_56 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_55, 0), kwargs = {})
#   %add_57 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_56, 0), kwargs = {})
#   %add_58 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_57, 0), kwargs = {})
#   %add_59 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_58, 0), kwargs = {})
#   %add_60 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_59, 0), kwargs = {})
#   %add_61 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_60, 0), kwargs = {})
#   %add_62 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_61, 0), kwargs = {})
#   %add_63 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_62, 0), kwargs = {})
#   %add_64 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_63, 0), kwargs = {})
#   %add_65 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_64, 0), kwargs = {})
#   %add_66 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_65, 0), kwargs = {})
#   %add_67 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_66, 0), kwargs = {})
#   %add_68 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_67, 0), kwargs = {})
#   %add_69 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_68, 0), kwargs = {})
#   %add_70 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_69, 0), kwargs = {})
#   %add_71 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_70, 0), kwargs = {})
#   %add_72 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_71, 0), kwargs = {})
#   %add_73 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_72, 0), kwargs = {})
#   %add_74 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_73, 0), kwargs = {})
#   %add_75 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_74, 0), kwargs = {})
#   %add_76 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_75, 0), kwargs = {})
#   %add_77 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_76, 0), kwargs = {})
#   %add_78 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_77, 0), kwargs = {})
#   %add_79 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_78, 0), kwargs = {})
#   %add_80 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_79, 0), kwargs = {})
#   %add_81 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_80, 0), kwargs = {})
#   %add_82 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_81, 0), kwargs = {})
#   %add_83 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_82, 0), kwargs = {})
#   %add_84 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_83, 0), kwargs = {})
#   %add_85 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_84, 0), kwargs = {})
#   %add_86 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_85, 0), kwargs = {})
#   %add_87 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_86, 0), kwargs = {})
#   %add_88 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_87, 0), kwargs = {})
#   %add_89 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_88, 0), kwargs = {})
#   %add_90 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_89, 0), kwargs = {})
#   %add_91 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_90, 0), kwargs = {})
#   %add_92 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_91, 0), kwargs = {})
#   %add_93 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_92, 0), kwargs = {})
#   %add_94 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_93, 0), kwargs = {})
#   %add_95 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_94, 0), kwargs = {})
#   %add_96 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_95, 0), kwargs = {})
#   %add_97 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_96, 0), kwargs = {})
#   %add_98 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_97, 0), kwargs = {})
#   %add_99 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_98, 0), kwargs = {})
#   return %add_98,%add_99
triton_poi_fused_add_view_0 = async_compile.triton('triton_poi_fused_add_view_0', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.pointwise(
    size_hints={'x': 16777216}, 
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'out_ptr1': '*fp32', 'xnumel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_add_view_0', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'atomic_add_found': False, 'num_load': 1, 'num_store': 1, 'num_reduction': 0, 'backend_hash': '7FE6F64464F9571C4109CEEA43ED8B98A4C490C939CDEA41FCB8CED7CF50A2BF', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 116396280}},
    min_elem_per_thread=0
)
@triton.jit
def triton_poi_fused_add_view_0(in_ptr0, out_ptr1, xnumel, XBLOCK : tl.constexpr):
    xnumel = 9699690
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = xindex < xnumel
    x2 = xindex
    x0 = (xindex % 2310)
    x1 = xindex // 2310
    tmp0 = tl.load(in_ptr0 + (x2), xmask)
    tmp1 = tl.full([1], 0.0, tl.float32)
    tmp2 = tmp0 + tmp1
    tmp3 = tmp2 + tmp1
    tmp4 = tmp3 + tmp1
    tmp5 = tmp4 + tmp1
    tmp6 = tmp5 + tmp1
    tmp7 = tmp6 + tmp1
    tmp8 = tmp7 + tmp1
    tmp9 = tmp8 + tmp1
    tmp10 = tmp9 + tmp1
    tmp11 = tmp10 + tmp1
    tmp12 = tmp11 + tmp1
    tmp13 = tmp12 + tmp1
    tmp14 = tmp13 + tmp1
    tmp15 = tmp14 + tmp1
    tmp16 = tmp15 + tmp1
    tmp17 = tmp16 + tmp1
    tmp18 = tmp17 + tmp1
    tmp19 = tmp18 + tmp1
    tmp20 = tmp19 + tmp1
    tmp21 = tmp20 + tmp1
    tmp22 = tmp21 + tmp1
    tmp23 = tmp22 + tmp1
    tmp24 = tmp23 + tmp1
    tmp25 = tmp24 + tmp1
    tmp26 = tmp25 + tmp1
    tmp27 = tmp26 + tmp1
    tmp28 = tmp27 + tmp1
    tmp29 = tmp28 + tmp1
    tmp30 = tmp29 + tmp1
    tmp31 = tmp30 + tmp1
    tmp32 = tmp31 + tmp1
    tmp33 = tmp32 + tmp1
    tmp34 = tmp33 + tmp1
    tmp35 = tmp34 + tmp1
    tmp36 = tmp35 + tmp1
    tmp37 = tmp36 + tmp1
    tmp38 = tmp37 + tmp1
    tmp39 = tmp38 + tmp1
    tmp40 = tmp39 + tmp1
    tmp41 = tmp40 + tmp1
    tmp42 = tmp41 + tmp1
    tmp43 = tmp42 + tmp1
    tmp44 = tmp43 + tmp1
    tmp45 = tmp44 + tmp1
    tmp46 = tmp45 + tmp1
    tmp47 = tmp46 + tmp1
    tmp48 = tmp47 + tmp1
    tmp49 = tmp48 + tmp1
    tmp50 = tmp49 + tmp1
    tmp51 = tmp50 + tmp1
    tmp52 = tmp51 + tmp1
    tmp53 = tmp52 + tmp1
    tmp54 = tmp53 + tmp1
    tmp55 = tmp54 + tmp1
    tmp56 = tmp55 + tmp1
    tmp57 = tmp56 + tmp1
    tmp58 = tmp57 + tmp1
    tmp59 = tmp58 + tmp1
    tmp60 = tmp59 + tmp1
    tmp61 = tmp60 + tmp1
    tmp62 = tmp61 + tmp1
    tmp63 = tmp62 + tmp1
    tmp64 = tmp63 + tmp1
    tmp65 = tmp64 + tmp1
    tmp66 = tmp65 + tmp1
    tmp67 = tmp66 + tmp1
    tmp68 = tmp67 + tmp1
    tmp69 = tmp68 + tmp1
    tmp70 = tmp69 + tmp1
    tmp71 = tmp70 + tmp1
    tmp72 = tmp71 + tmp1
    tmp73 = tmp72 + tmp1
    tmp74 = tmp73 + tmp1
    tmp75 = tmp74 + tmp1
    tmp76 = tmp75 + tmp1
    tmp77 = tmp76 + tmp1
    tmp78 = tmp77 + tmp1
    tmp79 = tmp78 + tmp1
    tmp80 = tmp79 + tmp1
    tmp81 = tmp80 + tmp1
    tmp82 = tmp81 + tmp1
    tmp83 = tmp82 + tmp1
    tmp84 = tmp83 + tmp1
    tmp85 = tmp84 + tmp1
    tmp86 = tmp85 + tmp1
    tmp87 = tmp86 + tmp1
    tmp88 = tmp87 + tmp1
    tmp89 = tmp88 + tmp1
    tmp90 = tmp89 + tmp1
    tmp91 = tmp90 + tmp1
    tmp92 = tmp91 + tmp1
    tmp93 = tmp92 + tmp1
    tmp94 = tmp93 + tmp1
    tmp95 = tmp94 + tmp1
    tmp96 = tmp95 + tmp1
    tmp97 = tmp96 + tmp1
    tmp98 = tmp97 + tmp1
    tmp99 = tmp98 + tmp1
    tmp100 = tmp99 + tmp1
    tmp101 = tmp100 + tmp1
    tl.store(out_ptr1 + (x2), tmp101, xmask)
''', device_str='cuda')


async_compile.wait(globals())
del async_compile

class Runner:
    def __init__(self, partitions):
        self.partitions = partitions

    def recursively_apply_fns(self, fns):
        new_callables = []
        for fn, c in zip(fns, self.partitions):
            new_callables.append(fn(c))
        self.partitions = new_callables

    def call(self, args):
        arg0_1, = args
        args.clear()
        assert_size_stride(arg0_1, (2, 3, 5, 7, 11, 13, 17, 19), (4849845, 1616615, 323323, 46189, 4199, 323, 19, 1))
        with torch.cuda._DeviceGuard(0):
            torch.cuda.set_device(0)
            buf1 = empty_strided_cuda((19, 17, 13, 11, 7, 5, 3, 2), (510510, 30030, 2310, 210, 30, 6, 2, 1), torch.float32)
            # Topologically Sorted Source Nodes: [out, out_1, out_4, out_7, out_10, out_13, out_16, out_19, out_22, out_25, out_28, out_31, out_34, out_37, out_40, out_43, out_46, out_49, out_52, out_55, out_58, out_61, out_64, out_67, out_70, out_73, out_76, out_79, out_82, out_85, out_88, out_91, out_94, out_97, out_100, out_103, out_106, out_109, out_112, out_115, out_118, out_121, out_124, out_127, out_130, out_133, out_136, out_139, out_142, out_145, out_148, out_151, out_154, out_157, out_160, out_163, out_166, out_169, out_172, out_175, out_178, out_181, out_184, out_187, out_190, out_193, out_196, out_199, out_202, out_205, out_208, out_211, out_214, out_217, out_220, out_223, out_226, out_229, out_232, out_235, out_238, out_241, out_244, out_247, out_250, out_253, out_256, out_259, out_262, out_265, out_268, out_271, out_274, out_277, out_280, out_283, out_286, out_289, out_292, out_295, out_298], Original ATen: [aten.view, aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_view_0.run(arg0_1, buf1, 9699690, stream=stream0)
            del arg0_1
        return (reinterpret_tensor(buf1, (2, 3, 5, 7, 11, 13, 17, 19), (4849845, 1616615, 323323, 46189, 4199, 323, 19, 1), 0), )

runner = Runner(partitions=[])
call = runner.call
recursively_apply_fns = runner.recursively_apply_fns


def benchmark_compiled_module(times=10, repeat=10):
    from torch._dynamo.testing import rand_strided
    from torch._inductor.utils import print_performance
    arg0_1 = rand_strided((2, 3, 5, 7, 11, 13, 17, 19), (4849845, 1616615, 323323, 46189, 4199, 323, 19, 1), device='cuda:0', dtype=torch.float32)
    fn = lambda: call([arg0_1])
    return print_performance(fn, times=times, repeat=repeat)


if __name__ == "__main__":
    from torch._inductor.wrapper_benchmark import compiled_module_main
    compiled_module_main('None', benchmark_compiled_module)

Output code written to: /tmp/torchinductor_root/md/cmd45hzpjvcqfcrqyrv2cvqisubi4s6z4dvxlgnhvpvho7jiw72m.py
