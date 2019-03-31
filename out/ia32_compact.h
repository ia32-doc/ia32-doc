#pragma once
#include <stdint.h>

/**
 * @defgroup intel_manual \
 *           Intel Manual
 * @{
 */
/**
 * @defgroup control_registers \
 *           Control registers
 * @{
 */
typedef union {
  struct {
    uint64_t protection_enable                                       : 1;
    uint64_t monitor_coprocessor                                     : 1;
    uint64_t emulate_fpu                                             : 1;
    uint64_t task_switched                                           : 1;
    uint64_t extension_type                                          : 1;
    uint64_t numeric_error                                           : 1;
    uint64_t reserved_1                                              : 10;
    uint64_t write_protect                                           : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t alignment_mask                                          : 1;
    uint64_t reserved_3                                              : 10;
    uint64_t not_write_through                                       : 1;
    uint64_t cache_disable                                           : 1;
    uint64_t paging_enable                                           : 1;
  };

  uint64_t flags;
} cr0;

typedef union {
  struct {
    uint64_t reserved_1                                              : 3;
    uint64_t page_level_write_through                                : 1;
    uint64_t page_level_cache_disable                                : 1;
    uint64_t reserved_2                                              : 7;
    uint64_t address_of_page_directory                               : 36;
  };

  uint64_t flags;
} cr3;

typedef union {
  struct {
    uint64_t virtual_mode_extensions                                 : 1;
    uint64_t protected_mode_virtual_interrupts                       : 1;
    uint64_t timestamp_disable                                       : 1;
    uint64_t debugging_extensions                                    : 1;
    uint64_t page_size_extensions                                    : 1;
    uint64_t physical_address_extension                              : 1;
    uint64_t machine_check_enable                                    : 1;
    uint64_t page_global_enable                                      : 1;
    uint64_t performance_monitoring_counter_enable                   : 1;
    uint64_t os_fxsave_fxrstor_support                               : 1;
    uint64_t os_xmm_exception_support                                : 1;
    uint64_t usermode_instruction_prevention                         : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t vmx_enable                                              : 1;
    uint64_t smx_enable                                              : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t fsgsbase_enable                                         : 1;
    uint64_t pcid_enable                                             : 1;
    uint64_t os_xsave                                                : 1;
    uint64_t reserved_3                                              : 1;
    uint64_t smep_enable                                             : 1;
    uint64_t smap_enable                                             : 1;
    uint64_t protection_key_enable                                   : 1;
  };

  uint64_t flags;
} cr4;

typedef union {
  struct {
    uint64_t task_priority_level                                     : 4;
    uint64_t reserved                                                : 60;
  };

  uint64_t flags;
} cr8;

/**
 * @}
 */

/**
 * @defgroup debug_registers \
 *           Debug registers
 * @{
 */
typedef union {
  struct {
    uint64_t breakpoint_condition                                    : 4;
    uint64_t reserved_1                                              : 9;
    uint64_t debug_register_access_detected                          : 1;
    uint64_t single_instruction                                      : 1;
    uint64_t task_switch                                             : 1;
    uint64_t restricted_transactional_memory                         : 1;
  };

  uint64_t flags;
} dr6;

typedef union {
  struct {
    uint64_t local_breakpoint_0                                      : 1;
    uint64_t global_breakpoint_0                                     : 1;
    uint64_t local_breakpoint_1                                      : 1;
    uint64_t global_breakpoint_1                                     : 1;
    uint64_t local_breakpoint_2                                      : 1;
    uint64_t global_breakpoint_2                                     : 1;
    uint64_t local_breakpoint_3                                      : 1;
    uint64_t global_breakpoint_3                                     : 1;
    uint64_t local_exact_breakpoint                                  : 1;
    uint64_t global_exact_breakpoint                                 : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t restricted_transactional_memory                         : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t general_detect                                          : 1;
    uint64_t reserved_3                                              : 2;
    uint64_t read_write_0                                            : 2;
    uint64_t length_0                                                : 2;
    uint64_t read_write_1                                            : 2;
    uint64_t length_1                                                : 2;
    uint64_t read_write_2                                            : 2;
    uint64_t length_2                                                : 2;
    uint64_t read_write_3                                            : 2;
    uint64_t length_3                                                : 2;
  };

  uint64_t flags;
} dr7;

/**
 * @}
 */

/**
 * @defgroup cpuid \
 *           CPUID
 * @{
 */
#define CPUID_SIGNATURE                                              0x00000000
typedef struct {
  uint32_t max_cpuid_input_value;
  uint32_t ebx_value_genu;
  uint32_t ecx_value_ntel;
  uint32_t edx_value_inei;
} cpuid_eax_00;

#define CPUID_VERSION_INFO                                           0x00000001
typedef struct {
  union {
    struct {
      uint32_t stepping_id                                           : 4;
      uint32_t model                                                 : 4;
      uint32_t family_id                                             : 4;
      uint32_t processor_type                                        : 2;
      uint32_t reserved_1                                            : 2;
      uint32_t extended_model_id                                     : 4;
      uint32_t extended_family_id                                    : 8;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t brand_index                                           : 8;
      uint32_t clflush_line_size                                     : 8;
      uint32_t max_addressable_ids                                   : 8;
      uint32_t initial_apic_id                                       : 8;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t streaming_simd_extensions_3                           : 1;
      uint32_t pclmulqdq_instruction                                 : 1;
      uint32_t ds_area_64bit_layout                                  : 1;
      uint32_t monitor_mwait_instruction                             : 1;
      uint32_t cpl_qualified_debug_store                             : 1;
      uint32_t virtual_machine_extensions                            : 1;
      uint32_t safer_mode_extensions                                 : 1;
      uint32_t enhanced_intel_speedstep_technology                   : 1;
      uint32_t thermal_monitor_2                                     : 1;
      uint32_t supplemental_streaming_simd_extensions_3              : 1;
      uint32_t l1_context_id                                         : 1;
      uint32_t silicon_debug                                         : 1;
      uint32_t fma_extensions                                        : 1;
      uint32_t cmpxchg16b_instruction                                : 1;
      uint32_t xtpr_update_control                                   : 1;
      uint32_t perfmon_and_debug_capability                          : 1;
      uint32_t reserved_1                                            : 1;
      uint32_t process_context_identifiers                           : 1;
      uint32_t direct_cache_access                                   : 1;
      uint32_t sse41_support                                         : 1;
      uint32_t sse42_support                                         : 1;
      uint32_t x2apic_support                                        : 1;
      uint32_t movbe_instruction                                     : 1;
      uint32_t popcnt_instruction                                    : 1;
      uint32_t tsc_deadline                                          : 1;
      uint32_t aesni_instruction_extensions                          : 1;
      uint32_t xsave_xrstor_instruction                              : 1;
      uint32_t osx_save                                              : 1;
      uint32_t avx_support                                           : 1;
      uint32_t half_precision_conversion_instructions                : 1;
      uint32_t rdrand_instruction                                    : 1;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t floating_point_unit_on_chip                           : 1;
      uint32_t virtual_8086_mode_enhancements                        : 1;
      uint32_t debugging_extensions                                  : 1;
      uint32_t page_size_extension                                   : 1;
      uint32_t timestamp_counter                                     : 1;
      uint32_t rdmsr_wrmsr_instructions                              : 1;
      uint32_t physical_address_extension                            : 1;
      uint32_t machine_check_exception                               : 1;
      uint32_t cmpxchg8b_instruction                                 : 1;
      uint32_t apic_on_chip                                          : 1;
      uint32_t reserved_1                                            : 1;
      uint32_t sysenter_sysexit_instructions                         : 1;
      uint32_t memory_type_range_registers                           : 1;
      uint32_t page_global_bit                                       : 1;
      uint32_t machine_check_architecture                            : 1;
      uint32_t conditional_move_instructions                         : 1;
      uint32_t page_attribute_table                                  : 1;
      uint32_t page_size_extension_36bit                             : 1;
      uint32_t processor_serial_number                               : 1;
      uint32_t clflush_instruction                                   : 1;
      uint32_t reserved_2                                            : 1;
      uint32_t debug_store                                           : 1;
      uint32_t thermal_control_msrs_for_acpi                         : 1;
      uint32_t mmx_support                                           : 1;
      uint32_t fxsave_fxrstor_instructions                           : 1;
      uint32_t sse_support                                           : 1;
      uint32_t sse2_support                                          : 1;
      uint32_t self_snoop                                            : 1;
      uint32_t hyper_threading_technology                            : 1;
      uint32_t thermal_monitor                                       : 1;
      uint32_t reserved_3                                            : 1;
      uint32_t pending_break_enable                                  : 1;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_01;

#define CPUID_CACHE_PARAMS                                           0x00000004
typedef struct {
  union {
    struct {
      uint32_t cache_type_field                                      : 5;
      uint32_t cache_level                                           : 3;
      uint32_t self_initializing_cache_level                         : 1;
      uint32_t fully_associative_cache                               : 1;
      uint32_t reserved_1                                            : 4;
      uint32_t max_addressable_ids_for_logical_processors_sharing_this_cache: 12;
      uint32_t max_addressable_ids_for_processor_cores_in_physical_package: 6;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t system_coherency_line_size                            : 12;
      uint32_t physical_line_partitions                              : 10;
      uint32_t ways_of_associativity                                 : 10;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t number_of_sets                                        : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t write_back_invalidate                                 : 1;
      uint32_t cache_inclusiveness                                   : 1;
      uint32_t complex_cache_indexing                                : 1;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_04;

#define CPUID_MONITOR_MWAIT                                          0x00000005
typedef struct {
  union {
    struct {
      uint32_t smallest_monitor_line_size                            : 16;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t largest_monitor_line_size                             : 16;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t enumeration_of_monitor_mwait_extensions               : 1;
      uint32_t supports_treating_interrupts_as_break_event_for_mwait : 1;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t number_of_c0_sub_c_states                             : 4;
      uint32_t number_of_c1_sub_c_states                             : 4;
      uint32_t number_of_c2_sub_c_states                             : 4;
      uint32_t number_of_c3_sub_c_states                             : 4;
      uint32_t number_of_c4_sub_c_states                             : 4;
      uint32_t number_of_c5_sub_c_states                             : 4;
      uint32_t number_of_c6_sub_c_states                             : 4;
      uint32_t number_of_c7_sub_c_states                             : 4;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_05;

#define CPUID_THERMAL_POWER_MANAGEMENT                               0x00000006
typedef struct {
  union {
    struct {
      uint32_t temperature_sensor_supported                          : 1;
      uint32_t intel_turbo_boost_technology_available                : 1;
      uint32_t apic_timer_always_running                             : 1;
      uint32_t reserved_1                                            : 1;
      uint32_t power_limit_notification                              : 1;
      uint32_t clock_modulation_duty                                 : 1;
      uint32_t package_thermal_management                            : 1;
      uint32_t hwp_base_registers                                    : 1;
      uint32_t hwp_notification                                      : 1;
      uint32_t hwp_activity_window                                   : 1;
      uint32_t hwp_energy_performance_preference                     : 1;
      uint32_t hwp_package_level_request                             : 1;
      uint32_t reserved_2                                            : 1;
      uint32_t hdc                                                   : 1;
      uint32_t intel_turbo_boost_max_technology_3_available          : 1;
      uint32_t hwp_capabilities                                      : 1;
      uint32_t hwp_peci_override                                     : 1;
      uint32_t flexible_hwp                                          : 1;
      uint32_t fast_access_mode_for_hwp_request_msr                  : 1;
      uint32_t reserved_3                                            : 1;
      uint32_t ignoring_idle_logical_processor_hwp_request           : 1;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t number_of_interrupt_thresholds_in_thermal_sensor      : 4;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t hardware_coordination_feedback_capability             : 1;
      uint32_t reserved_1                                            : 2;
      uint32_t performance_energy_bias_preference                    : 1;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_06;

#define CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS                      0x00000007
typedef struct {
  union {
    struct {
      uint32_t number_of_sub_leaves                                  : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t fsgsbase                                              : 1;
      uint32_t ia32_tsc_adjust_msr                                   : 1;
      uint32_t sgx                                                   : 1;
      uint32_t bmi1                                                  : 1;
      uint32_t hle                                                   : 1;
      uint32_t avx2                                                  : 1;
      uint32_t fdp_excptn_only                                       : 1;
      uint32_t smep                                                  : 1;
      uint32_t bmi2                                                  : 1;
      uint32_t enhanced_rep_movsb_stosb                              : 1;
      uint32_t invpcid                                               : 1;
      uint32_t rtm                                                   : 1;
      uint32_t rdt_m                                                 : 1;
      uint32_t deprecates                                            : 1;
      uint32_t mpx                                                   : 1;
      uint32_t rdt                                                   : 1;
      uint32_t avx512f                                               : 1;
      uint32_t avx512dq                                              : 1;
      uint32_t rdseed                                                : 1;
      uint32_t adx                                                   : 1;
      uint32_t smap                                                  : 1;
      uint32_t avx512_ifma                                           : 1;
      uint32_t reserved_1                                            : 1;
      uint32_t clflushopt                                            : 1;
      uint32_t clwb                                                  : 1;
      uint32_t intel                                                 : 1;
      uint32_t avx512pf                                              : 1;
      uint32_t avx512er                                              : 1;
      uint32_t avx512cd                                              : 1;
      uint32_t sha                                                   : 1;
      uint32_t avx512bw                                              : 1;
      uint32_t avx512vl                                              : 1;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t prefetchwt1                                           : 1;
      uint32_t avx512_vbmi                                           : 1;
      uint32_t umip                                                  : 1;
      uint32_t pku                                                   : 1;
      uint32_t ospke                                                 : 1;
      uint32_t reserved_1                                            : 12;
      uint32_t mawau                                                 : 5;
      uint32_t rdpid                                                 : 1;
      uint32_t reserved_2                                            : 7;
      uint32_t sgx_lc                                                : 1;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_07;

#define CPUID_DIRECT_CACHE_ACCESS_INFO                               0x00000009
typedef struct {
  union {
    struct {
      uint32_t ia32_platform_dca_cap                                 : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_09;

#define CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING                   0x0000000A
typedef struct {
  union {
    struct {
      uint32_t version_id_of_architectural_performance_monitoring    : 8;
      uint32_t number_of_performance_monitoring_counter_per_logical_processor: 8;
      uint32_t bit_width_of_performance_monitoring_counter           : 8;
      uint32_t ebx_bit_vector_length                                 : 8;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t core_cycle_event_not_available                        : 1;
      uint32_t instruction_retired_event_not_available               : 1;
      uint32_t reference_cycles_event_not_available                  : 1;
      uint32_t last_level_cache_reference_event_not_available        : 1;
      uint32_t last_level_cache_misses_event_not_available           : 1;
      uint32_t branch_instruction_retired_event_not_available        : 1;
      uint32_t branch_mispredict_retired_event_not_available         : 1;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t number_of_fixed_function_performance_counters         : 5;
      uint32_t bit_width_of_fixed_function_performance_counters      : 8;
      uint32_t reserved_1                                            : 2;
      uint32_t any_thread_deprecation                                : 1;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_0a;

#define CPUID_EXTENDED_TOPOLOGY                                      0x0000000B
typedef struct {
  union {
    struct {
      uint32_t x2apic_id_to_unique_topology_id_shift                 : 5;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t number_of_logical_processors_at_this_level_type       : 16;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t level_number                                          : 8;
      uint32_t level_type                                            : 8;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t x2apic_id                                             : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_0b;

/**
 * @defgroup cpuid_eax_0d \
 *           EAX = 0x0D
 * @{
 */
#define CPUID_EXTENDED_STATE                                         0x0000000D
typedef struct {
  union {
    struct {
      uint32_t x87_state                                             : 1;
      uint32_t sse_state                                             : 1;
      uint32_t avx_state                                             : 1;
      uint32_t mpx_state                                             : 2;
      uint32_t avx_512_state                                         : 3;
      uint32_t used_for_ia32_xss_1                                   : 1;
      uint32_t pkru_state                                            : 1;
      uint32_t reserved_1                                            : 3;
      uint32_t used_for_ia32_xss_2                                   : 1;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t max_size_required_by_enabled_features_in_xcr0         : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t max_size_of_xsave_xrstor_save_area                    : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t xcr0_supported_bits                                   : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_0d_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t reserved_1                                            : 1;
      uint32_t supports_xsavec_and_compacted_xrstor                  : 1;
      uint32_t supports_xgetbv_with_ecx_1                            : 1;
      uint32_t supports_xsave_xrstor_and_ia32_xss                    : 1;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t size_of_xsave_aread                                   : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t used_for_xcr0_1                                       : 8;
      uint32_t pt_state                                              : 1;
      uint32_t used_for_xcr0_2                                       : 1;
      uint32_t reserved_1                                            : 3;
      uint32_t hwp_state                                             : 1;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_0d_ecx_01;

typedef struct {
  union {
    struct {
      uint32_t ia32_platform_dca_cap                                 : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t ecx_2                                                 : 1;
      uint32_t ecx_1                                                 : 1;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_0d_ecx_n;

/**
 * @}
 */

/**
 * @defgroup cpuid_eax_0f \
 *           EAX = 0x0F
 * @{
 */
#define CPUID_INTEL_RDT_MONITORING                                   0x0000000F
typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t rmid_max_range                                        : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved_1                                            : 1;
      uint32_t supports_l3_cache_intel_rdt_monitoring                : 1;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_0f_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t conversion_factor                                     : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t rmid_max_range                                        : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t supports_l3_occupancy_monitoring                      : 1;
      uint32_t supports_l3_total_bandwidth_monitoring                : 1;
      uint32_t supports_l3_local_bandwidth_monitoring                : 1;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_0f_ecx_01;

/**
 * @}
 */

/**
 * @defgroup cpuid_eax_10 \
 *           EAX = 0x10
 * @{
 */
#define CPUID_INTEL_RDT_ALLOCATION                                   0x00000010
typedef struct {
  union {
    struct {
      uint32_t ia32_platform_dca_cap                                 : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t reserved_1                                            : 1;
      uint32_t supports_l3_cache_allocation_technology               : 1;
      uint32_t supports_l2_cache_allocation_technology               : 1;
      uint32_t supports_memory_bandwidth_allocation                  : 1;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_10_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t length_of_capacity_bit_mask                           : 5;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t ebx_0                                                 : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved_1                                            : 2;
      uint32_t code_and_data_priorization_technology_supported       : 1;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t highest_cos_number_supported                          : 16;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_10_ecx_01;

typedef struct {
  union {
    struct {
      uint32_t length_of_capacity_bit_mask                           : 5;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t ebx_0                                                 : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t highest_cos_number_supported                          : 16;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_10_ecx_02;

typedef struct {
  union {
    struct {
      uint32_t max_mba_throttling_value                              : 12;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved_1                                            : 2;
      uint32_t response_of_delay_is_linear                           : 1;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t highest_cos_number_supported                          : 16;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_10_ecx_03;

/**
 * @}
 */

/**
 * @defgroup cpuid_eax_12 \
 *           EAX = 0x12
 * @{
 */
#define CPUID_INTEL_SGX                                              0x00000012
typedef struct {
  union {
    struct {
      uint32_t sgx1                                                  : 1;
      uint32_t sgx2                                                  : 1;
      uint32_t reserved_1                                            : 3;
      uint32_t sgx_enclv_advanced                                    : 1;
      uint32_t sgx_encls_advanced                                    : 1;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t miscselect                                            : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t max_enclave_size_not64                                : 8;
      uint32_t max_enclave_size_64                                   : 8;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_12_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t valid_secs_attributes_0                               : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t valid_secs_attributes_1                               : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t valid_secs_attributes_2                               : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t valid_secs_attributes_3                               : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_12_ecx_01;

typedef struct {
  union {
    struct {
      uint32_t sub_leaf_type                                         : 4;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t zero                                                  : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t zero                                                  : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t zero                                                  : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_12_ecx_02p_slt_0;

typedef struct {
  union {
    struct {
      uint32_t sub_leaf_type                                         : 4;
      uint32_t reserved_1                                            : 8;
      uint32_t epc_base_physical_address_1                           : 20;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t epc_base_physical_address_2                           : 20;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t epc_section_property                                  : 4;
      uint32_t reserved_1                                            : 8;
      uint32_t epc_size_1                                            : 20;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t epc_size_2                                            : 20;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_12_ecx_02p_slt_1;

/**
 * @}
 */

/**
 * @defgroup cpuid_eax_14 \
 *           EAX = 0x14
 * @{
 */
#define CPUID_INTEL_PROCESSOR_TRACE                                  0x00000014
typedef struct {
  union {
    struct {
      uint32_t max_sub_leaf                                          : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t flag0                                                 : 1;
      uint32_t flag1                                                 : 1;
      uint32_t flag2                                                 : 1;
      uint32_t flag3                                                 : 1;
      uint32_t flag4                                                 : 1;
      uint32_t flag5                                                 : 1;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t flag0                                                 : 1;
      uint32_t flag1                                                 : 1;
      uint32_t flag2                                                 : 1;
      uint32_t flag3                                                 : 1;
      uint32_t reserved_1                                            : 27;
      uint32_t flag31                                                : 1;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_14_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t number_of_configurable_address_ranges_for_filtering   : 3;
      uint32_t reserved_1                                            : 13;
      uint32_t bitmap_of_supported_mtc_period_encodings              : 16;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t bitmap_of_supported_cycle_threshold_value_encodings   : 16;
      uint32_t bitmap_of_supported_configurable_psb_frequency_encodings: 16;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_14_ecx_01;

/**
 * @}
 */

#define CPUID_TIME_STAMP_COUNTER                                     0x00000015
typedef struct {
  union {
    struct {
      uint32_t denominator                                           : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t numerator                                             : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t nominal_frequency                                     : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_15;

#define CPUID_PROCESSOR_FREQUENCY                                    0x00000016
typedef struct {
  union {
    struct {
      uint32_t procesor_base_frequency_mhz                           : 16;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t processor_maximum_frequency_mhz                       : 16;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t bus_frequency_mhz                                     : 16;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_16;

/**
 * @defgroup cpuid_eax_17 \
 *           EAX = 0x17
 * @{
 */
#define CPUID_SOC_VENDOR                                             0x00000017
typedef struct {
  union {
    struct {
      uint32_t max_soc_id_index                                      : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t soc_vendor_id                                         : 16;
      uint32_t is_vendor_scheme                                      : 1;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t project_id                                            : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t stepping_id                                           : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_17_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t soc_vendor_brand_string                               : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t soc_vendor_brand_string                               : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t soc_vendor_brand_string                               : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t soc_vendor_brand_string                               : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_17_ecx_01_03;

typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_17_ecx_n;

/**
 * @}
 */

/**
 * @defgroup cpuid_eax_18 \
 *           EAX = 0x18
 * @{
 */
#define CPUID_DETERMINISTIC_ADDRESS_TRANSLATION_PARAMETERS           0x00000018
typedef struct {
  union {
    struct {
      uint32_t max_sub_leaf                                          : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t page_entries_4kb_supported                            : 1;
      uint32_t page_entries_2mb_supported                            : 1;
      uint32_t page_entries_4mb_supported                            : 1;
      uint32_t page_entries_1gb_supported                            : 1;
      uint32_t reserved_1                                            : 4;
      uint32_t partitioning                                          : 3;
      uint32_t reserved_2                                            : 5;
      uint32_t ways_of_associativity_00                              : 16;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t number_of_sets                                        : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t translation_cache_type_field                          : 5;
      uint32_t translation_cache_level                               : 3;
      uint32_t fully_associative_structure                           : 1;
      uint32_t reserved_1                                            : 5;
      uint32_t max_addressable_ids_for_logical_processors            : 12;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_18_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t page_entries_4kb_supported                            : 1;
      uint32_t page_entries_2mb_supported                            : 1;
      uint32_t page_entries_4mb_supported                            : 1;
      uint32_t page_entries_1gb_supported                            : 1;
      uint32_t reserved_1                                            : 4;
      uint32_t partitioning                                          : 3;
      uint32_t reserved_2                                            : 5;
      uint32_t ways_of_associativity_01                              : 16;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t number_of_sets                                        : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t translation_cache_type_field                          : 5;
      uint32_t translation_cache_level                               : 3;
      uint32_t fully_associative_structure                           : 1;
      uint32_t reserved_1                                            : 5;
      uint32_t max_addressable_ids_for_logical_processors            : 12;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_18_ecx_01p;

/**
 * @}
 */

#define CPUID_EXTENDED_FUNCTION                                      0x80000000
typedef struct {
  union {
    struct {
      uint32_t max_extended_functions                                : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_80000000;

#define CPUID_EXTENDED_CPU_SIGNATURE                                 0x80000001
typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t lahf_sahf_available_in_64_bit_mode                    : 1;
      uint32_t reserved_1                                            : 4;
      uint32_t lzcnt                                                 : 1;
      uint32_t reserved_2                                            : 2;
      uint32_t prefetchw                                             : 1;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved_1                                            : 11;
      uint32_t syscall_sysret_available_in_64_bit_mode               : 1;
      uint32_t reserved_2                                            : 8;
      uint32_t execute_disable_bit_available                         : 1;
      uint32_t reserved_3                                            : 5;
      uint32_t pages_1gb_available                                   : 1;
      uint32_t rdtscp_available                                      : 1;
      uint32_t reserved_4                                            : 1;
      uint32_t ia64_available                                        : 1;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_80000001;

#define CPUID_BRAND_STRING1                                          0x80000002
#define CPUID_BRAND_STRING2                                          0x80000003
#define CPUID_BRAND_STRING3                                          0x80000004
typedef struct {
  union {
    struct {
      uint32_t processor_brand_string_1                              : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t processor_brand_string_2                              : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t processor_brand_string_3                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t processor_brand_string_4                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_80000002;

typedef struct {
  union {
    struct {
      uint32_t processor_brand_string_5                              : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t processor_brand_string_6                              : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t processor_brand_string_7                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t processor_brand_string_8                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_80000003;

typedef struct {
  union {
    struct {
      uint32_t processor_brand_string_9                              : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t processor_brand_string_10                             : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t processor_brand_string_11                             : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t processor_brand_string_12                             : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_80000004;

typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_80000005;

#define CPUID_EXTENDED_CACHE_INFO                                    0x80000006
typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t cache_line_size_in_bytes                              : 8;
      uint32_t reserved_1                                            : 4;
      uint32_t l2_associativity_field                                : 4;
      uint32_t cache_size_in_1k_units                                : 16;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_80000006;

#define CPUID_EXTENDED_TIME_STAMP_COUNTER                            0x80000007
typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
    };

    uint32_t flags;
  } ecx;

  union {
    struct {
      uint32_t reserved_1                                            : 8;
      uint32_t invariant_tsc_available                               : 1;
    };

    uint32_t flags;
  } edx;

} cpuid_eax_80000007;

/**
 * @}
 */

/**
 * @defgroup model_specific_registers \
 *           Model Specific Registers
 * @{
 */
/**
 * @defgroup ia32_p5_mc \
 *           IA32_P5_MC_(x)
 * @{
 */
#define IA32_P5_MC_ADDR                                              0x00000000
#define IA32_P5_MC_TYPE                                              0x00000001
/**
 * @}
 */

#define IA32_MONITOR_FILTER_SIZE                                     0x00000006
#define IA32_TIME_STAMP_COUNTER                                      0x00000010
#define IA32_PLATFORM_ID                                             0x00000017
typedef union {
  struct {
    uint64_t reserved_1                                              : 50;
    uint64_t platform_id                                             : 3;
  };

  uint64_t flags;
} ia32_platform_id_register;

#define IA32_APIC_BASE                                               0x0000001B
typedef union {
  struct {
    uint64_t reserved_1                                              : 8;
    uint64_t bsp_flag                                                : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t enable_x2apic_mode                                      : 1;
    uint64_t apic_global_enable                                      : 1;
    uint64_t apic_base                                               : 36;
  };

  uint64_t flags;
} ia32_apic_base_register;

#define IA32_FEATURE_CONTROL                                         0x0000003A
typedef union {
  struct {
    uint64_t lock_bit                                                : 1;
    uint64_t enable_vmx_inside_smx                                   : 1;
    uint64_t enable_vmx_outside_smx                                  : 1;
    uint64_t reserved_1                                              : 5;
    uint64_t senter_local_function_enables                           : 7;
    uint64_t senter_global_enable                                    : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t sgx_launch_control_enable                               : 1;
    uint64_t sgx_global_enable                                       : 1;
    uint64_t reserved_3                                              : 1;
    uint64_t lmce_on                                                 : 1;
  };

  uint64_t flags;
} ia32_feature_control_register;

#define IA32_TSC_ADJUST                                              0x0000003B
typedef struct {
  uint64_t thread_adjust;
} ia32_tsc_adjust_register;

#define IA32_BIOS_UPDT_TRIG                                          0x00000079
#define IA32_BIOS_SIGN_ID                                            0x0000008B
typedef union {
  struct {
    uint64_t reserved                                                : 32;
    uint64_t microcode_update_signature                              : 32;
  };

  uint64_t flags;
} ia32_bios_sign_id_register;

/**
 * @defgroup ia32_sgxlepubkeyhash \
 *           IA32_SGXLEPUBKEYHASH[(64*n+63):(64*n)]
 * @{
 */
#define IA32_SGXLEPUBKEYHASH0                                        0x0000008C
#define IA32_SGXLEPUBKEYHASH1                                        0x0000008D
#define IA32_SGXLEPUBKEYHASH2                                        0x0000008E
#define IA32_SGXLEPUBKEYHASH3                                        0x0000008F
/**
 * @}
 */

#define IA32_SMM_MONITOR_CTL                                         0x0000009B
typedef union {
  struct {
    uint64_t valid                                                   : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t smi_unblocking_by_vmxoff                                : 1;
    uint64_t reserved_2                                              : 9;
    uint64_t mseg_base                                               : 20;
  };

  uint64_t flags;
} ia32_smm_monitor_ctl_register;

typedef struct {
  uint32_t mseg_header_revision;
  uint32_t monitor_features;

#define IA32_STM_FEATURES_IA32E                                      0x00000001
  uint32_t gdtr_limit;
  uint32_t gdtr_base_offset;
  uint32_t cs_selector;
  uint32_t eip_offset;
  uint32_t esp_offset;
  uint32_t cr3_offset;
} ia32_mseg_header;

#define IA32_SMBASE                                                  0x0000009E
/**
 * @defgroup ia32_pmc \
 *           IA32_PMC(n)
 * @{
 */
#define IA32_PMC0                                                    0x000000C1
#define IA32_PMC1                                                    0x000000C2
#define IA32_PMC2                                                    0x000000C3
#define IA32_PMC3                                                    0x000000C4
#define IA32_PMC4                                                    0x000000C5
#define IA32_PMC5                                                    0x000000C6
#define IA32_PMC6                                                    0x000000C7
#define IA32_PMC7                                                    0x000000C8
/**
 * @}
 */

#define IA32_MPERF                                                   0x000000E7
typedef struct {
  uint64_t c0_mcnt;
} ia32_mperf_register;

#define IA32_APERF                                                   0x000000E8
typedef struct {
  uint64_t c0_acnt;
} ia32_aperf_register;

#define IA32_MTRRCAP                                                 0x000000FE
typedef union {
  struct {
    uint64_t variable_range_registers_count                          : 8;
    uint64_t fixed_range_registers_supported                         : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t write_combining                                         : 1;
    uint64_t system_management_range_register                        : 1;
  };

  uint64_t flags;
} ia32_mtrrcap_register;

#define IA32_SYSENTER_CS                                             0x00000174
typedef union {
  struct {
    uint64_t cs_selector                                             : 16;
    uint64_t not_used_1                                              : 16;
    uint64_t not_used_2                                              : 32;
  };

  uint64_t flags;
} ia32_sysenter_cs_register;

#define IA32_SYSENTER_ESP                                            0x00000175
#define IA32_SYSENTER_EIP                                            0x00000176
#define IA32_MCG_CAP                                                 0x00000179
typedef union {
  struct {
    uint64_t count                                                   : 8;
    uint64_t mcg_ctl_p                                               : 1;
    uint64_t mcg_ext_p                                               : 1;
    uint64_t mcp_cmci_p                                              : 1;
    uint64_t mcg_tes_p                                               : 1;
    uint64_t reserved_1                                              : 4;
    uint64_t mcg_ext_cnt                                             : 8;
    uint64_t mcg_ser_p                                               : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t mcg_elog_p                                              : 1;
    uint64_t mcg_lmce_p                                              : 1;
  };

  uint64_t flags;
} ia32_mcg_cap_register;

#define IA32_MCG_STATUS                                              0x0000017A
typedef union {
  struct {
    uint64_t ripv                                                    : 1;
    uint64_t eipv                                                    : 1;
    uint64_t mcip                                                    : 1;
    uint64_t lmce_s                                                  : 1;
  };

  uint64_t flags;
} ia32_mcg_status_register;

#define IA32_MCG_CTL                                                 0x0000017B
/**
 * @defgroup ia32_perfevtsel \
 *           IA32_PERFEVTSEL(n)
 * @{
 */
#define IA32_PERFEVTSEL0                                             0x00000186
#define IA32_PERFEVTSEL1                                             0x00000187
#define IA32_PERFEVTSEL2                                             0x00000188
#define IA32_PERFEVTSEL3                                             0x00000189
typedef union {
  struct {
    uint64_t event_select                                            : 8;
    uint64_t u_mask                                                  : 8;
    uint64_t usr                                                     : 1;
    uint64_t os                                                      : 1;
    uint64_t edge                                                    : 1;
    uint64_t pc                                                      : 1;
    uint64_t intr                                                    : 1;
    uint64_t any_thread                                              : 1;
    uint64_t en                                                      : 1;
    uint64_t inv                                                     : 1;
    uint64_t cmask                                                   : 8;
  };

  uint64_t flags;
} ia32_perfevtsel_register;

/**
 * @}
 */

#define IA32_PERF_STATUS                                             0x00000198
typedef union {
  struct {
    uint64_t current_performance_state_value                         : 16;
  };

  uint64_t flags;
} ia32_perf_status_register;

#define IA32_PERF_CTL                                                0x00000199
typedef union {
  struct {
    uint64_t target_performance_state_value                          : 16;
    uint64_t reserved_1                                              : 16;
    uint64_t ida_engage                                              : 1;
  };

  uint64_t flags;
} ia32_perf_ctl_register;

#define IA32_CLOCK_MODULATION                                        0x0000019A
typedef union {
  struct {
    uint64_t extended_on_demand_clock_modulation_duty_cycle          : 1;
    uint64_t on_demand_clock_modulation_duty_cycle                   : 3;
    uint64_t on_demand_clock_modulation_enable                       : 1;
  };

  uint64_t flags;
} ia32_clock_modulation_register;

#define IA32_THERM_INTERRUPT                                         0x0000019B
typedef union {
  struct {
    uint64_t high_temperature_interrupt_enable                       : 1;
    uint64_t low_temperature_interrupt_enable                        : 1;
    uint64_t prochot_interrupt_enable                                : 1;
    uint64_t forcepr_interrupt_enable                                : 1;
    uint64_t critical_temperature_interrupt_enable                   : 1;
    uint64_t reserved_1                                              : 3;
    uint64_t threshold1_value                                        : 7;
    uint64_t threshold1_interrupt_enable                             : 1;
    uint64_t threshold2_value                                        : 7;
    uint64_t threshold2_interrupt_enable                             : 1;
    uint64_t power_limit_notification_enable                         : 1;
  };

  uint64_t flags;
} ia32_therm_interrupt_register;

#define IA32_THERM_STATUS                                            0x0000019C
typedef union {
  struct {
    uint64_t thermal_status                                          : 1;
    uint64_t thermal_status_log                                      : 1;
    uint64_t prochot_forcepr_event                                   : 1;
    uint64_t prochot_forcepr_log                                     : 1;
    uint64_t critical_temperature_status                             : 1;
    uint64_t critical_temperature_status_log                         : 1;
    uint64_t thermal_threshold1_status                               : 1;
    uint64_t thermal_threshold1_log                                  : 1;
    uint64_t thermal_threshold2_status                               : 1;
    uint64_t thermal_threshold2_log                                  : 1;
    uint64_t power_limitation_status                                 : 1;
    uint64_t power_limitation_log                                    : 1;
    uint64_t current_limit_status                                    : 1;
    uint64_t current_limit_log                                       : 1;
    uint64_t cross_domain_limit_status                               : 1;
    uint64_t cross_domain_limit_log                                  : 1;
    uint64_t digital_readout                                         : 7;
    uint64_t reserved_1                                              : 4;
    uint64_t resolution_in_degrees_celsius                           : 4;
    uint64_t reading_valid                                           : 1;
  };

  uint64_t flags;
} ia32_therm_status_register;

#define IA32_MISC_ENABLE                                             0x000001A0
typedef union {
  struct {
    uint64_t fast_strings_enable                                     : 1;
    uint64_t reserved_1                                              : 2;
    uint64_t automatic_thermal_control_circuit_enable                : 1;
    uint64_t reserved_2                                              : 3;
    uint64_t performance_monitoring_available                        : 1;
    uint64_t reserved_3                                              : 3;
    uint64_t branch_trace_storage_unavailable                        : 1;
    uint64_t processor_event_based_sampling_unavailable              : 1;
    uint64_t reserved_4                                              : 3;
    uint64_t enhanced_intel_speedstep_technology_enable              : 1;
    uint64_t reserved_5                                              : 1;
    uint64_t enable_monitor_fsm                                      : 1;
    uint64_t reserved_6                                              : 3;
    uint64_t limit_cpuid_maxval                                      : 1;
    uint64_t xtpr_message_disable                                    : 1;
    uint64_t reserved_7                                              : 10;
    uint64_t xd_bit_disable                                          : 1;
  };

  uint64_t flags;
} ia32_misc_enable_register;

#define IA32_ENERGY_PERF_BIAS                                        0x000001B0
typedef union {
  struct {
    uint64_t power_policy_preference                                 : 4;
  };

  uint64_t flags;
} ia32_energy_perf_bias_register;

#define IA32_PACKAGE_THERM_STATUS                                    0x000001B1
typedef union {
  struct {
    uint64_t thermal_status                                          : 1;
    uint64_t thermal_status_log                                      : 1;
    uint64_t prochot_event                                           : 1;
    uint64_t prochot_log                                             : 1;
    uint64_t critical_temperature_status                             : 1;
    uint64_t critical_temperature_status_log                         : 1;
    uint64_t thermal_threshold1_status                               : 1;
    uint64_t thermal_threshold1_log                                  : 1;
    uint64_t thermal_threshold2_status                               : 1;
    uint64_t thermal_threshold2_log                                  : 1;
    uint64_t power_limitation_status                                 : 1;
    uint64_t power_limitation_log                                    : 1;
    uint64_t reserved_1                                              : 4;
    uint64_t digital_readout                                         : 7;
  };

  uint64_t flags;
} ia32_package_therm_status_register;

#define IA32_PACKAGE_THERM_INTERRUPT                                 0x000001B2
typedef union {
  struct {
    uint64_t high_temperature_interrupt_enable                       : 1;
    uint64_t low_temperature_interrupt_enable                        : 1;
    uint64_t prochot_interrupt_enable                                : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t overheat_interrupt_enable                               : 1;
    uint64_t reserved_2                                              : 3;
    uint64_t threshold1_value                                        : 7;
    uint64_t threshold1_interrupt_enable                             : 1;
    uint64_t threshold2_value                                        : 7;
    uint64_t threshold2_interrupt_enable                             : 1;
    uint64_t power_limit_notification_enable                         : 1;
  };

  uint64_t flags;
} ia32_package_therm_interrupt_register;

#define IA32_DEBUGCTL                                                0x000001D9
typedef union {
  struct {
    uint64_t lbr                                                     : 1;
    uint64_t btf                                                     : 1;
    uint64_t reserved_1                                              : 4;
    uint64_t tr                                                      : 1;
    uint64_t bts                                                     : 1;
    uint64_t btint                                                   : 1;
    uint64_t bts_off_os                                              : 1;
    uint64_t bts_off_usr                                             : 1;
    uint64_t freeze_lbrs_on_pmi                                      : 1;
    uint64_t freeze_perfmon_on_pmi                                   : 1;
    uint64_t enable_uncore_pmi                                       : 1;
    uint64_t freeze_while_smm                                        : 1;
    uint64_t rtm_debug                                               : 1;
  };

  uint64_t flags;
} ia32_debugctl_register;

#define IA32_SMRR_PHYSBASE                                           0x000001F2
typedef union {
  struct {
    uint64_t type                                                    : 8;
    uint64_t reserved_1                                              : 4;
    uint64_t smrr_physical_base_address                              : 20;
  };

  uint64_t flags;
} ia32_smrr_physbase_register;

#define IA32_SMRR_PHYSMASK                                           0x000001F3
typedef union {
  struct {
    uint64_t reserved_1                                              : 11;
    uint64_t enable_range_mask                                       : 1;
    uint64_t smrr_address_range_mask                                 : 20;
  };

  uint64_t flags;
} ia32_smrr_physmask_register;

#define IA32_PLATFORM_DCA_CAP                                        0x000001F8
#define IA32_CPU_DCA_CAP                                             0x000001F9
#define IA32_DCA_0_CAP                                               0x000001FA
typedef union {
  struct {
    uint64_t dca_active                                              : 1;
    uint64_t transaction                                             : 2;
    uint64_t dca_type                                                : 4;
    uint64_t dca_queue_size                                          : 4;
    uint64_t reserved_1                                              : 2;
    uint64_t dca_delay                                               : 4;
    uint64_t reserved_2                                              : 7;
    uint64_t sw_block                                                : 1;
    uint64_t reserved_3                                              : 1;
    uint64_t hw_block                                                : 1;
  };

  uint64_t flags;
} ia32_dca_0_cap_register;

/**
 * @defgroup ia32_mtrr_physbase \
 *           IA32_MTRR_PHYSBASE(n)
 * @{
 */
typedef union {
  struct {
    uint64_t type                                                    : 8;
    uint64_t reserved_1                                              : 4;
    uint64_t physical_addres_base                                    : 36;
  };

  uint64_t flags;
} ia32_mtrr_physbase_register;

#define IA32_MTRR_PHYSBASE0                                          0x00000200
#define IA32_MTRR_PHYSBASE1                                          0x00000202
#define IA32_MTRR_PHYSBASE2                                          0x00000204
#define IA32_MTRR_PHYSBASE3                                          0x00000206
#define IA32_MTRR_PHYSBASE4                                          0x00000208
#define IA32_MTRR_PHYSBASE5                                          0x0000020A
#define IA32_MTRR_PHYSBASE6                                          0x0000020C
#define IA32_MTRR_PHYSBASE7                                          0x0000020E
#define IA32_MTRR_PHYSBASE8                                          0x00000210
#define IA32_MTRR_PHYSBASE9                                          0x00000212
/**
 * @}
 */

/**
 * @defgroup ia32_mtrr_physmask \
 *           IA32_MTRR_PHYSMASK(n)
 * @{
 */
typedef union {
  struct {
    uint64_t type                                                    : 8;
    uint64_t reserved_1                                              : 3;
    uint64_t valid                                                   : 1;
    uint64_t physical_addres_mask                                    : 36;
  };

  uint64_t flags;
} ia32_mtrr_physmask_register;

#define IA32_MTRR_PHYSMASK0                                          0x00000201
#define IA32_MTRR_PHYSMASK1                                          0x00000203
#define IA32_MTRR_PHYSMASK2                                          0x00000205
#define IA32_MTRR_PHYSMASK3                                          0x00000207
#define IA32_MTRR_PHYSMASK4                                          0x00000209
#define IA32_MTRR_PHYSMASK5                                          0x0000020B
#define IA32_MTRR_PHYSMASK6                                          0x0000020D
#define IA32_MTRR_PHYSMASK7                                          0x0000020F
#define IA32_MTRR_PHYSMASK8                                          0x00000211
#define IA32_MTRR_PHYSMASK9                                          0x00000213
/**
 * @}
 */

/**
 * @defgroup ia32_mtrr_fix \
 *           IA32_MTRR_FIX(x)
 * @{
 */
/**
 * @defgroup ia32_mtrr_fix64k \
 *           IA32_MTRR_FIX64K(x)
 * @{
 */
#define IA32_MTRR_FIX64K_BASE                                        0x00000000
#define IA32_MTRR_FIX64K_SIZE                                        0x00010000
#define IA32_MTRR_FIX64K_00000                                       0x00000250
/**
 * @}
 */

/**
 * @defgroup ia32_mtrr_fix16k \
 *           IA32_MTRR_FIX16K(x)
 * @{
 */
#define IA32_MTRR_FIX16K_BASE                                        0x00080000
#define IA32_MTRR_FIX16K_SIZE                                        0x00004000
#define IA32_MTRR_FIX16K_80000                                       0x00000258
#define IA32_MTRR_FIX16K_A0000                                       0x00000259
/**
 * @}
 */

/**
 * @defgroup ia32_mtrr_fix4k \
 *           IA32_MTRR_FIX4K(x)
 * @{
 */
#define IA32_MTRR_FIX4K_BASE                                         0x000C0000
#define IA32_MTRR_FIX4K_SIZE                                         0x00001000
#define IA32_MTRR_FIX4K_C0000                                        0x00000268
#define IA32_MTRR_FIX4K_C8000                                        0x00000269
#define IA32_MTRR_FIX4K_D0000                                        0x0000026A
#define IA32_MTRR_FIX4K_D8000                                        0x0000026B
#define IA32_MTRR_FIX4K_E0000                                        0x0000026C
#define IA32_MTRR_FIX4K_E8000                                        0x0000026D
#define IA32_MTRR_FIX4K_F0000                                        0x0000026E
#define IA32_MTRR_FIX4K_F8000                                        0x0000026F
/**
 * @}
 */

#define IA32_MTRR_FIX_COUNT                                          ((1 + 2 + 8) * 8)
#define IA32_MTRR_VARIABLE_COUNT                                     0x000000FF
#define IA32_MTRR_COUNT                                              (IA32_MTRR_FIX_COUNT + IA32_MTRR_VARIABLE_COUNT)
/**
 * @}
 */

#define IA32_PAT                                                     0x00000277
typedef union {
  struct {
    uint64_t pa0                                                     : 3;
    uint64_t reserved_1                                              : 5;
    uint64_t pa1                                                     : 3;
    uint64_t reserved_2                                              : 5;
    uint64_t pa2                                                     : 3;
    uint64_t reserved_3                                              : 5;
    uint64_t pa3                                                     : 3;
    uint64_t reserved_4                                              : 5;
    uint64_t pa4                                                     : 3;
    uint64_t reserved_5                                              : 5;
    uint64_t pa5                                                     : 3;
    uint64_t reserved_6                                              : 5;
    uint64_t pa6                                                     : 3;
    uint64_t reserved_7                                              : 5;
    uint64_t pa7                                                     : 3;
  };

  uint64_t flags;
} ia32_pat_register;

/**
 * @defgroup ia32_mc_ctl2 \
 *           IA32_MC(i)_CTL2
 * @{
 */
#define IA32_MC0_CTL2                                                0x00000280
#define IA32_MC1_CTL2                                                0x00000281
#define IA32_MC2_CTL2                                                0x00000282
#define IA32_MC3_CTL2                                                0x00000283
#define IA32_MC4_CTL2                                                0x00000284
#define IA32_MC5_CTL2                                                0x00000285
#define IA32_MC6_CTL2                                                0x00000286
#define IA32_MC7_CTL2                                                0x00000287
#define IA32_MC8_CTL2                                                0x00000288
#define IA32_MC9_CTL2                                                0x00000289
#define IA32_MC10_CTL2                                               0x0000028A
#define IA32_MC11_CTL2                                               0x0000028B
#define IA32_MC12_CTL2                                               0x0000028C
#define IA32_MC13_CTL2                                               0x0000028D
#define IA32_MC14_CTL2                                               0x0000028E
#define IA32_MC15_CTL2                                               0x0000028F
#define IA32_MC16_CTL2                                               0x00000290
#define IA32_MC17_CTL2                                               0x00000291
#define IA32_MC18_CTL2                                               0x00000292
#define IA32_MC19_CTL2                                               0x00000293
#define IA32_MC20_CTL2                                               0x00000294
#define IA32_MC21_CTL2                                               0x00000295
#define IA32_MC22_CTL2                                               0x00000296
#define IA32_MC23_CTL2                                               0x00000297
#define IA32_MC24_CTL2                                               0x00000298
#define IA32_MC25_CTL2                                               0x00000299
#define IA32_MC26_CTL2                                               0x0000029A
#define IA32_MC27_CTL2                                               0x0000029B
#define IA32_MC28_CTL2                                               0x0000029C
#define IA32_MC29_CTL2                                               0x0000029D
#define IA32_MC30_CTL2                                               0x0000029E
#define IA32_MC31_CTL2                                               0x0000029F
typedef union {
  struct {
    uint64_t corrected_error_count_threshold                         : 15;
    uint64_t reserved_1                                              : 15;
    uint64_t cmci_en                                                 : 1;
  };

  uint64_t flags;
} ia32_mc_ctl2_register;

/**
 * @}
 */

#define IA32_MTRR_DEF_TYPE                                           0x000002FF
typedef union {
  struct {
    uint64_t default_memory_type                                     : 3;
    uint64_t reserved_1                                              : 7;
    uint64_t fixed_range_mtrr_enable                                 : 1;
    uint64_t mtrr_enable                                             : 1;
  };

  uint64_t flags;
} ia32_mtrr_def_type_register;

/**
 * @defgroup ia32_fixed_ctr \
 *           IA32_FIXED_CTR(n)
 * @{
 */
#define IA32_FIXED_CTR0                                              0x00000309
#define IA32_FIXED_CTR1                                              0x0000030A
#define IA32_FIXED_CTR2                                              0x0000030B
/**
 * @}
 */

#define IA32_PERF_CAPABILITIES                                       0x00000345
typedef union {
  struct {
    uint64_t lbr_format                                              : 6;
    uint64_t pebs_trap                                               : 1;
    uint64_t pebs_save_arch_regs                                     : 1;
    uint64_t pebs_record_format                                      : 4;
    uint64_t freeze_while_smm_is_supported                           : 1;
    uint64_t full_width_counter_write                                : 1;
  };

  uint64_t flags;
} ia32_perf_capabilities_register;

#define IA32_FIXED_CTR_CTRL                                          0x0000038D
typedef union {
  struct {
    uint64_t en0_os                                                  : 1;
    uint64_t en0_usr                                                 : 1;
    uint64_t any_thread0                                             : 1;
    uint64_t en0_pmi                                                 : 1;
    uint64_t en1_os                                                  : 1;
    uint64_t en1_usr                                                 : 1;
    uint64_t any_thread1                                             : 1;
    uint64_t en1_pmi                                                 : 1;
    uint64_t en2_os                                                  : 1;
    uint64_t en2_usr                                                 : 1;
    uint64_t any_thread2                                             : 1;
    uint64_t en2_pmi                                                 : 1;
  };

  uint64_t flags;
} ia32_fixed_ctr_ctrl_register;

#define IA32_PERF_GLOBAL_STATUS                                      0x0000038E
typedef union {
  struct {
    uint64_t ovf_pmc0                                                : 1;
    uint64_t ovf_pmc1                                                : 1;
    uint64_t ovf_pmc2                                                : 1;
    uint64_t ovf_pmc3                                                : 1;
    uint64_t reserved_1                                              : 28;
    uint64_t ovf_fixedctr0                                           : 1;
    uint64_t ovf_fixedctr1                                           : 1;
    uint64_t ovf_fixedctr2                                           : 1;
    uint64_t reserved_2                                              : 20;
    uint64_t trace_topa_pmi                                          : 1;
    uint64_t reserved_3                                              : 2;
    uint64_t lbr_frz                                                 : 1;
    uint64_t ctr_frz                                                 : 1;
    uint64_t asci                                                    : 1;
    uint64_t ovf_uncore                                              : 1;
    uint64_t ovf_buf                                                 : 1;
    uint64_t cond_chgd                                               : 1;
  };

  uint64_t flags;
} ia32_perf_global_status_register;

#define IA32_PERF_GLOBAL_CTRL                                        0x0000038F
typedef struct {
  uint32_t en_pmcn;
  uint32_t en_fixed_ctrn;
} ia32_perf_global_ctrl_register;

#define IA32_PERF_GLOBAL_STATUS_RESET                                0x00000390
typedef union {
  struct {
    uint64_t clear_ovf_pmcn                                          : 32;
    uint64_t clear_ovf_fixed_ctrn                                    : 3;
    uint64_t reserved_1                                              : 20;
    uint64_t clear_trace_topa_pmi                                    : 1;
    uint64_t reserved_2                                              : 2;
    uint64_t clear_lbr_frz                                           : 1;
    uint64_t clear_ctr_frz                                           : 1;
    uint64_t clear_asci                                              : 1;
    uint64_t clear_ovf_uncore                                        : 1;
    uint64_t clear_ovf_buf                                           : 1;
    uint64_t clear_cond_chgd                                         : 1;
  };

  uint64_t flags;
} ia32_perf_global_status_reset_register;

#define IA32_PERF_GLOBAL_STATUS_SET                                  0x00000391
typedef union {
  struct {
    uint64_t ovf_pmcn                                                : 32;
    uint64_t ovf_fixed_ctrn                                          : 3;
    uint64_t reserved_1                                              : 20;
    uint64_t trace_topa_pmi                                          : 1;
    uint64_t reserved_2                                              : 2;
    uint64_t lbr_frz                                                 : 1;
    uint64_t ctr_frz                                                 : 1;
    uint64_t asci                                                    : 1;
    uint64_t ovf_uncore                                              : 1;
    uint64_t ovf_buf                                                 : 1;
  };

  uint64_t flags;
} ia32_perf_global_status_set_register;

#define IA32_PERF_GLOBAL_INUSE                                       0x00000392
typedef union {
  struct {
    uint64_t ia32_perfevtseln_in_use                                 : 32;
    uint64_t ia32_fixed_ctrn_in_use                                  : 3;
    uint64_t reserved_1                                              : 28;
    uint64_t pmi_in_use                                              : 1;
  };

  uint64_t flags;
} ia32_perf_global_inuse_register;

#define IA32_PEBS_ENABLE                                             0x000003F1
typedef union {
  struct {
    uint64_t enable_pebs                                             : 1;
    uint64_t reservedormodelspecific1                                : 3;
    uint64_t reserved_1                                              : 28;
    uint64_t reservedormodelspecific2                                : 4;
  };

  uint64_t flags;
} ia32_pebs_enable_register;

/**
 * @defgroup ia32_mc_ctl \
 *           IA32_MC(i)_CTL
 * @{
 */
#define IA32_MC0_CTL                                                 0x00000400
#define IA32_MC1_CTL                                                 0x00000404
#define IA32_MC2_CTL                                                 0x00000408
#define IA32_MC3_CTL                                                 0x0000040C
#define IA32_MC4_CTL                                                 0x00000410
#define IA32_MC5_CTL                                                 0x00000414
#define IA32_MC6_CTL                                                 0x00000418
#define IA32_MC7_CTL                                                 0x0000041C
#define IA32_MC8_CTL                                                 0x00000420
#define IA32_MC9_CTL                                                 0x00000424
#define IA32_MC10_CTL                                                0x00000428
#define IA32_MC11_CTL                                                0x0000042C
#define IA32_MC12_CTL                                                0x00000430
#define IA32_MC13_CTL                                                0x00000434
#define IA32_MC14_CTL                                                0x00000438
#define IA32_MC15_CTL                                                0x0000043C
#define IA32_MC16_CTL                                                0x00000440
#define IA32_MC17_CTL                                                0x00000444
#define IA32_MC18_CTL                                                0x00000448
#define IA32_MC19_CTL                                                0x0000044C
#define IA32_MC20_CTL                                                0x00000450
#define IA32_MC21_CTL                                                0x00000454
#define IA32_MC22_CTL                                                0x00000458
#define IA32_MC23_CTL                                                0x0000045C
#define IA32_MC24_CTL                                                0x00000460
#define IA32_MC25_CTL                                                0x00000464
#define IA32_MC26_CTL                                                0x00000468
#define IA32_MC27_CTL                                                0x0000046C
#define IA32_MC28_CTL                                                0x00000470
/**
 * @}
 */

/**
 * @defgroup ia32_mc_status \
 *           IA32_MC(i)_STATUS
 * @{
 */
#define IA32_MC0_STATUS                                              0x00000401
#define IA32_MC1_STATUS                                              0x00000405
#define IA32_MC2_STATUS                                              0x00000409
#define IA32_MC3_STATUS                                              0x0000040D
#define IA32_MC4_STATUS                                              0x00000411
#define IA32_MC5_STATUS                                              0x00000415
#define IA32_MC6_STATUS                                              0x00000419
#define IA32_MC7_STATUS                                              0x0000041D
#define IA32_MC8_STATUS                                              0x00000421
#define IA32_MC9_STATUS                                              0x00000425
#define IA32_MC10_STATUS                                             0x00000429
#define IA32_MC11_STATUS                                             0x0000042D
#define IA32_MC12_STATUS                                             0x00000431
#define IA32_MC13_STATUS                                             0x00000435
#define IA32_MC14_STATUS                                             0x00000439
#define IA32_MC15_STATUS                                             0x0000043D
#define IA32_MC16_STATUS                                             0x00000441
#define IA32_MC17_STATUS                                             0x00000445
#define IA32_MC18_STATUS                                             0x00000449
#define IA32_MC19_STATUS                                             0x0000044D
#define IA32_MC20_STATUS                                             0x00000451
#define IA32_MC21_STATUS                                             0x00000455
#define IA32_MC22_STATUS                                             0x00000459
#define IA32_MC23_STATUS                                             0x0000045D
#define IA32_MC24_STATUS                                             0x00000461
#define IA32_MC25_STATUS                                             0x00000465
#define IA32_MC26_STATUS                                             0x00000469
#define IA32_MC27_STATUS                                             0x0000046D
#define IA32_MC28_STATUS                                             0x00000471
/**
 * @}
 */

/**
 * @defgroup ia32_mc_addr \
 *           IA32_MC(i)_ADDR
 * @{
 */
#define IA32_MC0_ADDR                                                0x00000402
#define IA32_MC1_ADDR                                                0x00000406
#define IA32_MC2_ADDR                                                0x0000040A
#define IA32_MC3_ADDR                                                0x0000040E
#define IA32_MC4_ADDR                                                0x00000412
#define IA32_MC5_ADDR                                                0x00000416
#define IA32_MC6_ADDR                                                0x0000041A
#define IA32_MC7_ADDR                                                0x0000041E
#define IA32_MC8_ADDR                                                0x00000422
#define IA32_MC9_ADDR                                                0x00000426
#define IA32_MC10_ADDR                                               0x0000042A
#define IA32_MC11_ADDR                                               0x0000042E
#define IA32_MC12_ADDR                                               0x00000432
#define IA32_MC13_ADDR                                               0x00000436
#define IA32_MC14_ADDR                                               0x0000043A
#define IA32_MC15_ADDR                                               0x0000043E
#define IA32_MC16_ADDR                                               0x00000442
#define IA32_MC17_ADDR                                               0x00000446
#define IA32_MC18_ADDR                                               0x0000044A
#define IA32_MC19_ADDR                                               0x0000044E
#define IA32_MC20_ADDR                                               0x00000452
#define IA32_MC21_ADDR                                               0x00000456
#define IA32_MC22_ADDR                                               0x0000045A
#define IA32_MC23_ADDR                                               0x0000045E
#define IA32_MC24_ADDR                                               0x00000462
#define IA32_MC25_ADDR                                               0x00000466
#define IA32_MC26_ADDR                                               0x0000046A
#define IA32_MC27_ADDR                                               0x0000046E
#define IA32_MC28_ADDR                                               0x00000472
/**
 * @}
 */

/**
 * @defgroup ia32_mc_misc \
 *           IA32_MC(i)_MISC
 * @{
 */
#define IA32_MC0_MISC                                                0x00000403
#define IA32_MC1_MISC                                                0x00000407
#define IA32_MC2_MISC                                                0x0000040B
#define IA32_MC3_MISC                                                0x0000040F
#define IA32_MC4_MISC                                                0x00000413
#define IA32_MC5_MISC                                                0x00000417
#define IA32_MC6_MISC                                                0x0000041B
#define IA32_MC7_MISC                                                0x0000041F
#define IA32_MC8_MISC                                                0x00000423
#define IA32_MC9_MISC                                                0x00000427
#define IA32_MC10_MISC                                               0x0000042B
#define IA32_MC11_MISC                                               0x0000042F
#define IA32_MC12_MISC                                               0x00000433
#define IA32_MC13_MISC                                               0x00000437
#define IA32_MC14_MISC                                               0x0000043B
#define IA32_MC15_MISC                                               0x0000043F
#define IA32_MC16_MISC                                               0x00000443
#define IA32_MC17_MISC                                               0x00000447
#define IA32_MC18_MISC                                               0x0000044B
#define IA32_MC19_MISC                                               0x0000044F
#define IA32_MC20_MISC                                               0x00000453
#define IA32_MC21_MISC                                               0x00000457
#define IA32_MC22_MISC                                               0x0000045B
#define IA32_MC23_MISC                                               0x0000045F
#define IA32_MC24_MISC                                               0x00000463
#define IA32_MC25_MISC                                               0x00000467
#define IA32_MC26_MISC                                               0x0000046B
#define IA32_MC27_MISC                                               0x0000046F
#define IA32_MC28_MISC                                               0x00000473
/**
 * @}
 */

#define IA32_VMX_BASIC                                               0x00000480
typedef union {
  struct {
    uint64_t vmcs_revision_id                                        : 31;
    uint64_t must_be_zero                                            : 1;
    uint64_t vmcs_size_in_bytes                                      : 13;
    uint64_t reserved_1                                              : 3;
    uint64_t vmcs_physical_address_width                             : 1;
    uint64_t dual_monitor                                            : 1;
    uint64_t memory_type                                             : 4;
    uint64_t ins_outs_vmexit_information                             : 1;
    uint64_t true_controls                                           : 1;
  };

  uint64_t flags;
} ia32_vmx_basic_register;

#define IA32_VMX_PINBASED_CTLS                                       0x00000481
typedef union {
  struct {
    uint64_t external_interrupt_exiting                              : 1;
    uint64_t reserved_1                                              : 2;
    uint64_t nmi_exiting                                             : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t virtual_nmis                                            : 1;
    uint64_t activate_vmx_preemption_timer                           : 1;
    uint64_t process_posted_interrupts                               : 1;
  };

  uint64_t flags;
} ia32_vmx_pinbased_ctls_register;

#define IA32_VMX_PROCBASED_CTLS                                      0x00000482
typedef union {
  struct {
    uint64_t reserved_1                                              : 2;
    uint64_t interrupt_window_exiting                                : 1;
    uint64_t use_tsc_offsetting                                      : 1;
    uint64_t reserved_2                                              : 3;
    uint64_t hlt_exiting                                             : 1;
    uint64_t reserved_3                                              : 1;
    uint64_t invlpg_exiting                                          : 1;
    uint64_t mwait_exiting                                           : 1;
    uint64_t rdpmc_exiting                                           : 1;
    uint64_t rdtsc_exiting                                           : 1;
    uint64_t reserved_4                                              : 2;
    uint64_t cr3_load_exiting                                        : 1;
    uint64_t cr3_store_exiting                                       : 1;
    uint64_t reserved_5                                              : 2;
    uint64_t cr8_load_exiting                                        : 1;
    uint64_t cr8_store_exiting                                       : 1;
    uint64_t use_tpr_shadow                                          : 1;
    uint64_t nmi_window_exiting                                      : 1;
    uint64_t mov_dr_exiting                                          : 1;
    uint64_t unconditional_io_exiting                                : 1;
    uint64_t use_io_bitmaps                                          : 1;
    uint64_t reserved_6                                              : 1;
    uint64_t monitor_trap_flag                                       : 1;
    uint64_t use_msr_bitmaps                                         : 1;
    uint64_t monitor_exiting                                         : 1;
    uint64_t pause_exiting                                           : 1;
    uint64_t activate_secondary_controls                             : 1;
  };

  uint64_t flags;
} ia32_vmx_procbased_ctls_register;

#define IA32_VMX_EXIT_CTLS                                           0x00000483
typedef union {
  struct {
    uint64_t reserved_1                                              : 2;
    uint64_t save_debug_controls                                     : 1;
    uint64_t reserved_2                                              : 6;
    uint64_t host_address_space_size                                 : 1;
    uint64_t reserved_3                                              : 2;
    uint64_t load_ia32_perf_global_ctrl                              : 1;
    uint64_t reserved_4                                              : 2;
    uint64_t acknowledge_interrupt_on_exit                           : 1;
    uint64_t reserved_5                                              : 2;
    uint64_t save_ia32_pat                                           : 1;
    uint64_t load_ia32_pat                                           : 1;
    uint64_t save_ia32_efer                                          : 1;
    uint64_t load_ia32_efer                                          : 1;
    uint64_t save_vmx_preemption_timer_value                         : 1;
    uint64_t clear_ia32_bndcfgs                                      : 1;
    uint64_t conceal_vmx_from_pt                                     : 1;
  };

  uint64_t flags;
} ia32_vmx_exit_ctls_register;

#define IA32_VMX_ENTRY_CTLS                                          0x00000484
typedef union {
  struct {
    uint64_t reserved_1                                              : 2;
    uint64_t load_debug_controls                                     : 1;
    uint64_t reserved_2                                              : 6;
    uint64_t ia32e_mode_guest                                        : 1;
    uint64_t entry_to_smm                                            : 1;
    uint64_t deactivate_dual_monitor_treatment                       : 1;
    uint64_t reserved_3                                              : 1;
    uint64_t load_ia32_perf_global_ctrl                              : 1;
    uint64_t load_ia32_pat                                           : 1;
    uint64_t load_ia32_efer                                          : 1;
    uint64_t load_ia32_bndcfgs                                       : 1;
    uint64_t conceal_vmx_from_pt                                     : 1;
  };

  uint64_t flags;
} ia32_vmx_entry_ctls_register;

#define IA32_VMX_MISC                                                0x00000485
typedef union {
  struct {
    uint64_t preemption_timer_tsc_relationship                       : 5;
    uint64_t store_efer_lma_on_vmexit                                : 1;
    uint64_t activity_states                                         : 3;
    uint64_t reserved_1                                              : 5;
    uint64_t intel_pt_available_in_vmx                               : 1;
    uint64_t rdmsr_can_read_ia32_smbase_msr_in_smm                   : 1;
    uint64_t cr3_target_count                                        : 9;
    uint64_t max_number_of_msr                                       : 3;
    uint64_t smm_monitor_ctl_b2                                      : 1;
    uint64_t vmwrite_vmexit_info                                     : 1;
    uint64_t zero_length_instruction_vmentry_injection               : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t mseg_id                                                 : 32;
  };

  uint64_t flags;
} ia32_vmx_misc_register;

#define IA32_VMX_CR0_FIXED0                                          0x00000486
#define IA32_VMX_CR0_FIXED1                                          0x00000487
#define IA32_VMX_CR4_FIXED0                                          0x00000488
#define IA32_VMX_CR4_FIXED1                                          0x00000489
#define IA32_VMX_VMCS_ENUM                                           0x0000048A
typedef union {
  struct {
    uint64_t access_type                                             : 1;
    uint64_t highest_index_value                                     : 9;
    uint64_t field_type                                              : 2;
    uint64_t reserved_1                                              : 1;
    uint64_t field_width                                             : 2;
  };

  uint64_t flags;
} ia32_vmx_vmcs_enum_register;

#define IA32_VMX_PROCBASED_CTLS2                                     0x0000048B
typedef union {
  struct {
    uint64_t virtualize_apic_accesses                                : 1;
    uint64_t enable_ept                                              : 1;
    uint64_t descriptor_table_exiting                                : 1;
    uint64_t enable_rdtscp                                           : 1;
    uint64_t virtualize_x2apic_mode                                  : 1;
    uint64_t enable_vpid                                             : 1;
    uint64_t wbinvd_exiting                                          : 1;
    uint64_t unrestricted_guest                                      : 1;
    uint64_t apic_register_virtualization                            : 1;
    uint64_t virtual_interrupt_delivery                              : 1;
    uint64_t pause_loop_exiting                                      : 1;
    uint64_t rdrand_exiting                                          : 1;
    uint64_t enable_invpcid                                          : 1;
    uint64_t enable_vm_functions                                     : 1;
    uint64_t vmcs_shadowing                                          : 1;
    uint64_t enable_encls_exiting                                    : 1;
    uint64_t rdseed_exiting                                          : 1;
    uint64_t enable_pml                                              : 1;
    uint64_t ept_violation                                           : 1;
    uint64_t conceal_vmx_from_pt                                     : 1;
    uint64_t enable_xsaves                                           : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t mode_based_execute_control_for_ept                      : 1;
    uint64_t reserved_2                                              : 2;
    uint64_t use_tsc_scaling                                         : 1;
  };

  uint64_t flags;
} ia32_vmx_procbased_ctls2_register;

#define IA32_VMX_EPT_VPID_CAP                                        0x0000048C
typedef union {
  struct {
    uint64_t execute_only_pages                                      : 1;
    uint64_t reserved_1                                              : 5;
    uint64_t page_walk_length_4                                      : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t memory_type_uncacheable                                 : 1;
    uint64_t reserved_3                                              : 5;
    uint64_t memory_type_write_back                                  : 1;
    uint64_t reserved_4                                              : 1;
    uint64_t pde_2mb_pages                                           : 1;
    uint64_t pdpte_1gb_pages                                         : 1;
    uint64_t reserved_5                                              : 2;
    uint64_t invept                                                  : 1;
    uint64_t ept_accessed_and_dirty_flags                            : 1;
    uint64_t advanced_vmexit_ept_violations_information              : 1;
    uint64_t reserved_6                                              : 2;
    uint64_t invept_single_context                                   : 1;
    uint64_t invept_all_contexts                                     : 1;
    uint64_t reserved_7                                              : 5;
    uint64_t invvpid                                                 : 1;
    uint64_t reserved_8                                              : 7;
    uint64_t invvpid_individual_address                              : 1;
    uint64_t invvpid_single_context                                  : 1;
    uint64_t invvpid_all_contexts                                    : 1;
    uint64_t invvpid_single_context_retain_globals                   : 1;
  };

  uint64_t flags;
} ia32_vmx_ept_vpid_cap_register;

/**
 * @defgroup ia32_vmx_true_ctls \
 *           IA32_VMX_TRUE_(x)_CTLS
 * @{
 */
#define IA32_VMX_TRUE_PINBASED_CTLS                                  0x0000048D
#define IA32_VMX_TRUE_PROCBASED_CTLS                                 0x0000048E
#define IA32_VMX_TRUE_EXIT_CTLS                                      0x0000048F
#define IA32_VMX_TRUE_ENTRY_CTLS                                     0x00000490
typedef union {
  struct {
    uint64_t allowed_0_settings                                      : 32;
    uint64_t allowed_1_settings                                      : 32;
  };

  uint64_t flags;
} ia32_vmx_true_ctls_register;

/**
 * @}
 */

#define IA32_VMX_VMFUNC                                              0x00000491
typedef union {
  struct {
    uint64_t eptp_switching                                          : 1;
  };

  uint64_t flags;
} ia32_vmx_vmfunc_register;

/**
 * @defgroup ia32_a_pmc \
 *           IA32_A_PMC(n)
 * @{
 */
#define IA32_A_PMC0                                                  0x000004C1
#define IA32_A_PMC1                                                  0x000004C2
#define IA32_A_PMC2                                                  0x000004C3
#define IA32_A_PMC3                                                  0x000004C4
#define IA32_A_PMC4                                                  0x000004C5
#define IA32_A_PMC5                                                  0x000004C6
#define IA32_A_PMC6                                                  0x000004C7
#define IA32_A_PMC7                                                  0x000004C8
/**
 * @}
 */

#define IA32_MCG_EXT_CTL                                             0x000004D0
typedef union {
  struct {
    uint64_t lmce_en                                                 : 1;
  };

  uint64_t flags;
} ia32_mcg_ext_ctl_register;

#define IA32_SGX_SVN_STATUS                                          0x00000500
typedef union {
  struct {
    uint64_t lock                                                    : 1;
    uint64_t reserved_1                                              : 15;
    uint64_t sgx_svn_sinit                                           : 8;
  };

  uint64_t flags;
} ia32_sgx_svn_status_register;

#define IA32_RTIT_OUTPUT_BASE                                        0x00000560
typedef union {
  struct {
    uint64_t reserved_1                                              : 7;
    uint64_t base_physical_address                                   : 41;
  };

  uint64_t flags;
} ia32_rtit_output_base_register;

#define IA32_RTIT_OUTPUT_MASK_PTRS                                   0x00000561
typedef union {
  struct {
    uint64_t lower_mask                                              : 7;
    uint64_t mask_or_table_offset                                    : 25;
    uint64_t output_offset                                           : 32;
  };

  uint64_t flags;
} ia32_rtit_output_mask_ptrs_register;

#define IA32_RTIT_CTL                                                0x00000570
typedef union {
  struct {
    uint64_t trace_en                                                : 1;
    uint64_t cyc_en                                                  : 1;
    uint64_t os                                                      : 1;
    uint64_t user                                                    : 1;
    uint64_t pwr_evt_en                                              : 1;
    uint64_t fup_on_ptw                                              : 1;
    uint64_t fabric_en                                               : 1;
    uint64_t cr3_filter                                              : 1;
    uint64_t topa                                                    : 1;
    uint64_t mtc_en                                                  : 1;
    uint64_t tsc_en                                                  : 1;
    uint64_t dis_retc                                                : 1;
    uint64_t ptw_en                                                  : 1;
    uint64_t branch_en                                               : 1;
    uint64_t mtc_freq                                                : 4;
    uint64_t reserved_1                                              : 1;
    uint64_t cyc_thresh                                              : 4;
    uint64_t reserved_2                                              : 1;
    uint64_t psb_freq                                                : 4;
    uint64_t reserved_3                                              : 4;
    uint64_t addr0_cfg                                               : 4;
    uint64_t addr1_cfg                                               : 4;
    uint64_t addr2_cfg                                               : 4;
    uint64_t addr3_cfg                                               : 4;
    uint64_t reserved_4                                              : 8;
    uint64_t inject_psb_pmi_on_enable                                : 1;
  };

  uint64_t flags;
} ia32_rtit_ctl_register;

#define IA32_RTIT_STATUS                                             0x00000571
typedef union {
  struct {
    uint64_t filter_en                                               : 1;
    uint64_t contex_en                                               : 1;
    uint64_t trigger_en                                              : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t error                                                   : 1;
    uint64_t stopped                                                 : 1;
    uint64_t pend_psb                                                : 1;
    uint64_t pend_topa_pmi                                           : 1;
    uint64_t reserved_2                                              : 24;
    uint64_t packet_byte_cnt                                         : 17;
  };

  uint64_t flags;
} ia32_rtit_status_register;

#define IA32_RTIT_CR3_MATCH                                          0x00000572
typedef union {
  struct {
    uint64_t reserved_1                                              : 5;
    uint64_t cr3_value_to_match                                      : 59;
  };

  uint64_t flags;
} ia32_rtit_cr3_match_register;

/**
 * @defgroup ia32_rtit_addr \
 *           IA32_RTIT_ADDR(x)
 * @{
 */
/**
 * @defgroup ia32_rtit_addr_a \
 *           IA32_RTIT_ADDR(n)_A
 * @{
 */
#define IA32_RTIT_ADDR0_A                                            0x00000580
#define IA32_RTIT_ADDR1_A                                            0x00000582
#define IA32_RTIT_ADDR2_A                                            0x00000584
#define IA32_RTIT_ADDR3_A                                            0x00000586
/**
 * @}
 */

/**
 * @defgroup ia32_rtit_addr_b \
 *           IA32_RTIT_ADDR(n)_B
 * @{
 */
#define IA32_RTIT_ADDR0_B                                            0x00000581
#define IA32_RTIT_ADDR1_B                                            0x00000583
#define IA32_RTIT_ADDR2_B                                            0x00000585
#define IA32_RTIT_ADDR3_B                                            0x00000587
/**
 * @}
 */

typedef union {
  struct {
    uint64_t virtual_address                                         : 48;
    uint64_t sign_ext_va                                             : 16;
  };

  uint64_t flags;
} ia32_rtit_addr_register;

/**
 * @}
 */

#define IA32_DS_AREA                                                 0x00000600
#define IA32_TSC_DEADLINE                                            0x000006E0
#define IA32_PM_ENABLE                                               0x00000770
typedef union {
  struct {
    uint64_t hwp_enable                                              : 1;
  };

  uint64_t flags;
} ia32_pm_enable_register;

#define IA32_HWP_CAPABILITIES                                        0x00000771
typedef union {
  struct {
    uint64_t highest_performance                                     : 8;
    uint64_t guaranteed_performance                                  : 8;
    uint64_t most_efficient_performance                              : 8;
    uint64_t lowest_performance                                      : 8;
  };

  uint64_t flags;
} ia32_hwp_capabilities_register;

#define IA32_HWP_REQUEST_PKG                                         0x00000772
typedef union {
  struct {
    uint64_t minimum_performance                                     : 8;
    uint64_t maximum_performance                                     : 8;
    uint64_t desired_performance                                     : 8;
    uint64_t energy_performance_preference                           : 8;
    uint64_t activity_window                                         : 10;
  };

  uint64_t flags;
} ia32_hwp_request_pkg_register;

#define IA32_HWP_INTERRUPT                                           0x00000773
typedef union {
  struct {
    uint64_t en_guaranteed_performance_change                        : 1;
    uint64_t en_excursion_minimum                                    : 1;
  };

  uint64_t flags;
} ia32_hwp_interrupt_register;

#define IA32_HWP_REQUEST                                             0x00000774
typedef union {
  struct {
    uint64_t minimum_performance                                     : 8;
    uint64_t maximum_performance                                     : 8;
    uint64_t desired_performance                                     : 8;
    uint64_t energy_performance_preference                           : 8;
    uint64_t activity_window                                         : 10;
    uint64_t package_control                                         : 1;
  };

  uint64_t flags;
} ia32_hwp_request_register;

#define IA32_HWP_STATUS                                              0x00000777
typedef union {
  struct {
    uint64_t guaranteed_performance_change                           : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t excursion_to_minimum                                    : 1;
  };

  uint64_t flags;
} ia32_hwp_status_register;

#define IA32_X2APIC_APICID                                           0x00000802
#define IA32_X2APIC_VERSION                                          0x00000803
#define IA32_X2APIC_TPR                                              0x00000808
#define IA32_X2APIC_PPR                                              0x0000080A
#define IA32_X2APIC_EOI                                              0x0000080B
#define IA32_X2APIC_LDR                                              0x0000080D
#define IA32_X2APIC_SIVR                                             0x0000080F
/**
 * @defgroup ia32_x2apic_isr \
 *           IA32_X2APIC_ISR(n)
 * @{
 */
#define IA32_X2APIC_ISR0                                             0x00000810
#define IA32_X2APIC_ISR1                                             0x00000811
#define IA32_X2APIC_ISR2                                             0x00000812
#define IA32_X2APIC_ISR3                                             0x00000813
#define IA32_X2APIC_ISR4                                             0x00000814
#define IA32_X2APIC_ISR5                                             0x00000815
#define IA32_X2APIC_ISR6                                             0x00000816
#define IA32_X2APIC_ISR7                                             0x00000817
/**
 * @}
 */

/**
 * @defgroup ia32_x2apic_tmr \
 *           IA32_X2APIC_TMR(n)
 * @{
 */
#define IA32_X2APIC_TMR0                                             0x00000818
#define IA32_X2APIC_TMR1                                             0x00000819
#define IA32_X2APIC_TMR2                                             0x0000081A
#define IA32_X2APIC_TMR3                                             0x0000081B
#define IA32_X2APIC_TMR4                                             0x0000081C
#define IA32_X2APIC_TMR5                                             0x0000081D
#define IA32_X2APIC_TMR6                                             0x0000081E
#define IA32_X2APIC_TMR7                                             0x0000081F
/**
 * @}
 */

/**
 * @defgroup ia32_x2apic_irr \
 *           IA32_X2APIC_IRR(n)
 * @{
 */
#define IA32_X2APIC_IRR0                                             0x00000820
#define IA32_X2APIC_IRR1                                             0x00000821
#define IA32_X2APIC_IRR2                                             0x00000822
#define IA32_X2APIC_IRR3                                             0x00000823
#define IA32_X2APIC_IRR4                                             0x00000824
#define IA32_X2APIC_IRR5                                             0x00000825
#define IA32_X2APIC_IRR6                                             0x00000826
#define IA32_X2APIC_IRR7                                             0x00000827
/**
 * @}
 */

#define IA32_X2APIC_ESR                                              0x00000828
#define IA32_X2APIC_LVT_CMCI                                         0x0000082F
#define IA32_X2APIC_ICR                                              0x00000830
#define IA32_X2APIC_LVT_TIMER                                        0x00000832
#define IA32_X2APIC_LVT_THERMAL                                      0x00000833
#define IA32_X2APIC_LVT_PMI                                          0x00000834
#define IA32_X2APIC_LVT_LINT0                                        0x00000835
#define IA32_X2APIC_LVT_LINT1                                        0x00000836
#define IA32_X2APIC_LVT_ERROR                                        0x00000837
#define IA32_X2APIC_INIT_COUNT                                       0x00000838
#define IA32_X2APIC_CUR_COUNT                                        0x00000839
#define IA32_X2APIC_DIV_CONF                                         0x0000083E
#define IA32_X2APIC_SELF_IPI                                         0x0000083F
#define IA32_DEBUG_INTERFACE                                         0x00000C80
typedef union {
  struct {
    uint64_t enable                                                  : 1;
    uint64_t reserved_1                                              : 29;
    uint64_t lock                                                    : 1;
    uint64_t debug_occurred                                          : 1;
  };

  uint64_t flags;
} ia32_debug_interface_register;

#define IA32_L3_QOS_CFG                                              0x00000C81
typedef union {
  struct {
    uint64_t enable                                                  : 1;
  };

  uint64_t flags;
} ia32_l3_qos_cfg_register;

#define IA32_L2_QOS_CFG                                              0x00000C82
typedef union {
  struct {
    uint64_t enable                                                  : 1;
  };

  uint64_t flags;
} ia32_l2_qos_cfg_register;

#define IA32_QM_EVTSEL                                               0x00000C8D
typedef union {
  struct {
    uint64_t event_id                                                : 8;
    uint64_t reserved_1                                              : 24;
    uint64_t resource_monitoring_id                                  : 32;
  };

  uint64_t flags;
} ia32_qm_evtsel_register;

#define IA32_QM_CTR                                                  0x00000C8E
typedef union {
  struct {
    uint64_t resource_monitored_data                                 : 62;
    uint64_t unavailable                                             : 1;
    uint64_t error                                                   : 1;
  };

  uint64_t flags;
} ia32_qm_ctr_register;

#define IA32_PQR_ASSOC                                               0x00000C8F
typedef union {
  struct {
    uint64_t resource_monitoring_id                                  : 32;
    uint64_t cos                                                     : 32;
  };

  uint64_t flags;
} ia32_pqr_assoc_register;

#define IA32_BNDCFGS                                                 0x00000D90
typedef union {
  struct {
    uint64_t enable                                                  : 1;
    uint64_t bnd_preserve                                            : 1;
    uint64_t reserved_1                                              : 10;
    uint64_t bound_directory_base_address                            : 52;
  };

  uint64_t flags;
} ia32_bndcfgs_register;

#define IA32_XSS                                                     0x00000DA0
typedef union {
  struct {
    uint64_t reserved_1                                              : 8;
    uint64_t trace_packet_configuration_state                        : 1;
  };

  uint64_t flags;
} ia32_xss_register;

#define IA32_PKG_HDC_CTL                                             0x00000DB0
typedef union {
  struct {
    uint64_t hdc_pkg_enable                                          : 1;
  };

  uint64_t flags;
} ia32_pkg_hdc_ctl_register;

#define IA32_PM_CTL1                                                 0x00000DB1
typedef union {
  struct {
    uint64_t hdc_allow_block                                         : 1;
  };

  uint64_t flags;
} ia32_pm_ctl1_register;

#define IA32_THREAD_STALL                                            0x00000DB2
typedef struct {
  uint64_t stall_cycle_cnt;
} ia32_thread_stall_register;

#define IA32_EFER                                                    0xC0000080
typedef union {
  struct {
    uint64_t syscall_enable                                          : 1;
    uint64_t reserved_1                                              : 7;
    uint64_t ia32e_mode_enable                                       : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t ia32e_mode_active                                       : 1;
    uint64_t execute_disable_bit_enable                              : 1;
  };

  uint64_t flags;
} ia32_efer_register;

#define IA32_STAR                                                    0xC0000081
#define IA32_LSTAR                                                   0xC0000082
#define IA32_CSTAR                                                   0xC0000083
#define IA32_FMASK                                                   0xC0000084
#define IA32_FS_BASE                                                 0xC0000100
#define IA32_GS_BASE                                                 0xC0000101
#define IA32_KERNEL_GS_BASE                                          0xC0000102
#define IA32_TSC_AUX                                                 0xC0000103
typedef union {
  struct {
    uint64_t tsc_auxiliary_signature                                 : 32;
  };

  uint64_t flags;
} ia32_tsc_aux_register;

/**
 * @}
 */

/**
 * @defgroup paging \
 *           Paging
 * @{
 */
/**
 * @defgroup paging_32 \
 *           32-Bit Paging
 * @{
 */
typedef union {
  struct {
    uint32_t present                                                 : 1;
    uint32_t write                                                   : 1;
    uint32_t supervisor                                              : 1;
    uint32_t page_level_write_through                                : 1;
    uint32_t page_level_cache_disable                                : 1;
    uint32_t accessed                                                : 1;
    uint32_t dirty                                                   : 1;
    uint32_t large_page                                              : 1;
    uint32_t global                                                  : 1;
    uint32_t ignored_1                                               : 3;
    uint32_t pat                                                     : 1;
    uint32_t page_frame_number_low                                   : 8;
    uint32_t reserved_1                                              : 1;
    uint32_t page_frame_number_high                                  : 10;
  };

  uint32_t flags;
} pde_4mb_32;

typedef union {
  struct {
    uint32_t present                                                 : 1;
    uint32_t write                                                   : 1;
    uint32_t supervisor                                              : 1;
    uint32_t page_level_write_through                                : 1;
    uint32_t page_level_cache_disable                                : 1;
    uint32_t accessed                                                : 1;
    uint32_t ignored_1                                               : 1;
    uint32_t large_page                                              : 1;
    uint32_t ignored_2                                               : 4;
    uint32_t page_frame_number                                       : 20;
  };

  uint32_t flags;
} pde_32;

typedef union {
  struct {
    uint32_t present                                                 : 1;
    uint32_t write                                                   : 1;
    uint32_t supervisor                                              : 1;
    uint32_t page_level_write_through                                : 1;
    uint32_t page_level_cache_disable                                : 1;
    uint32_t accessed                                                : 1;
    uint32_t dirty                                                   : 1;
    uint32_t pat                                                     : 1;
    uint32_t global                                                  : 1;
    uint32_t ignored_1                                               : 3;
    uint32_t page_frame_number                                       : 20;
  };

  uint32_t flags;
} pte_32;

typedef union {
  struct {
    uint32_t present                                                 : 1;
    uint32_t write                                                   : 1;
    uint32_t supervisor                                              : 1;
    uint32_t page_level_write_through                                : 1;
    uint32_t page_level_cache_disable                                : 1;
    uint32_t accessed                                                : 1;
    uint32_t dirty                                                   : 1;
    uint32_t large_page                                              : 1;
    uint32_t global                                                  : 1;
    uint32_t ignored_1                                               : 3;
    uint32_t page_frame_number                                       : 20;
  };

  uint32_t flags;
} pt_entry_32;

/**
 * @}
 */

/**
 * @defgroup paging_64 \
 *           64-Bit (4-Level) Paging
 * @{
 */
typedef union {
  struct {
    uint64_t present                                                 : 1;
    uint64_t write                                                   : 1;
    uint64_t supervisor                                              : 1;
    uint64_t page_level_write_through                                : 1;
    uint64_t page_level_cache_disable                                : 1;
    uint64_t accessed                                                : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t must_be_zero                                            : 1;
    uint64_t ignored_1                                               : 4;
    uint64_t page_frame_number                                       : 36;
    uint64_t reserved_2                                              : 4;
    uint64_t ignored_2                                               : 11;
    uint64_t execute_disable                                         : 1;
  };

  uint64_t flags;
} pml4e_64;

typedef union {
  struct {
    uint64_t present                                                 : 1;
    uint64_t write                                                   : 1;
    uint64_t supervisor                                              : 1;
    uint64_t page_level_write_through                                : 1;
    uint64_t page_level_cache_disable                                : 1;
    uint64_t accessed                                                : 1;
    uint64_t dirty                                                   : 1;
    uint64_t large_page                                              : 1;
    uint64_t global                                                  : 1;
    uint64_t ignored_1                                               : 3;
    uint64_t pat                                                     : 1;
    uint64_t reserved_1                                              : 17;
    uint64_t page_frame_number                                       : 18;
    uint64_t reserved_2                                              : 4;
    uint64_t ignored_2                                               : 7;
    uint64_t protection_key                                          : 4;
    uint64_t execute_disable                                         : 1;
  };

  uint64_t flags;
} pdpte_1gb_64;

typedef union {
  struct {
    uint64_t present                                                 : 1;
    uint64_t write                                                   : 1;
    uint64_t supervisor                                              : 1;
    uint64_t page_level_write_through                                : 1;
    uint64_t page_level_cache_disable                                : 1;
    uint64_t accessed                                                : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t large_page                                              : 1;
    uint64_t ignored_1                                               : 4;
    uint64_t page_frame_number                                       : 36;
    uint64_t reserved_2                                              : 4;
    uint64_t ignored_2                                               : 11;
    uint64_t execute_disable                                         : 1;
  };

  uint64_t flags;
} pdpte_64;

typedef union {
  struct {
    uint64_t present                                                 : 1;
    uint64_t write                                                   : 1;
    uint64_t supervisor                                              : 1;
    uint64_t page_level_write_through                                : 1;
    uint64_t page_level_cache_disable                                : 1;
    uint64_t accessed                                                : 1;
    uint64_t dirty                                                   : 1;
    uint64_t large_page                                              : 1;
    uint64_t global                                                  : 1;
    uint64_t ignored_1                                               : 3;
    uint64_t pat                                                     : 1;
    uint64_t reserved_1                                              : 8;
    uint64_t page_frame_number                                       : 27;
    uint64_t reserved_2                                              : 4;
    uint64_t ignored_2                                               : 7;
    uint64_t protection_key                                          : 4;
    uint64_t execute_disable                                         : 1;
  };

  uint64_t flags;
} pde_2mb_64;

typedef union {
  struct {
    uint64_t present                                                 : 1;
    uint64_t write                                                   : 1;
    uint64_t supervisor                                              : 1;
    uint64_t page_level_write_through                                : 1;
    uint64_t page_level_cache_disable                                : 1;
    uint64_t accessed                                                : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t large_page                                              : 1;
    uint64_t ignored_1                                               : 4;
    uint64_t page_frame_number                                       : 36;
    uint64_t reserved_2                                              : 4;
    uint64_t ignored_2                                               : 11;
    uint64_t execute_disable                                         : 1;
  };

  uint64_t flags;
} pde_64;

typedef union {
  struct {
    uint64_t present                                                 : 1;
    uint64_t write                                                   : 1;
    uint64_t supervisor                                              : 1;
    uint64_t page_level_write_through                                : 1;
    uint64_t page_level_cache_disable                                : 1;
    uint64_t accessed                                                : 1;
    uint64_t dirty                                                   : 1;
    uint64_t pat                                                     : 1;
    uint64_t global                                                  : 1;
    uint64_t ignored_1                                               : 3;
    uint64_t page_frame_number                                       : 36;
    uint64_t reserved_1                                              : 4;
    uint64_t ignored_2                                               : 7;
    uint64_t protection_key                                          : 4;
    uint64_t execute_disable                                         : 1;
  };

  uint64_t flags;
} pte_64;

typedef union {
  struct {
    uint64_t present                                                 : 1;
    uint64_t write                                                   : 1;
    uint64_t supervisor                                              : 1;
    uint64_t page_level_write_through                                : 1;
    uint64_t page_level_cache_disable                                : 1;
    uint64_t accessed                                                : 1;
    uint64_t dirty                                                   : 1;
    uint64_t large_page                                              : 1;
    uint64_t global                                                  : 1;
    uint64_t ignored_1                                               : 3;
    uint64_t page_frame_number                                       : 36;
    uint64_t reserved_1                                              : 4;
    uint64_t ignored_2                                               : 7;
    uint64_t protection_key                                          : 4;
    uint64_t execute_disable                                         : 1;
  };

  uint64_t flags;
} pt_entry_64;

/**
 * @}
 */

/**
 * @}
 */

/**
 * @defgroup segment_descriptors \
 *           Segment descriptors
 * @{
 */
#pragma pack(push, 1)
typedef struct {
  uint16_t limit;
  uint32_t base_address;
} segment_descriptor_register_32;
#pragma pack(pop)

#pragma pack(push, 1)
typedef struct {
  uint16_t limit;
  uint64_t base_address;
} segment_descriptor_register_64;
#pragma pack(pop)

typedef union {
  struct {
    uint32_t reserved_1                                              : 8;
    uint32_t type                                                    : 4;
    uint32_t descriptor_type                                         : 1;
    uint32_t descriptor_privilege_level                              : 2;
    uint32_t present                                                 : 1;
    uint32_t reserved_2                                              : 4;
    uint32_t available_bit                                           : 1;
    uint32_t long_mode                                               : 1;
    uint32_t default_big                                             : 1;
    uint32_t granularity                                             : 1;
  };

  uint32_t flags;
} segment_access_rights;

typedef struct {
  uint16_t segment_limit_low;
  uint16_t base_address_low;
  union {
    struct {
      uint32_t base_address_middle                                   : 8;
      uint32_t type                                                  : 4;
      uint32_t descriptor_type                                       : 1;
      uint32_t descriptor_privilege_level                            : 2;
      uint32_t present                                               : 1;
      uint32_t segment_limit_high                                    : 4;
      uint32_t available_bit                                         : 1;
      uint32_t long_mode                                             : 1;
      uint32_t default_big                                           : 1;
      uint32_t granularity                                           : 1;
      uint32_t base_address_high                                     : 8;
    };

    uint32_t flags;
  } ;

} segment_descriptor_32;

typedef struct {
  uint16_t segment_limit_low;
  uint16_t base_address_low;
  union {
    struct {
      uint32_t base_address_middle                                   : 8;
      uint32_t type                                                  : 4;
      uint32_t descriptor_type                                       : 1;
      uint32_t descriptor_privilege_level                            : 2;
      uint32_t present                                               : 1;
      uint32_t segment_limit_high                                    : 4;
      uint32_t available_bit                                         : 1;
      uint32_t long_mode                                             : 1;
      uint32_t default_big                                           : 1;
      uint32_t granularity                                           : 1;
      uint32_t base_address_high                                     : 8;
    };

    uint32_t flags;
  } ;

  uint32_t base_address_upper;
  uint32_t must_be_zero;
} segment_descriptor_64;

#define SEGMENT_DESCRIPTOR_TYPE_SYSTEM                               0x00000000
#define SEGMENT_DESCRIPTOR_TYPE_CODE_OR_DATA                         0x00000001
/**
 * @defgroup segment_descriptor_code_and_data_type \
 *           Code- and Data-Segment Descriptor Types
 * @{
 */
#define SEGMENT_DESCRIPTOR_TYPE_DATA_R                               0x00000000
#define SEGMENT_DESCRIPTOR_TYPE_DATA_RA                              0x00000001
#define SEGMENT_DESCRIPTOR_TYPE_DATA_RW                              0x00000002
#define SEGMENT_DESCRIPTOR_TYPE_DATA_RWA                             0x00000003
#define SEGMENT_DESCRIPTOR_TYPE_DATA_RE                              0x00000004
#define SEGMENT_DESCRIPTOR_TYPE_DATA_REA                             0x00000005
#define SEGMENT_DESCRIPTOR_TYPE_DATA_RWE                             0x00000006
#define SEGMENT_DESCRIPTOR_TYPE_DATA_RWEA                            0x00000007
#define SEGMENT_DESCRIPTOR_TYPE_CODE_E                               0x00000008
#define SEGMENT_DESCRIPTOR_TYPE_CODE_EA                              0x00000009
#define SEGMENT_DESCRIPTOR_TYPE_CODE_ER                              0x0000000A
#define SEGMENT_DESCRIPTOR_TYPE_CODE_ERA                             0x0000000B
#define SEGMENT_DESCRIPTOR_TYPE_CODE_EC                              0x0000000C
#define SEGMENT_DESCRIPTOR_TYPE_CODE_ECA                             0x0000000D
#define SEGMENT_DESCRIPTOR_TYPE_CODE_ERC                             0x0000000E
#define SEGMENT_DESCRIPTOR_TYPE_CODE_ERCA                            0x0000000F
/**
 * @}
 */

/**
 * @defgroup segment_descriptor_system_type \
 *           System Descriptor Types
 * @{
 */
#define SEGMENT_DESCRIPTOR_TYPE_RESERVED_1                           0x00000000
#define SEGMENT_DESCRIPTOR_TYPE_TSS_16_AVAILABLE                     0x00000001
#define SEGMENT_DESCRIPTOR_TYPE_LDT                                  0x00000002
#define SEGMENT_DESCRIPTOR_TYPE_TSS_16_BUSY                          0x00000003
#define SEGMENT_DESCRIPTOR_TYPE_CALL_GATE_16                         0x00000004
#define SEGMENT_DESCRIPTOR_TYPE_TASK_GATE                            0x00000005
#define SEGMENT_DESCRIPTOR_TYPE_INTERRUPT_GATE_16                    0x00000006
#define SEGMENT_DESCRIPTOR_TYPE_TRAP_GATE_16                         0x00000007
#define SEGMENT_DESCRIPTOR_TYPE_RESERVED_2                           0x00000008
#define SEGMENT_DESCRIPTOR_TYPE_TSS_AVAILABLE                        0x00000009
#define SEGMENT_DESCRIPTOR_TYPE_RESERVED_3                           0x0000000A
#define SEGMENT_DESCRIPTOR_TYPE_TSS_BUSY                             0x0000000B
#define SEGMENT_DESCRIPTOR_TYPE_CALL_GATE                            0x0000000C
#define SEGMENT_DESCRIPTOR_TYPE_RESERVED_4                           0x0000000D
#define SEGMENT_DESCRIPTOR_TYPE_INTERRUPT_GATE                       0x0000000E
#define SEGMENT_DESCRIPTOR_TYPE_TRAP_GATE                            0x0000000F
/**
 * @}
 */

typedef union {
  struct {
    uint16_t request_privilege_level                                 : 2;
    uint16_t table_indicator                                         : 1;
    uint16_t index                                                   : 13;
  };

  uint16_t flags;
} segment_selector;

/**
 * @}
 */

/**
 * @defgroup vmx \
 *           VMX
 * @{
 */
/**
 * @{
 */
/**
 * @defgroup vmx_basic_exit_reasons \
 *           VMX Basic Exit Reasons
 * @{
 */
#define VMX_EXIT_REASON_XCPT_OR_NMI                                  0x00000000
#define VMX_EXIT_REASON_EXT_INT                                      0x00000001
#define VMX_EXIT_REASON_TRIPLE_FAULT                                 0x00000002
#define VMX_EXIT_REASON_INIT_SIGNAL                                  0x00000003
#define VMX_EXIT_REASON_SIPI                                         0x00000004
#define VMX_EXIT_REASON_IO_SMI                                       0x00000005
#define VMX_EXIT_REASON_SMI                                          0x00000006
#define VMX_EXIT_REASON_INT_WINDOW                                   0x00000007
#define VMX_EXIT_REASON_NMI_WINDOW                                   0x00000008
#define VMX_EXIT_REASON_TASK_SWITCH                                  0x00000009
#define VMX_EXIT_REASON_CPUID                                        0x0000000A
#define VMX_EXIT_REASON_GETSEC                                       0x0000000B
#define VMX_EXIT_REASON_HLT                                          0x0000000C
#define VMX_EXIT_REASON_INVD                                         0x0000000D
#define VMX_EXIT_REASON_INVLPG                                       0x0000000E
#define VMX_EXIT_REASON_RDPMC                                        0x0000000F
#define VMX_EXIT_REASON_RDTSC                                        0x00000010
#define VMX_EXIT_REASON_RSM                                          0x00000011
#define VMX_EXIT_REASON_VMCALL                                       0x00000012
#define VMX_EXIT_REASON_VMCLEAR                                      0x00000013
#define VMX_EXIT_REASON_VMLAUNCH                                     0x00000014
#define VMX_EXIT_REASON_VMPTRLD                                      0x00000015
#define VMX_EXIT_REASON_VMPTRST                                      0x00000016
#define VMX_EXIT_REASON_VMREAD                                       0x00000017
#define VMX_EXIT_REASON_VMRESUME                                     0x00000018
#define VMX_EXIT_REASON_VMWRITE                                      0x00000019
#define VMX_EXIT_REASON_VMXOFF                                       0x0000001A
#define VMX_EXIT_REASON_VMXON                                        0x0000001B
#define VMX_EXIT_REASON_MOV_CRX                                      0x0000001C
#define VMX_EXIT_REASON_MOV_DRX                                      0x0000001D
#define VMX_EXIT_REASON_IO_INSTR                                     0x0000001E
#define VMX_EXIT_REASON_RDMSR                                        0x0000001F
#define VMX_EXIT_REASON_WRMSR                                        0x00000020
#define VMX_EXIT_REASON_ERR_INVALID_GUEST_STATE                      0x00000021
#define VMX_EXIT_REASON_ERR_MSR_LOAD                                 0x00000022
#define VMX_EXIT_REASON_MWAIT                                        0x00000024
#define VMX_EXIT_REASON_MTF                                          0x00000025
#define VMX_EXIT_REASON_MONITOR                                      0x00000027
#define VMX_EXIT_REASON_PAUSE                                        0x00000028
#define VMX_EXIT_REASON_ERR_MACHINE_CHECK                            0x00000029
#define VMX_EXIT_REASON_TPR_BELOW_THRESHOLD                          0x0000002B
#define VMX_EXIT_REASON_APIC_ACCESS                                  0x0000002C
#define VMX_EXIT_REASON_VIRTUALIZED_EOI                              0x0000002D
#define VMX_EXIT_REASON_XDTR_ACCESS                                  0x0000002E
#define VMX_EXIT_REASON_TR_ACCESS                                    0x0000002F
#define VMX_EXIT_REASON_EPT_VIOLATION                                0x00000030
#define VMX_EXIT_REASON_EPT_MISCONFIG                                0x00000031
#define VMX_EXIT_REASON_INVEPT                                       0x00000032
#define VMX_EXIT_REASON_RDTSCP                                       0x00000033
#define VMX_EXIT_REASON_PREEMPT_TIMER                                0x00000034
#define VMX_EXIT_REASON_INVVPID                                      0x00000035
#define VMX_EXIT_REASON_WBINVD                                       0x00000036
#define VMX_EXIT_REASON_XSETBV                                       0x00000037
#define VMX_EXIT_REASON_APIC_WRITE                                   0x00000038
#define VMX_EXIT_REASON_RDRAND                                       0x00000039
#define VMX_EXIT_REASON_INVPCID                                      0x0000003A
#define VMX_EXIT_REASON_VMFUNC                                       0x0000003B
#define VMX_EXIT_REASON_ENCLS                                        0x0000003C
#define VMX_EXIT_REASON_RDSEED                                       0x0000003D
#define VMX_EXIT_REASON_PML_FULL                                     0x0000003E
#define VMX_EXIT_REASON_XSAVES                                       0x0000003F
#define VMX_EXIT_REASON_XRSTORS                                      0x00000040
/**
 * @}
 */

/**
 * @defgroup vmx_instruction_error_numbers \
 *           VM Instruction Error Numbers
 * @{
 */
#define VMX_ERROR_VMCALL                                             0x00000001
#define VMX_ERROR_VMCLEAR_INVALID_PHYS_ADDR                          0x00000002
#define VMX_ERROR_VMCLEAR_INVALID_VMXON_PTR                          0x00000003
#define VMX_ERROR_VMLAUCH_NON_CLEAR_VMCS                             0x00000004
#define VMX_ERROR_VMRESUME_NON_LAUNCHED_VMCS                         0x00000005
#define VMX_ERROR_VMRESUME_CORRUPTED_VMCS                            0x00000006
#define VMX_ERROR_VMENTRY_INVALID_CONTROL_FIELDS                     0x00000007
#define VMX_ERROR_VMENTRY_INVALID_HOST_STATE                         0x00000008
#define VMX_ERROR_VMPTRLD_INVALID_PHYS_ADDR                          0x00000009
#define VMX_ERROR_VMPTRLD_VMXON_PTR                                  0x0000000A
#define VMX_ERROR_VMPTRLD_WRONG_VMCS_REVISION                        0x0000000B
#define VMX_ERROR_VMREAD_VMWRITE_INVALID_COMPONENT                   0x0000000C
#define VMX_ERROR_VMWRITE_READONLY_COMPONENT                         0x0000000D
#define VMX_ERROR_VMXON_IN_VMX_ROOT_OP                               0x0000000F
#define VMX_ERROR_VMENTRY_INVALID_VMCS_EXEC_PTR                      0x00000010
#define VMX_ERROR_VMENTRY_NON_LAUNCHED_EXEC_VMCS                     0x00000011
#define VMX_ERROR_VMENTRY_EXEC_VMCS_PTR                              0x00000012
#define VMX_ERROR_VMCALL_NON_CLEAR_VMCS                              0x00000013
#define VMX_ERROR_VMCALL_INVALID_VMEXIT_FIELDS                       0x00000014
#define VMX_ERROR_VMCALL_INVALID_MSEG_REVISION                       0x00000016
#define VMX_ERROR_VMXOFF_DUAL_MONITOR                                0x00000017
#define VMX_ERROR_VMCALL_INVALID_SMM_MONITOR                         0x00000018
#define VMX_ERROR_VMENTRY_INVALID_VM_EXEC_CTRL                       0x00000019
#define VMX_ERROR_VMENTRY_MOV_SS                                     0x0000001A
#define VMX_ERROR_INVEPTVPID_INVALID_OPERAND                         0x0000001C
/**
 * @}
 */

/**
 * @defgroup vmx_exceptions \
 *           Virtualization Exceptions
 * @{
 */
typedef struct {
  uint32_t reason;
  uint32_t exception_mask;
  uint64_t exit;
  uint64_t guest_linear_address;
  uint64_t guest_physical_address;
  uint16_t current_eptp_index;
} vmx_ve_except_info;

/**
 * @}
 */

/**
 * @defgroup vmx_basic_exit_information \
 *           Basic VM-Exit Information
 * @{
 */
typedef union {
  struct {
    uint64_t breakpoint_condition                                    : 4;
    uint64_t reserved_1                                              : 9;
    uint64_t debug_register_access_detected                          : 1;
    uint64_t single_instruction                                      : 1;
  };

  uint64_t flags;
} vmx_exit_qualification_debug_exception;

typedef union {
  struct {
    uint64_t selector                                                : 16;
    uint64_t reserved_1                                              : 14;
    uint64_t type                                                    : 2;
#define VMX_EXIT_QUALIFICATION_TYPE_CALL                             0x00000000
#define VMX_EXIT_QUALIFICATION_TYPE_IRET                             0x00000001
#define VMX_EXIT_QUALIFICATION_TYPE_JMP                              0x00000002
#define VMX_EXIT_QUALIFICATION_TYPE_IDT                              0x00000003
  };

  uint64_t flags;
} vmx_exit_qualification_task_switch;

typedef union {
  struct {
    uint64_t cr_number                                               : 4;
#define VMX_EXIT_QUALIFICATION_REGISTER_CR0                          0x00000000
#define VMX_EXIT_QUALIFICATION_REGISTER_CR2                          0x00000002
#define VMX_EXIT_QUALIFICATION_REGISTER_CR3                          0x00000003
#define VMX_EXIT_QUALIFICATION_REGISTER_CR4                          0x00000004
#define VMX_EXIT_QUALIFICATION_REGISTER_CR8                          0x00000008
    uint64_t access_type                                             : 2;
#define VMX_EXIT_QUALIFICATION_ACCESS_MOV_TO_CR                      0x00000000
#define VMX_EXIT_QUALIFICATION_ACCESS_MOV_FROM_CR                    0x00000001
#define VMX_EXIT_QUALIFICATION_ACCESS_CLTS                           0x00000002
#define VMX_EXIT_QUALIFICATION_ACCESS_LMSW                           0x00000003
    uint64_t lmsw_operand_type                                       : 1;
#define VMX_EXIT_QUALIFICATION_LMSW_OP_REGISTER                      0x00000000
#define VMX_EXIT_QUALIFICATION_LMSW_OP_MEMORY                        0x00000001
    uint64_t reserved_1                                              : 1;
    uint64_t gp_register                                             : 4;
#define VMX_EXIT_QUALIFICATION_GENREG_RAX                            0x00000000
#define VMX_EXIT_QUALIFICATION_GENREG_RCX                            0x00000001
#define VMX_EXIT_QUALIFICATION_GENREG_RDX                            0x00000002
#define VMX_EXIT_QUALIFICATION_GENREG_RBX                            0x00000003
#define VMX_EXIT_QUALIFICATION_GENREG_RSP                            0x00000004
#define VMX_EXIT_QUALIFICATION_GENREG_RBP                            0x00000005
#define VMX_EXIT_QUALIFICATION_GENREG_RSI                            0x00000006
#define VMX_EXIT_QUALIFICATION_GENREG_RDI                            0x00000007
#define VMX_EXIT_QUALIFICATION_GENREG_R8                             0x00000008
#define VMX_EXIT_QUALIFICATION_GENREG_R9                             0x00000009
#define VMX_EXIT_QUALIFICATION_GENREG_R10                            0x0000000A
#define VMX_EXIT_QUALIFICATION_GENREG_R11                            0x0000000B
#define VMX_EXIT_QUALIFICATION_GENREG_R12                            0x0000000C
#define VMX_EXIT_QUALIFICATION_GENREG_R13                            0x0000000D
#define VMX_EXIT_QUALIFICATION_GENREG_R14                            0x0000000E
#define VMX_EXIT_QUALIFICATION_GENREG_R15                            0x0000000F
    uint64_t reserved_2                                              : 4;
    uint64_t lmsw_source_data                                        : 16;
  };

  uint64_t flags;
} vmx_exit_qualification_cr_access;

typedef union {
  struct {
    uint64_t dr_number                                               : 3;
#define VMX_EXIT_QUALIFICATION_REGISTER_DR0                          0x00000000
#define VMX_EXIT_QUALIFICATION_REGISTER_DR1                          0x00000001
#define VMX_EXIT_QUALIFICATION_REGISTER_DR2                          0x00000002
#define VMX_EXIT_QUALIFICATION_REGISTER_DR3                          0x00000003
#define VMX_EXIT_QUALIFICATION_REGISTER_DR6                          0x00000006
#define VMX_EXIT_QUALIFICATION_REGISTER_DR7                          0x00000007
    uint64_t reserved_1                                              : 1;
    uint64_t direction_of_access                                     : 1;
#define VMX_EXIT_QUALIFICATION_DIRECTION_MOV_TO_DR                   0x00000000
#define VMX_EXIT_QUALIFICATION_DIRECTION_MOV_FROM_DR                 0x00000001
    uint64_t reserved_2                                              : 3;
    uint64_t gp_register                                             : 4;
  };

  uint64_t flags;
} vmx_exit_qualification_dr_access;

typedef union {
  struct {
    uint64_t size_of_access                                          : 3;
#define VMX_EXIT_QUALIFICATION_WIDTH_1B                              0x00000000
#define VMX_EXIT_QUALIFICATION_WIDTH_2B                              0x00000001
#define VMX_EXIT_QUALIFICATION_WIDTH_4B                              0x00000003
    uint64_t direction_of_access                                     : 1;
#define VMX_EXIT_QUALIFICATION_DIRECTION_OUT                         0x00000000
#define VMX_EXIT_QUALIFICATION_DIRECTION_IN                          0x00000001
    uint64_t string_instruction                                      : 1;
#define VMX_EXIT_QUALIFICATION_IS_STRING_NOT_STRING                  0x00000000
#define VMX_EXIT_QUALIFICATION_IS_STRING_STRING                      0x00000001
    uint64_t rep_prefixed                                            : 1;
#define VMX_EXIT_QUALIFICATION_IS_REP_NOT_REP                        0x00000000
#define VMX_EXIT_QUALIFICATION_IS_REP_REP                            0x00000001
    uint64_t operand_encoding                                        : 1;
#define VMX_EXIT_QUALIFICATION_ENCODING_DX                           0x00000000
#define VMX_EXIT_QUALIFICATION_ENCODING_IMM                          0x00000001
    uint64_t reserved_1                                              : 9;
    uint64_t port_number                                             : 16;
  };

  uint64_t flags;
} vmx_exit_qualification_io_inst;

typedef union {
  struct {
    uint64_t page_offset                                             : 12;
    uint64_t access_type                                             : 4;
#define VMX_EXIT_QUALIFICATION_TYPE_LINEAR_READ                      0x00000000
#define VMX_EXIT_QUALIFICATION_TYPE_LINEAR_WRITE                     0x00000001
#define VMX_EXIT_QUALIFICATION_TYPE_LINEAR_INSTR_FETCH               0x00000002
#define VMX_EXIT_QUALIFICATION_TYPE_LINEAR_EVENT_DELIVERY            0x00000003
#define VMX_EXIT_QUALIFICATION_TYPE_PHYSICAL_EVENT_DELIVERY          0x0000000A
#define VMX_EXIT_QUALIFICATION_TYPE_PHYSICAL_INSTR                   0x0000000F
  };

  uint64_t flags;
} vmx_exit_qualification_apic_access;

typedef union {
  struct {
    uint64_t data_read                                               : 1;
    uint64_t data_write                                              : 1;
    uint64_t instruction_fetch                                       : 1;
    uint64_t entry_present                                           : 1;
    uint64_t entry_write                                             : 1;
    uint64_t entry_execute                                           : 1;
    uint64_t entry_execute_for_user_mode                             : 1;
    uint64_t valid_guest_linear_address                              : 1;
    uint64_t ept_translated_access                                   : 1;
    uint64_t user_mode_linear_address                                : 1;
    uint64_t readable_writable_page                                  : 1;
    uint64_t execute_disable_page                                    : 1;
    uint64_t nmi_unblocking                                          : 1;
  };

  uint64_t flags;
} vmx_exit_qualification_ept_violation;

/**
 * @}
 */

/**
 * @defgroup vmx_vmexit_instruction_information \
 *           Information for VM Exits Due to Instruction Execution
 * @{
 */
typedef union {
  struct {
    uint64_t reserved_1                                              : 7;
    uint64_t address_size                                            : 3;
    uint64_t reserved_2                                              : 5;
    uint64_t segment_register                                        : 3;
  };

  uint64_t flags;
} vmx_vmexit_instruction_info_ins_outs;

typedef union {
  struct {
    uint64_t scaling                                                 : 2;
    uint64_t reserved_1                                              : 5;
    uint64_t address_size                                            : 3;
    uint64_t reserved_2                                              : 5;
    uint64_t segment_register                                        : 3;
    uint64_t gp_register                                             : 4;
    uint64_t gp_register_invalid                                     : 1;
    uint64_t base_register                                           : 4;
    uint64_t base_register_invalid                                   : 1;
    uint64_t register_2                                              : 4;
  };

  uint64_t flags;
} vmx_vmexit_instruction_info_invalidate;

typedef union {
  struct {
    uint64_t scaling                                                 : 2;
    uint64_t reserved_1                                              : 5;
    uint64_t address_size                                            : 3;
    uint64_t reserved_2                                              : 1;
    uint64_t operand_size                                            : 1;
    uint64_t reserved_3                                              : 3;
    uint64_t segment_register                                        : 3;
    uint64_t gp_register                                             : 4;
    uint64_t gp_register_invalid                                     : 1;
    uint64_t base_register                                           : 4;
    uint64_t base_register_invalid                                   : 1;
    uint64_t instruction_identity                                    : 2;
  };

  uint64_t flags;
} vmx_vmexit_instruction_info_gdtr_idtr_access;

typedef union {
  struct {
    uint64_t scaling                                                 : 2;
    uint64_t reserved_1                                              : 1;
    uint64_t reg_1                                                   : 4;
    uint64_t address_size                                            : 3;
    uint64_t memory_register                                         : 1;
    uint64_t reserved_2                                              : 4;
    uint64_t segment_register                                        : 3;
    uint64_t gp_register                                             : 4;
    uint64_t gp_register_invalid                                     : 1;
    uint64_t base_register                                           : 4;
    uint64_t base_register_invalid                                   : 1;
    uint64_t instruction_identity                                    : 2;
  };

  uint64_t flags;
} vmx_vmexit_instruction_info_ldtr_tr_access;

typedef union {
  struct {
    uint64_t reserved_1                                              : 3;
    uint64_t destination_register                                    : 4;
    uint64_t reserved_2                                              : 4;
    uint64_t operand_size                                            : 2;
  };

  uint64_t flags;
} vmx_vmexit_instruction_info_rdrand_rdseed;

typedef union {
  struct {
    uint64_t scaling                                                 : 2;
    uint64_t reserved_1                                              : 5;
    uint64_t address_size                                            : 3;
    uint64_t reserved_2                                              : 5;
    uint64_t segment_register                                        : 3;
    uint64_t gp_register                                             : 4;
    uint64_t gp_register_invalid                                     : 1;
    uint64_t base_register                                           : 4;
    uint64_t base_register_invalid                                   : 1;
  };

  uint64_t flags;
} vmx_vmexit_instruction_info_vmx_and_xsaves;

typedef union {
  struct {
    uint64_t scaling                                                 : 2;
    uint64_t reserved_1                                              : 1;
    uint64_t register_1                                              : 4;
    uint64_t address_size                                            : 3;
    uint64_t memory_register                                         : 1;
    uint64_t reserved_2                                              : 4;
    uint64_t segment_register                                        : 3;
    uint64_t gp_register                                             : 4;
    uint64_t gp_register_invalid                                     : 1;
    uint64_t base_register                                           : 4;
    uint64_t base_register_invalid                                   : 1;
    uint64_t register_2                                              : 4;
  };

  uint64_t flags;
} vmx_vmexit_instruction_info_vmread_vmwrite;

/**
 * @}
 */

typedef union {
  struct {
    uint32_t type                                                    : 4;
    uint32_t descriptor_type                                         : 1;
    uint32_t descriptor_privilege_level                              : 2;
    uint32_t present                                                 : 1;
    uint32_t reserved_1                                              : 4;
    uint32_t available_bit                                           : 1;
    uint32_t long_mode                                               : 1;
    uint32_t default_big                                             : 1;
    uint32_t granularity                                             : 1;
    uint32_t unusable                                                : 1;
  };

  uint32_t flags;
} vmx_segment_access_rights;

typedef union {
  struct {
    uint32_t blocking_by_sti                                         : 1;
    uint32_t blocking_by_mov_ss                                      : 1;
    uint32_t blocking_by_smi                                         : 1;
    uint32_t blocking_by_nmi                                         : 1;
    uint32_t enclave_interruption                                    : 1;
  };

  uint32_t flags;
} vmx_interruptibility_state;

typedef enum {
  vmx_active                                                   = 0x00000000,
  vmx_hlt                                                      = 0x00000001,
  vmx_shutdown                                                 = 0x00000002,
  vmx_wait_for_sipi                                            = 0x00000003,
} vmx_guest_activity_state;

/**
 * @}
 */

typedef struct {
#define IO_BITMAP_A_MIN                                              0x00000000
#define IO_BITMAP_A_MAX                                              0x00007FFF
#define IO_BITMAP_B_MIN                                              0x00008000
#define IO_BITMAP_B_MAX                                              0x0000FFFF
  uint8_t io_a[4096];
  uint8_t io_b[4096];
} vmx_io_bitmap;

typedef struct {
#define MSR_ID_LOW_MIN                                               0x00000000
#define MSR_ID_LOW_MAX                                               0x00001FFF
#define MSR_ID_HIGH_MIN                                              0xC0000000
#define MSR_ID_HIGH_MAX                                              0xC0001FFF
  uint8_t rdmsr_low[1024];
  uint8_t rdmsr_high[1024];
  uint8_t wrmsr_low[1024];
  uint8_t wrmsr_high[1024];
} vmx_msr_bitmap;

/**
 * @defgroup ept \
 *           The extended page-table mechanism
 * @{
 */
typedef union {
  struct {
    uint64_t memory_type                                             : 3;
    uint64_t page_walk_length                                        : 3;
#define EPT_PAGE_WALK_LENGTH_4                                       0x00000003
    uint64_t enable_access_and_dirty_flags                           : 1;
    uint64_t reserved_1                                              : 5;
    uint64_t page_frame_number                                       : 36;
  };

  uint64_t flags;
} eptp;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
    uint64_t write_access                                            : 1;
    uint64_t execute_access                                          : 1;
    uint64_t reserved_1                                              : 5;
    uint64_t accessed                                                : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t user_mode_execute                                       : 1;
    uint64_t reserved_3                                              : 1;
    uint64_t page_frame_number                                       : 36;
  };

  uint64_t flags;
} epml4e;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
    uint64_t write_access                                            : 1;
    uint64_t execute_access                                          : 1;
    uint64_t memory_type                                             : 3;
    uint64_t ignore_pat                                              : 1;
    uint64_t large_page                                              : 1;
    uint64_t accessed                                                : 1;
    uint64_t dirty                                                   : 1;
    uint64_t user_mode_execute                                       : 1;
    uint64_t reserved_1                                              : 19;
    uint64_t page_frame_number                                       : 18;
    uint64_t reserved_2                                              : 15;
    uint64_t suppress_ve                                             : 1;
  };

  uint64_t flags;
} ept_pdpte_1gb;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
    uint64_t write_access                                            : 1;
    uint64_t execute_access                                          : 1;
    uint64_t reserved_1                                              : 5;
    uint64_t accessed                                                : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t user_mode_execute                                       : 1;
    uint64_t reserved_3                                              : 1;
    uint64_t page_frame_number                                       : 36;
  };

  uint64_t flags;
} ept_pdpte;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
    uint64_t write_access                                            : 1;
    uint64_t execute_access                                          : 1;
    uint64_t memory_type                                             : 3;
    uint64_t ignore_pat                                              : 1;
    uint64_t large_page                                              : 1;
    uint64_t accessed                                                : 1;
    uint64_t dirty                                                   : 1;
    uint64_t user_mode_execute                                       : 1;
    uint64_t reserved_1                                              : 10;
    uint64_t page_frame_number                                       : 27;
    uint64_t reserved_2                                              : 15;
    uint64_t suppress_ve                                             : 1;
  };

  uint64_t flags;
} ept_pde_2mb;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
    uint64_t write_access                                            : 1;
    uint64_t execute_access                                          : 1;
    uint64_t reserved_1                                              : 5;
    uint64_t accessed                                                : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t user_mode_execute                                       : 1;
    uint64_t reserved_3                                              : 1;
    uint64_t page_frame_number                                       : 36;
  };

  uint64_t flags;
} ept_pde;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
    uint64_t write_access                                            : 1;
    uint64_t execute_access                                          : 1;
    uint64_t memory_type                                             : 3;
    uint64_t ignore_pat                                              : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t accessed                                                : 1;
    uint64_t dirty                                                   : 1;
    uint64_t user_mode_execute                                       : 1;
    uint64_t reserved_2                                              : 1;
    uint64_t page_frame_number                                       : 36;
    uint64_t reserved_3                                              : 15;
    uint64_t suppress_ve                                             : 1;
  };

  uint64_t flags;
} ept_pte;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
    uint64_t write_access                                            : 1;
    uint64_t execute_access                                          : 1;
    uint64_t memory_type                                             : 3;
    uint64_t ignore_pat                                              : 1;
    uint64_t large_page                                              : 1;
    uint64_t accessed                                                : 1;
    uint64_t dirty                                                   : 1;
    uint64_t user_mode_execute                                       : 1;
    uint64_t reserved_1                                              : 1;
    uint64_t page_frame_number                                       : 36;
    uint64_t reserved_2                                              : 15;
    uint64_t suppress_ve                                             : 1;
  };

  uint64_t flags;
} ept_entry;

/**
 * @defgroup ept_table_level \
 *           EPT Table level numbers
 * @{
 */
#define EPT_LEVEL_PML4E                                              0x00000003
#define EPT_LEVEL_PDPTE                                              0x00000002
#define EPT_LEVEL_PDE                                                0x00000001
#define EPT_LEVEL_PTE                                                0x00000000
/**
 * @}
 */

/**
 * @defgroup ept_entry_count \
 *           EPT Entry counts
 * @{
 */
#define EPML4_ENTRY_COUNT                                            0x00000200
#define EPDPTE_ENTRY_COUNT                                           0x00000200
#define EPDE_ENTRY_COUNT                                             0x00000200
/**
 * @}
 */

/**
 * @}
 */

typedef enum {
  invept_single_context                                        = 0x00000001,
  invept_all_context                                           = 0x00000002,
} invept_type;

typedef enum {
  invvpid_individual_address                                   = 0x00000000,
  invvpid_single_context                                       = 0x00000001,
  invvpid_all_context                                          = 0x00000002,
  invvpid_single_context_retaining_globals                     = 0x00000003,
} invvpid_type;

typedef struct {
  uint64_t ept_pointer;
  uint64_t reserved;
} invept_descriptor;

typedef struct {
  uint16_t vpid;
  uint16_t reserved1;
  uint32_t reserved2;
  uint64_t linear_address;
} invvpid_descriptor;

typedef struct {
  uint32_t revision_id;
  uint32_t abort_indicator;
  uint8_t data[4088];
} vmcs;

/**
 * @defgroup vmcs_fields \
 *           VMCS (VM Control Structure)
 * @{
 */
typedef union {
  struct {
    uint16_t access_type                                             : 1;
    uint16_t index                                                   : 9;
    uint16_t type                                                    : 2;
    uint16_t must_be_zero                                            : 1;
    uint16_t width                                                   : 2;
  };

  uint16_t flags;
} vmcs_component_encoding;

/**
 * @defgroup vmcs_16_bit \
 *           16-Bit Fields
 * @{
 */
/**
 * @defgroup vmcs_16_bit_control_fields \
 *           16-Bit Control Fields
 * @{
 */
#define VMCS_CTRL_VPID                                               0x00000000
#define VMCS_CTRL_POSTED_INTR_NOTIFY_VECTOR                          0x00000002
#define VMCS_CTRL_EPTP_INDEX                                         0x00000004
/**
 * @}
 */

/**
 * @defgroup vmcs_16_bit_guest_state_fields \
 *           16-Bit Guest-State Fields
 * @{
 */
#define VMCS_GUEST_ES_SEL                                            0x00000800
#define VMCS_GUEST_CS_SEL                                            0x00000802
#define VMCS_GUEST_SS_SEL                                            0x00000804
#define VMCS_GUEST_DS_SEL                                            0x00000806
#define VMCS_GUEST_FS_SEL                                            0x00000808
#define VMCS_GUEST_GS_SEL                                            0x0000080A
#define VMCS_GUEST_LDTR_SEL                                          0x0000080C
#define VMCS_GUEST_TR_SEL                                            0x0000080E
#define VMCS_GUEST_INTR_STATUS                                       0x00000810
#define VMCS_GUEST_PML_INDEX                                         0x00000812
/**
 * @}
 */

/**
 * @defgroup vmcs_16_bit_host_state_fields \
 *           16-Bit Host-State Fields
 * @{
 */
#define VMCS_HOST_ES_SEL                                             0x00000C00
#define VMCS_HOST_CS_SEL                                             0x00000C02
#define VMCS_HOST_SS_SEL                                             0x00000C04
#define VMCS_HOST_DS_SEL                                             0x00000C06
#define VMCS_HOST_FS_SEL                                             0x00000C08
#define VMCS_HOST_GS_SEL                                             0x00000C0A
#define VMCS_HOST_TR_SEL                                             0x00000C0C
/**
 * @}
 */

/**
 * @}
 */

/**
 * @defgroup vmcs_64_bit \
 *           64-Bit Fields
 * @{
 */
/**
 * @defgroup vmcs_64_bit_control_fields \
 *           64-Bit Control Fields
 * @{
 */
#define VMCS_CTRL_IO_BITMAP_A                                        0x00002000
#define VMCS_CTRL_IO_BITMAP_B                                        0x00002002
#define VMCS_CTRL_MSR_BITMAP                                         0x00002004
#define VMCS_CTRL_VMEXIT_MSR_STORE                                   0x00002006
#define VMCS_CTRL_VMEXIT_MSR_LOAD                                    0x00002008
#define VMCS_CTRL_VMENTRY_MSR_LOAD                                   0x0000200A
#define VMCS_CTRL_EXEC_VMCS_PTR                                      0x0000200C
#define VMCS_CTRL_PML_ADDR                                           0x0000200E
#define VMCS_CTRL_TSC_OFFSET                                         0x00002010
#define VMCS_CTRL_VAPIC_PAGEADDR                                     0x00002012
#define VMCS_CTRL_APIC_ACCESSADDR                                    0x00002014
#define VMCS_CTRL_POSTED_INTR_DESC                                   0x00002016
#define VMCS_CTRL_VMFUNC_CTRLS                                       0x00002018
#define VMCS_CTRL_EPTP                                               0x0000201A
#define VMCS_CTRL_EOI_BITMAP_0                                       0x0000201C
#define VMCS_CTRL_EOI_BITMAP_1                                       0x0000201E
#define VMCS_CTRL_EOI_BITMAP_2                                       0x00002020
#define VMCS_CTRL_EOI_BITMAP_3                                       0x00002022
#define VMCS_CTRL_EPTP_LIST                                          0x00002024
#define VMCS_CTRL_VMREAD_BITMAP                                      0x00002026
#define VMCS_CTRL_VMWRITE_BITMAP                                     0x00002028
#define VMCS_CTRL_VIRTXCPT_INFO_ADDR                                 0x0000202A
#define VMCS_CTRL_XSS_EXITING_BITMAP                                 0x0000202C
#define VMCS_CTRL_ENCLS_EXITING_BITMAP                               0x0000202E
#define VMCS_CTRL_TSC_MULTIPLIER                                     0x00002032
/**
 * @}
 */

/**
 * @defgroup vmcs_64_bit_read_only_data_fields \
 *           64-Bit Read-Only Data Field
 * @{
 */
#define VMCS_GUEST_PHYS_ADDR                                         0x00002400
/**
 * @}
 */

/**
 * @defgroup vmcs_64_bit_guest_state_fields \
 *           64-Bit Guest-State Fields
 * @{
 */
#define VMCS_GUEST_VMCS_LINK_PTR                                     0x00002800
#define VMCS_GUEST_DEBUGCTL                                          0x00002802
#define VMCS_GUEST_PAT                                               0x00002804
#define VMCS_GUEST_EFER                                              0x00002806
#define VMCS_GUEST_PERF_GLOBAL_CTRL                                  0x00002808
#define VMCS_GUEST_PDPTE0                                            0x0000280A
#define VMCS_GUEST_PDPTE1                                            0x0000280C
#define VMCS_GUEST_PDPTE2                                            0x0000280E
#define VMCS_GUEST_PDPTE3                                            0x00002810
/**
 * @}
 */

/**
 * @defgroup vmcs_64_bit_host_state_fields \
 *           64-Bit Host-State Fields
 * @{
 */
#define VMCS_HOST_PAT                                                0x00002C00
#define VMCS_HOST_EFER                                               0x00002C02
#define VMCS_HOST_PERF_GLOBAL_CTRL                                   0x00002C04
/**
 * @}
 */

/**
 * @}
 */

/**
 * @defgroup vmcs_32_bit \
 *           32-Bit Fields
 * @{
 */
/**
 * @defgroup vmcs_32_bit_control_fields \
 *           32-Bit Control Fields
 * @{
 */
#define VMCS_CTRL_PIN_EXEC                                           0x00004000
#define VMCS_CTRL_PROC_EXEC                                          0x00004002
#define VMCS_CTRL_EXCEPTION_BITMAP                                   0x00004004
#define VMCS_CTRL_PAGEFAULT_ERROR_MASK                               0x00004006
#define VMCS_CTRL_PAGEFAULT_ERROR_MATCH                              0x00004008
#define VMCS_CTRL_CR3_TARGET_COUNT                                   0x0000400A
#define VMCS_CTRL_EXIT                                               0x0000400C
#define VMCS_CTRL_EXIT_MSR_STORE_COUNT                               0x0000400E
#define VMCS_CTRL_EXIT_MSR_LOAD_COUNT                                0x00004010
#define VMCS_CTRL_ENTRY                                              0x00004012
#define VMCS_CTRL_ENTRY_MSR_LOAD_COUNT                               0x00004014
#define VMCS_CTRL_ENTRY_INTERRUPTION_INFO                            0x00004016
#define VMCS_CTRL_ENTRY_EXCEPTION_ERRCODE                            0x00004018
#define VMCS_CTRL_ENTRY_INSTR_LENGTH                                 0x0000401A
#define VMCS_CTRL_TPR_THRESHOLD                                      0x0000401C
#define VMCS_CTRL_PROC_EXEC2                                         0x0000401E
#define VMCS_CTRL_PLE_GAP                                            0x00004020
#define VMCS_CTRL_PLE_WINDOW                                         0x00004022
/**
 * @}
 */

/**
 * @defgroup vmcs_32_bit_read_only_data_fields \
 *           32-Bit Read-Only Data Fields
 * @{
 */
#define VMCS_VM_INSTR_ERROR                                          0x00004400
#define VMCS_EXIT_REASON                                             0x00004402
#define VMCS_EXIT_INTERRUPTION_INFO                                  0x00004404
#define VMCS_EXIT_INTERRUPTION_ERROR_CODE                            0x00004406
#define VMCS_IDT_VECTORING_INFO                                      0x00004408
#define VMCS_IDT_VECTORING_ERROR_CODE                                0x0000440A
#define VMCS_EXIT_INSTR_LENGTH                                       0x0000440C
#define VMCS_EXIT_INSTR_INFO                                         0x0000440E
/**
 * @}
 */

/**
 * @defgroup vmcs_32_bit_guest_state_fields \
 *           32-Bit Guest-State Fields
 * @{
 */
#define VMCS_GUEST_ES_LIMIT                                          0x00004800
#define VMCS_GUEST_CS_LIMIT                                          0x00004802
#define VMCS_GUEST_SS_LIMIT                                          0x00004804
#define VMCS_GUEST_DS_LIMIT                                          0x00004806
#define VMCS_GUEST_FS_LIMIT                                          0x00004808
#define VMCS_GUEST_GS_LIMIT                                          0x0000480A
#define VMCS_GUEST_LDTR_LIMIT                                        0x0000480C
#define VMCS_GUEST_TR_LIMIT                                          0x0000480E
#define VMCS_GUEST_GDTR_LIMIT                                        0x00004810
#define VMCS_GUEST_IDTR_LIMIT                                        0x00004812
#define VMCS_GUEST_ES_ACCESS_RIGHTS                                  0x00004814
#define VMCS_GUEST_CS_ACCESS_RIGHTS                                  0x00004816
#define VMCS_GUEST_SS_ACCESS_RIGHTS                                  0x00004818
#define VMCS_GUEST_DS_ACCESS_RIGHTS                                  0x0000481A
#define VMCS_GUEST_FS_ACCESS_RIGHTS                                  0x0000481C
#define VMCS_GUEST_GS_ACCESS_RIGHTS                                  0x0000481E
#define VMCS_GUEST_LDTR_ACCESS_RIGHTS                                0x00004820
#define VMCS_GUEST_TR_ACCESS_RIGHTS                                  0x00004822
#define VMCS_GUEST_INTERRUPTIBILITY_STATE                            0x00004824
#define VMCS_GUEST_ACTIVITY_STATE                                    0x00004826
#define VMCS_GUEST_SMBASE                                            0x00004828
#define VMCS_GUEST_SYSENTER_CS                                       0x0000482A
#define VMCS_GUEST_PREEMPT_TIMER_VALUE                               0x0000482E
/**
 * @}
 */

/**
 * @defgroup vmcs_32_bit_host_state_fields \
 *           32-Bit Host-State Field
 * @{
 */
#define VMCS_SYSENTER_CS                                             0x00004C00
/**
 * @}
 */

/**
 * @}
 */

/**
 * @defgroup vmcs_natural_width \
 *           Natural-Width Fields
 * @{
 */
/**
 * @defgroup vmcs_natural_width_control_fields \
 *           Natural-Width Control Fields
 * @{
 */
#define VMCS_CTRL_CR0_MASK                                           0x00006000
#define VMCS_CTRL_CR4_MASK                                           0x00006002
#define VMCS_CTRL_CR0_READ_SHADOW                                    0x00006004
#define VMCS_CTRL_CR4_READ_SHADOW                                    0x00006006
#define VMCS_CTRL_CR3_TARGET_VAL0                                    0x00006008
#define VMCS_CTRL_CR3_TARGET_VAL1                                    0x0000600A
#define VMCS_CTRL_CR3_TARGET_VAL2                                    0x0000600C
#define VMCS_CTRL_CR3_TARGET_VAL3                                    0x0000600E
/**
 * @}
 */

/**
 * @defgroup vmcs_natural_width_read_only_data_fields \
 *           Natural-Width Read-Only Data Fields
 * @{
 */
#define VMCS_EXIT_QUALIFICATION                                      0x00006400
#define VMCS_IO_RCX                                                  0x00006402
#define VMCS_IO_RSX                                                  0x00006404
#define VMCS_IO_RDI                                                  0x00006406
#define VMCS_IO_RIP                                                  0x00006408
#define VMCS_EXIT_GUEST_LINEAR_ADDR                                  0x0000640A
/**
 * @}
 */

/**
 * @defgroup vmcs_natural_width_guest_state_fields \
 *           Natural-Width Guest-State Fields
 * @{
 */
#define VMCS_GUEST_CR0                                               0x00006800
#define VMCS_GUEST_CR3                                               0x00006802
#define VMCS_GUEST_CR4                                               0x00006804
#define VMCS_GUEST_ES_BASE                                           0x00006806
#define VMCS_GUEST_CS_BASE                                           0x00006808
#define VMCS_GUEST_SS_BASE                                           0x0000680A
#define VMCS_GUEST_DS_BASE                                           0x0000680C
#define VMCS_GUEST_FS_BASE                                           0x0000680E
#define VMCS_GUEST_GS_BASE                                           0x00006810
#define VMCS_GUEST_LDTR_BASE                                         0x00006812
#define VMCS_GUEST_TR_BASE                                           0x00006814
#define VMCS_GUEST_GDTR_BASE                                         0x00006816
#define VMCS_GUEST_IDTR_BASE                                         0x00006818
#define VMCS_GUEST_DR7                                               0x0000681A
#define VMCS_GUEST_RSP                                               0x0000681C
#define VMCS_GUEST_RIP                                               0x0000681E
#define VMCS_GUEST_RFLAGS                                            0x00006820
#define VMCS_GUEST_PENDING_DEBUG_EXCEPTIONS                          0x00006822
#define VMCS_GUEST_SYSENTER_ESP                                      0x00006824
#define VMCS_GUEST_SYSENTER_EIP                                      0x00006826
/**
 * @}
 */

/**
 * @defgroup vmcs_natural_width_host_state_fields \
 *           Natural-Width Host-State Fields
 * @{
 */
#define VMCS_HOST_CR0                                                0x00006C00
#define VMCS_HOST_CR3                                                0x00006C02
#define VMCS_HOST_CR4                                                0x00006C04
#define VMCS_HOST_FS_BASE                                            0x00006C06
#define VMCS_HOST_GS_BASE                                            0x00006C08
#define VMCS_HOST_TR_BASE                                            0x00006C0A
#define VMCS_HOST_GDTR_BASE                                          0x00006C0C
#define VMCS_HOST_IDTR_BASE                                          0x00006C0E
#define VMCS_HOST_SYSENTER_ESP                                       0x00006C10
#define VMCS_HOST_SYSENTER_EIP                                       0x00006C12
#define VMCS_HOST_RSP                                                0x00006C14
#define VMCS_HOST_RIP                                                0x00006C16
/**
 * @}
 */

/**
 * @}
 */

/**
 * @}
 */

typedef enum {
  external_interrupt                                           = 0x00000000,
  non_maskable_interrupt                                       = 0x00000002,
  hardware_exception                                           = 0x00000003,
  software_interrupt                                           = 0x00000004,
  privileged_software_exception                                = 0x00000005,
  software_exception                                           = 0x00000006,
  other_event                                                  = 0x00000007,
} interruption_type;

typedef union {
  struct {
    uint32_t vector                                                  : 8;
    uint32_t interruption_type                                       : 3;
    uint32_t deliver_error_code                                      : 1;
    uint32_t reserved_1                                              : 19;
    uint32_t valid                                                   : 1;
  };

  uint32_t flags;
} vmentry_interrupt_info;

typedef union {
  struct {
    uint32_t vector                                                  : 8;
    uint32_t interruption_type                                       : 3;
    uint32_t error_code_valid                                        : 1;
    uint32_t nmi_unblocking                                          : 1;
    uint32_t reserved_1                                              : 18;
    uint32_t valid                                                   : 1;
  };

  uint32_t flags;
} vmexit_interrupt_info;

/**
 * @}
 */

/**
 * @defgroup apic \
 *           Advanced Programmable Interrupt Controller (APIC)
 * @{
 */
#define APIC_BASE                                                    0xFEE00000
#define APIC_ID                                                      0x00000020
#define APIC_VERSION                                                 0x00000030
#define APIC_TPR                                                     0x00000080
#define APIC_APR                                                     0x00000090
#define APIC_PPR                                                     0x000000A0
#define APIC_EOI                                                     0x000000B0
#define APIC_REMOTE_READ                                             0x000000C0
#define APIC_LOGICAL_DESTINATION                                     0x000000D0
#define APIC_DESTINATION_FORMAT                                      0x000000E0
#define APIC_SIV                                                     0x000000F0
#define APIC_ISR_31_0                                                0x00000100
#define APIC_ISR_63_32                                               0x00000110
#define APIC_ISR_95_64                                               0x00000120
#define APIC_ISR_127_96                                              0x00000130
#define APIC_ISR_159_128                                             0x00000140
#define APIC_ISR_191_160                                             0x00000150
#define APIC_ISR_223_192                                             0x00000160
#define APIC_ISR_255_224                                             0x00000170
#define APIC_TMR_31_0                                                0x00000180
#define APIC_TMR_63_32                                               0x00000190
#define APIC_TMR_95_64                                               0x000001A0
#define APIC_TMR_127_96                                              0x000001B0
#define APIC_TMR_159_128                                             0x000001C0
#define APIC_TMR_191_160                                             0x000001D0
#define APIC_TMR_223_192                                             0x000001E0
#define APIC_TMR_255_224                                             0x000001F0
#define APIC_IRR_31_0                                                0x00000200
#define APIC_IRR_63_32                                               0x00000210
#define APIC_IRR_95_64                                               0x00000220
#define APIC_IRR_127_96                                              0x00000230
#define APIC_IRR_159_128                                             0x00000240
#define APIC_IRR_191_160                                             0x00000250
#define APIC_IRR_223_192                                             0x00000260
#define APIC_IRR_255_224                                             0x00000270
#define APIC_ERROR_STATUS                                            0x00000280
#define APIC_CMCI                                                    0x000002F0
#define APIC_ICR_0_31                                                0x00000300
#define APIC_ICR_32_63                                               0x00000310
#define APIC_LVT_TIMER                                               0x00000320
#define APIC_LVT_THERMAL_SENSOR                                      0x00000330
#define APIC_LVT_PERFORMANCE_MONITORING_COUNTERS                     0x00000340
#define APIC_LVT_LINT0                                               0x00000350
#define APIC_LVT_LINT1                                               0x00000360
#define APIC_LVT_ERROR                                               0x00000370
#define APIC_INITIAL_COUNT                                           0x00000380
#define APIC_CURRENT_COUNT                                           0x00000390
#define APIC_DIVIDE_CONFIGURATION                                    0x000003E0
/**
 * @}
 */

typedef union {
  struct {
    uint32_t carry_flag                                              : 1;
    uint32_t read_as_1                                               : 1;
    uint32_t parity_flag                                             : 1;
    uint32_t reserved_1                                              : 1;
    uint32_t auxiliary_carry_flag                                    : 1;
    uint32_t reserved_2                                              : 1;
    uint32_t zero_flag                                               : 1;
    uint32_t sign_flag                                               : 1;
    uint32_t trap_flag                                               : 1;
    uint32_t interrupt_enable_flag                                   : 1;
    uint32_t direction_flag                                          : 1;
    uint32_t overflow_flag                                           : 1;
    uint32_t io_privilege_level                                      : 2;
    uint32_t nested_task_flag                                        : 1;
    uint32_t reserved_3                                              : 1;
    uint32_t resume_flag                                             : 1;
    uint32_t virtual_8086_mode_flag                                  : 1;
    uint32_t alignment_check_flag                                    : 1;
    uint32_t virtual_interrupt_flag                                  : 1;
    uint32_t virtual_interrupt_pending_flag                          : 1;
    uint32_t identification_flag                                     : 1;
  };

  uint32_t flags;
} efl;

/**
 * @defgroup exceptions \
 *           Exceptions
 * @{
 */
typedef enum {
  divide_error                                                 = 0x00000000,
  debug                                                        = 0x00000001,
  breakpoint                                                   = 0x00000003,
  overflow                                                     = 0x00000004,
  bound_range_exceeded                                         = 0x00000005,
  invalid_opcode                                               = 0x00000006,
  device_not_available                                         = 0x00000007,
  double_fault                                                 = 0x00000008,
  coprocessor_segment_overrun                                  = 0x00000009,
  invalid_tss                                                  = 0x0000000A,
  segment_not_present                                          = 0x0000000B,
  stack_segment_fault                                          = 0x0000000C,
  general_protection                                           = 0x0000000D,
  page_fault                                                   = 0x0000000E,
  x87_floating_point_error                                     = 0x00000010,
  alignment_check                                              = 0x00000011,
  machine_check                                                = 0x00000012,
  simd_floating_point_error                                    = 0x00000013,
  virtualization_exception                                     = 0x00000014,
} exception_vector;

typedef union {
  struct {
    uint32_t external_event                                          : 1;
    uint32_t descriptor_location                                     : 1;
    uint32_t gdt_ldt                                                 : 1;
    uint32_t index                                                   : 13;
  };

  uint32_t flags;
} exception_error_code;

typedef union {
  struct {
    uint32_t present                                                 : 1;
    uint32_t write                                                   : 1;
    uint32_t user_mode_access                                        : 1;
    uint32_t reserved_bit_violation                                  : 1;
    uint32_t execute                                                 : 1;
    uint32_t protection_key_violation                                : 1;
    uint32_t reserved_1                                              : 9;
    uint32_t sgx                                                     : 1;
  };

  uint32_t flags;
} page_fault_exception;

/**
 * @}
 */

/**
 * @defgroup memory_type \
 *           Memory caching type
 * @{
 */
#define MEMORY_TYPE_UC                                               0x00000000
#define MEMORY_TYPE_WC                                               0x00000001
#define MEMORY_TYPE_WT                                               0x00000004
#define MEMORY_TYPE_WP                                               0x00000005
#define MEMORY_TYPE_WB                                               0x00000006
#define MEMORY_TYPE_INVALID                                          0x000000FF
/**
 * @}
 */

/**
 * @}
 */


