#pragma once

#include <cstdint>

// Allocate the input buffer for the benchmark (should be done outside timing).
// Returns the buffer pointer as a uint64_t.
uint64_t method4_create_input();

// Run the custom emulation chain (method4) on a pre-allocated buffer.
// Returns the final output buffer pointer (caller must free it).
//
// Notes:
// - Device selection is controlled by which `libcommon` was built/loaded.
uint64_t method4_custom_chain(uint64_t in_ptr);

// Free a buffer allocated by method4_create_input or returned by
// method4_custom_chain.
void method4_free_buf(uint64_t ptr);
