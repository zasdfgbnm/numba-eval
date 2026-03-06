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


# kernel path: /tmp/torchinductor_root/ls/clsmcahugmhxz4iwi7lsuagmcczlzuedyzp2bckykvexbh7zukoc.py
# Topologically Sorted Source Nodes: [out, out_1], Original ATen: [aten.view, aten.linalg_vector_norm]
# Source node to ATen node mapping:
#   out => view
#   out_1 => pow_1, sum_1
# Graph fragment:
#   %arg0_1 : Tensor "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = PlaceHolder[target=arg0_1]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %pow_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%view, 2.0), kwargs = {})
#   %sum_1 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_1, [0], True), kwargs = {})
#   return %sum_1
triton_per_fused_linalg_vector_norm_view_0 = async_compile.triton('triton_per_fused_linalg_vector_norm_view_0', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.persistent_reduction(
    size_hints={'x': 524288, 'r0_': 32},
    reduction_hint=ReductionHint.DEFAULT,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'out_ptr0': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_linalg_vector_norm_view_0', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 1, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 42882840, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_linalg_vector_norm_view_0(in_ptr0, out_ptr0, xnumel, r0_numel, XBLOCK : tl.constexpr):
    xnumel = 510510
    r0_numel = 19
    R0_BLOCK: tl.constexpr = 32
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_index = tl.arange(0, R0_BLOCK)[None, :]
    r0_offset = 0
    r0_mask = r0_index < r0_numel
    roffset = r0_offset
    rindex = r0_index
    r0_2 = r0_index
    x3 = xindex
    x0 = (xindex % 2310)
    x1 = xindex // 2310
    tmp0 = tl.load(in_ptr0 + (x3 + 510510*r0_2), r0_mask & xmask, other=0.0)
    tmp1 = tmp0 * tmp0
    tmp2 = tl.broadcast_to(tmp1, [XBLOCK, R0_BLOCK])
    tmp4 = tl.where(r0_mask & xmask, tmp2, 0)
    tmp5 = tl.sum(tmp4, 1)[:, None].to(tl.float32)
    tl.store(out_ptr0 + (x0 + 2336*x1), tmp5, xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/sq/csqb7hgcmqivgg35dxtz4u6izuckbddzm3a6kr2kx5yzj7vidmgr.py
# Topologically Sorted Source Nodes: [out, out_1, out_4], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
# Source node to ATen node mapping:
#   out => view
#   out_1 => clamp_min, div, expand, pow_2
#   out_4 => pow_3, sum_2
# Graph fragment:
#   %arg0_1 : Tensor "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = PlaceHolder[target=arg0_1]
#   %sum_1 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_1]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %pow_2 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_1, 0.5), kwargs = {})
#   %clamp_min : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_2, 1e-12), kwargs = {})
#   %expand : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][0, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%view, %expand), kwargs = {})
#   %pow_3 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%div, 2.0), kwargs = {})
#   %sum_2 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_3, [1], True), kwargs = {})
#   return %sum_2
triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_1 = async_compile.triton('triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_1', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.persistent_reduction(
    size_hints={'x': 1048576, 'r0_': 32},
    reduction_hint=ReductionHint.DEFAULT,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'in_ptr1': '*fp32', 'out_ptr0': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_1', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 2, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 45405360, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_1(in_ptr0, in_ptr1, out_ptr0, xnumel, r0_numel, XBLOCK : tl.constexpr):
    xnumel = 570570
    r0_numel = 17
    R0_BLOCK: tl.constexpr = 32
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_index = tl.arange(0, R0_BLOCK)[None, :]
    r0_offset = 0
    r0_mask = r0_index < r0_numel
    roffset = r0_offset
    rindex = r0_index
    r0_3 = r0_index
    x2 = xindex // 30030
    x4 = (xindex % 30030)
    x0 = (xindex % 2310)
    x1 = ((xindex // 2310) % 13)
    x5 = xindex // 2310
    tmp0 = tl.load(in_ptr0 + (x4 + 30030*r0_3 + 510510*x2), r0_mask & xmask, other=0.0)
    tmp1 = tl.load(in_ptr1 + (x0 + 2336*x1 + 30368*r0_3), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp2 = tl.sqrt_rn(tmp1)
    tmp3 = tl.full([1, 1], 1e-12, tl.float32)
    tmp4 = triton_helpers.maximum(tmp2, tmp3)
    tmp5 = (tmp0 / tmp4)
    tmp6 = tmp5 * tmp5
    tmp7 = tl.broadcast_to(tmp6, [XBLOCK, R0_BLOCK])
    tmp9 = tl.where(r0_mask & xmask, tmp7, 0)
    tmp10 = tl.sum(tmp9, 1)[:, None].to(tl.float32)
    tl.store(out_ptr0 + (x0 + 2336*x5), tmp10, xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/gq/cgqrk7ibgzfkrfq4ewi55qa67ubjpuuzpwmjjdvd4yt35elskzwa.py
# Topologically Sorted Source Nodes: [out, out_1, out_4, out_7], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
# Source node to ATen node mapping:
#   out => view
#   out_1 => clamp_min, div, expand, pow_2
#   out_4 => clamp_min_1, div_1, expand_1, pow_4
#   out_7 => pow_5, sum_3
# Graph fragment:
#   %arg0_1 : Tensor "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = PlaceHolder[target=arg0_1]
#   %sum_1 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_1]
#   %sum_2 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30368, 576992, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_2]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %pow_2 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_1, 0.5), kwargs = {})
#   %clamp_min : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_2, 1e-12), kwargs = {})
#   %expand : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][0, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%view, %expand), kwargs = {})
#   %pow_4 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_2, 0.5), kwargs = {})
#   %clamp_min_1 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_4, 1e-12), kwargs = {})
#   %expand_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][30030, 0, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div, %expand_1), kwargs = {})
#   %pow_5 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%div_1, 2.0), kwargs = {})
#   %sum_3 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39270, 2310, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_5, [2], True), kwargs = {})
#   return %sum_3
triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_2 = async_compile.triton('triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_2', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.persistent_reduction(
    size_hints={'x': 1048576, 'r0_': 16},
    reduction_hint=ReductionHint.DEFAULT,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'in_ptr1': '*fp32', 'in_ptr2': '*fp32', 'out_ptr0': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_2', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 3, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 49092120, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_2(in_ptr0, in_ptr1, in_ptr2, out_ptr0, xnumel, r0_numel, XBLOCK : tl.constexpr):
    xnumel = 746130
    r0_numel = 13
    R0_BLOCK: tl.constexpr = 16
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_index = tl.arange(0, R0_BLOCK)[None, :]
    r0_offset = 0
    r0_mask = r0_index < r0_numel
    roffset = r0_offset
    rindex = r0_index
    r0_3 = r0_index
    x0 = (xindex % 2310)
    x4 = xindex // 2310
    x1 = ((xindex // 2310) % 17)
    x2 = xindex // 39270
    tmp0 = tl.load(in_ptr0 + (x0 + 2310*r0_3 + 30030*x4), r0_mask & xmask, other=0.0)
    tmp1 = tl.load(in_ptr1 + (x0 + 2336*r0_3 + 30368*x1), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp6 = tl.load(in_ptr2 + (x0 + 2336*r0_3 + 30368*x2), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp2 = tl.sqrt_rn(tmp1)
    tmp3 = tl.full([1, 1], 1e-12, tl.float32)
    tmp4 = triton_helpers.maximum(tmp2, tmp3)
    tmp5 = (tmp0 / tmp4)
    tmp7 = tl.sqrt_rn(tmp6)
    tmp8 = triton_helpers.maximum(tmp7, tmp3)
    tmp9 = (tmp5 / tmp8)
    tmp10 = tmp9 * tmp9
    tmp11 = tl.broadcast_to(tmp10, [XBLOCK, R0_BLOCK])
    tmp13 = tl.where(r0_mask & xmask, tmp11, 0)
    tmp14 = tl.sum(tmp13, 1)[:, None].to(tl.float32)
    tl.store(out_ptr0 + (x0 + 2336*x4), tmp14, xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/wa/cwagpibwpmhdo6k5oqd6zdr7ah6gncfkxcnsnhd5vyo5zi5knqzy.py
# Topologically Sorted Source Nodes: [out, out_1, out_4, out_7, out_10], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
# Source node to ATen node mapping:
#   out => view
#   out_1 => clamp_min, div, expand, pow_2
#   out_10 => clamp_min_3, div_3, expand_3, pow_7, pow_8, sum_4
#   out_4 => clamp_min_1, div_1, expand_1, pow_4
#   out_7 => clamp_min_2, div_2, expand_2, pow_6
# Graph fragment:
#   %arg0_1 : Tensor "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = PlaceHolder[target=arg0_1]
#   %sum_1 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_1]
#   %sum_2 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30368, 576992, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_2]
#   %sum_3 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39712, 2336, 754528, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_3]
#   %sum_4 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46784, 2752, 210, 888896, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_4]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %pow_2 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_1, 0.5), kwargs = {})
#   %clamp_min : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_2, 1e-12), kwargs = {})
#   %expand : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][0, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%view, %expand), kwargs = {})
#   %pow_4 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_2, 0.5), kwargs = {})
#   %clamp_min_1 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_4, 1e-12), kwargs = {})
#   %expand_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][30030, 0, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div, %expand_1), kwargs = {})
#   %pow_6 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39270, 2310, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_3, 0.5), kwargs = {})
#   %clamp_min_2 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39270, 2310, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_6, 1e-12), kwargs = {})
#   %expand_2 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][39270, 2310, 0, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_2, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_2 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_1, %expand_2), kwargs = {})
#   %pow_7 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%div_2, 2.0), kwargs = {})
#   %sum_4 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46410, 2730, 210, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_7, [3], True), kwargs = {})
#   %pow_8 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46410, 2730, 210, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_4, 0.5), kwargs = {})
#   %clamp_min_3 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46410, 2730, 210, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_8, 1e-12), kwargs = {})
#   %expand_3 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][46410, 2730, 210, 0, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_3, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_3 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_2, %expand_3), kwargs = {})
#   return %sum_4,%div_3
triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_3 = async_compile.triton('triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_3', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.persistent_reduction(
    size_hints={'x': 1048576, 'r0_': 16},
    reduction_hint=ReductionHint.DEFAULT,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'in_ptr1': '*fp32', 'in_ptr2': '*fp32', 'in_ptr3': '*fp32', 'out_ptr1': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]], (4,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_3', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 4, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 123705120, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_3(in_ptr0, in_ptr1, in_ptr2, in_ptr3, out_ptr1, xnumel, r0_numel, XBLOCK : tl.constexpr):
    xnumel = 881790
    r0_numel = 11
    R0_BLOCK: tl.constexpr = 16
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_index = tl.arange(0, R0_BLOCK)[None, :]
    r0_offset = 0
    r0_mask = r0_index < r0_numel
    roffset = r0_offset
    rindex = r0_index
    r0_4 = r0_index
    x0 = (xindex % 210)
    x5 = xindex // 210
    x6 = ((xindex // 210) % 221)
    x1 = ((xindex // 210) % 13)
    x3 = xindex // 46410
    x7 = xindex // 2730
    x8 = (xindex % 2730)
    tmp0 = tl.load(in_ptr0 + (x0 + 210*r0_4 + 2310*x5), r0_mask & xmask, other=0.0)
    tmp1 = tl.load(in_ptr1 + (x0 + 210*r0_4 + 2336*x6), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp6 = tl.load(in_ptr2 + (x0 + 210*r0_4 + 2336*x1 + 30368*x3), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp10 = tl.load(in_ptr3 + (x0 + 210*r0_4 + 2336*x7), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp2 = tl.sqrt_rn(tmp1)
    tmp3 = tl.full([1, 1], 1e-12, tl.float32)
    tmp4 = triton_helpers.maximum(tmp2, tmp3)
    tmp5 = (tmp0 / tmp4)
    tmp7 = tl.sqrt_rn(tmp6)
    tmp8 = triton_helpers.maximum(tmp7, tmp3)
    tmp9 = (tmp5 / tmp8)
    tmp11 = tl.sqrt_rn(tmp10)
    tmp12 = triton_helpers.maximum(tmp11, tmp3)
    tmp13 = (tmp9 / tmp12)
    tmp14 = tmp13 * tmp13
    tmp15 = tl.broadcast_to(tmp14, [XBLOCK, R0_BLOCK])
    tmp17 = tl.where(r0_mask & xmask, tmp15, 0)
    tmp18 = tl.sum(tmp17, 1)[:, None].to(tl.float32)
    tmp19 = tl.sqrt_rn(tmp18)
    tmp20 = triton_helpers.maximum(tmp19, tmp3)
    tmp21 = (tmp13 / tmp20)
    tl.store(out_ptr1 + (x0 + 210*r0_4 + 2336*x5), tmp21, r0_mask & xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/bw/cbwrov55e5grrkmpftewdhgkadkxwhr7jqmipyj54x4nyjcmtpin.py
# Topologically Sorted Source Nodes: [out_13], Original ATen: [aten.linalg_vector_norm]
# Source node to ATen node mapping:
#   out_13 => pow_9, sum_5
# Graph fragment:
#   %div_3 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=div_3]
#   %pow_9 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%div_3, 2.0), kwargs = {})
#   %sum_5 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_9, [0], True), kwargs = {})
#   return %sum_5
triton_per_fused_linalg_vector_norm_4 = async_compile.triton('triton_per_fused_linalg_vector_norm_4', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.persistent_reduction(
    size_hints={'x': 524288, 'r0_': 32},
    reduction_hint=ReductionHint.DEFAULT,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'out_ptr0': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_linalg_vector_norm_4', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 1, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 42882840, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_linalg_vector_norm_4(in_ptr0, out_ptr0, xnumel, r0_numel, XBLOCK : tl.constexpr):
    xnumel = 510510
    r0_numel = 19
    R0_BLOCK: tl.constexpr = 32
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_index = tl.arange(0, R0_BLOCK)[None, :]
    r0_offset = 0
    r0_mask = r0_index < r0_numel
    roffset = r0_offset
    rindex = r0_index
    r0_2 = r0_index
    x0 = (xindex % 2310)
    x1 = xindex // 2310
    tmp0 = tl.load(in_ptr0 + (x0 + 2336*x1 + 516256*r0_2), r0_mask & xmask, other=0.0)
    tmp1 = tmp0 * tmp0
    tmp2 = tl.broadcast_to(tmp1, [XBLOCK, R0_BLOCK])
    tmp4 = tl.where(r0_mask & xmask, tmp2, 0)
    tmp5 = tl.sum(tmp4, 1)[:, None].to(tl.float32)
    tl.store(out_ptr0 + (x0 + 2336*x1), tmp5, xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/f7/cf72d3skmq53ojnst7fg5dggwkdbutn2hi5kt7v4l3powj3mknlp.py
# Topologically Sorted Source Nodes: [out_13, out_16], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
# Source node to ATen node mapping:
#   out_13 => clamp_min_4, div_4, expand_4, pow_10
#   out_16 => pow_11, sum_6
# Graph fragment:
#   %div_3 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=div_3]
#   %sum_5 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_5]
#   %pow_10 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_5, 0.5), kwargs = {})
#   %clamp_min_4 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_10, 1e-12), kwargs = {})
#   %expand_4 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][0, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_4, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_4 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_3, %expand_4), kwargs = {})
#   %pow_11 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%div_4, 2.0), kwargs = {})
#   %sum_6 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_11, [1], True), kwargs = {})
#   return %sum_6
triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5 = async_compile.triton('triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.persistent_reduction(
    size_hints={'x': 1048576, 'r0_': 32},
    reduction_hint=ReductionHint.DEFAULT,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'in_ptr1': '*fp32', 'out_ptr0': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 2, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 45405360, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5(in_ptr0, in_ptr1, out_ptr0, xnumel, r0_numel, XBLOCK : tl.constexpr):
    xnumel = 570570
    r0_numel = 17
    R0_BLOCK: tl.constexpr = 32
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_index = tl.arange(0, R0_BLOCK)[None, :]
    r0_offset = 0
    r0_mask = r0_index < r0_numel
    roffset = r0_offset
    rindex = r0_index
    r0_3 = r0_index
    x0 = (xindex % 2310)
    x1 = ((xindex // 2310) % 13)
    x2 = xindex // 30030
    x4 = xindex // 2310
    tmp0 = tl.load(in_ptr0 + (x0 + 2336*x1 + 30368*r0_3 + 516256*x2), r0_mask & xmask, other=0.0)
    tmp1 = tl.load(in_ptr1 + (x0 + 2336*x1 + 30368*r0_3), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp2 = tl.sqrt_rn(tmp1)
    tmp3 = tl.full([1, 1], 1e-12, tl.float32)
    tmp4 = triton_helpers.maximum(tmp2, tmp3)
    tmp5 = (tmp0 / tmp4)
    tmp6 = tmp5 * tmp5
    tmp7 = tl.broadcast_to(tmp6, [XBLOCK, R0_BLOCK])
    tmp9 = tl.where(r0_mask & xmask, tmp7, 0)
    tmp10 = tl.sum(tmp9, 1)[:, None].to(tl.float32)
    tl.store(out_ptr0 + (x0 + 2336*x4), tmp10, xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/ha/cha2zkwy3pnlfewytb6o5s7wycpj75nzu7z2u3cawqbwmxtleik4.py
# Topologically Sorted Source Nodes: [out_13, out_16, out_19], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
# Source node to ATen node mapping:
#   out_13 => clamp_min_4, div_4, expand_4, pow_10
#   out_16 => clamp_min_5, div_5, expand_5, pow_12
#   out_19 => pow_13, sum_7
# Graph fragment:
#   %div_3 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=div_3]
#   %sum_5 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_5]
#   %sum_6 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30368, 576992, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_6]
#   %pow_10 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_5, 0.5), kwargs = {})
#   %clamp_min_4 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_10, 1e-12), kwargs = {})
#   %expand_4 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][0, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_4, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_4 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_3, %expand_4), kwargs = {})
#   %pow_12 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_6, 0.5), kwargs = {})
#   %clamp_min_5 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_12, 1e-12), kwargs = {})
#   %expand_5 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][30030, 0, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_5, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_5 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_4, %expand_5), kwargs = {})
#   %pow_13 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%div_5, 2.0), kwargs = {})
#   %sum_7 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39270, 2310, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_13, [2], True), kwargs = {})
#   return %sum_7
triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6 = async_compile.triton('triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.persistent_reduction(
    size_hints={'x': 1048576, 'r0_': 16},
    reduction_hint=ReductionHint.DEFAULT,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'in_ptr1': '*fp32', 'in_ptr2': '*fp32', 'out_ptr0': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 3, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 49092120, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6(in_ptr0, in_ptr1, in_ptr2, out_ptr0, xnumel, r0_numel, XBLOCK : tl.constexpr):
    xnumel = 746130
    r0_numel = 13
    R0_BLOCK: tl.constexpr = 16
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_index = tl.arange(0, R0_BLOCK)[None, :]
    r0_offset = 0
    r0_mask = r0_index < r0_numel
    roffset = r0_offset
    rindex = r0_index
    r0_3 = r0_index
    x0 = (xindex % 2310)
    x4 = xindex // 2310
    x1 = ((xindex // 2310) % 17)
    x2 = xindex // 39270
    tmp0 = tl.load(in_ptr0 + (x0 + 2336*r0_3 + 30368*x4), r0_mask & xmask, other=0.0)
    tmp1 = tl.load(in_ptr1 + (x0 + 2336*r0_3 + 30368*x1), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp6 = tl.load(in_ptr2 + (x0 + 2336*r0_3 + 30368*x2), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp2 = tl.sqrt_rn(tmp1)
    tmp3 = tl.full([1, 1], 1e-12, tl.float32)
    tmp4 = triton_helpers.maximum(tmp2, tmp3)
    tmp5 = (tmp0 / tmp4)
    tmp7 = tl.sqrt_rn(tmp6)
    tmp8 = triton_helpers.maximum(tmp7, tmp3)
    tmp9 = (tmp5 / tmp8)
    tmp10 = tmp9 * tmp9
    tmp11 = tl.broadcast_to(tmp10, [XBLOCK, R0_BLOCK])
    tmp13 = tl.where(r0_mask & xmask, tmp11, 0)
    tmp14 = tl.sum(tmp13, 1)[:, None].to(tl.float32)
    tl.store(out_ptr0 + (x0 + 2336*x4), tmp14, xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/vd/cvdofofin2pdyp7vf2twhd52wldnuzunh3pht4vcc6uiufjxrqno.py
# Topologically Sorted Source Nodes: [out_13, out_16, out_19, out_22], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
# Source node to ATen node mapping:
#   out_13 => clamp_min_4, div_4, expand_4, pow_10
#   out_16 => clamp_min_5, div_5, expand_5, pow_12
#   out_19 => clamp_min_6, div_6, expand_6, pow_14
#   out_22 => clamp_min_7, div_7, expand_7, pow_15, pow_16, sum_8
# Graph fragment:
#   %div_3 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=div_3]
#   %sum_5 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_5]
#   %sum_6 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30368, 576992, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_6]
#   %sum_7 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39712, 2336, 754528, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_7]
#   %sum_8 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46784, 2752, 210, 888896, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_8]
#   %pow_10 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_5, 0.5), kwargs = {})
#   %clamp_min_4 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_10, 1e-12), kwargs = {})
#   %expand_4 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][0, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_4, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_4 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_3, %expand_4), kwargs = {})
#   %pow_12 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_6, 0.5), kwargs = {})
#   %clamp_min_5 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_12, 1e-12), kwargs = {})
#   %expand_5 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][30030, 0, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_5, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_5 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_4, %expand_5), kwargs = {})
#   %pow_14 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39270, 2310, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_7, 0.5), kwargs = {})
#   %clamp_min_6 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39270, 2310, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_14, 1e-12), kwargs = {})
#   %expand_6 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][39270, 2310, 0, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_6, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_6 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_5, %expand_6), kwargs = {})
#   %pow_15 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%div_6, 2.0), kwargs = {})
#   %sum_8 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46410, 2730, 210, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_15, [3], True), kwargs = {})
#   %pow_16 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46410, 2730, 210, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_8, 0.5), kwargs = {})
#   %clamp_min_7 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46410, 2730, 210, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_16, 1e-12), kwargs = {})
#   %expand_7 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][46410, 2730, 210, 0, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_7, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_7 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_6, %expand_7), kwargs = {})
#   return %sum_8,%div_7
triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7 = async_compile.triton('triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.persistent_reduction(
    size_hints={'x': 1048576, 'r0_': 16},
    reduction_hint=ReductionHint.DEFAULT,
    filename=__file__,
    triton_meta={'signature': {'in_out_ptr0': '*fp32', 'in_ptr0': '*fp32', 'in_ptr1': '*fp32', 'in_ptr2': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7', 'mutated_arg_names': ['in_out_ptr0'], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 4, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 123705120, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7(in_out_ptr0, in_ptr0, in_ptr1, in_ptr2, xnumel, r0_numel, XBLOCK : tl.constexpr):
    xnumel = 881790
    r0_numel = 11
    R0_BLOCK: tl.constexpr = 16
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_index = tl.arange(0, R0_BLOCK)[None, :]
    r0_offset = 0
    r0_mask = r0_index < r0_numel
    roffset = r0_offset
    rindex = r0_index
    r0_4 = r0_index
    x0 = (xindex % 210)
    x5 = xindex // 210
    x6 = ((xindex // 210) % 221)
    x1 = ((xindex // 210) % 13)
    x3 = xindex // 46410
    x7 = xindex // 2730
    x8 = (xindex % 2730)
    tmp0 = tl.load(in_out_ptr0 + (x0 + 210*r0_4 + 2336*x5), r0_mask & xmask, other=0.0)
    tmp1 = tl.load(in_ptr0 + (x0 + 210*r0_4 + 2336*x6), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp6 = tl.load(in_ptr1 + (x0 + 210*r0_4 + 2336*x1 + 30368*x3), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp10 = tl.load(in_ptr2 + (x0 + 210*r0_4 + 2336*x7), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp2 = tl.sqrt_rn(tmp1)
    tmp3 = tl.full([1, 1], 1e-12, tl.float32)
    tmp4 = triton_helpers.maximum(tmp2, tmp3)
    tmp5 = (tmp0 / tmp4)
    tmp7 = tl.sqrt_rn(tmp6)
    tmp8 = triton_helpers.maximum(tmp7, tmp3)
    tmp9 = (tmp5 / tmp8)
    tmp11 = tl.sqrt_rn(tmp10)
    tmp12 = triton_helpers.maximum(tmp11, tmp3)
    tmp13 = (tmp9 / tmp12)
    tmp14 = tmp13 * tmp13
    tmp15 = tl.broadcast_to(tmp14, [XBLOCK, R0_BLOCK])
    tmp17 = tl.where(r0_mask & xmask, tmp15, 0)
    tmp18 = tl.sum(tmp17, 1)[:, None].to(tl.float32)
    tmp19 = tl.sqrt_rn(tmp18)
    tmp20 = triton_helpers.maximum(tmp19, tmp3)
    tmp21 = (tmp13 / tmp20)
    tl.store(in_out_ptr0 + (x0 + 210*r0_4 + 2336*x5), tmp21, r0_mask & xmask)
''', device_str='cuda')


# kernel path: /tmp/torchinductor_root/ua/cuag6qeftlyx7nyjxqz7jfemkx37stoxdnninhnatcjp7j35cybe.py
# Topologically Sorted Source Nodes: [out_289, out_292, out_295, out_298], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
# Source node to ATen node mapping:
#   out_289 => clamp_min_96, div_96, expand_96, pow_194
#   out_292 => clamp_min_97, div_97, expand_97, pow_196
#   out_295 => clamp_min_98, div_98, expand_98, pow_198
#   out_298 => clamp_min_99, div_99, expand_99, pow_199, pow_200, sum_100
# Graph fragment:
#   %div_95 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=div_95]
#   %sum_97 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_97]
#   %sum_98 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30368, 576992, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_98]
#   %sum_99 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39712, 2336, 754528, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_99]
#   %sum_100 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46784, 2752, 210, 888896, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_100]
#   %pow_194 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_97, 0.5), kwargs = {})
#   %clamp_min_96 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_194, 1e-12), kwargs = {})
#   %expand_96 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][0, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_96, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_96 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_95, %expand_96), kwargs = {})
#   %pow_196 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_98, 0.5), kwargs = {})
#   %clamp_min_97 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_196, 1e-12), kwargs = {})
#   %expand_97 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][30030, 0, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_97, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_97 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_96, %expand_97), kwargs = {})
#   %pow_198 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39270, 2310, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_99, 0.5), kwargs = {})
#   %clamp_min_98 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39270, 2310, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_198, 1e-12), kwargs = {})
#   %expand_98 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][39270, 2310, 0, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_98, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_98 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_97, %expand_98), kwargs = {})
#   %pow_199 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%div_98, 2.0), kwargs = {})
#   %sum_100 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46410, 2730, 210, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_199, [3], True), kwargs = {})
#   %pow_200 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46410, 2730, 210, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_100, 0.5), kwargs = {})
#   %clamp_min_99 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46410, 2730, 210, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_200, 1e-12), kwargs = {})
#   %expand_99 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][46410, 2730, 210, 0, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min_99, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div_99 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.div.Tensor](args = (%div_98, %expand_99), kwargs = {})
#   return %sum_100,%div_99
triton_per_fused_clamp_min_div_expand_linalg_vector_norm_8 = async_compile.triton('triton_per_fused_clamp_min_div_expand_linalg_vector_norm_8', '''
import triton
import triton.language as tl

from torch._inductor.runtime import triton_helpers, triton_heuristics
from torch._inductor.runtime.triton_helpers import libdevice, math as tl_math
from torch._inductor.runtime.hints import AutotuneHint, ReductionHint, TileHint, DeviceProperties
triton_helpers.set_driver_to_gpu()

@triton_heuristics.persistent_reduction(
    size_hints={'x': 1048576, 'r0_': 16},
    reduction_hint=ReductionHint.DEFAULT,
    filename=__file__,
    triton_meta={'signature': {'in_ptr0': '*fp32', 'in_ptr1': '*fp32', 'in_ptr2': '*fp32', 'in_ptr3': '*fp32', 'out_ptr1': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]], (2,): [['tt.divisibility', 16]], (3,): [['tt.divisibility', 16]], (4,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_clamp_min_div_expand_linalg_vector_norm_8', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 4, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 123705120, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_clamp_min_div_expand_linalg_vector_norm_8(in_ptr0, in_ptr1, in_ptr2, in_ptr3, out_ptr1, xnumel, r0_numel, XBLOCK : tl.constexpr):
    xnumel = 881790
    r0_numel = 11
    R0_BLOCK: tl.constexpr = 16
    rnumel = r0_numel
    RBLOCK: tl.constexpr = R0_BLOCK
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_index = tl.arange(0, R0_BLOCK)[None, :]
    r0_offset = 0
    r0_mask = r0_index < r0_numel
    roffset = r0_offset
    rindex = r0_index
    r0_4 = r0_index
    x0 = (xindex % 210)
    x5 = xindex // 210
    x6 = ((xindex // 210) % 221)
    x1 = ((xindex // 210) % 13)
    x3 = xindex // 46410
    x7 = xindex // 2730
    x8 = (xindex % 2730)
    tmp0 = tl.load(in_ptr0 + (x0 + 210*r0_4 + 2336*x5), r0_mask & xmask, other=0.0)
    tmp1 = tl.load(in_ptr1 + (x0 + 210*r0_4 + 2336*x6), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp6 = tl.load(in_ptr2 + (x0 + 210*r0_4 + 2336*x1 + 30368*x3), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp10 = tl.load(in_ptr3 + (x0 + 210*r0_4 + 2336*x7), r0_mask & xmask, eviction_policy='evict_last', other=0.0)
    tmp2 = tl.sqrt_rn(tmp1)
    tmp3 = tl.full([1, 1], 1e-12, tl.float32)
    tmp4 = triton_helpers.maximum(tmp2, tmp3)
    tmp5 = (tmp0 / tmp4)
    tmp7 = tl.sqrt_rn(tmp6)
    tmp8 = triton_helpers.maximum(tmp7, tmp3)
    tmp9 = (tmp5 / tmp8)
    tmp11 = tl.sqrt_rn(tmp10)
    tmp12 = triton_helpers.maximum(tmp11, tmp3)
    tmp13 = (tmp9 / tmp12)
    tmp14 = tmp13 * tmp13
    tmp15 = tl.broadcast_to(tmp14, [XBLOCK, R0_BLOCK])
    tmp17 = tl.where(r0_mask & xmask, tmp15, 0)
    tmp18 = tl.sum(tmp17, 1)[:, None].to(tl.float32)
    tmp19 = tl.sqrt_rn(tmp18)
    tmp20 = triton_helpers.maximum(tmp19, tmp3)
    tmp21 = (tmp13 / tmp20)
    tl.store(out_ptr1 + (x0 + 210*r0_4 + 2310*x5), tmp21, r0_mask & xmask)
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
            buf0 = empty_strided_cuda((1, 17, 13, 11, 7, 5, 3, 2), (516256, 30368, 2336, 210, 30, 6, 2, 1), torch.float32)
            # Topologically Sorted Source Nodes: [out, out_1], Original ATen: [aten.view, aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_view_0:1
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_view_0.run(arg0_1, buf0, 510510, 19, stream=stream0)
            buf1 = empty_strided_cuda((19, 1, 13, 11, 7, 5, 3, 2), (30368, 576992, 2336, 210, 30, 6, 2, 1), torch.float32)
            # Topologically Sorted Source Nodes: [out, out_1, out_4], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_1:2
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_1.run(arg0_1, buf0, buf1, 570570, 17, stream=stream0)
            buf2 = empty_strided_cuda((19, 17, 1, 11, 7, 5, 3, 2), (39712, 2336, 754528, 210, 30, 6, 2, 1), torch.float32)
            # Topologically Sorted Source Nodes: [out, out_1, out_4, out_7], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_2:3
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_2.run(arg0_1, buf0, buf1, buf2, 746130, 13, stream=stream0)
            buf4 = empty_strided_cuda((19, 17, 13, 11, 7, 5, 3, 2), (516256, 30368, 2336, 210, 30, 6, 2, 1), torch.float32)
            # Topologically Sorted Source Nodes: [out, out_1, out_4, out_7, out_10], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_3:4
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_3.run(arg0_1, buf0, buf1, buf2, buf4, 881790, 11, stream=stream0)
            del arg0_1
            buf5 = buf0; del buf0  # reuse
            # Topologically Sorted Source Nodes: [out_13], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:5
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf4, buf5, 510510, 19, stream=stream0)
            buf6 = buf1; del buf1  # reuse
            # Topologically Sorted Source Nodes: [out_13, out_16], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:6
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf4, buf5, buf6, 570570, 17, stream=stream0)
            buf7 = buf2; del buf2  # reuse
            # Topologically Sorted Source Nodes: [out_13, out_16, out_19], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:7
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf4, buf5, buf6, buf7, 746130, 13, stream=stream0)
            buf9 = buf4; del buf4  # reuse
            # Topologically Sorted Source Nodes: [out_13, out_16, out_19, out_22], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:8
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf9, buf5, buf6, buf7, 881790, 11, stream=stream0)
            buf10 = buf5; del buf5  # reuse
            # Topologically Sorted Source Nodes: [out_25], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:9
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf9, buf10, 510510, 19, stream=stream0)
            buf11 = buf6; del buf6  # reuse
            # Topologically Sorted Source Nodes: [out_25, out_28], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:10
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf9, buf10, buf11, 570570, 17, stream=stream0)
            buf12 = buf7; del buf7  # reuse
            # Topologically Sorted Source Nodes: [out_25, out_28, out_31], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:11
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf9, buf10, buf11, buf12, 746130, 13, stream=stream0)
            buf14 = buf9; del buf9  # reuse
            # Topologically Sorted Source Nodes: [out_25, out_28, out_31, out_34], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:12
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf14, buf10, buf11, buf12, 881790, 11, stream=stream0)
            buf15 = buf10; del buf10  # reuse
            # Topologically Sorted Source Nodes: [out_37], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:13
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf14, buf15, 510510, 19, stream=stream0)
            buf16 = buf11; del buf11  # reuse
            # Topologically Sorted Source Nodes: [out_37, out_40], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:14
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf14, buf15, buf16, 570570, 17, stream=stream0)
            buf17 = buf12; del buf12  # reuse
            # Topologically Sorted Source Nodes: [out_37, out_40, out_43], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:15
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf14, buf15, buf16, buf17, 746130, 13, stream=stream0)
            buf19 = buf14; del buf14  # reuse
            # Topologically Sorted Source Nodes: [out_37, out_40, out_43, out_46], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:16
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf19, buf15, buf16, buf17, 881790, 11, stream=stream0)
            buf20 = buf15; del buf15  # reuse
            # Topologically Sorted Source Nodes: [out_49], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:17
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf19, buf20, 510510, 19, stream=stream0)
            buf21 = buf16; del buf16  # reuse
            # Topologically Sorted Source Nodes: [out_49, out_52], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:18
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf19, buf20, buf21, 570570, 17, stream=stream0)
            buf22 = buf17; del buf17  # reuse
            # Topologically Sorted Source Nodes: [out_49, out_52, out_55], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:19
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf19, buf20, buf21, buf22, 746130, 13, stream=stream0)
            buf24 = buf19; del buf19  # reuse
            # Topologically Sorted Source Nodes: [out_49, out_52, out_55, out_58], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:20
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf24, buf20, buf21, buf22, 881790, 11, stream=stream0)
            buf25 = buf20; del buf20  # reuse
            # Topologically Sorted Source Nodes: [out_61], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:21
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf24, buf25, 510510, 19, stream=stream0)
            buf26 = buf21; del buf21  # reuse
            # Topologically Sorted Source Nodes: [out_61, out_64], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:22
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf24, buf25, buf26, 570570, 17, stream=stream0)
            buf27 = buf22; del buf22  # reuse
            # Topologically Sorted Source Nodes: [out_61, out_64, out_67], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:23
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf24, buf25, buf26, buf27, 746130, 13, stream=stream0)
            buf29 = buf24; del buf24  # reuse
            # Topologically Sorted Source Nodes: [out_61, out_64, out_67, out_70], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:24
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf29, buf25, buf26, buf27, 881790, 11, stream=stream0)
            buf30 = buf25; del buf25  # reuse
            # Topologically Sorted Source Nodes: [out_73], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:25
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf29, buf30, 510510, 19, stream=stream0)
            buf31 = buf26; del buf26  # reuse
            # Topologically Sorted Source Nodes: [out_73, out_76], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:26
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf29, buf30, buf31, 570570, 17, stream=stream0)
            buf32 = buf27; del buf27  # reuse
            # Topologically Sorted Source Nodes: [out_73, out_76, out_79], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:27
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf29, buf30, buf31, buf32, 746130, 13, stream=stream0)
            buf34 = buf29; del buf29  # reuse
            # Topologically Sorted Source Nodes: [out_73, out_76, out_79, out_82], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:28
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf34, buf30, buf31, buf32, 881790, 11, stream=stream0)
            buf35 = buf30; del buf30  # reuse
            # Topologically Sorted Source Nodes: [out_85], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:29
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf34, buf35, 510510, 19, stream=stream0)
            buf36 = buf31; del buf31  # reuse
            # Topologically Sorted Source Nodes: [out_85, out_88], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:30
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf34, buf35, buf36, 570570, 17, stream=stream0)
            buf37 = buf32; del buf32  # reuse
            # Topologically Sorted Source Nodes: [out_85, out_88, out_91], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:31
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf34, buf35, buf36, buf37, 746130, 13, stream=stream0)
            buf39 = buf34; del buf34  # reuse
            # Topologically Sorted Source Nodes: [out_85, out_88, out_91, out_94], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:32
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf39, buf35, buf36, buf37, 881790, 11, stream=stream0)
            buf40 = buf35; del buf35  # reuse
            # Topologically Sorted Source Nodes: [out_97], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:33
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf39, buf40, 510510, 19, stream=stream0)
            buf41 = buf36; del buf36  # reuse
            # Topologically Sorted Source Nodes: [out_97, out_100], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:34
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf39, buf40, buf41, 570570, 17, stream=stream0)
            buf42 = buf37; del buf37  # reuse
            # Topologically Sorted Source Nodes: [out_97, out_100, out_103], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:35
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf39, buf40, buf41, buf42, 746130, 13, stream=stream0)
            buf44 = buf39; del buf39  # reuse
            # Topologically Sorted Source Nodes: [out_97, out_100, out_103, out_106], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:36
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf44, buf40, buf41, buf42, 881790, 11, stream=stream0)
            buf45 = buf40; del buf40  # reuse
            # Topologically Sorted Source Nodes: [out_109], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:37
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf44, buf45, 510510, 19, stream=stream0)
            buf46 = buf41; del buf41  # reuse
            # Topologically Sorted Source Nodes: [out_109, out_112], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:38
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf44, buf45, buf46, 570570, 17, stream=stream0)
            buf47 = buf42; del buf42  # reuse
            # Topologically Sorted Source Nodes: [out_109, out_112, out_115], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:39
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf44, buf45, buf46, buf47, 746130, 13, stream=stream0)
            buf49 = buf44; del buf44  # reuse
            # Topologically Sorted Source Nodes: [out_109, out_112, out_115, out_118], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:40
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf49, buf45, buf46, buf47, 881790, 11, stream=stream0)
            buf50 = buf45; del buf45  # reuse
            # Topologically Sorted Source Nodes: [out_121], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:41
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf49, buf50, 510510, 19, stream=stream0)
            buf51 = buf46; del buf46  # reuse
            # Topologically Sorted Source Nodes: [out_121, out_124], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:42
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf49, buf50, buf51, 570570, 17, stream=stream0)
            buf52 = buf47; del buf47  # reuse
            # Topologically Sorted Source Nodes: [out_121, out_124, out_127], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:43
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf49, buf50, buf51, buf52, 746130, 13, stream=stream0)
            buf54 = buf49; del buf49  # reuse
            # Topologically Sorted Source Nodes: [out_121, out_124, out_127, out_130], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:44
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf54, buf50, buf51, buf52, 881790, 11, stream=stream0)
            buf55 = buf50; del buf50  # reuse
            # Topologically Sorted Source Nodes: [out_133], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:45
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf54, buf55, 510510, 19, stream=stream0)
            buf56 = buf51; del buf51  # reuse
            # Topologically Sorted Source Nodes: [out_133, out_136], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:46
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf54, buf55, buf56, 570570, 17, stream=stream0)
            buf57 = buf52; del buf52  # reuse
            # Topologically Sorted Source Nodes: [out_133, out_136, out_139], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:47
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf54, buf55, buf56, buf57, 746130, 13, stream=stream0)
            buf59 = buf54; del buf54  # reuse
            # Topologically Sorted Source Nodes: [out_133, out_136, out_139, out_142], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:48
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf59, buf55, buf56, buf57, 881790, 11, stream=stream0)
            buf60 = buf55; del buf55  # reuse
            # Topologically Sorted Source Nodes: [out_145], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:49
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf59, buf60, 510510, 19, stream=stream0)
            buf61 = buf56; del buf56  # reuse
            # Topologically Sorted Source Nodes: [out_145, out_148], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:50
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf59, buf60, buf61, 570570, 17, stream=stream0)
            buf62 = buf57; del buf57  # reuse
            # Topologically Sorted Source Nodes: [out_145, out_148, out_151], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:51
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf59, buf60, buf61, buf62, 746130, 13, stream=stream0)
            buf64 = buf59; del buf59  # reuse
            # Topologically Sorted Source Nodes: [out_145, out_148, out_151, out_154], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:52
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf64, buf60, buf61, buf62, 881790, 11, stream=stream0)
            buf65 = buf60; del buf60  # reuse
            # Topologically Sorted Source Nodes: [out_157], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:53
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf64, buf65, 510510, 19, stream=stream0)
            buf66 = buf61; del buf61  # reuse
            # Topologically Sorted Source Nodes: [out_157, out_160], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:54
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf64, buf65, buf66, 570570, 17, stream=stream0)
            buf67 = buf62; del buf62  # reuse
            # Topologically Sorted Source Nodes: [out_157, out_160, out_163], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:55
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf64, buf65, buf66, buf67, 746130, 13, stream=stream0)
            buf69 = buf64; del buf64  # reuse
            # Topologically Sorted Source Nodes: [out_157, out_160, out_163, out_166], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:56
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf69, buf65, buf66, buf67, 881790, 11, stream=stream0)
            buf70 = buf65; del buf65  # reuse
            # Topologically Sorted Source Nodes: [out_169], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:57
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf69, buf70, 510510, 19, stream=stream0)
            buf71 = buf66; del buf66  # reuse
            # Topologically Sorted Source Nodes: [out_169, out_172], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:58
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf69, buf70, buf71, 570570, 17, stream=stream0)
            buf72 = buf67; del buf67  # reuse
            # Topologically Sorted Source Nodes: [out_169, out_172, out_175], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:59
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf69, buf70, buf71, buf72, 746130, 13, stream=stream0)
            buf74 = buf69; del buf69  # reuse
            # Topologically Sorted Source Nodes: [out_169, out_172, out_175, out_178], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:60
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf74, buf70, buf71, buf72, 881790, 11, stream=stream0)
            buf75 = buf70; del buf70  # reuse
            # Topologically Sorted Source Nodes: [out_181], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:61
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf74, buf75, 510510, 19, stream=stream0)
            buf76 = buf71; del buf71  # reuse
            # Topologically Sorted Source Nodes: [out_181, out_184], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:62
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf74, buf75, buf76, 570570, 17, stream=stream0)
            buf77 = buf72; del buf72  # reuse
            # Topologically Sorted Source Nodes: [out_181, out_184, out_187], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:63
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf74, buf75, buf76, buf77, 746130, 13, stream=stream0)
            buf79 = buf74; del buf74  # reuse
            # Topologically Sorted Source Nodes: [out_181, out_184, out_187, out_190], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:64
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf79, buf75, buf76, buf77, 881790, 11, stream=stream0)
            buf80 = buf75; del buf75  # reuse
            # Topologically Sorted Source Nodes: [out_193], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:65
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf79, buf80, 510510, 19, stream=stream0)
            buf81 = buf76; del buf76  # reuse
            # Topologically Sorted Source Nodes: [out_193, out_196], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:66
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf79, buf80, buf81, 570570, 17, stream=stream0)
            buf82 = buf77; del buf77  # reuse
            # Topologically Sorted Source Nodes: [out_193, out_196, out_199], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:67
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf79, buf80, buf81, buf82, 746130, 13, stream=stream0)
            buf84 = buf79; del buf79  # reuse
            # Topologically Sorted Source Nodes: [out_193, out_196, out_199, out_202], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:68
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf84, buf80, buf81, buf82, 881790, 11, stream=stream0)
            buf85 = buf80; del buf80  # reuse
            # Topologically Sorted Source Nodes: [out_205], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:69
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf84, buf85, 510510, 19, stream=stream0)
            buf86 = buf81; del buf81  # reuse
            # Topologically Sorted Source Nodes: [out_205, out_208], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:70
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf84, buf85, buf86, 570570, 17, stream=stream0)
            buf87 = buf82; del buf82  # reuse
            # Topologically Sorted Source Nodes: [out_205, out_208, out_211], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:71
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf84, buf85, buf86, buf87, 746130, 13, stream=stream0)
            buf89 = buf84; del buf84  # reuse
            # Topologically Sorted Source Nodes: [out_205, out_208, out_211, out_214], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:72
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf89, buf85, buf86, buf87, 881790, 11, stream=stream0)
            buf90 = buf85; del buf85  # reuse
            # Topologically Sorted Source Nodes: [out_217], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:73
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf89, buf90, 510510, 19, stream=stream0)
            buf91 = buf86; del buf86  # reuse
            # Topologically Sorted Source Nodes: [out_217, out_220], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:74
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf89, buf90, buf91, 570570, 17, stream=stream0)
            buf92 = buf87; del buf87  # reuse
            # Topologically Sorted Source Nodes: [out_217, out_220, out_223], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:75
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf89, buf90, buf91, buf92, 746130, 13, stream=stream0)
            buf94 = buf89; del buf89  # reuse
            # Topologically Sorted Source Nodes: [out_217, out_220, out_223, out_226], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:76
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf94, buf90, buf91, buf92, 881790, 11, stream=stream0)
            buf95 = buf90; del buf90  # reuse
            # Topologically Sorted Source Nodes: [out_229], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:77
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf94, buf95, 510510, 19, stream=stream0)
            buf96 = buf91; del buf91  # reuse
            # Topologically Sorted Source Nodes: [out_229, out_232], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:78
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf94, buf95, buf96, 570570, 17, stream=stream0)
            buf97 = buf92; del buf92  # reuse
            # Topologically Sorted Source Nodes: [out_229, out_232, out_235], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:79
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf94, buf95, buf96, buf97, 746130, 13, stream=stream0)
            buf99 = buf94; del buf94  # reuse
            # Topologically Sorted Source Nodes: [out_229, out_232, out_235, out_238], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:80
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf99, buf95, buf96, buf97, 881790, 11, stream=stream0)
            buf100 = buf95; del buf95  # reuse
            # Topologically Sorted Source Nodes: [out_241], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:81
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf99, buf100, 510510, 19, stream=stream0)
            buf101 = buf96; del buf96  # reuse
            # Topologically Sorted Source Nodes: [out_241, out_244], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:82
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf99, buf100, buf101, 570570, 17, stream=stream0)
            buf102 = buf97; del buf97  # reuse
            # Topologically Sorted Source Nodes: [out_241, out_244, out_247], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:83
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf99, buf100, buf101, buf102, 746130, 13, stream=stream0)
            buf104 = buf99; del buf99  # reuse
            # Topologically Sorted Source Nodes: [out_241, out_244, out_247, out_250], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:84
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf104, buf100, buf101, buf102, 881790, 11, stream=stream0)
            buf105 = buf100; del buf100  # reuse
            # Topologically Sorted Source Nodes: [out_253], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:85
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf104, buf105, 510510, 19, stream=stream0)
            buf106 = buf101; del buf101  # reuse
            # Topologically Sorted Source Nodes: [out_253, out_256], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:86
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf104, buf105, buf106, 570570, 17, stream=stream0)
            buf107 = buf102; del buf102  # reuse
            # Topologically Sorted Source Nodes: [out_253, out_256, out_259], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:87
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf104, buf105, buf106, buf107, 746130, 13, stream=stream0)
            buf109 = buf104; del buf104  # reuse
            # Topologically Sorted Source Nodes: [out_253, out_256, out_259, out_262], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:88
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf109, buf105, buf106, buf107, 881790, 11, stream=stream0)
            buf110 = buf105; del buf105  # reuse
            # Topologically Sorted Source Nodes: [out_265], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:89
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf109, buf110, 510510, 19, stream=stream0)
            buf111 = buf106; del buf106  # reuse
            # Topologically Sorted Source Nodes: [out_265, out_268], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:90
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf109, buf110, buf111, 570570, 17, stream=stream0)
            buf112 = buf107; del buf107  # reuse
            # Topologically Sorted Source Nodes: [out_265, out_268, out_271], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:91
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf109, buf110, buf111, buf112, 746130, 13, stream=stream0)
            buf114 = buf109; del buf109  # reuse
            # Topologically Sorted Source Nodes: [out_265, out_268, out_271, out_274], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:92
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf114, buf110, buf111, buf112, 881790, 11, stream=stream0)
            buf115 = buf110; del buf110  # reuse
            # Topologically Sorted Source Nodes: [out_277], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:93
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf114, buf115, 510510, 19, stream=stream0)
            buf116 = buf111; del buf111  # reuse
            # Topologically Sorted Source Nodes: [out_277, out_280], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:94
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf114, buf115, buf116, 570570, 17, stream=stream0)
            buf117 = buf112; del buf112  # reuse
            # Topologically Sorted Source Nodes: [out_277, out_280, out_283], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:95
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf114, buf115, buf116, buf117, 746130, 13, stream=stream0)
            buf119 = buf114; del buf114  # reuse
            # Topologically Sorted Source Nodes: [out_277, out_280, out_283, out_286], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7:96
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_7.run(buf119, buf115, buf116, buf117, 881790, 11, stream=stream0)
            buf120 = buf115; del buf115  # reuse
            # Topologically Sorted Source Nodes: [out_289], Original ATen: [aten.linalg_vector_norm]
            # [Provenance debug handles] triton_per_fused_linalg_vector_norm_4:97
            stream0 = get_raw_stream(0)
            triton_per_fused_linalg_vector_norm_4.run(buf119, buf120, 510510, 19, stream=stream0)
            buf121 = buf116; del buf116  # reuse
            # Topologically Sorted Source Nodes: [out_289, out_292], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5:98
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_5.run(buf119, buf120, buf121, 570570, 17, stream=stream0)
            buf122 = buf117; del buf117  # reuse
            # Topologically Sorted Source Nodes: [out_289, out_292, out_295], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6:99
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_6.run(buf119, buf120, buf121, buf122, 746130, 13, stream=stream0)
            buf124 = empty_strided_cuda((19, 17, 13, 11, 7, 5, 3, 2), (510510, 30030, 2310, 210, 30, 6, 2, 1), torch.float32)
            # Topologically Sorted Source Nodes: [out_289, out_292, out_295, out_298], Original ATen: [aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_8:100
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_8.run(buf119, buf120, buf121, buf122, buf124, 881790, 11, stream=stream0)
            del buf119
            del buf120
            del buf121
            del buf122
        return (reinterpret_tensor(buf124, (2, 3, 5, 7, 11, 13, 17, 19), (4849845, 1616615, 323323, 46189, 4199, 323, 19, 1), 0), )

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
