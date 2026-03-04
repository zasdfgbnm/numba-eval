# Auto-generated Dynamo guard conditions for method1.2
# 100 compiled frame(s)

# === Frame 0: _method1_2_inner ===
# file: method1.2/run.py  firstlineno: 1
#
# CacheEntry 0, compile_id=0/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['tensor'], accessed_by=FrameLocalsGuardAccessor(key='tensor', framelocals_idx=0), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['tensor'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:3 in _method1_2_inner
#   | | +- NO_HASATTR: hasattr(L['tensor'], '_dynamo_dynamic_indices') == False      #   # method1.2/run.py:3 in _method1_2_inner
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  # from benchmark import time_cpu  # type: ignore[import-not-found]  # method1.2/run.py:6 in _method1_2_inner
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  # from benchmark import time_cpu  # type: ignore[import-not-found]  # method1.2/run.py:6 in _method1_2_inner
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  # from benchmark import time_cpu  # type: ignore[import-not-found]  # method1.2/run.py:6 in _method1_2_inner
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['tensor'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['tensor'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 1: torch_dynamo_resume_in__method1_2_inner_at_6 ===
# file: method1.2/run.py  firstlineno: 6
#
# CacheEntry 0, compile_id=1/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:7 in torch_dynamo_resume_in__method1_2_inner_at_6
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:7 in torch_dynamo_resume_in__method1_2_inner_at_6
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  # # (Dynamo does not support graph_break inside a for/while loop).  # method1.2/run.py:10 in torch_dynamo_resume_in__method1_2_inner_at_6
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  # # (Dynamo does not support graph_break inside a for/while loop).  # method1.2/run.py:10 in torch_dynamo_resume_in__method1_2_inner_at_6
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  # # (Dynamo does not support graph_break inside a for/while loop).  # method1.2/run.py:10 in torch_dynamo_resume_in__method1_2_inner_at_6
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 2: torch_dynamo_resume_in__method1_2_inner_at_10 ===
# file: method1.2/run.py  firstlineno: 10
#
# CacheEntry 0, compile_id=2/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  # _lines = ["def _method1_2_inner(tensor):"]  # method1.2/run.py:11 in torch_dynamo_resume_in__method1_2_inner_at_10
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         # _lines = ["def _method1_2_inner(tensor):"]  # method1.2/run.py:11 in torch_dynamo_resume_in__method1_2_inner_at_10
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  # _lines.append("    out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)")  # method1.2/run.py:14 in torch_dynamo_resume_in__method1_2_inner_at_10
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  # _lines.append("    out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)")  # method1.2/run.py:14 in torch_dynamo_resume_in__method1_2_inner_at_10
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  # _lines.append("    out = out.reshape(19, 17, 13, 11, 7, 5, 3, 2)")  # method1.2/run.py:14 in torch_dynamo_resume_in__method1_2_inner_at_10
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 3: torch_dynamo_resume_in__method1_2_inner_at_14 ===
# file: method1.2/run.py  firstlineno: 14
#
# CacheEntry 0, compile_id=3/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  # _lines.append("    out = out.add(0)")  # method1.2/run.py:15 in torch_dynamo_resume_in__method1_2_inner_at_14
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         # _lines.append("    out = out.add(0)")  # method1.2/run.py:15 in torch_dynamo_resume_in__method1_2_inner_at_14
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  # _lines.append("    return out")  # method1.2/run.py:18 in torch_dynamo_resume_in__method1_2_inner_at_14
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  # _lines.append("    return out")  # method1.2/run.py:18 in torch_dynamo_resume_in__method1_2_inner_at_14
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  # _lines.append("    return out")  # method1.2/run.py:18 in torch_dynamo_resume_in__method1_2_inner_at_14
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 4: torch_dynamo_resume_in__method1_2_inner_at_18 ===
# file: method1.2/run.py  firstlineno: 18
#
# CacheEntry 0, compile_id=4/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  # exec(compile("\n".join(_lines), __file__, "exec"))  # method1.2/run.py:19 in torch_dynamo_resume_in__method1_2_inner_at_18
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         # exec(compile("\n".join(_lines), __file__, "exec"))  # method1.2/run.py:19 in torch_dynamo_resume_in__method1_2_inner_at_18
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:22 in torch_dynamo_resume_in__method1_2_inner_at_18
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:22 in torch_dynamo_resume_in__method1_2_inner_at_18
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:22 in torch_dynamo_resume_in__method1_2_inner_at_18
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 5: torch_dynamo_resume_in__method1_2_inner_at_22 ===
# file: method1.2/run.py  firstlineno: 22
#
# CacheEntry 0, compile_id=5/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:23 in torch_dynamo_resume_in__method1_2_inner_at_22
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:23 in torch_dynamo_resume_in__method1_2_inner_at_22
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:26 in torch_dynamo_resume_in__method1_2_inner_at_22
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:26 in torch_dynamo_resume_in__method1_2_inner_at_22
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:26 in torch_dynamo_resume_in__method1_2_inner_at_22
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 6: torch_dynamo_resume_in__method1_2_inner_at_26 ===
# file: method1.2/run.py  firstlineno: 26
#
# CacheEntry 0, compile_id=6/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:27 in torch_dynamo_resume_in__method1_2_inner_at_26
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:27 in torch_dynamo_resume_in__method1_2_inner_at_26
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  # parser.add_argument("--device", default="cuda")  # method1.2/run.py:30 in torch_dynamo_resume_in__method1_2_inner_at_26
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  # parser.add_argument("--device", default="cuda")  # method1.2/run.py:30 in torch_dynamo_resume_in__method1_2_inner_at_26
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  # parser.add_argument("--device", default="cuda")  # method1.2/run.py:30 in torch_dynamo_resume_in__method1_2_inner_at_26
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 7: torch_dynamo_resume_in__method1_2_inner_at_30 ===
# file: method1.2/run.py  firstlineno: 30
#
# CacheEntry 0, compile_id=7/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  # args = parser.parse_args()  # method1.2/run.py:31 in torch_dynamo_resume_in__method1_2_inner_at_30
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         # args = parser.parse_args()  # method1.2/run.py:31 in torch_dynamo_resume_in__method1_2_inner_at_30
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  # tensor = torch.empty((2, 3, 5, 7, 11, 13, 17, 19), device=device, dtype=torch.float32)  # method1.2/run.py:34 in torch_dynamo_resume_in__method1_2_inner_at_30
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  # tensor = torch.empty((2, 3, 5, 7, 11, 13, 17, 19), device=device, dtype=torch.float32)  # method1.2/run.py:34 in torch_dynamo_resume_in__method1_2_inner_at_30
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  # tensor = torch.empty((2, 3, 5, 7, 11, 13, 17, 19), device=device, dtype=torch.float32)  # method1.2/run.py:34 in torch_dynamo_resume_in__method1_2_inner_at_30
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 8: torch_dynamo_resume_in__method1_2_inner_at_34 ===
# file: method1.2/run.py  firstlineno: 34
#
# CacheEntry 0, compile_id=8/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:35 in torch_dynamo_resume_in__method1_2_inner_at_34
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:35 in torch_dynamo_resume_in__method1_2_inner_at_34
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:38 in torch_dynamo_resume_in__method1_2_inner_at_34
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:38 in torch_dynamo_resume_in__method1_2_inner_at_34
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:38 in torch_dynamo_resume_in__method1_2_inner_at_34
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 9: torch_dynamo_resume_in__method1_2_inner_at_38 ===
# file: method1.2/run.py  firstlineno: 38
#
# CacheEntry 0, compile_id=9/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  # seconds = time_cpu(op, 1)  # method1.2/run.py:39 in torch_dynamo_resume_in__method1_2_inner_at_38
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         # seconds = time_cpu(op, 1)  # method1.2/run.py:39 in torch_dynamo_resume_in__method1_2_inner_at_38
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  # print(json.dumps(result, indent=2))  # method1.2/run.py:42 in torch_dynamo_resume_in__method1_2_inner_at_38
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  # print(json.dumps(result, indent=2))  # method1.2/run.py:42 in torch_dynamo_resume_in__method1_2_inner_at_38
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  # print(json.dumps(result, indent=2))  # method1.2/run.py:42 in torch_dynamo_resume_in__method1_2_inner_at_38
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 10: torch_dynamo_resume_in__method1_2_inner_at_42 ===
# file: method1.2/run.py  firstlineno: 42
#
# CacheEntry 0, compile_id=10/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:43 in torch_dynamo_resume_in__method1_2_inner_at_42
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:43 in torch_dynamo_resume_in__method1_2_inner_at_42
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  # main()  # method1.2/run.py:46 in torch_dynamo_resume_in__method1_2_inner_at_42
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  # main()  # method1.2/run.py:46 in torch_dynamo_resume_in__method1_2_inner_at_42
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  # main()  # method1.2/run.py:46 in torch_dynamo_resume_in__method1_2_inner_at_42
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 11: torch_dynamo_resume_in__method1_2_inner_at_46 ===
# file: method1.2/run.py  firstlineno: 46
#
# CacheEntry 0, compile_id=11/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:47 in torch_dynamo_resume_in__method1_2_inner_at_46
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:47 in torch_dynamo_resume_in__method1_2_inner_at_46
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:50 in torch_dynamo_resume_in__method1_2_inner_at_46
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:50 in torch_dynamo_resume_in__method1_2_inner_at_46
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:50 in torch_dynamo_resume_in__method1_2_inner_at_46
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 12: torch_dynamo_resume_in__method1_2_inner_at_50 ===
# file: method1.2/run.py  firstlineno: 50
#
# CacheEntry 0, compile_id=12/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:51 in torch_dynamo_resume_in__method1_2_inner_at_50
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:51 in torch_dynamo_resume_in__method1_2_inner_at_50
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:54 in torch_dynamo_resume_in__method1_2_inner_at_50
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:54 in torch_dynamo_resume_in__method1_2_inner_at_50
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:54 in torch_dynamo_resume_in__method1_2_inner_at_50
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 13: torch_dynamo_resume_in__method1_2_inner_at_54 ===
# file: method1.2/run.py  firstlineno: 54
#
# CacheEntry 0, compile_id=13/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:55 in torch_dynamo_resume_in__method1_2_inner_at_54
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:55 in torch_dynamo_resume_in__method1_2_inner_at_54
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:58 in torch_dynamo_resume_in__method1_2_inner_at_54
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:58 in torch_dynamo_resume_in__method1_2_inner_at_54
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:58 in torch_dynamo_resume_in__method1_2_inner_at_54
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 14: torch_dynamo_resume_in__method1_2_inner_at_58 ===
# file: method1.2/run.py  firstlineno: 58
#
# CacheEntry 0, compile_id=14/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:59 in torch_dynamo_resume_in__method1_2_inner_at_58
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:59 in torch_dynamo_resume_in__method1_2_inner_at_58
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:62 in torch_dynamo_resume_in__method1_2_inner_at_58
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:62 in torch_dynamo_resume_in__method1_2_inner_at_58
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:62 in torch_dynamo_resume_in__method1_2_inner_at_58
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 15: torch_dynamo_resume_in__method1_2_inner_at_62 ===
# file: method1.2/run.py  firstlineno: 62
#
# CacheEntry 0, compile_id=15/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:63 in torch_dynamo_resume_in__method1_2_inner_at_62
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:63 in torch_dynamo_resume_in__method1_2_inner_at_62
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:66 in torch_dynamo_resume_in__method1_2_inner_at_62
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:66 in torch_dynamo_resume_in__method1_2_inner_at_62
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:66 in torch_dynamo_resume_in__method1_2_inner_at_62
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 16: torch_dynamo_resume_in__method1_2_inner_at_66 ===
# file: method1.2/run.py  firstlineno: 66
#
# CacheEntry 0, compile_id=16/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:67 in torch_dynamo_resume_in__method1_2_inner_at_66
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:67 in torch_dynamo_resume_in__method1_2_inner_at_66
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:70 in torch_dynamo_resume_in__method1_2_inner_at_66
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:70 in torch_dynamo_resume_in__method1_2_inner_at_66
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:70 in torch_dynamo_resume_in__method1_2_inner_at_66
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 17: torch_dynamo_resume_in__method1_2_inner_at_70 ===
# file: method1.2/run.py  firstlineno: 70
#
# CacheEntry 0, compile_id=17/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:71 in torch_dynamo_resume_in__method1_2_inner_at_70
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:71 in torch_dynamo_resume_in__method1_2_inner_at_70
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:74 in torch_dynamo_resume_in__method1_2_inner_at_70
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:74 in torch_dynamo_resume_in__method1_2_inner_at_70
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:74 in torch_dynamo_resume_in__method1_2_inner_at_70
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 18: torch_dynamo_resume_in__method1_2_inner_at_74 ===
# file: method1.2/run.py  firstlineno: 74
#
# CacheEntry 0, compile_id=18/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:75 in torch_dynamo_resume_in__method1_2_inner_at_74
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:75 in torch_dynamo_resume_in__method1_2_inner_at_74
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:78 in torch_dynamo_resume_in__method1_2_inner_at_74
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:78 in torch_dynamo_resume_in__method1_2_inner_at_74
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:78 in torch_dynamo_resume_in__method1_2_inner_at_74
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 19: torch_dynamo_resume_in__method1_2_inner_at_78 ===
# file: method1.2/run.py  firstlineno: 78
#
# CacheEntry 0, compile_id=19/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:79 in torch_dynamo_resume_in__method1_2_inner_at_78
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:79 in torch_dynamo_resume_in__method1_2_inner_at_78
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:82 in torch_dynamo_resume_in__method1_2_inner_at_78
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:82 in torch_dynamo_resume_in__method1_2_inner_at_78
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:82 in torch_dynamo_resume_in__method1_2_inner_at_78
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 20: torch_dynamo_resume_in__method1_2_inner_at_82 ===
# file: method1.2/run.py  firstlineno: 82
#
# CacheEntry 0, compile_id=20/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:83 in torch_dynamo_resume_in__method1_2_inner_at_82
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:83 in torch_dynamo_resume_in__method1_2_inner_at_82
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:86 in torch_dynamo_resume_in__method1_2_inner_at_82
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:86 in torch_dynamo_resume_in__method1_2_inner_at_82
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:86 in torch_dynamo_resume_in__method1_2_inner_at_82
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 21: torch_dynamo_resume_in__method1_2_inner_at_86 ===
# file: method1.2/run.py  firstlineno: 86
#
# CacheEntry 0, compile_id=21/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:87 in torch_dynamo_resume_in__method1_2_inner_at_86
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:87 in torch_dynamo_resume_in__method1_2_inner_at_86
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:90 in torch_dynamo_resume_in__method1_2_inner_at_86
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:90 in torch_dynamo_resume_in__method1_2_inner_at_86
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:90 in torch_dynamo_resume_in__method1_2_inner_at_86
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 22: torch_dynamo_resume_in__method1_2_inner_at_90 ===
# file: method1.2/run.py  firstlineno: 90
#
# CacheEntry 0, compile_id=22/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:91 in torch_dynamo_resume_in__method1_2_inner_at_90
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:91 in torch_dynamo_resume_in__method1_2_inner_at_90
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:94 in torch_dynamo_resume_in__method1_2_inner_at_90
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:94 in torch_dynamo_resume_in__method1_2_inner_at_90
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:94 in torch_dynamo_resume_in__method1_2_inner_at_90
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 23: torch_dynamo_resume_in__method1_2_inner_at_94 ===
# file: method1.2/run.py  firstlineno: 94
#
# CacheEntry 0, compile_id=23/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:95 in torch_dynamo_resume_in__method1_2_inner_at_94
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:95 in torch_dynamo_resume_in__method1_2_inner_at_94
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:98 in torch_dynamo_resume_in__method1_2_inner_at_94
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:98 in torch_dynamo_resume_in__method1_2_inner_at_94
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:98 in torch_dynamo_resume_in__method1_2_inner_at_94
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 24: torch_dynamo_resume_in__method1_2_inner_at_98 ===
# file: method1.2/run.py  firstlineno: 98
#
# CacheEntry 0, compile_id=24/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:99 in torch_dynamo_resume_in__method1_2_inner_at_98
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:99 in torch_dynamo_resume_in__method1_2_inner_at_98
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:102 in torch_dynamo_resume_in__method1_2_inner_at_98
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:102 in torch_dynamo_resume_in__method1_2_inner_at_98
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:102 in torch_dynamo_resume_in__method1_2_inner_at_98
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 25: torch_dynamo_resume_in__method1_2_inner_at_102 ===
# file: method1.2/run.py  firstlineno: 102
#
# CacheEntry 0, compile_id=25/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:103 in torch_dynamo_resume_in__method1_2_inner_at_102
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:103 in torch_dynamo_resume_in__method1_2_inner_at_102
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:106 in torch_dynamo_resume_in__method1_2_inner_at_102
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:106 in torch_dynamo_resume_in__method1_2_inner_at_102
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:106 in torch_dynamo_resume_in__method1_2_inner_at_102
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 26: torch_dynamo_resume_in__method1_2_inner_at_106 ===
# file: method1.2/run.py  firstlineno: 106
#
# CacheEntry 0, compile_id=26/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:107 in torch_dynamo_resume_in__method1_2_inner_at_106
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:107 in torch_dynamo_resume_in__method1_2_inner_at_106
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:110 in torch_dynamo_resume_in__method1_2_inner_at_106
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:110 in torch_dynamo_resume_in__method1_2_inner_at_106
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:110 in torch_dynamo_resume_in__method1_2_inner_at_106
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 27: torch_dynamo_resume_in__method1_2_inner_at_110 ===
# file: method1.2/run.py  firstlineno: 110
#
# CacheEntry 0, compile_id=27/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:111 in torch_dynamo_resume_in__method1_2_inner_at_110
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:111 in torch_dynamo_resume_in__method1_2_inner_at_110
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:114 in torch_dynamo_resume_in__method1_2_inner_at_110
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:114 in torch_dynamo_resume_in__method1_2_inner_at_110
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:114 in torch_dynamo_resume_in__method1_2_inner_at_110
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 28: torch_dynamo_resume_in__method1_2_inner_at_114 ===
# file: method1.2/run.py  firstlineno: 114
#
# CacheEntry 0, compile_id=28/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:115 in torch_dynamo_resume_in__method1_2_inner_at_114
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:115 in torch_dynamo_resume_in__method1_2_inner_at_114
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:118 in torch_dynamo_resume_in__method1_2_inner_at_114
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:118 in torch_dynamo_resume_in__method1_2_inner_at_114
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:118 in torch_dynamo_resume_in__method1_2_inner_at_114
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 29: torch_dynamo_resume_in__method1_2_inner_at_118 ===
# file: method1.2/run.py  firstlineno: 118
#
# CacheEntry 0, compile_id=29/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:119 in torch_dynamo_resume_in__method1_2_inner_at_118
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:119 in torch_dynamo_resume_in__method1_2_inner_at_118
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:122 in torch_dynamo_resume_in__method1_2_inner_at_118
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:122 in torch_dynamo_resume_in__method1_2_inner_at_118
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:122 in torch_dynamo_resume_in__method1_2_inner_at_118
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 30: torch_dynamo_resume_in__method1_2_inner_at_122 ===
# file: method1.2/run.py  firstlineno: 122
#
# CacheEntry 0, compile_id=30/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:123 in torch_dynamo_resume_in__method1_2_inner_at_122
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:123 in torch_dynamo_resume_in__method1_2_inner_at_122
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:126 in torch_dynamo_resume_in__method1_2_inner_at_122
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:126 in torch_dynamo_resume_in__method1_2_inner_at_122
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:126 in torch_dynamo_resume_in__method1_2_inner_at_122
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 31: torch_dynamo_resume_in__method1_2_inner_at_126 ===
# file: method1.2/run.py  firstlineno: 126
#
# CacheEntry 0, compile_id=31/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:127 in torch_dynamo_resume_in__method1_2_inner_at_126
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:127 in torch_dynamo_resume_in__method1_2_inner_at_126
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:130 in torch_dynamo_resume_in__method1_2_inner_at_126
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:130 in torch_dynamo_resume_in__method1_2_inner_at_126
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:130 in torch_dynamo_resume_in__method1_2_inner_at_126
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 32: torch_dynamo_resume_in__method1_2_inner_at_130 ===
# file: method1.2/run.py  firstlineno: 130
#
# CacheEntry 0, compile_id=32/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:131 in torch_dynamo_resume_in__method1_2_inner_at_130
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:131 in torch_dynamo_resume_in__method1_2_inner_at_130
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:134 in torch_dynamo_resume_in__method1_2_inner_at_130
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:134 in torch_dynamo_resume_in__method1_2_inner_at_130
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:134 in torch_dynamo_resume_in__method1_2_inner_at_130
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 33: torch_dynamo_resume_in__method1_2_inner_at_134 ===
# file: method1.2/run.py  firstlineno: 134
#
# CacheEntry 0, compile_id=33/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:135 in torch_dynamo_resume_in__method1_2_inner_at_134
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:135 in torch_dynamo_resume_in__method1_2_inner_at_134
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:138 in torch_dynamo_resume_in__method1_2_inner_at_134
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:138 in torch_dynamo_resume_in__method1_2_inner_at_134
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:138 in torch_dynamo_resume_in__method1_2_inner_at_134
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 34: torch_dynamo_resume_in__method1_2_inner_at_138 ===
# file: method1.2/run.py  firstlineno: 138
#
# CacheEntry 0, compile_id=34/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:139 in torch_dynamo_resume_in__method1_2_inner_at_138
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:139 in torch_dynamo_resume_in__method1_2_inner_at_138
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:142 in torch_dynamo_resume_in__method1_2_inner_at_138
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:142 in torch_dynamo_resume_in__method1_2_inner_at_138
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:142 in torch_dynamo_resume_in__method1_2_inner_at_138
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 35: torch_dynamo_resume_in__method1_2_inner_at_142 ===
# file: method1.2/run.py  firstlineno: 142
#
# CacheEntry 0, compile_id=35/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:143 in torch_dynamo_resume_in__method1_2_inner_at_142
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:143 in torch_dynamo_resume_in__method1_2_inner_at_142
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:146 in torch_dynamo_resume_in__method1_2_inner_at_142
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:146 in torch_dynamo_resume_in__method1_2_inner_at_142
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:146 in torch_dynamo_resume_in__method1_2_inner_at_142
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 36: torch_dynamo_resume_in__method1_2_inner_at_146 ===
# file: method1.2/run.py  firstlineno: 146
#
# CacheEntry 0, compile_id=36/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:147 in torch_dynamo_resume_in__method1_2_inner_at_146
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:147 in torch_dynamo_resume_in__method1_2_inner_at_146
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:150 in torch_dynamo_resume_in__method1_2_inner_at_146
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:150 in torch_dynamo_resume_in__method1_2_inner_at_146
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:150 in torch_dynamo_resume_in__method1_2_inner_at_146
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 37: torch_dynamo_resume_in__method1_2_inner_at_150 ===
# file: method1.2/run.py  firstlineno: 150
#
# CacheEntry 0, compile_id=37/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:151 in torch_dynamo_resume_in__method1_2_inner_at_150
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:151 in torch_dynamo_resume_in__method1_2_inner_at_150
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:154 in torch_dynamo_resume_in__method1_2_inner_at_150
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:154 in torch_dynamo_resume_in__method1_2_inner_at_150
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:154 in torch_dynamo_resume_in__method1_2_inner_at_150
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 38: torch_dynamo_resume_in__method1_2_inner_at_154 ===
# file: method1.2/run.py  firstlineno: 154
#
# CacheEntry 0, compile_id=38/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:155 in torch_dynamo_resume_in__method1_2_inner_at_154
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:155 in torch_dynamo_resume_in__method1_2_inner_at_154
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:158 in torch_dynamo_resume_in__method1_2_inner_at_154
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:158 in torch_dynamo_resume_in__method1_2_inner_at_154
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:158 in torch_dynamo_resume_in__method1_2_inner_at_154
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 39: torch_dynamo_resume_in__method1_2_inner_at_158 ===
# file: method1.2/run.py  firstlineno: 158
#
# CacheEntry 0, compile_id=39/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:159 in torch_dynamo_resume_in__method1_2_inner_at_158
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:159 in torch_dynamo_resume_in__method1_2_inner_at_158
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:162 in torch_dynamo_resume_in__method1_2_inner_at_158
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:162 in torch_dynamo_resume_in__method1_2_inner_at_158
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:162 in torch_dynamo_resume_in__method1_2_inner_at_158
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 40: torch_dynamo_resume_in__method1_2_inner_at_162 ===
# file: method1.2/run.py  firstlineno: 162
#
# CacheEntry 0, compile_id=40/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:163 in torch_dynamo_resume_in__method1_2_inner_at_162
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:163 in torch_dynamo_resume_in__method1_2_inner_at_162
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:166 in torch_dynamo_resume_in__method1_2_inner_at_162
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:166 in torch_dynamo_resume_in__method1_2_inner_at_162
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:166 in torch_dynamo_resume_in__method1_2_inner_at_162
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 41: torch_dynamo_resume_in__method1_2_inner_at_166 ===
# file: method1.2/run.py  firstlineno: 166
#
# CacheEntry 0, compile_id=41/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:167 in torch_dynamo_resume_in__method1_2_inner_at_166
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:167 in torch_dynamo_resume_in__method1_2_inner_at_166
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:170 in torch_dynamo_resume_in__method1_2_inner_at_166
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:170 in torch_dynamo_resume_in__method1_2_inner_at_166
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:170 in torch_dynamo_resume_in__method1_2_inner_at_166
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 42: torch_dynamo_resume_in__method1_2_inner_at_170 ===
# file: method1.2/run.py  firstlineno: 170
#
# CacheEntry 0, compile_id=42/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:171 in torch_dynamo_resume_in__method1_2_inner_at_170
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:171 in torch_dynamo_resume_in__method1_2_inner_at_170
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:174 in torch_dynamo_resume_in__method1_2_inner_at_170
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:174 in torch_dynamo_resume_in__method1_2_inner_at_170
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:174 in torch_dynamo_resume_in__method1_2_inner_at_170
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 43: torch_dynamo_resume_in__method1_2_inner_at_174 ===
# file: method1.2/run.py  firstlineno: 174
#
# CacheEntry 0, compile_id=43/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:175 in torch_dynamo_resume_in__method1_2_inner_at_174
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:175 in torch_dynamo_resume_in__method1_2_inner_at_174
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:178 in torch_dynamo_resume_in__method1_2_inner_at_174
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:178 in torch_dynamo_resume_in__method1_2_inner_at_174
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:178 in torch_dynamo_resume_in__method1_2_inner_at_174
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 44: torch_dynamo_resume_in__method1_2_inner_at_178 ===
# file: method1.2/run.py  firstlineno: 178
#
# CacheEntry 0, compile_id=44/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:179 in torch_dynamo_resume_in__method1_2_inner_at_178
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:179 in torch_dynamo_resume_in__method1_2_inner_at_178
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:182 in torch_dynamo_resume_in__method1_2_inner_at_178
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:182 in torch_dynamo_resume_in__method1_2_inner_at_178
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:182 in torch_dynamo_resume_in__method1_2_inner_at_178
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 45: torch_dynamo_resume_in__method1_2_inner_at_182 ===
# file: method1.2/run.py  firstlineno: 182
#
# CacheEntry 0, compile_id=45/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:183 in torch_dynamo_resume_in__method1_2_inner_at_182
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:183 in torch_dynamo_resume_in__method1_2_inner_at_182
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:186 in torch_dynamo_resume_in__method1_2_inner_at_182
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:186 in torch_dynamo_resume_in__method1_2_inner_at_182
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:186 in torch_dynamo_resume_in__method1_2_inner_at_182
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 46: torch_dynamo_resume_in__method1_2_inner_at_186 ===
# file: method1.2/run.py  firstlineno: 186
#
# CacheEntry 0, compile_id=46/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:187 in torch_dynamo_resume_in__method1_2_inner_at_186
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:187 in torch_dynamo_resume_in__method1_2_inner_at_186
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:190 in torch_dynamo_resume_in__method1_2_inner_at_186
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:190 in torch_dynamo_resume_in__method1_2_inner_at_186
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:190 in torch_dynamo_resume_in__method1_2_inner_at_186
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 47: torch_dynamo_resume_in__method1_2_inner_at_190 ===
# file: method1.2/run.py  firstlineno: 190
#
# CacheEntry 0, compile_id=47/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:191 in torch_dynamo_resume_in__method1_2_inner_at_190
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:191 in torch_dynamo_resume_in__method1_2_inner_at_190
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:194 in torch_dynamo_resume_in__method1_2_inner_at_190
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:194 in torch_dynamo_resume_in__method1_2_inner_at_190
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:194 in torch_dynamo_resume_in__method1_2_inner_at_190
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 48: torch_dynamo_resume_in__method1_2_inner_at_194 ===
# file: method1.2/run.py  firstlineno: 194
#
# CacheEntry 0, compile_id=48/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:195 in torch_dynamo_resume_in__method1_2_inner_at_194
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:195 in torch_dynamo_resume_in__method1_2_inner_at_194
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:198 in torch_dynamo_resume_in__method1_2_inner_at_194
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:198 in torch_dynamo_resume_in__method1_2_inner_at_194
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:198 in torch_dynamo_resume_in__method1_2_inner_at_194
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 49: torch_dynamo_resume_in__method1_2_inner_at_198 ===
# file: method1.2/run.py  firstlineno: 198
#
# CacheEntry 0, compile_id=49/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:199 in torch_dynamo_resume_in__method1_2_inner_at_198
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:199 in torch_dynamo_resume_in__method1_2_inner_at_198
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:202 in torch_dynamo_resume_in__method1_2_inner_at_198
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:202 in torch_dynamo_resume_in__method1_2_inner_at_198
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:202 in torch_dynamo_resume_in__method1_2_inner_at_198
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 50: torch_dynamo_resume_in__method1_2_inner_at_202 ===
# file: method1.2/run.py  firstlineno: 202
#
# CacheEntry 0, compile_id=50/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:203 in torch_dynamo_resume_in__method1_2_inner_at_202
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:203 in torch_dynamo_resume_in__method1_2_inner_at_202
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:206 in torch_dynamo_resume_in__method1_2_inner_at_202
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:206 in torch_dynamo_resume_in__method1_2_inner_at_202
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:206 in torch_dynamo_resume_in__method1_2_inner_at_202
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 51: torch_dynamo_resume_in__method1_2_inner_at_206 ===
# file: method1.2/run.py  firstlineno: 206
#
# CacheEntry 0, compile_id=51/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:207 in torch_dynamo_resume_in__method1_2_inner_at_206
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:207 in torch_dynamo_resume_in__method1_2_inner_at_206
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:210 in torch_dynamo_resume_in__method1_2_inner_at_206
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:210 in torch_dynamo_resume_in__method1_2_inner_at_206
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:210 in torch_dynamo_resume_in__method1_2_inner_at_206
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 52: torch_dynamo_resume_in__method1_2_inner_at_210 ===
# file: method1.2/run.py  firstlineno: 210
#
# CacheEntry 0, compile_id=52/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:211 in torch_dynamo_resume_in__method1_2_inner_at_210
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:211 in torch_dynamo_resume_in__method1_2_inner_at_210
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:214 in torch_dynamo_resume_in__method1_2_inner_at_210
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:214 in torch_dynamo_resume_in__method1_2_inner_at_210
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:214 in torch_dynamo_resume_in__method1_2_inner_at_210
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 53: torch_dynamo_resume_in__method1_2_inner_at_214 ===
# file: method1.2/run.py  firstlineno: 214
#
# CacheEntry 0, compile_id=53/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:215 in torch_dynamo_resume_in__method1_2_inner_at_214
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:215 in torch_dynamo_resume_in__method1_2_inner_at_214
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:218 in torch_dynamo_resume_in__method1_2_inner_at_214
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:218 in torch_dynamo_resume_in__method1_2_inner_at_214
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:218 in torch_dynamo_resume_in__method1_2_inner_at_214
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 54: torch_dynamo_resume_in__method1_2_inner_at_218 ===
# file: method1.2/run.py  firstlineno: 218
#
# CacheEntry 0, compile_id=54/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:219 in torch_dynamo_resume_in__method1_2_inner_at_218
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:219 in torch_dynamo_resume_in__method1_2_inner_at_218
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:222 in torch_dynamo_resume_in__method1_2_inner_at_218
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:222 in torch_dynamo_resume_in__method1_2_inner_at_218
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:222 in torch_dynamo_resume_in__method1_2_inner_at_218
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 55: torch_dynamo_resume_in__method1_2_inner_at_222 ===
# file: method1.2/run.py  firstlineno: 222
#
# CacheEntry 0, compile_id=55/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:223 in torch_dynamo_resume_in__method1_2_inner_at_222
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:223 in torch_dynamo_resume_in__method1_2_inner_at_222
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:226 in torch_dynamo_resume_in__method1_2_inner_at_222
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:226 in torch_dynamo_resume_in__method1_2_inner_at_222
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:226 in torch_dynamo_resume_in__method1_2_inner_at_222
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 56: torch_dynamo_resume_in__method1_2_inner_at_226 ===
# file: method1.2/run.py  firstlineno: 226
#
# CacheEntry 0, compile_id=56/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:227 in torch_dynamo_resume_in__method1_2_inner_at_226
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:227 in torch_dynamo_resume_in__method1_2_inner_at_226
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:230 in torch_dynamo_resume_in__method1_2_inner_at_226
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:230 in torch_dynamo_resume_in__method1_2_inner_at_226
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:230 in torch_dynamo_resume_in__method1_2_inner_at_226
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 57: torch_dynamo_resume_in__method1_2_inner_at_230 ===
# file: method1.2/run.py  firstlineno: 230
#
# CacheEntry 0, compile_id=57/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:231 in torch_dynamo_resume_in__method1_2_inner_at_230
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:231 in torch_dynamo_resume_in__method1_2_inner_at_230
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:234 in torch_dynamo_resume_in__method1_2_inner_at_230
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:234 in torch_dynamo_resume_in__method1_2_inner_at_230
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:234 in torch_dynamo_resume_in__method1_2_inner_at_230
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 58: torch_dynamo_resume_in__method1_2_inner_at_234 ===
# file: method1.2/run.py  firstlineno: 234
#
# CacheEntry 0, compile_id=58/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:235 in torch_dynamo_resume_in__method1_2_inner_at_234
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:235 in torch_dynamo_resume_in__method1_2_inner_at_234
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:238 in torch_dynamo_resume_in__method1_2_inner_at_234
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:238 in torch_dynamo_resume_in__method1_2_inner_at_234
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:238 in torch_dynamo_resume_in__method1_2_inner_at_234
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 59: torch_dynamo_resume_in__method1_2_inner_at_238 ===
# file: method1.2/run.py  firstlineno: 238
#
# CacheEntry 0, compile_id=59/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:239 in torch_dynamo_resume_in__method1_2_inner_at_238
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:239 in torch_dynamo_resume_in__method1_2_inner_at_238
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:242 in torch_dynamo_resume_in__method1_2_inner_at_238
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:242 in torch_dynamo_resume_in__method1_2_inner_at_238
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:242 in torch_dynamo_resume_in__method1_2_inner_at_238
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 60: torch_dynamo_resume_in__method1_2_inner_at_242 ===
# file: method1.2/run.py  firstlineno: 242
#
# CacheEntry 0, compile_id=60/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:243 in torch_dynamo_resume_in__method1_2_inner_at_242
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:243 in torch_dynamo_resume_in__method1_2_inner_at_242
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:246 in torch_dynamo_resume_in__method1_2_inner_at_242
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:246 in torch_dynamo_resume_in__method1_2_inner_at_242
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:246 in torch_dynamo_resume_in__method1_2_inner_at_242
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 61: torch_dynamo_resume_in__method1_2_inner_at_246 ===
# file: method1.2/run.py  firstlineno: 246
#
# CacheEntry 0, compile_id=61/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:247 in torch_dynamo_resume_in__method1_2_inner_at_246
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:247 in torch_dynamo_resume_in__method1_2_inner_at_246
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:250 in torch_dynamo_resume_in__method1_2_inner_at_246
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:250 in torch_dynamo_resume_in__method1_2_inner_at_246
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:250 in torch_dynamo_resume_in__method1_2_inner_at_246
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 62: torch_dynamo_resume_in__method1_2_inner_at_250 ===
# file: method1.2/run.py  firstlineno: 250
#
# CacheEntry 0, compile_id=62/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:251 in torch_dynamo_resume_in__method1_2_inner_at_250
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:251 in torch_dynamo_resume_in__method1_2_inner_at_250
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:254 in torch_dynamo_resume_in__method1_2_inner_at_250
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:254 in torch_dynamo_resume_in__method1_2_inner_at_250
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:254 in torch_dynamo_resume_in__method1_2_inner_at_250
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 63: torch_dynamo_resume_in__method1_2_inner_at_254 ===
# file: method1.2/run.py  firstlineno: 254
#
# CacheEntry 0, compile_id=63/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:255 in torch_dynamo_resume_in__method1_2_inner_at_254
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:255 in torch_dynamo_resume_in__method1_2_inner_at_254
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:258 in torch_dynamo_resume_in__method1_2_inner_at_254
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:258 in torch_dynamo_resume_in__method1_2_inner_at_254
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:258 in torch_dynamo_resume_in__method1_2_inner_at_254
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 64: torch_dynamo_resume_in__method1_2_inner_at_258 ===
# file: method1.2/run.py  firstlineno: 258
#
# CacheEntry 0, compile_id=64/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:259 in torch_dynamo_resume_in__method1_2_inner_at_258
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:259 in torch_dynamo_resume_in__method1_2_inner_at_258
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:262 in torch_dynamo_resume_in__method1_2_inner_at_258
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:262 in torch_dynamo_resume_in__method1_2_inner_at_258
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:262 in torch_dynamo_resume_in__method1_2_inner_at_258
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 65: torch_dynamo_resume_in__method1_2_inner_at_262 ===
# file: method1.2/run.py  firstlineno: 262
#
# CacheEntry 0, compile_id=65/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:263 in torch_dynamo_resume_in__method1_2_inner_at_262
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:263 in torch_dynamo_resume_in__method1_2_inner_at_262
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:266 in torch_dynamo_resume_in__method1_2_inner_at_262
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:266 in torch_dynamo_resume_in__method1_2_inner_at_262
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:266 in torch_dynamo_resume_in__method1_2_inner_at_262
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 66: torch_dynamo_resume_in__method1_2_inner_at_266 ===
# file: method1.2/run.py  firstlineno: 266
#
# CacheEntry 0, compile_id=66/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:267 in torch_dynamo_resume_in__method1_2_inner_at_266
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:267 in torch_dynamo_resume_in__method1_2_inner_at_266
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:270 in torch_dynamo_resume_in__method1_2_inner_at_266
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:270 in torch_dynamo_resume_in__method1_2_inner_at_266
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:270 in torch_dynamo_resume_in__method1_2_inner_at_266
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 67: torch_dynamo_resume_in__method1_2_inner_at_270 ===
# file: method1.2/run.py  firstlineno: 270
#
# CacheEntry 0, compile_id=67/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:271 in torch_dynamo_resume_in__method1_2_inner_at_270
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:271 in torch_dynamo_resume_in__method1_2_inner_at_270
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:274 in torch_dynamo_resume_in__method1_2_inner_at_270
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:274 in torch_dynamo_resume_in__method1_2_inner_at_270
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:274 in torch_dynamo_resume_in__method1_2_inner_at_270
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 68: torch_dynamo_resume_in__method1_2_inner_at_274 ===
# file: method1.2/run.py  firstlineno: 274
#
# CacheEntry 0, compile_id=68/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:275 in torch_dynamo_resume_in__method1_2_inner_at_274
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:275 in torch_dynamo_resume_in__method1_2_inner_at_274
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:278 in torch_dynamo_resume_in__method1_2_inner_at_274
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:278 in torch_dynamo_resume_in__method1_2_inner_at_274
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:278 in torch_dynamo_resume_in__method1_2_inner_at_274
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 69: torch_dynamo_resume_in__method1_2_inner_at_278 ===
# file: method1.2/run.py  firstlineno: 278
#
# CacheEntry 0, compile_id=69/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:279 in torch_dynamo_resume_in__method1_2_inner_at_278
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:279 in torch_dynamo_resume_in__method1_2_inner_at_278
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:282 in torch_dynamo_resume_in__method1_2_inner_at_278
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:282 in torch_dynamo_resume_in__method1_2_inner_at_278
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:282 in torch_dynamo_resume_in__method1_2_inner_at_278
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 70: torch_dynamo_resume_in__method1_2_inner_at_282 ===
# file: method1.2/run.py  firstlineno: 282
#
# CacheEntry 0, compile_id=70/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:283 in torch_dynamo_resume_in__method1_2_inner_at_282
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:283 in torch_dynamo_resume_in__method1_2_inner_at_282
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:286 in torch_dynamo_resume_in__method1_2_inner_at_282
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:286 in torch_dynamo_resume_in__method1_2_inner_at_282
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:286 in torch_dynamo_resume_in__method1_2_inner_at_282
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 71: torch_dynamo_resume_in__method1_2_inner_at_286 ===
# file: method1.2/run.py  firstlineno: 286
#
# CacheEntry 0, compile_id=71/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:287 in torch_dynamo_resume_in__method1_2_inner_at_286
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:287 in torch_dynamo_resume_in__method1_2_inner_at_286
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:290 in torch_dynamo_resume_in__method1_2_inner_at_286
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:290 in torch_dynamo_resume_in__method1_2_inner_at_286
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:290 in torch_dynamo_resume_in__method1_2_inner_at_286
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 72: torch_dynamo_resume_in__method1_2_inner_at_290 ===
# file: method1.2/run.py  firstlineno: 290
#
# CacheEntry 0, compile_id=72/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:291 in torch_dynamo_resume_in__method1_2_inner_at_290
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:291 in torch_dynamo_resume_in__method1_2_inner_at_290
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:294 in torch_dynamo_resume_in__method1_2_inner_at_290
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:294 in torch_dynamo_resume_in__method1_2_inner_at_290
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:294 in torch_dynamo_resume_in__method1_2_inner_at_290
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 73: torch_dynamo_resume_in__method1_2_inner_at_294 ===
# file: method1.2/run.py  firstlineno: 294
#
# CacheEntry 0, compile_id=73/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:295 in torch_dynamo_resume_in__method1_2_inner_at_294
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:295 in torch_dynamo_resume_in__method1_2_inner_at_294
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:298 in torch_dynamo_resume_in__method1_2_inner_at_294
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:298 in torch_dynamo_resume_in__method1_2_inner_at_294
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:298 in torch_dynamo_resume_in__method1_2_inner_at_294
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 74: torch_dynamo_resume_in__method1_2_inner_at_298 ===
# file: method1.2/run.py  firstlineno: 298
#
# CacheEntry 0, compile_id=74/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:299 in torch_dynamo_resume_in__method1_2_inner_at_298
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:299 in torch_dynamo_resume_in__method1_2_inner_at_298
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:302 in torch_dynamo_resume_in__method1_2_inner_at_298
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:302 in torch_dynamo_resume_in__method1_2_inner_at_298
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:302 in torch_dynamo_resume_in__method1_2_inner_at_298
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 75: torch_dynamo_resume_in__method1_2_inner_at_302 ===
# file: method1.2/run.py  firstlineno: 302
#
# CacheEntry 0, compile_id=75/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:303 in torch_dynamo_resume_in__method1_2_inner_at_302
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:303 in torch_dynamo_resume_in__method1_2_inner_at_302
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:306 in torch_dynamo_resume_in__method1_2_inner_at_302
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:306 in torch_dynamo_resume_in__method1_2_inner_at_302
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:306 in torch_dynamo_resume_in__method1_2_inner_at_302
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 76: torch_dynamo_resume_in__method1_2_inner_at_306 ===
# file: method1.2/run.py  firstlineno: 306
#
# CacheEntry 0, compile_id=76/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:307 in torch_dynamo_resume_in__method1_2_inner_at_306
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:307 in torch_dynamo_resume_in__method1_2_inner_at_306
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:310 in torch_dynamo_resume_in__method1_2_inner_at_306
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:310 in torch_dynamo_resume_in__method1_2_inner_at_306
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:310 in torch_dynamo_resume_in__method1_2_inner_at_306
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 77: torch_dynamo_resume_in__method1_2_inner_at_310 ===
# file: method1.2/run.py  firstlineno: 310
#
# CacheEntry 0, compile_id=77/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:311 in torch_dynamo_resume_in__method1_2_inner_at_310
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:311 in torch_dynamo_resume_in__method1_2_inner_at_310
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:314 in torch_dynamo_resume_in__method1_2_inner_at_310
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:314 in torch_dynamo_resume_in__method1_2_inner_at_310
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:314 in torch_dynamo_resume_in__method1_2_inner_at_310
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 78: torch_dynamo_resume_in__method1_2_inner_at_314 ===
# file: method1.2/run.py  firstlineno: 314
#
# CacheEntry 0, compile_id=78/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:315 in torch_dynamo_resume_in__method1_2_inner_at_314
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:315 in torch_dynamo_resume_in__method1_2_inner_at_314
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:318 in torch_dynamo_resume_in__method1_2_inner_at_314
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:318 in torch_dynamo_resume_in__method1_2_inner_at_314
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:318 in torch_dynamo_resume_in__method1_2_inner_at_314
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 79: torch_dynamo_resume_in__method1_2_inner_at_318 ===
# file: method1.2/run.py  firstlineno: 318
#
# CacheEntry 0, compile_id=79/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:319 in torch_dynamo_resume_in__method1_2_inner_at_318
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:319 in torch_dynamo_resume_in__method1_2_inner_at_318
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:322 in torch_dynamo_resume_in__method1_2_inner_at_318
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:322 in torch_dynamo_resume_in__method1_2_inner_at_318
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:322 in torch_dynamo_resume_in__method1_2_inner_at_318
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 80: torch_dynamo_resume_in__method1_2_inner_at_322 ===
# file: method1.2/run.py  firstlineno: 322
#
# CacheEntry 0, compile_id=80/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:323 in torch_dynamo_resume_in__method1_2_inner_at_322
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:323 in torch_dynamo_resume_in__method1_2_inner_at_322
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:326 in torch_dynamo_resume_in__method1_2_inner_at_322
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:326 in torch_dynamo_resume_in__method1_2_inner_at_322
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:326 in torch_dynamo_resume_in__method1_2_inner_at_322
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 81: torch_dynamo_resume_in__method1_2_inner_at_326 ===
# file: method1.2/run.py  firstlineno: 326
#
# CacheEntry 0, compile_id=81/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:327 in torch_dynamo_resume_in__method1_2_inner_at_326
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:327 in torch_dynamo_resume_in__method1_2_inner_at_326
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:330 in torch_dynamo_resume_in__method1_2_inner_at_326
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:330 in torch_dynamo_resume_in__method1_2_inner_at_326
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:330 in torch_dynamo_resume_in__method1_2_inner_at_326
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 82: torch_dynamo_resume_in__method1_2_inner_at_330 ===
# file: method1.2/run.py  firstlineno: 330
#
# CacheEntry 0, compile_id=82/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:331 in torch_dynamo_resume_in__method1_2_inner_at_330
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:331 in torch_dynamo_resume_in__method1_2_inner_at_330
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:334 in torch_dynamo_resume_in__method1_2_inner_at_330
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:334 in torch_dynamo_resume_in__method1_2_inner_at_330
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:334 in torch_dynamo_resume_in__method1_2_inner_at_330
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 83: torch_dynamo_resume_in__method1_2_inner_at_334 ===
# file: method1.2/run.py  firstlineno: 334
#
# CacheEntry 0, compile_id=83/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:335 in torch_dynamo_resume_in__method1_2_inner_at_334
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:335 in torch_dynamo_resume_in__method1_2_inner_at_334
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:338 in torch_dynamo_resume_in__method1_2_inner_at_334
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:338 in torch_dynamo_resume_in__method1_2_inner_at_334
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:338 in torch_dynamo_resume_in__method1_2_inner_at_334
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 84: torch_dynamo_resume_in__method1_2_inner_at_338 ===
# file: method1.2/run.py  firstlineno: 338
#
# CacheEntry 0, compile_id=84/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:339 in torch_dynamo_resume_in__method1_2_inner_at_338
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:339 in torch_dynamo_resume_in__method1_2_inner_at_338
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:342 in torch_dynamo_resume_in__method1_2_inner_at_338
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:342 in torch_dynamo_resume_in__method1_2_inner_at_338
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:342 in torch_dynamo_resume_in__method1_2_inner_at_338
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 85: torch_dynamo_resume_in__method1_2_inner_at_342 ===
# file: method1.2/run.py  firstlineno: 342
#
# CacheEntry 0, compile_id=85/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:343 in torch_dynamo_resume_in__method1_2_inner_at_342
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:343 in torch_dynamo_resume_in__method1_2_inner_at_342
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:346 in torch_dynamo_resume_in__method1_2_inner_at_342
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:346 in torch_dynamo_resume_in__method1_2_inner_at_342
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:346 in torch_dynamo_resume_in__method1_2_inner_at_342
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 86: torch_dynamo_resume_in__method1_2_inner_at_346 ===
# file: method1.2/run.py  firstlineno: 346
#
# CacheEntry 0, compile_id=86/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:347 in torch_dynamo_resume_in__method1_2_inner_at_346
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:347 in torch_dynamo_resume_in__method1_2_inner_at_346
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:350 in torch_dynamo_resume_in__method1_2_inner_at_346
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:350 in torch_dynamo_resume_in__method1_2_inner_at_346
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:350 in torch_dynamo_resume_in__method1_2_inner_at_346
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 87: torch_dynamo_resume_in__method1_2_inner_at_350 ===
# file: method1.2/run.py  firstlineno: 350
#
# CacheEntry 0, compile_id=87/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:351 in torch_dynamo_resume_in__method1_2_inner_at_350
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:351 in torch_dynamo_resume_in__method1_2_inner_at_350
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:354 in torch_dynamo_resume_in__method1_2_inner_at_350
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:354 in torch_dynamo_resume_in__method1_2_inner_at_350
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:354 in torch_dynamo_resume_in__method1_2_inner_at_350
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 88: torch_dynamo_resume_in__method1_2_inner_at_354 ===
# file: method1.2/run.py  firstlineno: 354
#
# CacheEntry 0, compile_id=88/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:355 in torch_dynamo_resume_in__method1_2_inner_at_354
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:355 in torch_dynamo_resume_in__method1_2_inner_at_354
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:358 in torch_dynamo_resume_in__method1_2_inner_at_354
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:358 in torch_dynamo_resume_in__method1_2_inner_at_354
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:358 in torch_dynamo_resume_in__method1_2_inner_at_354
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 89: torch_dynamo_resume_in__method1_2_inner_at_358 ===
# file: method1.2/run.py  firstlineno: 358
#
# CacheEntry 0, compile_id=89/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:359 in torch_dynamo_resume_in__method1_2_inner_at_358
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:359 in torch_dynamo_resume_in__method1_2_inner_at_358
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:362 in torch_dynamo_resume_in__method1_2_inner_at_358
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:362 in torch_dynamo_resume_in__method1_2_inner_at_358
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:362 in torch_dynamo_resume_in__method1_2_inner_at_358
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 90: torch_dynamo_resume_in__method1_2_inner_at_362 ===
# file: method1.2/run.py  firstlineno: 362
#
# CacheEntry 0, compile_id=90/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:363 in torch_dynamo_resume_in__method1_2_inner_at_362
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:363 in torch_dynamo_resume_in__method1_2_inner_at_362
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:366 in torch_dynamo_resume_in__method1_2_inner_at_362
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:366 in torch_dynamo_resume_in__method1_2_inner_at_362
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:366 in torch_dynamo_resume_in__method1_2_inner_at_362
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 91: torch_dynamo_resume_in__method1_2_inner_at_366 ===
# file: method1.2/run.py  firstlineno: 366
#
# CacheEntry 0, compile_id=91/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:367 in torch_dynamo_resume_in__method1_2_inner_at_366
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:367 in torch_dynamo_resume_in__method1_2_inner_at_366
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:370 in torch_dynamo_resume_in__method1_2_inner_at_366
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:370 in torch_dynamo_resume_in__method1_2_inner_at_366
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:370 in torch_dynamo_resume_in__method1_2_inner_at_366
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 92: torch_dynamo_resume_in__method1_2_inner_at_370 ===
# file: method1.2/run.py  firstlineno: 370
#
# CacheEntry 0, compile_id=92/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:371 in torch_dynamo_resume_in__method1_2_inner_at_370
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:371 in torch_dynamo_resume_in__method1_2_inner_at_370
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:374 in torch_dynamo_resume_in__method1_2_inner_at_370
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:374 in torch_dynamo_resume_in__method1_2_inner_at_370
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:374 in torch_dynamo_resume_in__method1_2_inner_at_370
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 93: torch_dynamo_resume_in__method1_2_inner_at_374 ===
# file: method1.2/run.py  firstlineno: 374
#
# CacheEntry 0, compile_id=93/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:375 in torch_dynamo_resume_in__method1_2_inner_at_374
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:375 in torch_dynamo_resume_in__method1_2_inner_at_374
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:378 in torch_dynamo_resume_in__method1_2_inner_at_374
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:378 in torch_dynamo_resume_in__method1_2_inner_at_374
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:378 in torch_dynamo_resume_in__method1_2_inner_at_374
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 94: torch_dynamo_resume_in__method1_2_inner_at_378 ===
# file: method1.2/run.py  firstlineno: 378
#
# CacheEntry 0, compile_id=94/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:379 in torch_dynamo_resume_in__method1_2_inner_at_378
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:379 in torch_dynamo_resume_in__method1_2_inner_at_378
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:382 in torch_dynamo_resume_in__method1_2_inner_at_378
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:382 in torch_dynamo_resume_in__method1_2_inner_at_378
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:382 in torch_dynamo_resume_in__method1_2_inner_at_378
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 95: torch_dynamo_resume_in__method1_2_inner_at_382 ===
# file: method1.2/run.py  firstlineno: 382
#
# CacheEntry 0, compile_id=95/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:383 in torch_dynamo_resume_in__method1_2_inner_at_382
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:383 in torch_dynamo_resume_in__method1_2_inner_at_382
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:386 in torch_dynamo_resume_in__method1_2_inner_at_382
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:386 in torch_dynamo_resume_in__method1_2_inner_at_382
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:386 in torch_dynamo_resume_in__method1_2_inner_at_382
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 96: torch_dynamo_resume_in__method1_2_inner_at_386 ===
# file: method1.2/run.py  firstlineno: 386
#
# CacheEntry 0, compile_id=96/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:387 in torch_dynamo_resume_in__method1_2_inner_at_386
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:387 in torch_dynamo_resume_in__method1_2_inner_at_386
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:390 in torch_dynamo_resume_in__method1_2_inner_at_386
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:390 in torch_dynamo_resume_in__method1_2_inner_at_386
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:390 in torch_dynamo_resume_in__method1_2_inner_at_386
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 97: torch_dynamo_resume_in__method1_2_inner_at_390 ===
# file: method1.2/run.py  firstlineno: 390
#
# CacheEntry 0, compile_id=97/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:391 in torch_dynamo_resume_in__method1_2_inner_at_390
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:391 in torch_dynamo_resume_in__method1_2_inner_at_390
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:394 in torch_dynamo_resume_in__method1_2_inner_at_390
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:394 in torch_dynamo_resume_in__method1_2_inner_at_390
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:394 in torch_dynamo_resume_in__method1_2_inner_at_390
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 98: torch_dynamo_resume_in__method1_2_inner_at_394 ===
# file: method1.2/run.py  firstlineno: 394
#
# CacheEntry 0, compile_id=98/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:395 in torch_dynamo_resume_in__method1_2_inner_at_394
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:395 in torch_dynamo_resume_in__method1_2_inner_at_394
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:398 in torch_dynamo_resume_in__method1_2_inner_at_394
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:398 in torch_dynamo_resume_in__method1_2_inner_at_394
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:398 in torch_dynamo_resume_in__method1_2_inner_at_394
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

# === Frame 99: torch_dynamo_resume_in__method1_2_inner_at_398 ===
# file: method1.2/run.py  firstlineno: 398
#
# CacheEntry 0, compile_id=99/0
# Guard tree:
#   
#   TREE_GUARD_MANAGER:
#   +- RootGuardManager
#   | +- LAMBDA_GUARD: torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None  # _dynamo/output_graph.py:905 in init_ambient_guards
#   | +- GLOBAL_STATE: ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   | +- TORCH_FUNCTION_MODE_STACK: ___check_torch_function_mode_stack()
#   | +- DEFAULT_DEVICE: utils_device.CURRENT_DEVICE == None                           # _dynamo/output_graph.py:892 in init_ambient_guards
#   | +- GuardManager: source=L['out'], accessed_by=FrameLocalsGuardAccessor(key='out', framelocals_idx=3), type=<class 'torch.Tensor'>, tag_safe=(True, False)
#   | | +- TENSOR_MATCH: check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])  #   # method1.2/run.py:399 in torch_dynamo_resume_in__method1_2_inner_at_398
#   | | +- NO_HASATTR: hasattr(L['out'], '_dynamo_dynamic_indices') == False         #   # method1.2/run.py:399 in torch_dynamo_resume_in__method1_2_inner_at_398
#   | +- GuardManager: source=G, accessed_by=GlobalsGuardAccessor, type=<class 'dict'>, tag_safe=(False, False)
#   | | +- GuardManager: source=G['torch'], accessed_by=DictGetItemGuardAccessor('torch'), type=<class 'module'>, tag_safe=(False, False)
#   | | | +- ID_MATCH: ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>  #   # method1.2/run.py:402 in torch_dynamo_resume_in__method1_2_inner_at_398
#   | | | +- GuardManager: source=G['torch']._dynamo, accessed_by=GetAttrGuardAccessor(_dynamo), type=<class 'module'>, tag_safe=(False, False)
#   | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>  #   # method1.2/run.py:402 in torch_dynamo_resume_in__method1_2_inner_at_398
#   | | | | +- GuardManager: source=G['torch']._dynamo.graph_break, accessed_by=GetAttrGuardAccessor(graph_break), type=<class 'function'>, tag_safe=(True, False)
#   | | | | | +- GuardManager: source=G['torch']._dynamo.graph_break.__code__, accessed_by=CodeGuardAccessor, type=<class 'code'>, tag_safe=(True, False)
#   | | | | | | +- ID_MATCH: ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>  #   # method1.2/run.py:402 in torch_dynamo_resume_in__method1_2_inner_at_398
#
# Guard conditions (code_parts):
#   torch._functorch.aot_autograd.utils.top_saved_tensors_hooks ids == None
#   ___check_global_state() against {"allow_bf16_reduce":0,"allow_fp16_reduce":0,"allow_tf32":true,"autocast_state":{"cached_enabled":true,"dtype":[15,5,5,15,5,5,15,15,5,5],"enabled":[false,false,false,false,false,false,false,false,false,false]},"default_dtype":6,"deterministic_algorithms":false,"deterministic_algorithms_warn_only":false,"grad_mode":true,"num_threads":144,"torch_function":true,"torch_function_all_disabled":false}
#   ___check_torch_function_mode_stack()
#   utils_device.CURRENT_DEVICE == None
#   check_tensor(L['out'], Tensor, DispatchKeySet(CUDA, BackendSelect, ADInplaceOrView, AutogradCUDA), torch.float32, device=0, requires_grad=False, size=[2, 3, 5, 7, 11, 13, 17, 19], stride=[4849845, 1616615, 323323, 46189, 4199, 323, 19, 1])
#   hasattr(L['out'], '_dynamo_dynamic_indices') == False
#   ___check_obj_id(G['torch'], 253860379462768), type=<module 'torch' from '/usr/local/lib/python3.12/dist-packages/torch/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo, 253860379598720), type=<module 'torch._dynamo' from '/usr/local/lib/python3.12/dist-packages/torch/_dynamo/__init__.py'>
#   ___check_obj_id(G['torch']._dynamo.graph_break.__code__, 253854649301264), type=<code object graph_break at 0xe6e124323910, file "/usr/local/lib/python3.12/dist-packages/torch/_dynamo/decorators.py", line 596>

