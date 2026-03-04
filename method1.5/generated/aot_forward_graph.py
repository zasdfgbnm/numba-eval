aot_config id: 0, fw_metadata=ViewAndMutationMeta(input_info=[InputAliasInfo(is_leaf=True, mutates_data=False, mutates_metadata=False, mutations_hidden_from_autograd=True, mutations_under_no_grad_or_inference_mode=False, mutation_inductor_storage_resize=False, mutates_storage_metadata=False, requires_grad=False, keep_input_mutations=True)], output_info=[], num_intermediate_bases=0, keep_input_mutations=True, traced_tangents=[], traced_tangents_descs=[], subclass_inp_meta=[PlainTensorMeta(unwrapped_idx=0, memory_format=None)], subclass_fw_graph_out_meta=[], subclass_tangent_meta=[], is_train=False, traced_tangent_metas=None, num_symints_saved_for_bw=None, num_tensors_saved_with_no_vc_check=None, num_opaque_objects_saved_for_bw=None, grad_enabled_mutation=None, deterministic=False, static_input_indices=[], tokens={}, indices_of_inputs_that_requires_grad_with_mutations_in_bw=[], bw_donated_idxs=None, num_backward_tokens=0, num_graphsafe_rng_states=0, graphsafe_rng_state_index=None, mutated_inp_stream_indices=None),subclass_metadata=None
TRACED GRAPH
 ===== Forward graph 0 =====
 /usr/local/lib/python3.12/dist-packages/torch/fx/_lazy_graph_module.py class <lambda>(torch.nn.Module):
    def forward(self, arg0_1: "f32[2, 3, 5, 7, 11, 13, 17, 19][4849845, 1616615, 323323, 46189, 4199, 323, 19, 1]cuda:0"):
        return ()


