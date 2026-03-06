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


# kernel path: /tmp/torchinductor_root/ei/ceihlbkqmkz5vnm25hageaylxyw3ffbdvd5z5ay5vairvlgxdx72.py
# Topologically Sorted Source Nodes: [out, sum_1], Original ATen: [aten.view, aten.sum]
# Source node to ATen node mapping:
#   out => view
#   sum_1 => sum_1
# Graph fragment:
#   %arg0_1 : Tensor "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = PlaceHolder[target=arg0_1]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %sum_1 : Tensor "f32[][]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.default](args = (%view,), kwargs = {})
#   return %buf0
triton_red_fused_sum_view_0 = async_compile.triton('triton_red_fused_sum_view_0', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.reduction(
    size_hints={'x': 2048, 'r0_': 8192},
    reduction_hint=ReductionHint.INNER,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'out_ptr0': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr', 'R0_BLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_red_fused_sum_view_0', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'atomic_add_found': False, 'num_load': 1, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '7FE6F64464F9571C4109CEEA43ED8B98A4C490C939CDEA41FCB8CED7CF50A2BF', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 9480, 'r0_': 38798760}}
)
@triton.jit
def triton_red_fused_sum_view_0(in_ptr0, out_ptr0, xnumel, r0_numel, XBLOCK : tl.constexpr, R0_BLOCK : tl.constexpr):
    xnumel = 1185
    r0_numel = 8186
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_base = tl.arange(0, R0_BLOCK)[None, :]
    rbase = r0_base
    x0 = xindex
    _tmp5 = tl.full([XBLOCK, R0_BLOCK], 0, tl.float32)
    for r0_offset in tl.range(0, r0_numel, R0_BLOCK):
        r0_index = r0_offset + r0_base
        r0_mask = r0_index < r0_numel
        roffset = r0_offset
        rindex = r0_index
        r0_1 = r0_index
        tmp0 = r0_1 + 8186*x0
        tmp1 = tl.full([1, 1], 9699690, tl.int32)
        tmp2 = tmp0 < tmp1
        tmp3 = tl.load(in_ptr0 + (2*((((r0_1 + 8186*x0) // 2) % 4849845)) + ((r0_1 % 2))), r0_mask & tmp2 & xmask, eviction_policy='evict_last', other=0.0)
        tmp4 = tl.broadcast_to(tmp3, [XBLOCK, R0_BLOCK])
        tmp6 = _tmp5 + tmp4
        _tmp5 = tl.where(r0_mask & xmask, tmp6, _tmp5)
    tmp5 = tl.sum(_tmp5, 1)[:, None]
    tl.store(out_ptr0 + (x0), tmp5, xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/pt/cptq4qx7rlcfx2w7stmdr5437ocsyyl7tsx5dn53ti7tmym4puo3.py
# Topologically Sorted Source Nodes: [out, sum_1], Original ATen: [aten.view, aten.sum]
# Source node to ATen node mapping:
#   out => view
#   sum_1 => sum_1
# Graph fragment:
#   %buf0 : Tensor "f32[1185][1]cuda:0" = PlaceHolder[target=buf0]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %sum_1 : Tensor "f32[][]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.default](args = (%view,), kwargs = {})
#   return %sum_1
triton_red_fused_sum_view_1 = async_compile.triton('triton_red_fused_sum_view_1', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.reduction(
    size_hints={'x': 1, 'r0_': 2048},
    reduction_hint=ReductionHint.INNER,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'out_ptr0': '*fp32', 'xnumel': 'constexpr', 'r0_numel': 'i32', 'XBLOCK': 'constexpr', 'R0_BLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {'xnumel': 1}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_red_fused_sum_view_1', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'atomic_add_found': False, 'num_load': 1, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '7FE6F64464F9571C4109CEEA43ED8B98A4C490C939CDEA41FCB8CED7CF50A2BF', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'r0_': 4740}}
)
@triton.jit
def triton_red_fused_sum_view_1(in_ptr0, out_ptr0, xnumel, r0_numel, XBLOCK : tl.constexpr, R0_BLOCK : tl.constexpr):
    xnumel = 1
    r0_numel = 1185
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = tl.full([XBLOCK], True, tl.int1)[:, None]
    r0_base = tl.arange(0, R0_BLOCK)[None, :]
    rbase = r0_base
    _tmp2 = tl.full([XBLOCK, R0_BLOCK], 0, tl.float32)
    for r0_offset in tl.range(0, r0_numel, R0_BLOCK):
        r0_index = r0_offset + r0_base
        r0_mask = r0_index < r0_numel
        roffset = r0_offset
        rindex = r0_index
        r0_0 = r0_index
        tmp0 = tl.load(in_ptr0 + (r0_0), r0_mask, eviction_policy='evict_first', other=0.0)
        tmp1 = tl.broadcast_to(tmp0, [XBLOCK, R0_BLOCK])
        tmp3 = _tmp2 + tmp1
        _tmp2 = tl.where(r0_mask, tmp3, _tmp2)
    tmp2 = tl.sum(_tmp2, 1)[:, None]
    tl.store(out_ptr0 + (tl.full([1, 1], 0, tl.int32).broadcast_to(XBLOCK, 1)), tmp2, None)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/tc/ctcxpx4v5nj64kk4tawrcvy2th2kmz4f66jhn2ipn24wi7r6wqhn.py
# Topologically Sorted Source Nodes: [out, out_1, sum_2], Original ATen: [aten.view, aten.add, aten.sum]
# Source node to ATen node mapping:
#   out => view
#   out_1 => add
#   sum_2 => sum_2
# Graph fragment:
#   %arg0_1 : Tensor "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = PlaceHolder[target=arg0_1]
#   %sum_1 : Tensor "f32[][]cuda:0" = PlaceHolder[target=sum_1]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %add : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.add.Tensor](args = (%view, %sum_1), kwargs = {})
#   %sum_2 : Tensor "f32[][]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.default](args = (%add,), kwargs = {})
#   return %buf3
triton_red_fused_add_sum_view_2 = async_compile.triton('triton_red_fused_add_sum_view_2', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.reduction(
    size_hints={'x': 2048, 'r0_': 8192},
    reduction_hint=ReductionHint.INNER,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'in_ptr1': '*fp32', 'out_ptr0': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr', 'R0_BLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_red_fused_add_sum_view_2', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'atomic_add_found': False, 'num_load': 2, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '7FE6F64464F9571C4109CEEA43ED8B98A4C490C939CDEA41FCB8CED7CF50A2BF', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 9480, 'r0_': 38798760}}
)
@triton.jit
def triton_red_fused_add_sum_view_2(in_ptr0, in_ptr1, out_ptr0, xnumel, r0_numel, XBLOCK : tl.constexpr, R0_BLOCK : tl.constexpr):
    xnumel = 1185
    r0_numel = 8186
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_base = tl.arange(0, R0_BLOCK)[None, :]
    rbase = r0_base
    x0 = xindex
    _tmp11 = tl.full([XBLOCK, R0_BLOCK], 0, tl.float32)
    for r0_offset in tl.range(0, r0_numel, R0_BLOCK):
        r0_index = r0_offset + r0_base
        r0_mask = r0_index < r0_numel
        roffset = r0_offset
        rindex = r0_index
        r0_1 = r0_index
        tmp0 = r0_1 + 8186*x0
        tmp1 = tl.full([1, 1], 9699690, tl.int32)
        tmp2 = tmp0 < tmp1
        tmp3 = tl.load(in_ptr0 + (2*((((r0_1 + 8186*x0) // 2) % 4849845)) + ((r0_1 % 2))), r0_mask & tmp2 & xmask, eviction_policy='evict_last', other=0.0)
        tmp4 = tl.load(in_ptr1 + (0))
        tmp5 = tl.broadcast_to(tmp4, [1, 1])
        tmp6 = tl.where(tmp2, tmp5, 0.0)
        tmp7 = tmp3 + tmp6
        tmp8 = tl.full(tmp7.shape, 0, tmp7.dtype)
        tmp9 = tl.where(tmp2, tmp7, tmp8)
        tmp10 = tl.broadcast_to(tmp9, [XBLOCK, R0_BLOCK])
        tmp12 = _tmp11 + tmp10
        _tmp11 = tl.where(r0_mask & xmask, tmp12, _tmp11)
    tmp11 = tl.sum(_tmp11, 1)[:, None]
    tl.store(out_ptr0 + (x0), tmp11, xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/3g/c3gibhhjnfrgfypzoekiv7cln5runmif3c3x5gdanoxvy7umcm6b.py
# Topologically Sorted Source Nodes: [out, out_1, out_4], Original ATen: [aten.view, aten.add]
# Source node to ATen node mapping:
#   out => view
#   out_1 => add
#   out_4 => add_1
# Graph fragment:
#   %arg0_1 : Tensor "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = PlaceHolder[target=arg0_1]
#   %sum_1 : Tensor "f32[][]cuda:0" = PlaceHolder[target=sum_1]
#   %add : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=add]
#   %sum_2 : Tensor "f32[][]cuda:0" = PlaceHolder[target=sum_2]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %add : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.add.Tensor](args = (%view, %sum_1), kwargs = {})
#   %add_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.add.Tensor](args = (%add, %sum_2), kwargs = {})
#   return %add,%add_1
triton_poi_fused_add_view_3 = async_compile.triton('triton_poi_fused_add_view_3', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.pointwise(
    size_hints={'x': 16777216}, 
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'in_ptr1': '*fp32', 'in_ptr2': '*fp32', 'out_ptr0': '*fp32', 'out_ptr1': '*fp32', 'xnumel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]], (4,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_add_view_3', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'atomic_add_found': False, 'num_load': 3, 'num_store': 2, 'num_reduction': 0, 'backend_hash': '7FE6F64464F9571C4109CEEA43ED8B98A4C490C939CDEA41FCB8CED7CF50A2BF', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 193993800}},
    min_elem_per_thread=0
)
@triton.jit
def triton_poi_fused_add_view_3(in_ptr0, in_ptr1, in_ptr2, out_ptr0, out_ptr1, xnumel, XBLOCK : tl.constexpr):
    xnumel = 9699690
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = xindex < xnumel
    x2 = xindex
    x0 = (xindex % 2310)
    x1 = xindex // 2310
    tmp0 = tl.load(in_ptr0 + (x2), xmask)
    tmp1 = tl.load(in_ptr1 + (0))
    tmp2 = tl.broadcast_to(tmp1, [XBLOCK])
    tmp4 = tl.load(in_ptr2 + (0))
    tmp5 = tl.broadcast_to(tmp4, [XBLOCK])
    tmp3 = tmp0 + tmp2
    tmp6 = tmp3 + tmp5
    tl.store(out_ptr0 + (x0 + 2336*x1), tmp3, xmask)
    tl.store(out_ptr1 + (x0 + 2336*x1), tmp6, xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/er/cerqjajvujqagxyd5224rr776nm2h7wyf2llovyy23y3a5knpbfd.py
# Topologically Sorted Source Nodes: [out_4, sum_3], Original ATen: [aten.add, aten.sum]
# Source node to ATen node mapping:
#   out_4 => add_1
#   sum_3 => sum_3
# Graph fragment:
#   %add : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=add]
#   %sum_2 : Tensor "f32[][]cuda:0" = PlaceHolder[target=sum_2]
#   %add_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.add.Tensor](args = (%add, %sum_2), kwargs = {})
#   %sum_3 : Tensor "f32[][]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.default](args = (%add_1,), kwargs = {})
#   return %buf6
triton_red_fused_add_sum_4 = async_compile.triton('triton_red_fused_add_sum_4', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.reduction(
    size_hints={'x': 2048, 'r0_': 8192},
    reduction_hint=ReductionHint.INNER,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'in_ptr1': '*fp32', 'out_ptr0': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr', 'R0_BLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_red_fused_add_sum_4', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': False, 'atomic_add_found': False, 'num_load': 2, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '7FE6F64464F9571C4109CEEA43ED8B98A4C490C939CDEA41FCB8CED7CF50A2BF', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 9480, 'r0_': 38798760}}
)
@triton.jit
def triton_red_fused_add_sum_4(in_ptr0, in_ptr1, out_ptr0, xnumel, r0_numel, XBLOCK : tl.constexpr, R0_BLOCK : tl.constexpr):
    xnumel = 1185
    r0_numel = 8186
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_base = tl.arange(0, R0_BLOCK)[None, :]
    rbase = r0_base
    x0 = xindex
    _tmp11 = tl.full([XBLOCK, R0_BLOCK], 0, tl.float32)
    for r0_offset in tl.range(0, r0_numel, R0_BLOCK):
        r0_index = r0_offset + r0_base
        r0_mask = r0_index < r0_numel
        roffset = r0_offset
        rindex = r0_index
        r0_1 = r0_index
        tmp0 = r0_1 + 8186*x0
        tmp1 = tl.full([1, 1], 9699690, tl.int32)
        tmp2 = tmp0 < tmp1
        tmp3 = tl.load(in_ptr0 + (2*((((r0_1 + 8186*x0) // 2) % 1155)) + 2336*((((r0_1 + 8186*x0) // 2310) % 4199)) + ((r0_1 % 2))), r0_mask & tmp2 & xmask, eviction_policy='evict_last', other=0.0)
        tmp4 = tl.load(in_ptr1 + (0))
        tmp5 = tl.broadcast_to(tmp4, [1, 1])
        tmp6 = tl.where(tmp2, tmp5, 0.0)
        tmp7 = tmp3 + tmp6
        tmp8 = tl.full(tmp7.shape, 0, tmp7.dtype)
        tmp9 = tl.where(tmp2, tmp7, tmp8)
        tmp10 = tl.broadcast_to(tmp9, [XBLOCK, R0_BLOCK])
        tmp12 = _tmp11 + tmp10
        _tmp11 = tl.where(r0_mask & xmask, tmp12, _tmp11)
    tmp11 = tl.sum(_tmp11, 1)[:, None]
    tl.store(out_ptr0 + (x0), tmp11, xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/tl/ctl667gjh5v4zbdcnrkj7ikzaeigm5jywzjkbtlaqnvrtpo3lfyr.py
# Topologically Sorted Source Nodes: [out_7, out_10], Original ATen: [aten.add]
# Source node to ATen node mapping:
#   out_10 => add_3
#   out_7 => add_2
# Graph fragment:
#   %add_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=add_1]
#   %sum_3 : Tensor "f32[][]cuda:0" = PlaceHolder[target=sum_3]
#   %add_2 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=add_2]
#   %sum_4 : Tensor "f32[][]cuda:0" = PlaceHolder[target=sum_4]
#   %add_2 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_1, %sum_3), kwargs = {})
#   %add_3 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_2, %sum_4), kwargs = {})
#   return %add_2,%add_3
triton_poi_fused_add_5 = async_compile.triton('triton_poi_fused_add_5', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.pointwise(
    size_hints={'x': 16777216}, 
    filename=__file__,
    triton_meta={'signature': {'in_out_ptr0': '*fp32', 'in_ptr0': '*fp32', 'in_ptr1': '*fp32', 'out_ptr0': '*fp32', 'xnumel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_add_5', 'mutated_arg_names': ['in_out_ptr0'], 'optimize_mem': True, 'no_x_dim': False, 'atomic_add_found': False, 'num_load': 3, 'num_store': 2, 'num_reduction': 0, 'backend_hash': '7FE6F64464F9571C4109CEEA43ED8B98A4C490C939CDEA41FCB8CED7CF50A2BF', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 193993800}},
    min_elem_per_thread=0
)
@triton.jit
def triton_poi_fused_add_5(in_out_ptr0, in_ptr0, in_ptr1, out_ptr0, xnumel, XBLOCK : tl.constexpr):
    xnumel = 9699690
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = xindex < xnumel
    x0 = (xindex % 2310)
    x1 = xindex // 2310
    tmp0 = tl.load(in_out_ptr0 + (x0 + 2336*x1), xmask)
    tmp1 = tl.load(in_ptr0 + (0))
    tmp2 = tl.broadcast_to(tmp1, [XBLOCK])
    tmp4 = tl.load(in_ptr1 + (0))
    tmp5 = tl.broadcast_to(tmp4, [XBLOCK])
    tmp3 = tmp0 + tmp2
    tmp6 = tmp3 + tmp5
    tl.store(in_out_ptr0 + (x0 + 2336*x1), tmp3, xmask)
    tl.store(out_ptr0 + (x0 + 2336*x1), tmp6, xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/te/cte4aut36tkni7xjph2jawpkamkdkkgfcwkjatcvuk5hrvq62veu.py
# Topologically Sorted Source Nodes: [out_295, out_298], Original ATen: [aten.add]
# Source node to ATen node mapping:
#   out_295 => add_98
#   out_298 => add_99
# Graph fragment:
#   %add_97 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=add_97]
#   %sum_99 : Tensor "f32[][]cuda:0" = PlaceHolder[target=sum_99]
#   %add_98 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=add_98]
#   %sum_100 : Tensor "f32[][]cuda:0" = PlaceHolder[target=sum_100]
#   %add_98 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_97, %sum_99), kwargs = {})
#   %add_99 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.add.Tensor](args = (%add_98, %sum_100), kwargs = {})
#   return %add_98,%add_99
triton_poi_fused_add_6 = async_compile.triton('triton_poi_fused_add_6', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.pointwise(
    size_hints={'x': 16777216}, 
    filename=__file__,
    triton_meta={'signature': {'in_out_ptr0': '*fp32', 'in_ptr0': '*fp32', 'in_ptr1': '*fp32', 'out_ptr0': '*fp32', 'xnumel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_poi_fused_add_6', 'mutated_arg_names': ['in_out_ptr0'], 'optimize_mem': True, 'no_x_dim': False, 'atomic_add_found': False, 'num_load': 3, 'num_store': 1, 'num_reduction': 0, 'backend_hash': '7FE6F64464F9571C4109CEEA43ED8B98A4C490C939CDEA41FCB8CED7CF50A2BF', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 116396280}},
    min_elem_per_thread=0
)
@triton.jit
def triton_poi_fused_add_6(in_out_ptr0, in_ptr0, in_ptr1, out_ptr0, xnumel, XBLOCK : tl.constexpr):
    xnumel = 9699690
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:]
    xmask = xindex < xnumel
    x0 = (xindex % 2310)
    x1 = xindex // 2310
    x2 = xindex
    tmp0 = tl.load(in_out_ptr0 + (x0 + 2336*x1), xmask)
    tmp1 = tl.load(in_ptr0 + (0))
    tmp2 = tl.broadcast_to(tmp1, [XBLOCK])
    tmp4 = tl.load(in_ptr1 + (0))
    tmp5 = tl.broadcast_to(tmp4, [XBLOCK])
    tmp3 = tmp0 + tmp2
    tmp6 = tmp3 + tmp5
    tl.store(out_ptr0 + (x2), tmp6, xmask)
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
            buf0 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out, sum_1], Original ATen: [aten.view, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_0.run(arg0_1, buf0, 1185, 8186, stream=stream0)
            buf1 = empty_strided_cuda((), (), torch.float32)
            # Topologically Sorted Source Nodes: [out, sum_1], Original ATen: [aten.view, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf0, buf1, 1, 1185, stream=stream0)
            buf3 = buf0; del buf0  # reuse
            # Topologically Sorted Source Nodes: [out, out_1, sum_2], Original ATen: [aten.view, aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_view_2.run(arg0_1, buf1, buf3, 1185, 8186, stream=stream0)
            buf4 = empty_strided_cuda((), (), torch.float32)
            # Topologically Sorted Source Nodes: [out, out_1, sum_2], Original ATen: [aten.view, aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf3, buf4, 1, 1185, stream=stream0)
            buf2 = empty_strided_cuda((19, 17, 13, 11, 7, 5, 3, 2), (516256, 30368, 2336, 210, 30, 6, 2, 1), torch.float32)
            buf5 = empty_strided_cuda((19, 17, 13, 11, 7, 5, 3, 2), (516256, 30368, 2336, 210, 30, 6, 2, 1), torch.float32)
            # Topologically Sorted Source Nodes: [out, out_1, out_4], Original ATen: [aten.view, aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_view_3.run(arg0_1, buf1, buf4, buf2, buf5, 9699690, stream=stream0)
            del arg0_1
            buf6 = buf3; del buf3  # reuse
            # Topologically Sorted Source Nodes: [out_4, sum_3], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf2, buf4, buf6, 1185, 8186, stream=stream0)
            buf7 = buf4; del buf4  # reuse
            # Topologically Sorted Source Nodes: [out_4, sum_3], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf6, buf7, 1, 1185, stream=stream0)
            buf9 = buf6; del buf6  # reuse
            # Topologically Sorted Source Nodes: [out_7, sum_4], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf5, buf7, buf9, 1185, 8186, stream=stream0)
            buf10 = buf1; del buf1  # reuse
            # Topologically Sorted Source Nodes: [out_7, sum_4], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf9, buf10, 1, 1185, stream=stream0)
            del buf9
            buf8 = buf5; del buf5  # reuse
            buf11 = buf2; del buf2  # reuse
            # Topologically Sorted Source Nodes: [out_7, out_10], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf8, buf7, buf10, buf11, 9699690, stream=stream0)
            buf12 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_10, sum_5], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf8, buf10, buf12, 1185, 8186, stream=stream0)
            buf13 = buf10; del buf10  # reuse
            # Topologically Sorted Source Nodes: [out_10, sum_5], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf12, buf13, 1, 1185, stream=stream0)
            buf15 = buf12; del buf12  # reuse
            # Topologically Sorted Source Nodes: [out_13, sum_6], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf11, buf13, buf15, 1185, 8186, stream=stream0)
            buf16 = buf7; del buf7  # reuse
            # Topologically Sorted Source Nodes: [out_13, sum_6], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf15, buf16, 1, 1185, stream=stream0)
            del buf15
            buf14 = buf11; del buf11  # reuse
            buf17 = buf8; del buf8  # reuse
            # Topologically Sorted Source Nodes: [out_13, out_16], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf14, buf13, buf16, buf17, 9699690, stream=stream0)
            buf18 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_16, sum_7], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf14, buf16, buf18, 1185, 8186, stream=stream0)
            buf19 = buf16; del buf16  # reuse
            # Topologically Sorted Source Nodes: [out_16, sum_7], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf18, buf19, 1, 1185, stream=stream0)
            buf21 = buf18; del buf18  # reuse
            # Topologically Sorted Source Nodes: [out_19, sum_8], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf17, buf19, buf21, 1185, 8186, stream=stream0)
            buf22 = buf13; del buf13  # reuse
            # Topologically Sorted Source Nodes: [out_19, sum_8], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf21, buf22, 1, 1185, stream=stream0)
            del buf21
            buf20 = buf17; del buf17  # reuse
            buf23 = buf14; del buf14  # reuse
            # Topologically Sorted Source Nodes: [out_19, out_22], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf20, buf19, buf22, buf23, 9699690, stream=stream0)
            buf24 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_22, sum_9], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf20, buf22, buf24, 1185, 8186, stream=stream0)
            buf25 = buf22; del buf22  # reuse
            # Topologically Sorted Source Nodes: [out_22, sum_9], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf24, buf25, 1, 1185, stream=stream0)
            buf27 = buf24; del buf24  # reuse
            # Topologically Sorted Source Nodes: [out_25, sum_10], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf23, buf25, buf27, 1185, 8186, stream=stream0)
            buf28 = buf19; del buf19  # reuse
            # Topologically Sorted Source Nodes: [out_25, sum_10], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf27, buf28, 1, 1185, stream=stream0)
            del buf27
            buf26 = buf23; del buf23  # reuse
            buf29 = buf20; del buf20  # reuse
            # Topologically Sorted Source Nodes: [out_25, out_28], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf26, buf25, buf28, buf29, 9699690, stream=stream0)
            buf30 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_28, sum_11], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf26, buf28, buf30, 1185, 8186, stream=stream0)
            buf31 = buf28; del buf28  # reuse
            # Topologically Sorted Source Nodes: [out_28, sum_11], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf30, buf31, 1, 1185, stream=stream0)
            buf33 = buf30; del buf30  # reuse
            # Topologically Sorted Source Nodes: [out_31, sum_12], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf29, buf31, buf33, 1185, 8186, stream=stream0)
            buf34 = buf25; del buf25  # reuse
            # Topologically Sorted Source Nodes: [out_31, sum_12], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf33, buf34, 1, 1185, stream=stream0)
            del buf33
            buf32 = buf29; del buf29  # reuse
            buf35 = buf26; del buf26  # reuse
            # Topologically Sorted Source Nodes: [out_31, out_34], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf32, buf31, buf34, buf35, 9699690, stream=stream0)
            buf36 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_34, sum_13], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf32, buf34, buf36, 1185, 8186, stream=stream0)
            buf37 = buf34; del buf34  # reuse
            # Topologically Sorted Source Nodes: [out_34, sum_13], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf36, buf37, 1, 1185, stream=stream0)
            buf39 = buf36; del buf36  # reuse
            # Topologically Sorted Source Nodes: [out_37, sum_14], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf35, buf37, buf39, 1185, 8186, stream=stream0)
            buf40 = buf31; del buf31  # reuse
            # Topologically Sorted Source Nodes: [out_37, sum_14], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf39, buf40, 1, 1185, stream=stream0)
            del buf39
            buf38 = buf35; del buf35  # reuse
            buf41 = buf32; del buf32  # reuse
            # Topologically Sorted Source Nodes: [out_37, out_40], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf38, buf37, buf40, buf41, 9699690, stream=stream0)
            buf42 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_40, sum_15], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf38, buf40, buf42, 1185, 8186, stream=stream0)
            buf43 = buf40; del buf40  # reuse
            # Topologically Sorted Source Nodes: [out_40, sum_15], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf42, buf43, 1, 1185, stream=stream0)
            buf45 = buf42; del buf42  # reuse
            # Topologically Sorted Source Nodes: [out_43, sum_16], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf41, buf43, buf45, 1185, 8186, stream=stream0)
            buf46 = buf37; del buf37  # reuse
            # Topologically Sorted Source Nodes: [out_43, sum_16], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf45, buf46, 1, 1185, stream=stream0)
            del buf45
            buf44 = buf41; del buf41  # reuse
            buf47 = buf38; del buf38  # reuse
            # Topologically Sorted Source Nodes: [out_43, out_46], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf44, buf43, buf46, buf47, 9699690, stream=stream0)
            buf48 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_46, sum_17], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf44, buf46, buf48, 1185, 8186, stream=stream0)
            buf49 = buf46; del buf46  # reuse
            # Topologically Sorted Source Nodes: [out_46, sum_17], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf48, buf49, 1, 1185, stream=stream0)
            buf51 = buf48; del buf48  # reuse
            # Topologically Sorted Source Nodes: [out_49, sum_18], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf47, buf49, buf51, 1185, 8186, stream=stream0)
            buf52 = buf43; del buf43  # reuse
            # Topologically Sorted Source Nodes: [out_49, sum_18], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf51, buf52, 1, 1185, stream=stream0)
            del buf51
            buf50 = buf47; del buf47  # reuse
            buf53 = buf44; del buf44  # reuse
            # Topologically Sorted Source Nodes: [out_49, out_52], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf50, buf49, buf52, buf53, 9699690, stream=stream0)
            buf54 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_52, sum_19], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf50, buf52, buf54, 1185, 8186, stream=stream0)
            buf55 = buf52; del buf52  # reuse
            # Topologically Sorted Source Nodes: [out_52, sum_19], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf54, buf55, 1, 1185, stream=stream0)
            buf57 = buf54; del buf54  # reuse
            # Topologically Sorted Source Nodes: [out_55, sum_20], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf53, buf55, buf57, 1185, 8186, stream=stream0)
            buf58 = buf49; del buf49  # reuse
            # Topologically Sorted Source Nodes: [out_55, sum_20], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf57, buf58, 1, 1185, stream=stream0)
            del buf57
            buf56 = buf53; del buf53  # reuse
            buf59 = buf50; del buf50  # reuse
            # Topologically Sorted Source Nodes: [out_55, out_58], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf56, buf55, buf58, buf59, 9699690, stream=stream0)
            buf60 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_58, sum_21], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf56, buf58, buf60, 1185, 8186, stream=stream0)
            buf61 = buf58; del buf58  # reuse
            # Topologically Sorted Source Nodes: [out_58, sum_21], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf60, buf61, 1, 1185, stream=stream0)
            buf63 = buf60; del buf60  # reuse
            # Topologically Sorted Source Nodes: [out_61, sum_22], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf59, buf61, buf63, 1185, 8186, stream=stream0)
            buf64 = buf55; del buf55  # reuse
            # Topologically Sorted Source Nodes: [out_61, sum_22], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf63, buf64, 1, 1185, stream=stream0)
            del buf63
            buf62 = buf59; del buf59  # reuse
            buf65 = buf56; del buf56  # reuse
            # Topologically Sorted Source Nodes: [out_61, out_64], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf62, buf61, buf64, buf65, 9699690, stream=stream0)
            buf66 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_64, sum_23], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf62, buf64, buf66, 1185, 8186, stream=stream0)
            buf67 = buf64; del buf64  # reuse
            # Topologically Sorted Source Nodes: [out_64, sum_23], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf66, buf67, 1, 1185, stream=stream0)
            buf69 = buf66; del buf66  # reuse
            # Topologically Sorted Source Nodes: [out_67, sum_24], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf65, buf67, buf69, 1185, 8186, stream=stream0)
            buf70 = buf61; del buf61  # reuse
            # Topologically Sorted Source Nodes: [out_67, sum_24], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf69, buf70, 1, 1185, stream=stream0)
            del buf69
            buf68 = buf65; del buf65  # reuse
            buf71 = buf62; del buf62  # reuse
            # Topologically Sorted Source Nodes: [out_67, out_70], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf68, buf67, buf70, buf71, 9699690, stream=stream0)
            buf72 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_70, sum_25], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf68, buf70, buf72, 1185, 8186, stream=stream0)
            buf73 = buf70; del buf70  # reuse
            # Topologically Sorted Source Nodes: [out_70, sum_25], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf72, buf73, 1, 1185, stream=stream0)
            buf75 = buf72; del buf72  # reuse
            # Topologically Sorted Source Nodes: [out_73, sum_26], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf71, buf73, buf75, 1185, 8186, stream=stream0)
            buf76 = buf67; del buf67  # reuse
            # Topologically Sorted Source Nodes: [out_73, sum_26], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf75, buf76, 1, 1185, stream=stream0)
            del buf75
            buf74 = buf71; del buf71  # reuse
            buf77 = buf68; del buf68  # reuse
            # Topologically Sorted Source Nodes: [out_73, out_76], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf74, buf73, buf76, buf77, 9699690, stream=stream0)
            buf78 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_76, sum_27], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf74, buf76, buf78, 1185, 8186, stream=stream0)
            buf79 = buf76; del buf76  # reuse
            # Topologically Sorted Source Nodes: [out_76, sum_27], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf78, buf79, 1, 1185, stream=stream0)
            buf81 = buf78; del buf78  # reuse
            # Topologically Sorted Source Nodes: [out_79, sum_28], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf77, buf79, buf81, 1185, 8186, stream=stream0)
            buf82 = buf73; del buf73  # reuse
            # Topologically Sorted Source Nodes: [out_79, sum_28], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf81, buf82, 1, 1185, stream=stream0)
            del buf81
            buf80 = buf77; del buf77  # reuse
            buf83 = buf74; del buf74  # reuse
            # Topologically Sorted Source Nodes: [out_79, out_82], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf80, buf79, buf82, buf83, 9699690, stream=stream0)
            buf84 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_82, sum_29], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf80, buf82, buf84, 1185, 8186, stream=stream0)
            buf85 = buf82; del buf82  # reuse
            # Topologically Sorted Source Nodes: [out_82, sum_29], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf84, buf85, 1, 1185, stream=stream0)
            buf87 = buf84; del buf84  # reuse
            # Topologically Sorted Source Nodes: [out_85, sum_30], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf83, buf85, buf87, 1185, 8186, stream=stream0)
            buf88 = buf79; del buf79  # reuse
            # Topologically Sorted Source Nodes: [out_85, sum_30], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf87, buf88, 1, 1185, stream=stream0)
            del buf87
            buf86 = buf83; del buf83  # reuse
            buf89 = buf80; del buf80  # reuse
            # Topologically Sorted Source Nodes: [out_85, out_88], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf86, buf85, buf88, buf89, 9699690, stream=stream0)
            buf90 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_88, sum_31], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf86, buf88, buf90, 1185, 8186, stream=stream0)
            buf91 = buf88; del buf88  # reuse
            # Topologically Sorted Source Nodes: [out_88, sum_31], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf90, buf91, 1, 1185, stream=stream0)
            buf93 = buf90; del buf90  # reuse
            # Topologically Sorted Source Nodes: [out_91, sum_32], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf89, buf91, buf93, 1185, 8186, stream=stream0)
            buf94 = buf85; del buf85  # reuse
            # Topologically Sorted Source Nodes: [out_91, sum_32], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf93, buf94, 1, 1185, stream=stream0)
            del buf93
            buf92 = buf89; del buf89  # reuse
            buf95 = buf86; del buf86  # reuse
            # Topologically Sorted Source Nodes: [out_91, out_94], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf92, buf91, buf94, buf95, 9699690, stream=stream0)
            buf96 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_94, sum_33], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf92, buf94, buf96, 1185, 8186, stream=stream0)
            buf97 = buf94; del buf94  # reuse
            # Topologically Sorted Source Nodes: [out_94, sum_33], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf96, buf97, 1, 1185, stream=stream0)
            buf99 = buf96; del buf96  # reuse
            # Topologically Sorted Source Nodes: [out_97, sum_34], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf95, buf97, buf99, 1185, 8186, stream=stream0)
            buf100 = buf91; del buf91  # reuse
            # Topologically Sorted Source Nodes: [out_97, sum_34], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf99, buf100, 1, 1185, stream=stream0)
            del buf99
            buf98 = buf95; del buf95  # reuse
            buf101 = buf92; del buf92  # reuse
            # Topologically Sorted Source Nodes: [out_97, out_100], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf98, buf97, buf100, buf101, 9699690, stream=stream0)
            buf102 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_100, sum_35], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf98, buf100, buf102, 1185, 8186, stream=stream0)
            buf103 = buf100; del buf100  # reuse
            # Topologically Sorted Source Nodes: [out_100, sum_35], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf102, buf103, 1, 1185, stream=stream0)
            buf105 = buf102; del buf102  # reuse
            # Topologically Sorted Source Nodes: [out_103, sum_36], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf101, buf103, buf105, 1185, 8186, stream=stream0)
            buf106 = buf97; del buf97  # reuse
            # Topologically Sorted Source Nodes: [out_103, sum_36], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf105, buf106, 1, 1185, stream=stream0)
            del buf105
            buf104 = buf101; del buf101  # reuse
            buf107 = buf98; del buf98  # reuse
            # Topologically Sorted Source Nodes: [out_103, out_106], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf104, buf103, buf106, buf107, 9699690, stream=stream0)
            buf108 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_106, sum_37], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf104, buf106, buf108, 1185, 8186, stream=stream0)
            buf109 = buf106; del buf106  # reuse
            # Topologically Sorted Source Nodes: [out_106, sum_37], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf108, buf109, 1, 1185, stream=stream0)
            buf111 = buf108; del buf108  # reuse
            # Topologically Sorted Source Nodes: [out_109, sum_38], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf107, buf109, buf111, 1185, 8186, stream=stream0)
            buf112 = buf103; del buf103  # reuse
            # Topologically Sorted Source Nodes: [out_109, sum_38], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf111, buf112, 1, 1185, stream=stream0)
            del buf111
            buf110 = buf107; del buf107  # reuse
            buf113 = buf104; del buf104  # reuse
            # Topologically Sorted Source Nodes: [out_109, out_112], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf110, buf109, buf112, buf113, 9699690, stream=stream0)
            buf114 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_112, sum_39], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf110, buf112, buf114, 1185, 8186, stream=stream0)
            buf115 = buf112; del buf112  # reuse
            # Topologically Sorted Source Nodes: [out_112, sum_39], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf114, buf115, 1, 1185, stream=stream0)
            buf117 = buf114; del buf114  # reuse
            # Topologically Sorted Source Nodes: [out_115, sum_40], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf113, buf115, buf117, 1185, 8186, stream=stream0)
            buf118 = buf109; del buf109  # reuse
            # Topologically Sorted Source Nodes: [out_115, sum_40], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf117, buf118, 1, 1185, stream=stream0)
            del buf117
            buf116 = buf113; del buf113  # reuse
            buf119 = buf110; del buf110  # reuse
            # Topologically Sorted Source Nodes: [out_115, out_118], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf116, buf115, buf118, buf119, 9699690, stream=stream0)
            buf120 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_118, sum_41], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf116, buf118, buf120, 1185, 8186, stream=stream0)
            buf121 = buf118; del buf118  # reuse
            # Topologically Sorted Source Nodes: [out_118, sum_41], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf120, buf121, 1, 1185, stream=stream0)
            buf123 = buf120; del buf120  # reuse
            # Topologically Sorted Source Nodes: [out_121, sum_42], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf119, buf121, buf123, 1185, 8186, stream=stream0)
            buf124 = buf115; del buf115  # reuse
            # Topologically Sorted Source Nodes: [out_121, sum_42], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf123, buf124, 1, 1185, stream=stream0)
            del buf123
            buf122 = buf119; del buf119  # reuse
            buf125 = buf116; del buf116  # reuse
            # Topologically Sorted Source Nodes: [out_121, out_124], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf122, buf121, buf124, buf125, 9699690, stream=stream0)
            buf126 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_124, sum_43], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf122, buf124, buf126, 1185, 8186, stream=stream0)
            buf127 = buf124; del buf124  # reuse
            # Topologically Sorted Source Nodes: [out_124, sum_43], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf126, buf127, 1, 1185, stream=stream0)
            buf129 = buf126; del buf126  # reuse
            # Topologically Sorted Source Nodes: [out_127, sum_44], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf125, buf127, buf129, 1185, 8186, stream=stream0)
            buf130 = buf121; del buf121  # reuse
            # Topologically Sorted Source Nodes: [out_127, sum_44], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf129, buf130, 1, 1185, stream=stream0)
            del buf129
            buf128 = buf125; del buf125  # reuse
            buf131 = buf122; del buf122  # reuse
            # Topologically Sorted Source Nodes: [out_127, out_130], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf128, buf127, buf130, buf131, 9699690, stream=stream0)
            buf132 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_130, sum_45], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf128, buf130, buf132, 1185, 8186, stream=stream0)
            buf133 = buf130; del buf130  # reuse
            # Topologically Sorted Source Nodes: [out_130, sum_45], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf132, buf133, 1, 1185, stream=stream0)
            buf135 = buf132; del buf132  # reuse
            # Topologically Sorted Source Nodes: [out_133, sum_46], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf131, buf133, buf135, 1185, 8186, stream=stream0)
            buf136 = buf127; del buf127  # reuse
            # Topologically Sorted Source Nodes: [out_133, sum_46], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf135, buf136, 1, 1185, stream=stream0)
            del buf135
            buf134 = buf131; del buf131  # reuse
            buf137 = buf128; del buf128  # reuse
            # Topologically Sorted Source Nodes: [out_133, out_136], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf134, buf133, buf136, buf137, 9699690, stream=stream0)
            buf138 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_136, sum_47], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf134, buf136, buf138, 1185, 8186, stream=stream0)
            buf139 = buf136; del buf136  # reuse
            # Topologically Sorted Source Nodes: [out_136, sum_47], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf138, buf139, 1, 1185, stream=stream0)
            buf141 = buf138; del buf138  # reuse
            # Topologically Sorted Source Nodes: [out_139, sum_48], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf137, buf139, buf141, 1185, 8186, stream=stream0)
            buf142 = buf133; del buf133  # reuse
            # Topologically Sorted Source Nodes: [out_139, sum_48], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf141, buf142, 1, 1185, stream=stream0)
            del buf141
            buf140 = buf137; del buf137  # reuse
            buf143 = buf134; del buf134  # reuse
            # Topologically Sorted Source Nodes: [out_139, out_142], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf140, buf139, buf142, buf143, 9699690, stream=stream0)
            buf144 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_142, sum_49], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf140, buf142, buf144, 1185, 8186, stream=stream0)
            buf145 = buf142; del buf142  # reuse
            # Topologically Sorted Source Nodes: [out_142, sum_49], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf144, buf145, 1, 1185, stream=stream0)
            buf147 = buf144; del buf144  # reuse
            # Topologically Sorted Source Nodes: [out_145, sum_50], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf143, buf145, buf147, 1185, 8186, stream=stream0)
            buf148 = buf139; del buf139  # reuse
            # Topologically Sorted Source Nodes: [out_145, sum_50], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf147, buf148, 1, 1185, stream=stream0)
            del buf147
            buf146 = buf143; del buf143  # reuse
            buf149 = buf140; del buf140  # reuse
            # Topologically Sorted Source Nodes: [out_145, out_148], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf146, buf145, buf148, buf149, 9699690, stream=stream0)
            buf150 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_148, sum_51], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf146, buf148, buf150, 1185, 8186, stream=stream0)
            buf151 = buf148; del buf148  # reuse
            # Topologically Sorted Source Nodes: [out_148, sum_51], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf150, buf151, 1, 1185, stream=stream0)
            buf153 = buf150; del buf150  # reuse
            # Topologically Sorted Source Nodes: [out_151, sum_52], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf149, buf151, buf153, 1185, 8186, stream=stream0)
            buf154 = buf145; del buf145  # reuse
            # Topologically Sorted Source Nodes: [out_151, sum_52], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf153, buf154, 1, 1185, stream=stream0)
            del buf153
            buf152 = buf149; del buf149  # reuse
            buf155 = buf146; del buf146  # reuse
            # Topologically Sorted Source Nodes: [out_151, out_154], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf152, buf151, buf154, buf155, 9699690, stream=stream0)
            buf156 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_154, sum_53], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf152, buf154, buf156, 1185, 8186, stream=stream0)
            buf157 = buf154; del buf154  # reuse
            # Topologically Sorted Source Nodes: [out_154, sum_53], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf156, buf157, 1, 1185, stream=stream0)
            buf159 = buf156; del buf156  # reuse
            # Topologically Sorted Source Nodes: [out_157, sum_54], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf155, buf157, buf159, 1185, 8186, stream=stream0)
            buf160 = buf151; del buf151  # reuse
            # Topologically Sorted Source Nodes: [out_157, sum_54], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf159, buf160, 1, 1185, stream=stream0)
            del buf159
            buf158 = buf155; del buf155  # reuse
            buf161 = buf152; del buf152  # reuse
            # Topologically Sorted Source Nodes: [out_157, out_160], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf158, buf157, buf160, buf161, 9699690, stream=stream0)
            buf162 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_160, sum_55], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf158, buf160, buf162, 1185, 8186, stream=stream0)
            buf163 = buf160; del buf160  # reuse
            # Topologically Sorted Source Nodes: [out_160, sum_55], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf162, buf163, 1, 1185, stream=stream0)
            buf165 = buf162; del buf162  # reuse
            # Topologically Sorted Source Nodes: [out_163, sum_56], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf161, buf163, buf165, 1185, 8186, stream=stream0)
            buf166 = buf157; del buf157  # reuse
            # Topologically Sorted Source Nodes: [out_163, sum_56], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf165, buf166, 1, 1185, stream=stream0)
            del buf165
            buf164 = buf161; del buf161  # reuse
            buf167 = buf158; del buf158  # reuse
            # Topologically Sorted Source Nodes: [out_163, out_166], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf164, buf163, buf166, buf167, 9699690, stream=stream0)
            buf168 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_166, sum_57], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf164, buf166, buf168, 1185, 8186, stream=stream0)
            buf169 = buf166; del buf166  # reuse
            # Topologically Sorted Source Nodes: [out_166, sum_57], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf168, buf169, 1, 1185, stream=stream0)
            buf171 = buf168; del buf168  # reuse
            # Topologically Sorted Source Nodes: [out_169, sum_58], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf167, buf169, buf171, 1185, 8186, stream=stream0)
            buf172 = buf163; del buf163  # reuse
            # Topologically Sorted Source Nodes: [out_169, sum_58], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf171, buf172, 1, 1185, stream=stream0)
            del buf171
            buf170 = buf167; del buf167  # reuse
            buf173 = buf164; del buf164  # reuse
            # Topologically Sorted Source Nodes: [out_169, out_172], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf170, buf169, buf172, buf173, 9699690, stream=stream0)
            buf174 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_172, sum_59], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf170, buf172, buf174, 1185, 8186, stream=stream0)
            buf175 = buf172; del buf172  # reuse
            # Topologically Sorted Source Nodes: [out_172, sum_59], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf174, buf175, 1, 1185, stream=stream0)
            buf177 = buf174; del buf174  # reuse
            # Topologically Sorted Source Nodes: [out_175, sum_60], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf173, buf175, buf177, 1185, 8186, stream=stream0)
            buf178 = buf169; del buf169  # reuse
            # Topologically Sorted Source Nodes: [out_175, sum_60], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf177, buf178, 1, 1185, stream=stream0)
            del buf177
            buf176 = buf173; del buf173  # reuse
            buf179 = buf170; del buf170  # reuse
            # Topologically Sorted Source Nodes: [out_175, out_178], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf176, buf175, buf178, buf179, 9699690, stream=stream0)
            buf180 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_178, sum_61], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf176, buf178, buf180, 1185, 8186, stream=stream0)
            buf181 = buf178; del buf178  # reuse
            # Topologically Sorted Source Nodes: [out_178, sum_61], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf180, buf181, 1, 1185, stream=stream0)
            buf183 = buf180; del buf180  # reuse
            # Topologically Sorted Source Nodes: [out_181, sum_62], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf179, buf181, buf183, 1185, 8186, stream=stream0)
            buf184 = buf175; del buf175  # reuse
            # Topologically Sorted Source Nodes: [out_181, sum_62], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf183, buf184, 1, 1185, stream=stream0)
            del buf183
            buf182 = buf179; del buf179  # reuse
            buf185 = buf176; del buf176  # reuse
            # Topologically Sorted Source Nodes: [out_181, out_184], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf182, buf181, buf184, buf185, 9699690, stream=stream0)
            buf186 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_184, sum_63], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf182, buf184, buf186, 1185, 8186, stream=stream0)
            buf187 = buf184; del buf184  # reuse
            # Topologically Sorted Source Nodes: [out_184, sum_63], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf186, buf187, 1, 1185, stream=stream0)
            buf189 = buf186; del buf186  # reuse
            # Topologically Sorted Source Nodes: [out_187, sum_64], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf185, buf187, buf189, 1185, 8186, stream=stream0)
            buf190 = buf181; del buf181  # reuse
            # Topologically Sorted Source Nodes: [out_187, sum_64], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf189, buf190, 1, 1185, stream=stream0)
            del buf189
            buf188 = buf185; del buf185  # reuse
            buf191 = buf182; del buf182  # reuse
            # Topologically Sorted Source Nodes: [out_187, out_190], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf188, buf187, buf190, buf191, 9699690, stream=stream0)
            buf192 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_190, sum_65], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf188, buf190, buf192, 1185, 8186, stream=stream0)
            buf193 = buf190; del buf190  # reuse
            # Topologically Sorted Source Nodes: [out_190, sum_65], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf192, buf193, 1, 1185, stream=stream0)
            buf195 = buf192; del buf192  # reuse
            # Topologically Sorted Source Nodes: [out_193, sum_66], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf191, buf193, buf195, 1185, 8186, stream=stream0)
            buf196 = buf187; del buf187  # reuse
            # Topologically Sorted Source Nodes: [out_193, sum_66], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf195, buf196, 1, 1185, stream=stream0)
            del buf195
            buf194 = buf191; del buf191  # reuse
            buf197 = buf188; del buf188  # reuse
            # Topologically Sorted Source Nodes: [out_193, out_196], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf194, buf193, buf196, buf197, 9699690, stream=stream0)
            buf198 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_196, sum_67], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf194, buf196, buf198, 1185, 8186, stream=stream0)
            buf199 = buf196; del buf196  # reuse
            # Topologically Sorted Source Nodes: [out_196, sum_67], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf198, buf199, 1, 1185, stream=stream0)
            buf201 = buf198; del buf198  # reuse
            # Topologically Sorted Source Nodes: [out_199, sum_68], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf197, buf199, buf201, 1185, 8186, stream=stream0)
            buf202 = buf193; del buf193  # reuse
            # Topologically Sorted Source Nodes: [out_199, sum_68], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf201, buf202, 1, 1185, stream=stream0)
            del buf201
            buf200 = buf197; del buf197  # reuse
            buf203 = buf194; del buf194  # reuse
            # Topologically Sorted Source Nodes: [out_199, out_202], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf200, buf199, buf202, buf203, 9699690, stream=stream0)
            buf204 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_202, sum_69], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf200, buf202, buf204, 1185, 8186, stream=stream0)
            buf205 = buf202; del buf202  # reuse
            # Topologically Sorted Source Nodes: [out_202, sum_69], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf204, buf205, 1, 1185, stream=stream0)
            buf207 = buf204; del buf204  # reuse
            # Topologically Sorted Source Nodes: [out_205, sum_70], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf203, buf205, buf207, 1185, 8186, stream=stream0)
            buf208 = buf199; del buf199  # reuse
            # Topologically Sorted Source Nodes: [out_205, sum_70], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf207, buf208, 1, 1185, stream=stream0)
            del buf207
            buf206 = buf203; del buf203  # reuse
            buf209 = buf200; del buf200  # reuse
            # Topologically Sorted Source Nodes: [out_205, out_208], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf206, buf205, buf208, buf209, 9699690, stream=stream0)
            buf210 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_208, sum_71], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf206, buf208, buf210, 1185, 8186, stream=stream0)
            buf211 = buf208; del buf208  # reuse
            # Topologically Sorted Source Nodes: [out_208, sum_71], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf210, buf211, 1, 1185, stream=stream0)
            buf213 = buf210; del buf210  # reuse
            # Topologically Sorted Source Nodes: [out_211, sum_72], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf209, buf211, buf213, 1185, 8186, stream=stream0)
            buf214 = buf205; del buf205  # reuse
            # Topologically Sorted Source Nodes: [out_211, sum_72], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf213, buf214, 1, 1185, stream=stream0)
            del buf213
            buf212 = buf209; del buf209  # reuse
            buf215 = buf206; del buf206  # reuse
            # Topologically Sorted Source Nodes: [out_211, out_214], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf212, buf211, buf214, buf215, 9699690, stream=stream0)
            buf216 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_214, sum_73], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf212, buf214, buf216, 1185, 8186, stream=stream0)
            buf217 = buf214; del buf214  # reuse
            # Topologically Sorted Source Nodes: [out_214, sum_73], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf216, buf217, 1, 1185, stream=stream0)
            buf219 = buf216; del buf216  # reuse
            # Topologically Sorted Source Nodes: [out_217, sum_74], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf215, buf217, buf219, 1185, 8186, stream=stream0)
            buf220 = buf211; del buf211  # reuse
            # Topologically Sorted Source Nodes: [out_217, sum_74], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf219, buf220, 1, 1185, stream=stream0)
            del buf219
            buf218 = buf215; del buf215  # reuse
            buf221 = buf212; del buf212  # reuse
            # Topologically Sorted Source Nodes: [out_217, out_220], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf218, buf217, buf220, buf221, 9699690, stream=stream0)
            buf222 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_220, sum_75], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf218, buf220, buf222, 1185, 8186, stream=stream0)
            buf223 = buf220; del buf220  # reuse
            # Topologically Sorted Source Nodes: [out_220, sum_75], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf222, buf223, 1, 1185, stream=stream0)
            buf225 = buf222; del buf222  # reuse
            # Topologically Sorted Source Nodes: [out_223, sum_76], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf221, buf223, buf225, 1185, 8186, stream=stream0)
            buf226 = buf217; del buf217  # reuse
            # Topologically Sorted Source Nodes: [out_223, sum_76], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf225, buf226, 1, 1185, stream=stream0)
            del buf225
            buf224 = buf221; del buf221  # reuse
            buf227 = buf218; del buf218  # reuse
            # Topologically Sorted Source Nodes: [out_223, out_226], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf224, buf223, buf226, buf227, 9699690, stream=stream0)
            buf228 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_226, sum_77], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf224, buf226, buf228, 1185, 8186, stream=stream0)
            buf229 = buf226; del buf226  # reuse
            # Topologically Sorted Source Nodes: [out_226, sum_77], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf228, buf229, 1, 1185, stream=stream0)
            buf231 = buf228; del buf228  # reuse
            # Topologically Sorted Source Nodes: [out_229, sum_78], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf227, buf229, buf231, 1185, 8186, stream=stream0)
            buf232 = buf223; del buf223  # reuse
            # Topologically Sorted Source Nodes: [out_229, sum_78], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf231, buf232, 1, 1185, stream=stream0)
            del buf231
            buf230 = buf227; del buf227  # reuse
            buf233 = buf224; del buf224  # reuse
            # Topologically Sorted Source Nodes: [out_229, out_232], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf230, buf229, buf232, buf233, 9699690, stream=stream0)
            buf234 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_232, sum_79], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf230, buf232, buf234, 1185, 8186, stream=stream0)
            buf235 = buf232; del buf232  # reuse
            # Topologically Sorted Source Nodes: [out_232, sum_79], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf234, buf235, 1, 1185, stream=stream0)
            buf237 = buf234; del buf234  # reuse
            # Topologically Sorted Source Nodes: [out_235, sum_80], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf233, buf235, buf237, 1185, 8186, stream=stream0)
            buf238 = buf229; del buf229  # reuse
            # Topologically Sorted Source Nodes: [out_235, sum_80], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf237, buf238, 1, 1185, stream=stream0)
            del buf237
            buf236 = buf233; del buf233  # reuse
            buf239 = buf230; del buf230  # reuse
            # Topologically Sorted Source Nodes: [out_235, out_238], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf236, buf235, buf238, buf239, 9699690, stream=stream0)
            buf240 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_238, sum_81], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf236, buf238, buf240, 1185, 8186, stream=stream0)
            buf241 = buf238; del buf238  # reuse
            # Topologically Sorted Source Nodes: [out_238, sum_81], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf240, buf241, 1, 1185, stream=stream0)
            buf243 = buf240; del buf240  # reuse
            # Topologically Sorted Source Nodes: [out_241, sum_82], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf239, buf241, buf243, 1185, 8186, stream=stream0)
            buf244 = buf235; del buf235  # reuse
            # Topologically Sorted Source Nodes: [out_241, sum_82], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf243, buf244, 1, 1185, stream=stream0)
            del buf243
            buf242 = buf239; del buf239  # reuse
            buf245 = buf236; del buf236  # reuse
            # Topologically Sorted Source Nodes: [out_241, out_244], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf242, buf241, buf244, buf245, 9699690, stream=stream0)
            buf246 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_244, sum_83], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf242, buf244, buf246, 1185, 8186, stream=stream0)
            buf247 = buf244; del buf244  # reuse
            # Topologically Sorted Source Nodes: [out_244, sum_83], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf246, buf247, 1, 1185, stream=stream0)
            buf249 = buf246; del buf246  # reuse
            # Topologically Sorted Source Nodes: [out_247, sum_84], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf245, buf247, buf249, 1185, 8186, stream=stream0)
            buf250 = buf241; del buf241  # reuse
            # Topologically Sorted Source Nodes: [out_247, sum_84], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf249, buf250, 1, 1185, stream=stream0)
            del buf249
            buf248 = buf245; del buf245  # reuse
            buf251 = buf242; del buf242  # reuse
            # Topologically Sorted Source Nodes: [out_247, out_250], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf248, buf247, buf250, buf251, 9699690, stream=stream0)
            buf252 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_250, sum_85], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf248, buf250, buf252, 1185, 8186, stream=stream0)
            buf253 = buf250; del buf250  # reuse
            # Topologically Sorted Source Nodes: [out_250, sum_85], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf252, buf253, 1, 1185, stream=stream0)
            buf255 = buf252; del buf252  # reuse
            # Topologically Sorted Source Nodes: [out_253, sum_86], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf251, buf253, buf255, 1185, 8186, stream=stream0)
            buf256 = buf247; del buf247  # reuse
            # Topologically Sorted Source Nodes: [out_253, sum_86], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf255, buf256, 1, 1185, stream=stream0)
            del buf255
            buf254 = buf251; del buf251  # reuse
            buf257 = buf248; del buf248  # reuse
            # Topologically Sorted Source Nodes: [out_253, out_256], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf254, buf253, buf256, buf257, 9699690, stream=stream0)
            buf258 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_256, sum_87], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf254, buf256, buf258, 1185, 8186, stream=stream0)
            buf259 = buf256; del buf256  # reuse
            # Topologically Sorted Source Nodes: [out_256, sum_87], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf258, buf259, 1, 1185, stream=stream0)
            buf261 = buf258; del buf258  # reuse
            # Topologically Sorted Source Nodes: [out_259, sum_88], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf257, buf259, buf261, 1185, 8186, stream=stream0)
            buf262 = buf253; del buf253  # reuse
            # Topologically Sorted Source Nodes: [out_259, sum_88], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf261, buf262, 1, 1185, stream=stream0)
            del buf261
            buf260 = buf257; del buf257  # reuse
            buf263 = buf254; del buf254  # reuse
            # Topologically Sorted Source Nodes: [out_259, out_262], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf260, buf259, buf262, buf263, 9699690, stream=stream0)
            buf264 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_262, sum_89], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf260, buf262, buf264, 1185, 8186, stream=stream0)
            buf265 = buf262; del buf262  # reuse
            # Topologically Sorted Source Nodes: [out_262, sum_89], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf264, buf265, 1, 1185, stream=stream0)
            buf267 = buf264; del buf264  # reuse
            # Topologically Sorted Source Nodes: [out_265, sum_90], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf263, buf265, buf267, 1185, 8186, stream=stream0)
            buf268 = buf259; del buf259  # reuse
            # Topologically Sorted Source Nodes: [out_265, sum_90], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf267, buf268, 1, 1185, stream=stream0)
            del buf267
            buf266 = buf263; del buf263  # reuse
            buf269 = buf260; del buf260  # reuse
            # Topologically Sorted Source Nodes: [out_265, out_268], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf266, buf265, buf268, buf269, 9699690, stream=stream0)
            buf270 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_268, sum_91], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf266, buf268, buf270, 1185, 8186, stream=stream0)
            buf271 = buf268; del buf268  # reuse
            # Topologically Sorted Source Nodes: [out_268, sum_91], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf270, buf271, 1, 1185, stream=stream0)
            buf273 = buf270; del buf270  # reuse
            # Topologically Sorted Source Nodes: [out_271, sum_92], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf269, buf271, buf273, 1185, 8186, stream=stream0)
            buf274 = buf265; del buf265  # reuse
            # Topologically Sorted Source Nodes: [out_271, sum_92], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf273, buf274, 1, 1185, stream=stream0)
            del buf273
            buf272 = buf269; del buf269  # reuse
            buf275 = buf266; del buf266  # reuse
            # Topologically Sorted Source Nodes: [out_271, out_274], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf272, buf271, buf274, buf275, 9699690, stream=stream0)
            buf276 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_274, sum_93], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf272, buf274, buf276, 1185, 8186, stream=stream0)
            buf277 = buf274; del buf274  # reuse
            # Topologically Sorted Source Nodes: [out_274, sum_93], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf276, buf277, 1, 1185, stream=stream0)
            buf279 = buf276; del buf276  # reuse
            # Topologically Sorted Source Nodes: [out_277, sum_94], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf275, buf277, buf279, 1185, 8186, stream=stream0)
            buf280 = buf271; del buf271  # reuse
            # Topologically Sorted Source Nodes: [out_277, sum_94], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf279, buf280, 1, 1185, stream=stream0)
            del buf279
            buf278 = buf275; del buf275  # reuse
            buf281 = buf272; del buf272  # reuse
            # Topologically Sorted Source Nodes: [out_277, out_280], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf278, buf277, buf280, buf281, 9699690, stream=stream0)
            buf282 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_280, sum_95], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf278, buf280, buf282, 1185, 8186, stream=stream0)
            buf283 = buf280; del buf280  # reuse
            # Topologically Sorted Source Nodes: [out_280, sum_95], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf282, buf283, 1, 1185, stream=stream0)
            buf285 = buf282; del buf282  # reuse
            # Topologically Sorted Source Nodes: [out_283, sum_96], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf281, buf283, buf285, 1185, 8186, stream=stream0)
            buf286 = buf277; del buf277  # reuse
            # Topologically Sorted Source Nodes: [out_283, sum_96], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf285, buf286, 1, 1185, stream=stream0)
            del buf285
            buf284 = buf281; del buf281  # reuse
            buf287 = buf278; del buf278  # reuse
            # Topologically Sorted Source Nodes: [out_283, out_286], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf284, buf283, buf286, buf287, 9699690, stream=stream0)
            buf288 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_286, sum_97], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf284, buf286, buf288, 1185, 8186, stream=stream0)
            buf289 = buf286; del buf286  # reuse
            # Topologically Sorted Source Nodes: [out_286, sum_97], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf288, buf289, 1, 1185, stream=stream0)
            buf291 = buf288; del buf288  # reuse
            # Topologically Sorted Source Nodes: [out_289, sum_98], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf287, buf289, buf291, 1185, 8186, stream=stream0)
            buf292 = buf283; del buf283  # reuse
            # Topologically Sorted Source Nodes: [out_289, sum_98], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf291, buf292, 1, 1185, stream=stream0)
            del buf291
            buf290 = buf287; del buf287  # reuse
            buf293 = buf284; del buf284  # reuse
            # Topologically Sorted Source Nodes: [out_289, out_292], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_5.run(buf290, buf289, buf292, buf293, 9699690, stream=stream0)
            buf294 = empty_strided_cuda((1185, ), (1, ), torch.float32)
            # Topologically Sorted Source Nodes: [out_292, sum_99], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf290, buf292, buf294, 1185, 8186, stream=stream0)
            del buf290
            buf295 = buf292; del buf292  # reuse
            # Topologically Sorted Source Nodes: [out_292, sum_99], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf294, buf295, 1, 1185, stream=stream0)
            buf297 = buf294; del buf294  # reuse
            # Topologically Sorted Source Nodes: [out_295, sum_100], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_add_sum_4.run(buf293, buf295, buf297, 1185, 8186, stream=stream0)
            buf298 = buf289; del buf289  # reuse
            # Topologically Sorted Source Nodes: [out_295, sum_100], Original ATen: [aten.add, aten.sum]
            stream0 = get_raw_stream(0)
            triton_red_fused_sum_view_1.run(buf297, buf298, 1, 1185, stream=stream0)
            del buf297
            buf296 = buf293; del buf293  # reuse
            buf299 = empty_strided_cuda((19, 17, 13, 11, 7, 5, 3, 2), (510510, 30030, 2310, 210, 30, 6, 2, 1), torch.float32)
            # Topologically Sorted Source Nodes: [out_295, out_298], Original ATen: [aten.add]
            stream0 = get_raw_stream(0)
            triton_poi_fused_add_6.run(buf296, buf295, buf298, buf299, 9699690, stream=stream0)
            del buf295
            del buf296
            del buf298
        return (reinterpret_tensor(buf299, (2, 3, 5, 7, 11, 13, 17, 19), (4849845, 1616615, 323323, 46189, 4199, 323, 19, 1), 0), )

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

