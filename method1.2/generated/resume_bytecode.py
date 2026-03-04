# Auto-generated Dynamo resume-function bytecode for method1.2
# 100 compiled frame(s) captured

# === _method1_2_inner ===
# file: method1.2/run.py  firstlineno: 1
# argcount: 1  varnames: ('tensor',)
#
# MODIFIED BYTECODE
  1           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_2_5b0eace1_177b_4e02_a9a0_4b4481b5a51c)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               3 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               4 (tmp_2)
             56 LOAD_FAST                0 (tensor)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               5 (tmp_3)
             92 LOAD_FAST                4 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               2 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                2 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              10 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              2 (graph_out_0)

  6         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              10 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              10 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_194_3)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              11 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              11 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_6 ===
# file: method1.2/run.py  firstlineno: 6
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
  6           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_6_06dbb732_bf94_4b33_9d82_0a10b1f212c1)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 10         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_398_7)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_10 ===
# file: method1.2/run.py  firstlineno: 10
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 10           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_10_809cbfdc_f219_4c0a_9593_198c3479dcb2)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 14         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_588_11)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_14 ===
# file: method1.2/run.py  firstlineno: 14
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 14           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_14_658eb1c5_2066_4b59_ba98_0b19c16609c2)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 18         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_778_15)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_18 ===
# file: method1.2/run.py  firstlineno: 18
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 18           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_18_5d1f3eff_446d_4f2f_bf30_7efab004221e)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 22         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_968_19)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_22 ===
# file: method1.2/run.py  firstlineno: 22
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 22           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_22_377c97e5_7b7f_4beb_a4f8_53f178328bde)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 26         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_1158_23)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_26 ===
# file: method1.2/run.py  firstlineno: 26
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 26           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_26_b06908d1_7e49_48b7_8777_213a68aadc42)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 30         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_1348_27)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_30 ===
# file: method1.2/run.py  firstlineno: 30
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 30           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_30_cc47ca33_8506_4225_9449_809d1b006431)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 34         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_1538_31)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_34 ===
# file: method1.2/run.py  firstlineno: 34
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 34           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_34_45e12ecc_ecbc_4b4b_964a_063baa86bdb2)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 38         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_1728_35)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_38 ===
# file: method1.2/run.py  firstlineno: 38
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 38           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_38_8441fb22_38e7_45ca_bd8a_09c29bfbce0b)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 42         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_1918_39)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_42 ===
# file: method1.2/run.py  firstlineno: 42
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 42           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_42_9126bc85_9c7e_463c_ab78_2ffafb35c23f)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 46         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_2108_43)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_46 ===
# file: method1.2/run.py  firstlineno: 46
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 46           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_46_0691ba4a_1386_46e0_8f4c_153ec534462d)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 50         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_2298_47)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_50 ===
# file: method1.2/run.py  firstlineno: 50
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 50           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_50_59660ac9_19c8_4746_b49d_6289009985a0)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 54         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_2488_51)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_54 ===
# file: method1.2/run.py  firstlineno: 54
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 54           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_54_6b7047ff_523e_4610_98c8_8f697150869a)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 58         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_2678_55)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_58 ===
# file: method1.2/run.py  firstlineno: 58
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 58           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_58_f7668d6c_ddce_417e_85aa_965cfeb03b9d)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 62         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_2868_59)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_62 ===
# file: method1.2/run.py  firstlineno: 62
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 62           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_62_0e4a8338_2120_4a04_8490_28a68b2076f4)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 66         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_3058_63)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_66 ===
# file: method1.2/run.py  firstlineno: 66
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 66           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_66_a89dff34_68ec_4204_8d24_ddf81385ddea)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 70         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_3248_67)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_70 ===
# file: method1.2/run.py  firstlineno: 70
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 70           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_70_a5f861a6_a725_4c81_9b15_ffb61d8710a5)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 74         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_3438_71)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_74 ===
# file: method1.2/run.py  firstlineno: 74
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 74           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_74_7e19f4d9_ead3_4a0c_837a_63a31a14e00b)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 78         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_3628_75)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_78 ===
# file: method1.2/run.py  firstlineno: 78
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 78           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_78_d639d07d_ccbf_4e07_996d_078285e474b5)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 82         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_3818_79)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_82 ===
# file: method1.2/run.py  firstlineno: 82
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 82           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_82_43d1af22_1afd_44aa_bd1e_834775528943)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 86         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_4008_83)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_86 ===
# file: method1.2/run.py  firstlineno: 86
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 86           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_86_61d7f079_5757_4bc7_a16f_24a2bb9f29c0)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 90         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_4198_87)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_90 ===
# file: method1.2/run.py  firstlineno: 90
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 90           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_90_14bda591_5b18_4f8d_9ae3_2f29b6e6b59d)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 94         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_4388_91)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_94 ===
# file: method1.2/run.py  firstlineno: 94
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 94           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_94_6176b0f8_e22e_4867_a687_582b6a835d03)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

 98         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_4578_95)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_98 ===
# file: method1.2/run.py  firstlineno: 98
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
 98           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_98_71020e58_58a5_41c1_a1ca_8c4c7fb05b05)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

102         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_4768_99)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_102 ===
# file: method1.2/run.py  firstlineno: 102
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
102           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_102_2c2f34b2_2791_4200_8b42_bd946e8d6031)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

106         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_4958_103)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_106 ===
# file: method1.2/run.py  firstlineno: 106
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
106           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_106_01341396_8ba2_4dab_b90e_7660426543a2)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

110         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_5148_107)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_110 ===
# file: method1.2/run.py  firstlineno: 110
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
110           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_110_b402af53_d937_42b1_a5af_6bf9c3d2213b)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

114         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_5338_111)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_114 ===
# file: method1.2/run.py  firstlineno: 114
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
114           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_114_f4a1b686_0268_4d13_bcc5_c5b9e992489f)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

118         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_5528_115)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_118 ===
# file: method1.2/run.py  firstlineno: 118
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
118           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_118_30b57a6a_962f_4367_b59e_c87027f54463)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

122         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_5718_119)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_122 ===
# file: method1.2/run.py  firstlineno: 122
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
122           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_122_b8657512_66c0_41d8_88c0_be55afa9acab)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

126         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_5908_123)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_126 ===
# file: method1.2/run.py  firstlineno: 126
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
126           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_126_b497059e_836b_416d_8611_cd45dd75f3e8)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

130         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_6098_127)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_130 ===
# file: method1.2/run.py  firstlineno: 130
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
130           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_130_5562b8de_cf8d_45ad_9ca3_32d4f677d871)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

134         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_6288_131)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_134 ===
# file: method1.2/run.py  firstlineno: 134
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
134           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_134_eb05167e_1722_48e5_b500_274b02d622a3)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

138         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_6478_135)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_138 ===
# file: method1.2/run.py  firstlineno: 138
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
138           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_138_ce310313_428e_4cfd_912b_16f929a213fe)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

142         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_6668_139)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_142 ===
# file: method1.2/run.py  firstlineno: 142
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
142           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_142_a6a2aabd_b8b8_4294_8f1b_4d407f9c3df5)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

146         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_6858_143)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_146 ===
# file: method1.2/run.py  firstlineno: 146
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
146           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_146_8fcac36f_2edf_4afa_8cd8_9f5397dd4ca6)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

150         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_7048_147)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_150 ===
# file: method1.2/run.py  firstlineno: 150
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
150           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_150_c1fbf71e_fdca_4cb4_8eaf_d0365e5d467e)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

154         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_7238_151)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_154 ===
# file: method1.2/run.py  firstlineno: 154
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
154           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_154_fc6f6346_0c65_4c5e_ad9f_26ae96ddd602)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

158         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_7428_155)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_158 ===
# file: method1.2/run.py  firstlineno: 158
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
158           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_158_1cf4507c_c7ef_4c67_8123_0775bae434f7)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

162         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_7618_159)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_162 ===
# file: method1.2/run.py  firstlineno: 162
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
162           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_162_11a0245c_66c2_4a39_9ef5_18618f4a5fe7)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

166         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_7808_163)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_166 ===
# file: method1.2/run.py  firstlineno: 166
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
166           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_166_5992163b_4cd0_409d_b592_d596f9836c13)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

170         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_7998_167)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_170 ===
# file: method1.2/run.py  firstlineno: 170
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
170           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_170_53162930_8ee8_48d7_8a0f_c86c50370c94)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

174         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_8188_171)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_174 ===
# file: method1.2/run.py  firstlineno: 174
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
174           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_174_ca3d4e59_7572_4a94_8b99_2e39da1a50b6)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

178         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_8378_175)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_178 ===
# file: method1.2/run.py  firstlineno: 178
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
178           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_178_7a19f2dd_332d_44d1_a240_3a8d7f330be9)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

182         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_8568_179)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_182 ===
# file: method1.2/run.py  firstlineno: 182
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
182           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_182_494a3862_6497_4331_ba44_1904a98e219a)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

186         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_8758_183)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_186 ===
# file: method1.2/run.py  firstlineno: 186
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
186           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_186_b891685f_1f66_4cd2_aa86_446461040843)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

190         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_8948_187)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_190 ===
# file: method1.2/run.py  firstlineno: 190
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
190           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_190_f419bf68_9d14_4a91_85c9_c10b79bbee90)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

194         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_9138_191)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_194 ===
# file: method1.2/run.py  firstlineno: 194
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
194           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_194_35ef8524_c2ab_4453_bf5b_da1f2f8ec018)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

198         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_9328_195)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_198 ===
# file: method1.2/run.py  firstlineno: 198
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
198           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_198_6c47d4bb_9cd9_4b56_ad85_5b8ab4486d9d)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

202         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_9518_199)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_202 ===
# file: method1.2/run.py  firstlineno: 202
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
202           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_202_fb1805cc_a6a1_44ba_906e_747352fa74b9)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

206         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_9708_203)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_206 ===
# file: method1.2/run.py  firstlineno: 206
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
206           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_206_e705f1f9_9100_4b3f_91b6_318c6d43ec8e)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

210         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_9898_207)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_210 ===
# file: method1.2/run.py  firstlineno: 210
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
210           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_210_328eaa9e_baa2_44a3_8fc1_eae1735b9890)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

214         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_10088_211)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_214 ===
# file: method1.2/run.py  firstlineno: 214
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
214           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_214_de3de5a0_b111_4a29_abf1_4cd48a2fd5b3)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

218         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_10278_215)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_218 ===
# file: method1.2/run.py  firstlineno: 218
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
218           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_218_492b0736_460b_47f6_999f_720b33cc6542)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

222         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_10468_219)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_222 ===
# file: method1.2/run.py  firstlineno: 222
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
222           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_222_53f57c98_5b76_4c31_a0e4_35591b7e39d7)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

226         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_10658_223)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_226 ===
# file: method1.2/run.py  firstlineno: 226
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
226           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_226_dc283ff3_ea88_432b_aea4_e0aee702a619)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

230         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_10848_227)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_230 ===
# file: method1.2/run.py  firstlineno: 230
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
230           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_230_5098a174_bdcf_4b59_ad94_d1b0e89d56d4)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

234         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_11038_231)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_234 ===
# file: method1.2/run.py  firstlineno: 234
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
234           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_234_92bddeeb_c672_49f1_8e43_81ea0750d586)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

238         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_11228_235)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_238 ===
# file: method1.2/run.py  firstlineno: 238
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
238           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_238_111e0de9_80ae_40a0_8ec8_1262b4619daa)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

242         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_11418_239)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_242 ===
# file: method1.2/run.py  firstlineno: 242
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
242           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_242_a4ff46e3_3500_4538_9da0_9470b3d4062f)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

246         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_11608_243)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_246 ===
# file: method1.2/run.py  firstlineno: 246
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
246           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_246_2fc21aee_9f15_45f5_bc99_1b7e9b01a6d5)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

250         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_11798_247)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_250 ===
# file: method1.2/run.py  firstlineno: 250
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
250           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_250_e0df21a5_0271_4428_a7e9_af22ae743ba7)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

254         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_11988_251)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_254 ===
# file: method1.2/run.py  firstlineno: 254
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
254           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_254_7b811f00_41ac_4861_a1a9_2dec66cbf57b)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

258         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_12178_255)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_258 ===
# file: method1.2/run.py  firstlineno: 258
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
258           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_258_c57cb50c_8a6e_413c_aa27_32b7b12fdf25)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

262         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_12368_259)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_262 ===
# file: method1.2/run.py  firstlineno: 262
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
262           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_262_dcbc0c2c_52fd_432a_b804_99c225b1b0b6)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

266         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_12558_263)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_266 ===
# file: method1.2/run.py  firstlineno: 266
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
266           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_266_9461b8f7_96b9_4e6b_8715_2d44311a4c28)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

270         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_12748_267)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_270 ===
# file: method1.2/run.py  firstlineno: 270
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
270           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_270_432e5b65_a19e_4d24_b948_2b5696bd8082)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

274         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_12938_271)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_274 ===
# file: method1.2/run.py  firstlineno: 274
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
274           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_274_bb30dda3_e881_411b_9399_48c52018042d)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

278         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_13128_275)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_278 ===
# file: method1.2/run.py  firstlineno: 278
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
278           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_278_c7e9435a_cc3c_40c9_a6e1_511baad90dd4)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

282         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_13318_279)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_282 ===
# file: method1.2/run.py  firstlineno: 282
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
282           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_282_7aa819e8_4dff_4152_82b7_970336e293d6)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

286         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_13508_283)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_286 ===
# file: method1.2/run.py  firstlineno: 286
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
286           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_286_01b031f0_33c4_48c7_a233_985e6482edb1)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

290         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_13698_287)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_290 ===
# file: method1.2/run.py  firstlineno: 290
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
290           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_290_2b027e74_bb66_4181_8c81_f67b7c253bbd)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

294         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_13888_291)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_294 ===
# file: method1.2/run.py  firstlineno: 294
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
294           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_294_cf0967cb_7065_4a52_baa4_72a737fd699e)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

298         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_14078_295)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_298 ===
# file: method1.2/run.py  firstlineno: 298
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
298           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_298_7975fe04_15c6_417f_851c_f588d065aaa8)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

302         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_14268_299)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_302 ===
# file: method1.2/run.py  firstlineno: 302
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
302           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_302_e71f91cf_d7ea_4744_9b20_519fe1d25f72)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

306         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_14458_303)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_306 ===
# file: method1.2/run.py  firstlineno: 306
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
306           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_306_74013732_f3ec_49b0_a0b8_7857a767f057)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

310         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_14648_307)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_310 ===
# file: method1.2/run.py  firstlineno: 310
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
310           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_310_257aa1e7_5c1d_47d0_9ff4_1e6cb802c68f)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

314         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_14838_311)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_314 ===
# file: method1.2/run.py  firstlineno: 314
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
314           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_314_90caf2e9_7853_4e58_a6d9_614f87918371)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

318         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_15028_315)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_318 ===
# file: method1.2/run.py  firstlineno: 318
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
318           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_318_48021652_3745_488d_9846_4ff3bf6225fd)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

322         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_15218_319)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_322 ===
# file: method1.2/run.py  firstlineno: 322
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
322           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_322_71362e41_f3ae_4dcb_83a2_939a4a2da740)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

326         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_15408_323)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_326 ===
# file: method1.2/run.py  firstlineno: 326
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
326           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_326_a160bb59_23c6_4f39_aaa5_68c74acef9c8)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

330         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_15598_327)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_330 ===
# file: method1.2/run.py  firstlineno: 330
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
330           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_330_22cfa2ba_1006_4ded_a8a7_2105b517dca2)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

334         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_15788_331)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_334 ===
# file: method1.2/run.py  firstlineno: 334
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
334           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_334_dc165fc0_5578_4f9d_91f3_8166b07f1944)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

338         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_15978_335)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_338 ===
# file: method1.2/run.py  firstlineno: 338
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
338           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_338_f8db0dfc_6300_4729_8db3_f9f5e90ad517)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

342         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_16168_339)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_342 ===
# file: method1.2/run.py  firstlineno: 342
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
342           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_342_09e528f5_9aaa_4a83_b6ae_0822ebdcabb3)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

346         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_16358_343)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_346 ===
# file: method1.2/run.py  firstlineno: 346
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
346           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_346_15603d21_b78b_4f4b_b334_b2511428bc79)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

350         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_16548_347)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_350 ===
# file: method1.2/run.py  firstlineno: 350
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
350           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_350_5118a6d2_899f_4e2a_9a7a_c4fe97e5954e)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

354         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_16738_351)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_354 ===
# file: method1.2/run.py  firstlineno: 354
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
354           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_354_67788c0c_e5fc_4718_8b4d_a912c02e23e4)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

358         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_16928_355)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_358 ===
# file: method1.2/run.py  firstlineno: 358
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
358           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_358_f82cea11_afb0_45ad_bff2_9cf3f34a61b3)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

362         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_17118_359)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_362 ===
# file: method1.2/run.py  firstlineno: 362
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
362           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_362_db477460_a822_4b5d_904b_de1b6d1d8a10)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

366         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_17308_363)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_366 ===
# file: method1.2/run.py  firstlineno: 366
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
366           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_366_e0e61dad_9ab2_4c7e_ac20_b5020a9404a2)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

370         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_17498_367)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_370 ===
# file: method1.2/run.py  firstlineno: 370
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
370           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_370_d65c175f_f746_4187_9bd2_890316f25cf8)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

374         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_17688_371)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_374 ===
# file: method1.2/run.py  firstlineno: 374
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
374           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_374_63a8c5f9_83c1_4538_9d2d_3c277d9b18f5)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

378         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_17878_375)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_378 ===
# file: method1.2/run.py  firstlineno: 378
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
378           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_378_11065be5_6731_4ab2_af18_f9912b9b4bee)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

382         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_18068_379)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_382 ===
# file: method1.2/run.py  firstlineno: 382
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
382           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_382_7798e671_19c1_4b77_ba1d_ce324d93312b)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

386         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_18258_383)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_386 ===
# file: method1.2/run.py  firstlineno: 386
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
386           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_386_ec24543b_5ea1_45a3_9b3b_5f784359bf95)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

390         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_18448_387)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_390 ===
# file: method1.2/run.py  firstlineno: 390
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
390           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_390_6d5c758a_a633_49af_93d6_186747c91057)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

394         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_18638_391)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_394 ===
# file: method1.2/run.py  firstlineno: 394
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
394           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_394_90414b9a_c5cc_46d8_9d09_66833e8a29e6)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

398         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_18828_395)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


# === torch_dynamo_resume_in__method1_2_inner_at_398 ===
# file: method1.2/run.py  firstlineno: 398
# argcount: 4  varnames: ('__nested_resume_fns', '__nested_frame_values', '___stack0', 'out')
#
# MODIFIED BYTECODE
398           0 RESUME                   0
              2 LOAD_GLOBAL             11 (NULL + __compiled_fn_398_f45cf91f_fbf2_4163_8b61_62f05abbaed8)
             12 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             22 LOAD_ATTR               14 (record_pregraph_bytecode_enter)
             42 COPY                     1
             44 STORE_FAST               7 (tmp_1)
             46 CALL                     0
             54 STORE_FAST               8 (tmp_2)
             56 LOAD_FAST                3 (out)
             58 LOAD_GLOBAL             13 (NULL + __import_torch_dot__dynamo_dot_utils)
             68 LOAD_ATTR               16 (record_pregraph_bytecode_exit)
             88 COPY                     1
             90 STORE_FAST               9 (tmp_3)
             92 LOAD_FAST                8 (tmp_2)
             94 CALL                     1
            102 POP_TOP
            104 CALL                     1
            112 STORE_FAST               6 (graph_out_0)
            114 BUILD_TUPLE              0
            116 BUILD_LIST               1
            118 PUSH_NULL
            120 LOAD_GLOBAL              4 (torch)
            130 LOAD_ATTR                6 (_dynamo)
            150 LOAD_ATTR                8 (graph_break)
            170 LOAD_FAST                6 (graph_out_0)
            172 LOAD_CONST               9 (0)
            174 BINARY_SUBSCR
            178 BUILD_LIST               1
            180 COPY                     1
            182 LOAD_CONST               9 (0)
            184 LOAD_CONST              12 (1)
            186 BINARY_SLICE
            188 SWAP                     2
            190 BUILD_LIST               0
            192 LIST_EXTEND              2
            194 POP_TOP
            196 BUILD_LIST               1
            198 SWAP                     3
            200 SWAP                     2
            202 DELETE_FAST              6 (graph_out_0)

402         204 CALL                     0
            212 BUILD_LIST               1
            214 COPY                     2
            216 LOAD_CONST               9 (0)
            218 BINARY_SUBSCR
            222 LOAD_CONST               9 (0)
            224 LOAD_CONST               9 (0)
            226 STORE_SLICE
            228 COPY                     1
            230 LOAD_CONST               9 (0)
            232 BINARY_SUBSCR
            236 SWAP                     2
            238 POP_TOP
            240 BUILD_LIST               1
            242 SWAP                     2
            244 COPY                     1
            246 LOAD_CONST               9 (0)
            248 BINARY_SUBSCR
            252 SWAP                     2
            254 POP_TOP
            256 BUILD_LIST               1
            258 SWAP                     2
            260 COPY                     1
            262 LOAD_CONST               9 (0)
            264 BINARY_SUBSCR
            268 COPY                     1
            270 COPY                     1
            272 LOAD_CONST              12 (1)
            274 BINARY_SUBSCR
            278 SWAP                     2
            280 POP_TOP
            282 BUILD_LIST               1
            284 SWAP                     2
            286 LOAD_CONST              12 (1)
            288 LOAD_CONST               0 (None)
            290 STORE_SLICE
            292 COPY                     2
            294 POP_TOP
            296 BUILD_LIST               0
            298 SWAP                     3
            300 POP_TOP
            302 LOAD_GLOBAL             18 (__resume_at_19018_399)
            312 SWAP                     3
            314 SWAP                     2
            316 COPY                     1
            318 COPY                     1
            320 LOAD_CONST              13 (-1)
            322 BINARY_SUBSCR
            326 SWAP                     2
            328 LOAD_CONST              13 (-1)
            330 DELETE_SUBSCR
            332 SWAP                     3
            334 SWAP                     2
            336 BUILD_LIST               2
            338 SWAP                     2
            340 LIST_EXTEND              1
            342 PUSH_NULL
            344 SWAP                     3
            346 SWAP                     2
            348 CALL_FUNCTION_EX         0
            350 RETURN_VALUE


