# ===== Subgraph 0 (model__0) =====

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


# kernel path: /tmp/torchinductor_root/hq/chq6torcl76ddwn643qy4mxluosp6nm6lzxr4uxnhmdb6tikxljh.py
# Topologically Sorted Source Nodes: [out, out_1], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
# Source node to ATen node mapping:
#   out => view
#   out_1 => clamp_min, div, expand, pow_1, pow_2, sum_1
# Graph fragment:
#   %arg0_1 : Tensor "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = PlaceHolder[target=arg0_1]
#   %sum_1 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][516256, 30368, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_1]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %pow_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%view, 2.0), kwargs = {})
#   %sum_1 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_1, [0], True), kwargs = {})
#   %pow_2 : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_1, 0.5), kwargs = {})
#   %clamp_min : Tensor "f32[1, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_2, 1e-12), kwargs = {})
#   %expand : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][0, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.div.Tensor](args = (%view, %expand), kwargs = {})
#   return %sum_1,%div
triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0 = async_compile.triton('triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0', '''
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
    triton_meta={'signature': {'in_ptr0': '*fp32', 'out_ptr1': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 1, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 116396280, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0(in_ptr0, out_ptr1, xnumel, r0_numel, XBLOCK : tl.constexpr):
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
    tmp6 = tl.sqrt_rn(tmp5)
    tmp7 = tl.full([1, 1], 1e-12, tl.float32)
    tmp8 = triton_helpers.maximum(tmp6, tmp7)
    tmp9 = (tmp0 / tmp8)
    tl.store(out_ptr1 + (x3 + 510510*r0_2), tmp9, r0_mask & xmask)
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
            # Topologically Sorted Source Nodes: [out, out_1], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0:1
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0.run(arg0_1, buf1, 510510, 19, stream=stream0)
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


# ===== Subgraph 1 (model__1) =====

# AOT ID: ['1_inference']
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


# kernel path: /tmp/torchinductor_root/hx/chx2l4oxvbri7utp2ht7qybpvppdrbyu7vvddmwlwdmfaizopflq.py
# Topologically Sorted Source Nodes: [out, out_1], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
# Source node to ATen node mapping:
#   out => view
#   out_1 => clamp_min, div, expand, pow_1, pow_2, sum_1
# Graph fragment:
#   %arg0_1 : Tensor "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = PlaceHolder[target=arg0_1]
#   %sum_1 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30368, 576992, 2336, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_1]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %pow_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%view, 2.0), kwargs = {})
#   %sum_1 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_1, [1], True), kwargs = {})
#   %pow_2 : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_1, 0.5), kwargs = {})
#   %clamp_min : Tensor "f32[19, 1, 13, 11, 7, 5, 3, 2][30030, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_2, 1e-12), kwargs = {})
#   %expand : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][30030, 0, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.div.Tensor](args = (%view, %expand), kwargs = {})
#   return %sum_1,%div
triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0 = async_compile.triton('triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0', '''
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
    triton_meta={'signature': {'in_ptr0': '*fp32', 'out_ptr1': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 1, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 116396280, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0(in_ptr0, out_ptr1, xnumel, r0_numel, XBLOCK : tl.constexpr):
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
    x5 = xindex // 2310
    tmp0 = tl.load(in_ptr0 + (x4 + 30030*r0_3 + 510510*x2), r0_mask & xmask, other=0.0)
    tmp1 = tmp0 * tmp0
    tmp2 = tl.broadcast_to(tmp1, [XBLOCK, R0_BLOCK])
    tmp4 = tl.where(r0_mask & xmask, tmp2, 0)
    tmp5 = tl.sum(tmp4, 1)[:, None].to(tl.float32)
    tmp6 = tl.sqrt_rn(tmp5)
    tmp7 = tl.full([1, 1], 1e-12, tl.float32)
    tmp8 = triton_helpers.maximum(tmp6, tmp7)
    tmp9 = (tmp0 / tmp8)
    tl.store(out_ptr1 + (x4 + 30030*r0_3 + 510510*x2), tmp9, r0_mask & xmask)
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
            # Topologically Sorted Source Nodes: [out, out_1], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0:1
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0.run(arg0_1, buf1, 570570, 17, stream=stream0)
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


# ===== Subgraph 2 (model__2) =====

# AOT ID: ['2_inference']
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


# kernel path: /tmp/torchinductor_root/rn/crnia7duyvjsvll36u2hjtvkxh644qsmtcocax4rz24jfl6momu2.py
# Topologically Sorted Source Nodes: [out, out_1], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
# Source node to ATen node mapping:
#   out => view
#   out_1 => clamp_min, div, expand, pow_1, pow_2, sum_1
# Graph fragment:
#   %arg0_1 : Tensor "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = PlaceHolder[target=arg0_1]
#   %sum_1 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39712, 2336, 754528, 210, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_1]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %pow_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%view, 2.0), kwargs = {})
#   %sum_1 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39270, 2310, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_1, [2], True), kwargs = {})
#   %pow_2 : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39270, 2310, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_1, 0.5), kwargs = {})
#   %clamp_min : Tensor "f32[19, 17, 1, 11, 7, 5, 3, 2][39270, 2310, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_2, 1e-12), kwargs = {})
#   %expand : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][39270, 2310, 0, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.div.Tensor](args = (%view, %expand), kwargs = {})
#   return %sum_1,%div
triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0 = async_compile.triton('triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0', '''
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
    triton_meta={'signature': {'in_ptr0': '*fp32', 'out_ptr1': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 1, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 116396280, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0(in_ptr0, out_ptr1, xnumel, r0_numel, XBLOCK : tl.constexpr):
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
    r0_2 = r0_index
    x0 = (xindex % 2310)
    x1 = xindex // 2310
    tmp0 = tl.load(in_ptr0 + (x0 + 2310*r0_2 + 30030*x1), r0_mask & xmask, other=0.0)
    tmp1 = tmp0 * tmp0
    tmp2 = tl.broadcast_to(tmp1, [XBLOCK, R0_BLOCK])
    tmp4 = tl.where(r0_mask & xmask, tmp2, 0)
    tmp5 = tl.sum(tmp4, 1)[:, None].to(tl.float32)
    tmp6 = tl.sqrt_rn(tmp5)
    tmp7 = tl.full([1, 1], 1e-12, tl.float32)
    tmp8 = triton_helpers.maximum(tmp6, tmp7)
    tmp9 = (tmp0 / tmp8)
    tl.store(out_ptr1 + (x0 + 2310*r0_2 + 30030*x1), tmp9, r0_mask & xmask)
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
            # Topologically Sorted Source Nodes: [out, out_1], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0:1
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0.run(arg0_1, buf1, 746130, 13, stream=stream0)
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


# ===== Subgraph 3 (model__3) =====

# AOT ID: ['3_inference']
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


# kernel path: /tmp/torchinductor_root/qf/cqfbrzsiwrgzeqquxxuwdnanuhp3qe42aliq7djhdzgfhaeuibro.py
# Topologically Sorted Source Nodes: [out, out_1], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
# Source node to ATen node mapping:
#   out => view
#   out_1 => clamp_min, div, expand, pow_1, pow_2, sum_1
# Graph fragment:
#   %arg0_1 : Tensor "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0" = PlaceHolder[target=arg0_1]
#   %sum_1 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46784, 2752, 210, 888896, 30, 6, 2, 1]cuda:0" = PlaceHolder[target=sum_1]
#   %view : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=2] = call_function[target=torch.ops.aten.reshape.default](args = (%arg0_1, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %pow_1 : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%view, 2.0), kwargs = {})
#   %sum_1 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46410, 2730, 210, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.sum.dim_IntList](args = (%pow_1, [3], True), kwargs = {})
#   %pow_2 : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46410, 2730, 210, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.pow.Tensor_Scalar](args = (%sum_1, 0.5), kwargs = {})
#   %clamp_min : Tensor "f32[19, 17, 13, 1, 7, 5, 3, 2][46410, 2730, 210, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.clamp_min.default](args = (%pow_2, 1e-12), kwargs = {})
#   %expand : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][46410, 2730, 210, 0, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.expand.default](args = (%clamp_min, [19, 17, 13, 11, 7, 5, 3, 2]), kwargs = {})
#   %div : Tensor "f32[19, 17, 13, 11, 7, 5, 3, 2][510510, 30030, 2310, 210, 30, 6, 2, 1]cuda:0"[num_users=1] = call_function[target=torch.ops.aten.div.Tensor](args = (%view, %expand), kwargs = {})
#   return %sum_1,%div
triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0 = async_compile.triton('triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0', '''
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
    triton_meta={'signature': {'in_ptr0': '*fp32', 'out_ptr1': '*fp32', 'xnumel': 'i32', 'r0_numel': 'i32', 'XBLOCK': 'constexpr'}, 'device': DeviceProperties(type='cuda', index=0, multi_processor_count=152, cc=100, major=10, regs_per_multiprocessor=65536, max_threads_per_multi_processor=2048, max_threads_per_block=1024, warp_size=32), 'constants': {}, 'native_matmul': False, 'enable_fp_fusion': True, 'launch_pdl': False, 'disable_ftz': False, 'configs': [{(0,): [['tt.divisibility', 16]], (1,): [['tt.divisibility', 16]]}]},
    inductor_meta={'grid_type': 'Grid1D', 'autotune_hints': set(), 'kernel_name': 'triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0', 'mutated_arg_names': [], 'optimize_mem': True, 'no_x_dim': None, 'atomic_add_found': False, 'num_load': 1, 'num_store': 1, 'num_reduction': 1, 'backend_hash': '46CDC24F34A1D23B3D54F4CFD93984714DE23DAB6D213E9C1EFCA195D44804B7', 'assert_indirect_indexing': True, 'autotune_local_cache': True, 'autotune_pointwise': True, 'autotune_remote_cache': None, 'force_disable_caches': False, 'dynamic_scale_rblock': True, 'max_autotune': False, 'max_autotune_pointwise': False, 'min_split_scan_rblock': 256, 'spill_threshold': 16, 'store_cubin': False, 'deterministic': False, 'force_filter_reduction_configs': False, 'are_deterministic_algorithms_enabled': False, 'tiling_scores': {'x': 116396280, 'r0_': 0}}
)
@triton.jit
def triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0(in_ptr0, out_ptr1, xnumel, r0_numel, XBLOCK : tl.constexpr):
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
    r0_3 = r0_index
    x0 = (xindex % 210)
    x4 = xindex // 210
    x2 = xindex // 2730
    x5 = (xindex % 2730)
    tmp0 = tl.load(in_ptr0 + (x0 + 210*r0_3 + 2310*x4), r0_mask & xmask, other=0.0)
    tmp1 = tmp0 * tmp0
    tmp2 = tl.broadcast_to(tmp1, [XBLOCK, R0_BLOCK])
    tmp4 = tl.where(r0_mask & xmask, tmp2, 0)
    tmp5 = tl.sum(tmp4, 1)[:, None].to(tl.float32)
    tmp6 = tl.sqrt_rn(tmp5)
    tmp7 = tl.full([1, 1], 1e-12, tl.float32)
    tmp8 = triton_helpers.maximum(tmp6, tmp7)
    tmp9 = (tmp0 / tmp8)
    tl.store(out_ptr1 + (x0 + 210*r0_3 + 2310*x4), tmp9, r0_mask & xmask)
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
            # Topologically Sorted Source Nodes: [out, out_1], Original ATen: [aten.view, aten.linalg_vector_norm, aten.clamp_min, aten.expand, aten.div]
            # [Provenance debug handles] triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0:1
            stream0 = get_raw_stream(0)
            triton_per_fused_clamp_min_div_expand_linalg_vector_norm_view_0.run(arg0_1, buf1, 881790, 11, stream=stream0)
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


