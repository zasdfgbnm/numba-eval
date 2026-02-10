#pragma once

#include <cstdint>

// Allocate the input buffer for the benchmark (should be done outside timing).
// Returns the buffer pointer as a uint64_t.
uint64_t create_method4_input();

// Run the custom emulation chain (method4) on a pre-allocated buffer.
// Returns the final output buffer pointer (caller must free it).
//
// Notes:
// - Device selection is controlled by which `libcommon` was built/loaded.
uint64_t run_method4_custom_chain(uint64_t in_ptr);

// Free a buffer allocated by create_method4_input or returned by
// run_method4_custom_chain.
void free_method4_buf(uint64_t ptr);
