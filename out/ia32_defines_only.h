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
#define CR0_PROTECTION_ENABLE                                        0x01
    uint64_t monitor_coprocessor                                     : 1;
#define CR0_MONITOR_COPROCESSOR                                      0x02
    uint64_t emulate_fpu                                             : 1;
#define CR0_EMULATE_FPU                                              0x04
    uint64_t task_switched                                           : 1;
#define CR0_TASK_SWITCHED                                            0x08
    uint64_t extension_type                                          : 1;
#define CR0_EXTENSION_TYPE                                           0x10
    uint64_t numeric_error                                           : 1;
#define CR0_NUMERIC_ERROR                                            0x20
    uint64_t reserved_1                                              : 10;
    uint64_t write_protect                                           : 1;
#define CR0_WRITE_PROTECT                                            0x10000
    uint64_t reserved_2                                              : 1;
    uint64_t alignment_mask                                          : 1;
#define CR0_ALIGNMENT_MASK                                           0x40000
    uint64_t reserved_3                                              : 10;
    uint64_t not_write_through                                       : 1;
#define CR0_NOT_WRITE_THROUGH                                        0x20000000
    uint64_t cache_disable                                           : 1;
#define CR0_CACHE_DISABLE                                            0x40000000
    uint64_t paging_enable                                           : 1;
#define CR0_PAGING_ENABLE                                            0x80000000
    uint64_t reserved_4                                              : 32;
  };

  uint64_t Flags;
} cr0;

typedef union {
  struct {
    uint64_t reserved_1                                              : 3;
    uint64_t page_level_write_through                                : 1;
#define CR3_PAGE_LEVEL_WRITE_THROUGH                                 0x08
    uint64_t page_level_cache_disable                                : 1;
#define CR3_PAGE_LEVEL_CACHE_DISABLE                                 0x10
    uint64_t reserved_2                                              : 7;
    uint64_t address_of_page_directory                               : 36;
#define CR3_ADDRESS_OF_PAGE_DIRECTORY                                0xFFFFFFFFF000
    uint64_t reserved_3                                              : 16;
  };

  uint64_t Flags;
} cr3;

typedef union {
  struct {
    uint64_t virtual_mode_extensions                                 : 1;
#define CR4_VIRTUAL_MODE_EXTENSIONS                                  0x01
    uint64_t protected_mode_virtual_interrupts                       : 1;
#define CR4_PROTECTED_MODE_VIRTUAL_INTERRUPTS                        0x02
    uint64_t timestamp_disable                                       : 1;
#define CR4_TIMESTAMP_DISABLE                                        0x04
    uint64_t debugging_extensions                                    : 1;
#define CR4_DEBUGGING_EXTENSIONS                                     0x08
    uint64_t page_size_extensions                                    : 1;
#define CR4_PAGE_SIZE_EXTENSIONS                                     0x10
    uint64_t physical_address_extension                              : 1;
#define CR4_PHYSICAL_ADDRESS_EXTENSION                               0x20
    uint64_t machine_check_enable                                    : 1;
#define CR4_MACHINE_CHECK_ENABLE                                     0x40
    uint64_t page_global_enable                                      : 1;
#define CR4_PAGE_GLOBAL_ENABLE                                       0x80
    uint64_t performance_monitoring_counter_enable                   : 1;
#define CR4_PERFORMANCE_MONITORING_COUNTER_ENABLE                    0x100
    uint64_t os_fxsave_fxrstor_support                               : 1;
#define CR4_OS_FXSAVE_FXRSTOR_SUPPORT                                0x200
    uint64_t os_xmm_exception_support                                : 1;
#define CR4_OS_XMM_EXCEPTION_SUPPORT                                 0x400
    uint64_t usermode_instruction_prevention                         : 1;
#define CR4_USERMODE_INSTRUCTION_PREVENTION                          0x800
    uint64_t reserved_1                                              : 1;
    uint64_t vmx_enable                                              : 1;
#define CR4_VMX_ENABLE                                               0x2000
    uint64_t smx_enable                                              : 1;
#define CR4_SMX_ENABLE                                               0x4000
    uint64_t reserved_2                                              : 1;
    uint64_t fsgsbase_enable                                         : 1;
#define CR4_FSGSBASE_ENABLE                                          0x10000
    uint64_t pcid_enable                                             : 1;
#define CR4_PCID_ENABLE                                              0x20000
    uint64_t os_xsave                                                : 1;
#define CR4_OS_XSAVE                                                 0x40000
    uint64_t reserved_3                                              : 1;
    uint64_t smep_enable                                             : 1;
#define CR4_SMEP_ENABLE                                              0x100000
    uint64_t smap_enable                                             : 1;
#define CR4_SMAP_ENABLE                                              0x200000
    uint64_t protection_key_enable                                   : 1;
#define CR4_PROTECTION_KEY_ENABLE                                    0x400000
    uint64_t reserved_4                                              : 41;
  };

  uint64_t Flags;
} cr4;

typedef union {
  struct {
    uint64_t task_priority_level                                     : 4;
#define CR8_TASK_PRIORITY_LEVEL                                      0x0F
    uint64_t reserved                                                : 60;
#define CR8_RESERVED                                                 0xFFFFFFFFFFFFFFF0
  };

  uint64_t Flags;
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
#define DR6_BREAKPOINT_CONDITION                                     0x0F
    uint64_t reserved_1                                              : 9;
    uint64_t debug_register_access_detected                          : 1;
#define DR6_DEBUG_REGISTER_ACCESS_DETECTED                           0x2000
    uint64_t single_instruction                                      : 1;
#define DR6_SINGLE_INSTRUCTION                                       0x4000
    uint64_t task_switch                                             : 1;
#define DR6_TASK_SWITCH                                              0x8000
    uint64_t restricted_transactional_memory                         : 1;
#define DR6_RESTRICTED_TRANSACTIONAL_MEMORY                          0x10000
    uint64_t reserved_2                                              : 47;
  };

  uint64_t Flags;
} dr6;

typedef union {
  struct {
    uint64_t local_breakpoint_0                                      : 1;
#define DR7_LOCAL_BREAKPOINT_0                                       0x01
    uint64_t global_breakpoint_0                                     : 1;
#define DR7_GLOBAL_BREAKPOINT_0                                      0x02
    uint64_t local_breakpoint_1                                      : 1;
#define DR7_LOCAL_BREAKPOINT_1                                       0x04
    uint64_t global_breakpoint_1                                     : 1;
#define DR7_GLOBAL_BREAKPOINT_1                                      0x08
    uint64_t local_breakpoint_2                                      : 1;
#define DR7_LOCAL_BREAKPOINT_2                                       0x10
    uint64_t global_breakpoint_2                                     : 1;
#define DR7_GLOBAL_BREAKPOINT_2                                      0x20
    uint64_t local_breakpoint_3                                      : 1;
#define DR7_LOCAL_BREAKPOINT_3                                       0x40
    uint64_t global_breakpoint_3                                     : 1;
#define DR7_GLOBAL_BREAKPOINT_3                                      0x80
    uint64_t local_exact_breakpoint                                  : 1;
#define DR7_LOCAL_EXACT_BREAKPOINT                                   0x100
    uint64_t global_exact_breakpoint                                 : 1;
#define DR7_GLOBAL_EXACT_BREAKPOINT                                  0x200
    uint64_t reserved_1                                              : 1;
    uint64_t restricted_transactional_memory                         : 1;
#define DR7_RESTRICTED_TRANSACTIONAL_MEMORY                          0x800
    uint64_t reserved_2                                              : 1;
    uint64_t general_detect                                          : 1;
#define DR7_GENERAL_DETECT                                           0x2000
    uint64_t reserved_3                                              : 2;
    uint64_t read_write_0                                            : 2;
#define DR7_READ_WRITE_0                                             0x30000
    uint64_t length_0                                                : 2;
#define DR7_LENGTH_0                                                 0xC0000
    uint64_t read_write_1                                            : 2;
#define DR7_READ_WRITE_1                                             0x300000
    uint64_t length_1                                                : 2;
#define DR7_LENGTH_1                                                 0xC00000
    uint64_t read_write_2                                            : 2;
#define DR7_READ_WRITE_2                                             0x3000000
    uint64_t length_2                                                : 2;
#define DR7_LENGTH_2                                                 0xC000000
    uint64_t read_write_3                                            : 2;
#define DR7_READ_WRITE_3                                             0x30000000
    uint64_t length_3                                                : 2;
#define DR7_LENGTH_3                                                 0xC0000000
    uint64_t reserved_4                                              : 32;
  };

  uint64_t Flags;
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
#define CPUID_EAX_STEPPING_ID                                        0x0F
      uint32_t model                                                 : 4;
#define CPUID_EAX_MODEL                                              0xF0
      uint32_t family_id                                             : 4;
#define CPUID_EAX_FAMILY_ID                                          0xF00
      uint32_t processor_type                                        : 2;
#define CPUID_EAX_PROCESSOR_TYPE                                     0x3000
      uint32_t reserved_1                                            : 2;
      uint32_t extended_model_id                                     : 4;
#define CPUID_EAX_EXTENDED_MODEL_ID                                  0xF0000
      uint32_t extended_family_id                                    : 8;
#define CPUID_EAX_EXTENDED_FAMILY_ID                                 0xFF00000
      uint32_t reserved_2                                            : 4;
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t brand_index                                           : 8;
#define CPUID_EBX_BRAND_INDEX                                        0xFF
      uint32_t clflush_line_size                                     : 8;
#define CPUID_EBX_CLFLUSH_LINE_SIZE                                  0xFF00
      uint32_t max_addressable_ids                                   : 8;
#define CPUID_EBX_MAX_ADDRESSABLE_IDS                                0xFF0000
      uint32_t initial_apic_id                                       : 8;
#define CPUID_EBX_INITIAL_APIC_ID                                    0xFF000000
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t streaming_simd_extensions_3                           : 1;
#define CPUID_ECX_STREAMING_SIMD_EXTENSIONS_3                        0x01
      uint32_t pclmulqdq_instruction                                 : 1;
#define CPUID_ECX_PCLMULQDQ_INSTRUCTION                              0x02
      uint32_t ds_area_64bit_layout                                  : 1;
#define CPUID_ECX_DS_AREA_64BIT_LAYOUT                               0x04
      uint32_t monitor_mwait_instruction                             : 1;
#define CPUID_ECX_MONITOR_MWAIT_INSTRUCTION                          0x08
      uint32_t cpl_qualified_debug_store                             : 1;
#define CPUID_ECX_CPL_QUALIFIED_DEBUG_STORE                          0x10
      uint32_t virtual_machine_extensions                            : 1;
#define CPUID_ECX_VIRTUAL_MACHINE_EXTENSIONS                         0x20
      uint32_t safer_mode_extensions                                 : 1;
#define CPUID_ECX_SAFER_MODE_EXTENSIONS                              0x40
      uint32_t enhanced_intel_speedstep_technology                   : 1;
#define CPUID_ECX_ENHANCED_INTEL_SPEEDSTEP_TECHNOLOGY                0x80
      uint32_t thermal_monitor_2                                     : 1;
#define CPUID_ECX_THERMAL_MONITOR_2                                  0x100
      uint32_t supplemental_streaming_simd_extensions_3              : 1;
#define CPUID_ECX_SUPPLEMENTAL_STREAMING_SIMD_EXTENSIONS_3           0x200
      uint32_t l1_context_id                                         : 1;
#define CPUID_ECX_L1_CONTEXT_ID                                      0x400
      uint32_t silicon_debug                                         : 1;
#define CPUID_ECX_SILICON_DEBUG                                      0x800
      uint32_t fma_extensions                                        : 1;
#define CPUID_ECX_FMA_EXTENSIONS                                     0x1000
      uint32_t cmpxchg16b_instruction                                : 1;
#define CPUID_ECX_CMPXCHG16B_INSTRUCTION                             0x2000
      uint32_t xtpr_update_control                                   : 1;
#define CPUID_ECX_XTPR_UPDATE_CONTROL                                0x4000
      uint32_t perfmon_and_debug_capability                          : 1;
#define CPUID_ECX_PERFMON_AND_DEBUG_CAPABILITY                       0x8000
      uint32_t reserved_1                                            : 1;
      uint32_t process_context_identifiers                           : 1;
#define CPUID_ECX_PROCESS_CONTEXT_IDENTIFIERS                        0x20000
      uint32_t direct_cache_access                                   : 1;
#define CPUID_ECX_DIRECT_CACHE_ACCESS                                0x40000
      uint32_t sse41_support                                         : 1;
#define CPUID_ECX_SSE41_SUPPORT                                      0x80000
      uint32_t sse42_support                                         : 1;
#define CPUID_ECX_SSE42_SUPPORT                                      0x100000
      uint32_t x2apic_support                                        : 1;
#define CPUID_ECX_X2APIC_SUPPORT                                     0x200000
      uint32_t movbe_instruction                                     : 1;
#define CPUID_ECX_MOVBE_INSTRUCTION                                  0x400000
      uint32_t popcnt_instruction                                    : 1;
#define CPUID_ECX_POPCNT_INSTRUCTION                                 0x800000
      uint32_t tsc_deadline                                          : 1;
#define CPUID_ECX_TSC_DEADLINE                                       0x1000000
      uint32_t aesni_instruction_extensions                          : 1;
#define CPUID_ECX_AESNI_INSTRUCTION_EXTENSIONS                       0x2000000
      uint32_t xsave_xrstor_instruction                              : 1;
#define CPUID_ECX_XSAVE_XRSTOR_INSTRUCTION                           0x4000000
      uint32_t osx_save                                              : 1;
#define CPUID_ECX_OSX_SAVE                                           0x8000000
      uint32_t avx_support                                           : 1;
#define CPUID_ECX_AVX_SUPPORT                                        0x10000000
      uint32_t half_precision_conversion_instructions                : 1;
#define CPUID_ECX_HALF_PRECISION_CONVERSION_INSTRUCTIONS             0x20000000
      uint32_t rdrand_instruction                                    : 1;
#define CPUID_ECX_RDRAND_INSTRUCTION                                 0x40000000
      uint32_t reserved_2                                            : 1;
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t floating_point_unit_on_chip                           : 1;
#define CPUID_EDX_FLOATING_POINT_UNIT_ON_CHIP                        0x01
      uint32_t virtual_8086_mode_enhancements                        : 1;
#define CPUID_EDX_VIRTUAL_8086_MODE_ENHANCEMENTS                     0x02
      uint32_t debugging_extensions                                  : 1;
#define CPUID_EDX_DEBUGGING_EXTENSIONS                               0x04
      uint32_t page_size_extension                                   : 1;
#define CPUID_EDX_PAGE_SIZE_EXTENSION                                0x08
      uint32_t timestamp_counter                                     : 1;
#define CPUID_EDX_TIMESTAMP_COUNTER                                  0x10
      uint32_t rdmsr_wrmsr_instructions                              : 1;
#define CPUID_EDX_RDMSR_WRMSR_INSTRUCTIONS                           0x20
      uint32_t physical_address_extension                            : 1;
#define CPUID_EDX_PHYSICAL_ADDRESS_EXTENSION                         0x40
      uint32_t machine_check_exception                               : 1;
#define CPUID_EDX_MACHINE_CHECK_EXCEPTION                            0x80
      uint32_t cmpxchg8b_instruction                                 : 1;
#define CPUID_EDX_CMPXCHG8B_INSTRUCTION                              0x100
      uint32_t apic_on_chip                                          : 1;
#define CPUID_EDX_APIC_ON_CHIP                                       0x200
      uint32_t reserved_1                                            : 1;
      uint32_t sysenter_sysexit_instructions                         : 1;
#define CPUID_EDX_SYSENTER_SYSEXIT_INSTRUCTIONS                      0x800
      uint32_t memory_type_range_registers                           : 1;
#define CPUID_EDX_MEMORY_TYPE_RANGE_REGISTERS                        0x1000
      uint32_t page_global_bit                                       : 1;
#define CPUID_EDX_PAGE_GLOBAL_BIT                                    0x2000
      uint32_t machine_check_architecture                            : 1;
#define CPUID_EDX_MACHINE_CHECK_ARCHITECTURE                         0x4000
      uint32_t conditional_move_instructions                         : 1;
#define CPUID_EDX_CONDITIONAL_MOVE_INSTRUCTIONS                      0x8000
      uint32_t page_attribute_table                                  : 1;
#define CPUID_EDX_PAGE_ATTRIBUTE_TABLE                               0x10000
      uint32_t page_size_extension_36bit                             : 1;
#define CPUID_EDX_PAGE_SIZE_EXTENSION_36BIT                          0x20000
      uint32_t processor_serial_number                               : 1;
#define CPUID_EDX_PROCESSOR_SERIAL_NUMBER                            0x40000
      uint32_t clflush_instruction                                   : 1;
#define CPUID_EDX_CLFLUSH_INSTRUCTION                                0x80000
      uint32_t reserved_2                                            : 1;
      uint32_t debug_store                                           : 1;
#define CPUID_EDX_DEBUG_STORE                                        0x200000
      uint32_t thermal_control_msrs_for_acpi                         : 1;
#define CPUID_EDX_THERMAL_CONTROL_MSRS_FOR_ACPI                      0x400000
      uint32_t mmx_support                                           : 1;
#define CPUID_EDX_MMX_SUPPORT                                        0x800000
      uint32_t fxsave_fxrstor_instructions                           : 1;
#define CPUID_EDX_FXSAVE_FXRSTOR_INSTRUCTIONS                        0x1000000
      uint32_t sse_support                                           : 1;
#define CPUID_EDX_SSE_SUPPORT                                        0x2000000
      uint32_t sse2_support                                          : 1;
#define CPUID_EDX_SSE2_SUPPORT                                       0x4000000
      uint32_t self_snoop                                            : 1;
#define CPUID_EDX_SELF_SNOOP                                         0x8000000
      uint32_t hyper_threading_technology                            : 1;
#define CPUID_EDX_HYPER_THREADING_TECHNOLOGY                         0x10000000
      uint32_t thermal_monitor                                       : 1;
#define CPUID_EDX_THERMAL_MONITOR                                    0x20000000
      uint32_t reserved_3                                            : 1;
      uint32_t pending_break_enable                                  : 1;
#define CPUID_EDX_PENDING_BREAK_ENABLE                               0x80000000
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_01;

#define CPUID_CACHE_PARAMS                                           0x00000004
typedef struct {
  union {
    struct {
      uint32_t cache_type_field                                      : 5;
#define CPUID_EAX_CACHE_TYPE_FIELD                                   0x1F
      uint32_t cache_level                                           : 3;
#define CPUID_EAX_CACHE_LEVEL                                        0xE0
      uint32_t self_initializing_cache_level                         : 1;
#define CPUID_EAX_SELF_INITIALIZING_CACHE_LEVEL                      0x100
      uint32_t fully_associative_cache                               : 1;
#define CPUID_EAX_FULLY_ASSOCIATIVE_CACHE                            0x200
      uint32_t reserved_1                                            : 4;
      uint32_t max_addressable_ids_for_logical_processors_sharing_this_cache: 12;
#define CPUID_EAX_MAX_ADDRESSABLE_IDS_FOR_LOGICAL_PROCESSORS_SHARING_THIS_CACHE 0x3FFC000
      uint32_t max_addressable_ids_for_processor_cores_in_physical_package: 6;
#define CPUID_EAX_MAX_ADDRESSABLE_IDS_FOR_PROCESSOR_CORES_IN_PHYSICAL_PACKAGE 0xFC000000
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t system_coherency_line_size                            : 12;
#define CPUID_EBX_SYSTEM_COHERENCY_LINE_SIZE                         0xFFF
      uint32_t physical_line_partitions                              : 10;
#define CPUID_EBX_PHYSICAL_LINE_PARTITIONS                           0x3FF000
      uint32_t ways_of_associativity                                 : 10;
#define CPUID_EBX_WAYS_OF_ASSOCIATIVITY                              0xFFC00000
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t number_of_sets                                        : 32;
#define CPUID_ECX_NUMBER_OF_SETS                                     0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t write_back_invalidate                                 : 1;
#define CPUID_EDX_WRITE_BACK_INVALIDATE                              0x01
      uint32_t cache_inclusiveness                                   : 1;
#define CPUID_EDX_CACHE_INCLUSIVENESS                                0x02
      uint32_t complex_cache_indexing                                : 1;
#define CPUID_EDX_COMPLEX_CACHE_INDEXING                             0x04
      uint32_t reserved_1                                            : 29;
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_04;

#define CPUID_MONITOR_MWAIT                                          0x00000005
typedef struct {
  union {
    struct {
      uint32_t smallest_monitor_line_size                            : 16;
#define CPUID_EAX_SMALLEST_MONITOR_LINE_SIZE                         0xFFFF
      uint32_t reserved_1                                            : 16;
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t largest_monitor_line_size                             : 16;
#define CPUID_EBX_LARGEST_MONITOR_LINE_SIZE                          0xFFFF
      uint32_t reserved_1                                            : 16;
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t enumeration_of_monitor_mwait_extensions               : 1;
#define CPUID_ECX_ENUMERATION_OF_MONITOR_MWAIT_EXTENSIONS            0x01
      uint32_t supports_treating_interrupts_as_break_event_for_mwait : 1;
#define CPUID_ECX_SUPPORTS_TREATING_INTERRUPTS_AS_BREAK_EVENT_FOR_MWAIT 0x02
      uint32_t reserved_1                                            : 30;
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t number_of_c0_sub_c_states                             : 4;
#define CPUID_EDX_NUMBER_OF_C0_SUB_C_STATES                          0x0F
      uint32_t number_of_c1_sub_c_states                             : 4;
#define CPUID_EDX_NUMBER_OF_C1_SUB_C_STATES                          0xF0
      uint32_t number_of_c2_sub_c_states                             : 4;
#define CPUID_EDX_NUMBER_OF_C2_SUB_C_STATES                          0xF00
      uint32_t number_of_c3_sub_c_states                             : 4;
#define CPUID_EDX_NUMBER_OF_C3_SUB_C_STATES                          0xF000
      uint32_t number_of_c4_sub_c_states                             : 4;
#define CPUID_EDX_NUMBER_OF_C4_SUB_C_STATES                          0xF0000
      uint32_t number_of_c5_sub_c_states                             : 4;
#define CPUID_EDX_NUMBER_OF_C5_SUB_C_STATES                          0xF00000
      uint32_t number_of_c6_sub_c_states                             : 4;
#define CPUID_EDX_NUMBER_OF_C6_SUB_C_STATES                          0xF000000
      uint32_t number_of_c7_sub_c_states                             : 4;
#define CPUID_EDX_NUMBER_OF_C7_SUB_C_STATES                          0xF0000000
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_05;

#define CPUID_THERMAL_POWER_MANAGEMENT                               0x00000006
typedef struct {
  union {
    struct {
      uint32_t temperature_sensor_supported                          : 1;
#define CPUID_EAX_TEMPERATURE_SENSOR_SUPPORTED                       0x01
      uint32_t intel_turbo_boost_technology_available                : 1;
#define CPUID_EAX_INTEL_TURBO_BOOST_TECHNOLOGY_AVAILABLE             0x02
      uint32_t apic_timer_always_running                             : 1;
#define CPUID_EAX_APIC_TIMER_ALWAYS_RUNNING                          0x04
      uint32_t reserved_1                                            : 1;
      uint32_t power_limit_notification                              : 1;
#define CPUID_EAX_POWER_LIMIT_NOTIFICATION                           0x10
      uint32_t clock_modulation_duty                                 : 1;
#define CPUID_EAX_CLOCK_MODULATION_DUTY                              0x20
      uint32_t package_thermal_management                            : 1;
#define CPUID_EAX_PACKAGE_THERMAL_MANAGEMENT                         0x40
      uint32_t hwp_base_registers                                    : 1;
#define CPUID_EAX_HWP_BASE_REGISTERS                                 0x80
      uint32_t hwp_notification                                      : 1;
#define CPUID_EAX_HWP_NOTIFICATION                                   0x100
      uint32_t hwp_activity_window                                   : 1;
#define CPUID_EAX_HWP_ACTIVITY_WINDOW                                0x200
      uint32_t hwp_energy_performance_preference                     : 1;
#define CPUID_EAX_HWP_ENERGY_PERFORMANCE_PREFERENCE                  0x400
      uint32_t hwp_package_level_request                             : 1;
#define CPUID_EAX_HWP_PACKAGE_LEVEL_REQUEST                          0x800
      uint32_t reserved_2                                            : 1;
      uint32_t hdc                                                   : 1;
#define CPUID_EAX_HDC                                                0x2000
      uint32_t intel_turbo_boost_max_technology_3_available          : 1;
#define CPUID_EAX_INTEL_TURBO_BOOST_MAX_TECHNOLOGY_3_AVAILABLE       0x4000
      uint32_t hwp_capabilities                                      : 1;
#define CPUID_EAX_HWP_CAPABILITIES                                   0x8000
      uint32_t hwp_peci_override                                     : 1;
#define CPUID_EAX_HWP_PECI_OVERRIDE                                  0x10000
      uint32_t flexible_hwp                                          : 1;
#define CPUID_EAX_FLEXIBLE_HWP                                       0x20000
      uint32_t fast_access_mode_for_hwp_request_msr                  : 1;
#define CPUID_EAX_FAST_ACCESS_MODE_FOR_HWP_REQUEST_MSR               0x40000
      uint32_t reserved_3                                            : 1;
      uint32_t ignoring_idle_logical_processor_hwp_request           : 1;
#define CPUID_EAX_IGNORING_IDLE_LOGICAL_PROCESSOR_HWP_REQUEST        0x100000
      uint32_t reserved_4                                            : 11;
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t number_of_interrupt_thresholds_in_thermal_sensor      : 4;
#define CPUID_EBX_NUMBER_OF_INTERRUPT_THRESHOLDS_IN_THERMAL_SENSOR   0x0F
      uint32_t reserved_1                                            : 28;
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t hardware_coordination_feedback_capability             : 1;
#define CPUID_ECX_HARDWARE_COORDINATION_FEEDBACK_CAPABILITY          0x01
      uint32_t reserved_1                                            : 2;
      uint32_t performance_energy_bias_preference                    : 1;
#define CPUID_ECX_PERFORMANCE_ENERGY_BIAS_PREFERENCE                 0x08
      uint32_t reserved_2                                            : 28;
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_06;

#define CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS                      0x00000007
typedef struct {
  union {
    struct {
      uint32_t number_of_sub_leaves                                  : 32;
#define CPUID_EAX_NUMBER_OF_SUB_LEAVES                               0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t fsgsbase                                              : 1;
#define CPUID_EBX_FSGSBASE                                           0x01
      uint32_t ia32_tsc_adjust_msr                                   : 1;
#define CPUID_EBX_IA32_TSC_ADJUST_MSR                                0x02
      uint32_t sgx                                                   : 1;
#define CPUID_EBX_SGX                                                0x04
      uint32_t bmi1                                                  : 1;
#define CPUID_EBX_BMI1                                               0x08
      uint32_t hle                                                   : 1;
#define CPUID_EBX_HLE                                                0x10
      uint32_t avx2                                                  : 1;
#define CPUID_EBX_AVX2                                               0x20
      uint32_t fdp_excptn_only                                       : 1;
#define CPUID_EBX_FDP_EXCPTN_ONLY                                    0x40
      uint32_t smep                                                  : 1;
#define CPUID_EBX_SMEP                                               0x80
      uint32_t bmi2                                                  : 1;
#define CPUID_EBX_BMI2                                               0x100
      uint32_t enhanced_rep_movsb_stosb                              : 1;
#define CPUID_EBX_ENHANCED_REP_MOVSB_STOSB                           0x200
      uint32_t invpcid                                               : 1;
#define CPUID_EBX_INVPCID                                            0x400
      uint32_t rtm                                                   : 1;
#define CPUID_EBX_RTM                                                0x800
      uint32_t rdt_m                                                 : 1;
#define CPUID_EBX_RDT_M                                              0x1000
      uint32_t deprecates                                            : 1;
#define CPUID_EBX_DEPRECATES                                         0x2000
      uint32_t mpx                                                   : 1;
#define CPUID_EBX_MPX                                                0x4000
      uint32_t rdt                                                   : 1;
#define CPUID_EBX_RDT                                                0x8000
      uint32_t avx512f                                               : 1;
#define CPUID_EBX_AVX512F                                            0x10000
      uint32_t avx512dq                                              : 1;
#define CPUID_EBX_AVX512DQ                                           0x20000
      uint32_t rdseed                                                : 1;
#define CPUID_EBX_RDSEED                                             0x40000
      uint32_t adx                                                   : 1;
#define CPUID_EBX_ADX                                                0x80000
      uint32_t smap                                                  : 1;
#define CPUID_EBX_SMAP                                               0x100000
      uint32_t avx512_ifma                                           : 1;
#define CPUID_EBX_AVX512_IFMA                                        0x200000
      uint32_t reserved_1                                            : 1;
      uint32_t clflushopt                                            : 1;
#define CPUID_EBX_CLFLUSHOPT                                         0x800000
      uint32_t clwb                                                  : 1;
#define CPUID_EBX_CLWB                                               0x1000000
      uint32_t intel                                                 : 1;
#define CPUID_EBX_INTEL                                              0x2000000
      uint32_t avx512pf                                              : 1;
#define CPUID_EBX_AVX512PF                                           0x4000000
      uint32_t avx512er                                              : 1;
#define CPUID_EBX_AVX512ER                                           0x8000000
      uint32_t avx512cd                                              : 1;
#define CPUID_EBX_AVX512CD                                           0x10000000
      uint32_t sha                                                   : 1;
#define CPUID_EBX_SHA                                                0x20000000
      uint32_t avx512bw                                              : 1;
#define CPUID_EBX_AVX512BW                                           0x40000000
      uint32_t avx512vl                                              : 1;
#define CPUID_EBX_AVX512VL                                           0x80000000
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t prefetchwt1                                           : 1;
#define CPUID_ECX_PREFETCHWT1                                        0x01
      uint32_t avx512_vbmi                                           : 1;
#define CPUID_ECX_AVX512_VBMI                                        0x02
      uint32_t umip                                                  : 1;
#define CPUID_ECX_UMIP                                               0x04
      uint32_t pku                                                   : 1;
#define CPUID_ECX_PKU                                                0x08
      uint32_t ospke                                                 : 1;
#define CPUID_ECX_OSPKE                                              0x10
      uint32_t reserved_1                                            : 12;
      uint32_t mawau                                                 : 5;
#define CPUID_ECX_MAWAU                                              0x3E0000
      uint32_t rdpid                                                 : 1;
#define CPUID_ECX_RDPID                                              0x400000
      uint32_t reserved_2                                            : 7;
      uint32_t sgx_lc                                                : 1;
#define CPUID_ECX_SGX_LC                                             0x40000000
      uint32_t reserved_3                                            : 1;
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_07;

#define CPUID_DIRECT_CACHE_ACCESS_INFO                               0x00000009
typedef struct {
  union {
    struct {
      uint32_t ia32_platform_dca_cap                                 : 32;
#define CPUID_EAX_IA32_PLATFORM_DCA_CAP                              0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EBX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_ECX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_09;

#define CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING                   0x0000000A
typedef struct {
  union {
    struct {
      uint32_t version_id_of_architectural_performance_monitoring    : 8;
#define CPUID_EAX_VERSION_ID_OF_ARCHITECTURAL_PERFORMANCE_MONITORING 0xFF
      uint32_t number_of_performance_monitoring_counter_per_logical_processor: 8;
#define CPUID_EAX_NUMBER_OF_PERFORMANCE_MONITORING_COUNTER_PER_LOGICAL_PROCESSOR 0xFF00
      uint32_t bit_width_of_performance_monitoring_counter           : 8;
#define CPUID_EAX_BIT_WIDTH_OF_PERFORMANCE_MONITORING_COUNTER        0xFF0000
      uint32_t ebx_bit_vector_length                                 : 8;
#define CPUID_EAX_EBX_BIT_VECTOR_LENGTH                              0xFF000000
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t core_cycle_event_not_available                        : 1;
#define CPUID_EBX_CORE_CYCLE_EVENT_NOT_AVAILABLE                     0x01
      uint32_t instruction_retired_event_not_available               : 1;
#define CPUID_EBX_INSTRUCTION_RETIRED_EVENT_NOT_AVAILABLE            0x02
      uint32_t reference_cycles_event_not_available                  : 1;
#define CPUID_EBX_REFERENCE_CYCLES_EVENT_NOT_AVAILABLE               0x04
      uint32_t last_level_cache_reference_event_not_available        : 1;
#define CPUID_EBX_LAST_LEVEL_CACHE_REFERENCE_EVENT_NOT_AVAILABLE     0x08
      uint32_t last_level_cache_misses_event_not_available           : 1;
#define CPUID_EBX_LAST_LEVEL_CACHE_MISSES_EVENT_NOT_AVAILABLE        0x10
      uint32_t branch_instruction_retired_event_not_available        : 1;
#define CPUID_EBX_BRANCH_INSTRUCTION_RETIRED_EVENT_NOT_AVAILABLE     0x20
      uint32_t branch_mispredict_retired_event_not_available         : 1;
#define CPUID_EBX_BRANCH_MISPREDICT_RETIRED_EVENT_NOT_AVAILABLE      0x40
      uint32_t reserved_1                                            : 25;
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_ECX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t number_of_fixed_function_performance_counters         : 5;
#define CPUID_EDX_NUMBER_OF_FIXED_FUNCTION_PERFORMANCE_COUNTERS      0x1F
      uint32_t bit_width_of_fixed_function_performance_counters      : 8;
#define CPUID_EDX_BIT_WIDTH_OF_FIXED_FUNCTION_PERFORMANCE_COUNTERS   0x1FE0
      uint32_t reserved_1                                            : 2;
      uint32_t any_thread_deprecation                                : 1;
#define CPUID_EDX_ANY_THREAD_DEPRECATION                             0x8000
      uint32_t reserved_2                                            : 16;
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_0a;

#define CPUID_EXTENDED_TOPOLOGY                                      0x0000000B
typedef struct {
  union {
    struct {
      uint32_t x2apic_id_to_unique_topology_id_shift                 : 5;
#define CPUID_EAX_X2APIC_ID_TO_UNIQUE_TOPOLOGY_ID_SHIFT              0x1F
      uint32_t reserved_1                                            : 27;
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t number_of_logical_processors_at_this_level_type       : 16;
#define CPUID_EBX_NUMBER_OF_LOGICAL_PROCESSORS_AT_THIS_LEVEL_TYPE    0xFFFF
      uint32_t reserved_1                                            : 16;
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t level_number                                          : 8;
#define CPUID_ECX_LEVEL_NUMBER                                       0xFF
      uint32_t level_type                                            : 8;
#define CPUID_ECX_LEVEL_TYPE                                         0xFF00
      uint32_t reserved_1                                            : 16;
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t x2apic_id                                             : 32;
#define CPUID_EDX_X2APIC_ID                                          0xFFFFFFFF
    };

    uint32_t Flags;
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
#define CPUID_EAX_X87_STATE                                          0x01
      uint32_t sse_state                                             : 1;
#define CPUID_EAX_SSE_STATE                                          0x02
      uint32_t avx_state                                             : 1;
#define CPUID_EAX_AVX_STATE                                          0x04
      uint32_t mpx_state                                             : 2;
#define CPUID_EAX_MPX_STATE                                          0x18
      uint32_t avx_512_state                                         : 3;
#define CPUID_EAX_AVX_512_STATE                                      0xE0
      uint32_t used_for_ia32_xss_1                                   : 1;
#define CPUID_EAX_USED_FOR_IA32_XSS_1                                0x100
      uint32_t pkru_state                                            : 1;
#define CPUID_EAX_PKRU_STATE                                         0x200
      uint32_t reserved_1                                            : 3;
      uint32_t used_for_ia32_xss_2                                   : 1;
#define CPUID_EAX_USED_FOR_IA32_XSS_2                                0x2000
      uint32_t reserved_2                                            : 18;
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t max_size_required_by_enabled_features_in_xcr0         : 32;
#define CPUID_EBX_MAX_SIZE_REQUIRED_BY_ENABLED_FEATURES_IN_XCR0      0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t max_size_of_xsave_xrstor_save_area                    : 32;
#define CPUID_ECX_MAX_SIZE_OF_XSAVE_XRSTOR_SAVE_AREA                 0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t xcr0_supported_bits                                   : 32;
#define CPUID_EDX_XCR0_SUPPORTED_BITS                                0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_0d_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t reserved_1                                            : 1;
      uint32_t supports_xsavec_and_compacted_xrstor                  : 1;
#define CPUID_EAX_SUPPORTS_XSAVEC_AND_COMPACTED_XRSTOR               0x02
      uint32_t supports_xgetbv_with_ecx_1                            : 1;
#define CPUID_EAX_SUPPORTS_XGETBV_WITH_ECX_1                         0x04
      uint32_t supports_xsave_xrstor_and_ia32_xss                    : 1;
#define CPUID_EAX_SUPPORTS_XSAVE_XRSTOR_AND_IA32_XSS                 0x08
      uint32_t reserved_2                                            : 28;
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t size_of_xsave_aread                                   : 32;
#define CPUID_EBX_SIZE_OF_XSAVE_AREAD                                0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t used_for_xcr0_1                                       : 8;
#define CPUID_ECX_USED_FOR_XCR0_1                                    0xFF
      uint32_t pt_state                                              : 1;
#define CPUID_ECX_PT_STATE                                           0x100
      uint32_t used_for_xcr0_2                                       : 1;
#define CPUID_ECX_USED_FOR_XCR0_2                                    0x200
      uint32_t reserved_1                                            : 3;
      uint32_t hwp_state                                             : 1;
#define CPUID_ECX_HWP_STATE                                          0x2000
      uint32_t reserved_2                                            : 18;
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_0d_ecx_01;

typedef struct {
  union {
    struct {
      uint32_t ia32_platform_dca_cap                                 : 32;
#define CPUID_EAX_IA32_PLATFORM_DCA_CAP                              0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EBX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t ecx_2                                                 : 1;
#define CPUID_ECX_ECX_2                                              0x01
      uint32_t ecx_1                                                 : 1;
#define CPUID_ECX_ECX_1                                              0x02
      uint32_t reserved_1                                            : 30;
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
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
#define CPUID_EAX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t rmid_max_range                                        : 32;
#define CPUID_EBX_RMID_MAX_RANGE                                     0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_ECX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved_1                                            : 1;
      uint32_t supports_l3_cache_intel_rdt_monitoring                : 1;
#define CPUID_EDX_SUPPORTS_L3_CACHE_INTEL_RDT_MONITORING             0x02
      uint32_t reserved_2                                            : 30;
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_0f_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EAX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t conversion_factor                                     : 32;
#define CPUID_EBX_CONVERSION_FACTOR                                  0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t rmid_max_range                                        : 32;
#define CPUID_ECX_RMID_MAX_RANGE                                     0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t supports_l3_occupancy_monitoring                      : 1;
#define CPUID_EDX_SUPPORTS_L3_OCCUPANCY_MONITORING                   0x01
      uint32_t supports_l3_total_bandwidth_monitoring                : 1;
#define CPUID_EDX_SUPPORTS_L3_TOTAL_BANDWIDTH_MONITORING             0x02
      uint32_t supports_l3_local_bandwidth_monitoring                : 1;
#define CPUID_EDX_SUPPORTS_L3_LOCAL_BANDWIDTH_MONITORING             0x04
      uint32_t reserved_1                                            : 29;
    };

    uint32_t Flags;
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
#define CPUID_EAX_IA32_PLATFORM_DCA_CAP                              0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t reserved_1                                            : 1;
      uint32_t supports_l3_cache_allocation_technology               : 1;
#define CPUID_EBX_SUPPORTS_L3_CACHE_ALLOCATION_TECHNOLOGY            0x02
      uint32_t supports_l2_cache_allocation_technology               : 1;
#define CPUID_EBX_SUPPORTS_L2_CACHE_ALLOCATION_TECHNOLOGY            0x04
      uint32_t supports_memory_bandwidth_allocation                  : 1;
#define CPUID_EBX_SUPPORTS_MEMORY_BANDWIDTH_ALLOCATION               0x08
      uint32_t reserved_2                                            : 28;
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_ECX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_10_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t length_of_capacity_bit_mask                           : 5;
#define CPUID_EAX_LENGTH_OF_CAPACITY_BIT_MASK                        0x1F
      uint32_t reserved_1                                            : 27;
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t ebx_0                                                 : 32;
#define CPUID_EBX_EBX_0                                              0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved_1                                            : 2;
      uint32_t code_and_data_priorization_technology_supported       : 1;
#define CPUID_ECX_CODE_AND_DATA_PRIORIZATION_TECHNOLOGY_SUPPORTED    0x04
      uint32_t reserved_2                                            : 29;
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t highest_cos_number_supported                          : 16;
#define CPUID_EDX_HIGHEST_COS_NUMBER_SUPPORTED                       0xFFFF
      uint32_t reserved_1                                            : 16;
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_10_ecx_01;

typedef struct {
  union {
    struct {
      uint32_t length_of_capacity_bit_mask                           : 5;
#define CPUID_EAX_LENGTH_OF_CAPACITY_BIT_MASK                        0x1F
      uint32_t reserved_1                                            : 27;
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t ebx_0                                                 : 32;
#define CPUID_EBX_EBX_0                                              0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_ECX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t highest_cos_number_supported                          : 16;
#define CPUID_EDX_HIGHEST_COS_NUMBER_SUPPORTED                       0xFFFF
      uint32_t reserved_1                                            : 16;
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_10_ecx_02;

typedef struct {
  union {
    struct {
      uint32_t max_mba_throttling_value                              : 12;
#define CPUID_EAX_MAX_MBA_THROTTLING_VALUE                           0xFFF
      uint32_t reserved_1                                            : 20;
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EBX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved_1                                            : 2;
      uint32_t response_of_delay_is_linear                           : 1;
#define CPUID_ECX_RESPONSE_OF_DELAY_IS_LINEAR                        0x04
      uint32_t reserved_2                                            : 29;
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t highest_cos_number_supported                          : 16;
#define CPUID_EDX_HIGHEST_COS_NUMBER_SUPPORTED                       0xFFFF
      uint32_t reserved_1                                            : 16;
    };

    uint32_t Flags;
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
#define CPUID_EAX_SGX1                                               0x01
      uint32_t sgx2                                                  : 1;
#define CPUID_EAX_SGX2                                               0x02
      uint32_t reserved_1                                            : 3;
      uint32_t sgx_enclv_advanced                                    : 1;
#define CPUID_EAX_SGX_ENCLV_ADVANCED                                 0x20
      uint32_t sgx_encls_advanced                                    : 1;
#define CPUID_EAX_SGX_ENCLS_ADVANCED                                 0x40
      uint32_t reserved_2                                            : 25;
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t miscselect                                            : 32;
#define CPUID_EBX_MISCSELECT                                         0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_ECX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t max_enclave_size_not64                                : 8;
#define CPUID_EDX_MAX_ENCLAVE_SIZE_NOT64                             0xFF
      uint32_t max_enclave_size_64                                   : 8;
#define CPUID_EDX_MAX_ENCLAVE_SIZE_64                                0xFF00
      uint32_t reserved_1                                            : 16;
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_12_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t valid_secs_attributes_0                               : 32;
#define CPUID_EAX_VALID_SECS_ATTRIBUTES_0                            0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t valid_secs_attributes_1                               : 32;
#define CPUID_EBX_VALID_SECS_ATTRIBUTES_1                            0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t valid_secs_attributes_2                               : 32;
#define CPUID_ECX_VALID_SECS_ATTRIBUTES_2                            0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t valid_secs_attributes_3                               : 32;
#define CPUID_EDX_VALID_SECS_ATTRIBUTES_3                            0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_12_ecx_01;

typedef struct {
  union {
    struct {
      uint32_t sub_leaf_type                                         : 4;
#define CPUID_EAX_SUB_LEAF_TYPE                                      0x0F
      uint32_t reserved_1                                            : 28;
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t zero                                                  : 32;
#define CPUID_EBX_ZERO                                               0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t zero                                                  : 32;
#define CPUID_ECX_ZERO                                               0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t zero                                                  : 32;
#define CPUID_EDX_ZERO                                               0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_12_ecx_02p_slt_0;

typedef struct {
  union {
    struct {
      uint32_t sub_leaf_type                                         : 4;
#define CPUID_EAX_SUB_LEAF_TYPE                                      0x0F
      uint32_t reserved_1                                            : 8;
      uint32_t epc_base_physical_address_1                           : 20;
#define CPUID_EAX_EPC_BASE_PHYSICAL_ADDRESS_1                        0xFFFFF000
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t epc_base_physical_address_2                           : 20;
#define CPUID_EBX_EPC_BASE_PHYSICAL_ADDRESS_2                        0xFFFFF
      uint32_t reserved_1                                            : 12;
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t epc_section_property                                  : 4;
#define CPUID_ECX_EPC_SECTION_PROPERTY                               0x0F
      uint32_t reserved_1                                            : 8;
      uint32_t epc_size_1                                            : 20;
#define CPUID_ECX_EPC_SIZE_1                                         0xFFFFF000
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t epc_size_2                                            : 20;
#define CPUID_EDX_EPC_SIZE_2                                         0xFFFFF
      uint32_t reserved_1                                            : 12;
    };

    uint32_t Flags;
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
#define CPUID_EAX_MAX_SUB_LEAF                                       0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t flag0                                                 : 1;
#define CPUID_EBX_FLAG0                                              0x01
      uint32_t flag1                                                 : 1;
#define CPUID_EBX_FLAG1                                              0x02
      uint32_t flag2                                                 : 1;
#define CPUID_EBX_FLAG2                                              0x04
      uint32_t flag3                                                 : 1;
#define CPUID_EBX_FLAG3                                              0x08
      uint32_t flag4                                                 : 1;
#define CPUID_EBX_FLAG4                                              0x10
      uint32_t flag5                                                 : 1;
#define CPUID_EBX_FLAG5                                              0x20
      uint32_t reserved_1                                            : 26;
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t flag0                                                 : 1;
#define CPUID_ECX_FLAG0                                              0x01
      uint32_t flag1                                                 : 1;
#define CPUID_ECX_FLAG1                                              0x02
      uint32_t flag2                                                 : 1;
#define CPUID_ECX_FLAG2                                              0x04
      uint32_t flag3                                                 : 1;
#define CPUID_ECX_FLAG3                                              0x08
      uint32_t reserved_1                                            : 27;
      uint32_t flag31                                                : 1;
#define CPUID_ECX_FLAG31                                             0x80000000
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_14_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t number_of_configurable_address_ranges_for_filtering   : 3;
#define CPUID_EAX_NUMBER_OF_CONFIGURABLE_ADDRESS_RANGES_FOR_FILTERING 0x07
      uint32_t reserved_1                                            : 13;
      uint32_t bitmap_of_supported_mtc_period_encodings              : 16;
#define CPUID_EAX_BITMAP_OF_SUPPORTED_MTC_PERIOD_ENCODINGS           0xFFFF0000
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t bitmap_of_supported_cycle_threshold_value_encodings   : 16;
#define CPUID_EBX_BITMAP_OF_SUPPORTED_CYCLE_THRESHOLD_VALUE_ENCODINGS 0xFFFF
      uint32_t bitmap_of_supported_configurable_psb_frequency_encodings: 16;
#define CPUID_EBX_BITMAP_OF_SUPPORTED_CONFIGURABLE_PSB_FREQUENCY_ENCODINGS 0xFFFF0000
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_ECX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
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
#define CPUID_EAX_DENOMINATOR                                        0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t numerator                                             : 32;
#define CPUID_EBX_NUMERATOR                                          0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t nominal_frequency                                     : 32;
#define CPUID_ECX_NOMINAL_FREQUENCY                                  0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_15;

#define CPUID_PROCESSOR_FREQUENCY                                    0x00000016
typedef struct {
  union {
    struct {
      uint32_t procesor_base_frequency_mhz                           : 16;
#define CPUID_EAX_PROCESOR_BASE_FREQUENCY_MHZ                        0xFFFF
      uint32_t reserved_1                                            : 16;
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t processor_maximum_frequency_mhz                       : 16;
#define CPUID_EBX_PROCESSOR_MAXIMUM_FREQUENCY_MHZ                    0xFFFF
      uint32_t reserved_1                                            : 16;
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t bus_frequency_mhz                                     : 16;
#define CPUID_ECX_BUS_FREQUENCY_MHZ                                  0xFFFF
      uint32_t reserved_1                                            : 16;
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
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
#define CPUID_EAX_MAX_SOC_ID_INDEX                                   0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t soc_vendor_id                                         : 16;
#define CPUID_EBX_SOC_VENDOR_ID                                      0xFFFF
      uint32_t is_vendor_scheme                                      : 1;
#define CPUID_EBX_IS_VENDOR_SCHEME                                   0x10000
      uint32_t reserved_1                                            : 15;
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t project_id                                            : 32;
#define CPUID_ECX_PROJECT_ID                                         0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t stepping_id                                           : 32;
#define CPUID_EDX_STEPPING_ID                                        0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_17_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t soc_vendor_brand_string                               : 32;
#define CPUID_EAX_SOC_VENDOR_BRAND_STRING                            0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t soc_vendor_brand_string                               : 32;
#define CPUID_EBX_SOC_VENDOR_BRAND_STRING                            0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t soc_vendor_brand_string                               : 32;
#define CPUID_ECX_SOC_VENDOR_BRAND_STRING                            0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t soc_vendor_brand_string                               : 32;
#define CPUID_EDX_SOC_VENDOR_BRAND_STRING                            0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_17_ecx_01_03;

typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EAX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EBX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_ECX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
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
#define CPUID_EAX_MAX_SUB_LEAF                                       0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t page_entries_4kb_supported                            : 1;
#define CPUID_EBX_PAGE_ENTRIES_4KB_SUPPORTED                         0x01
      uint32_t page_entries_2mb_supported                            : 1;
#define CPUID_EBX_PAGE_ENTRIES_2MB_SUPPORTED                         0x02
      uint32_t page_entries_4mb_supported                            : 1;
#define CPUID_EBX_PAGE_ENTRIES_4MB_SUPPORTED                         0x04
      uint32_t page_entries_1gb_supported                            : 1;
#define CPUID_EBX_PAGE_ENTRIES_1GB_SUPPORTED                         0x08
      uint32_t reserved_1                                            : 4;
      uint32_t partitioning                                          : 3;
#define CPUID_EBX_PARTITIONING                                       0x700
      uint32_t reserved_2                                            : 5;
      uint32_t ways_of_associativity_00                              : 16;
#define CPUID_EBX_WAYS_OF_ASSOCIATIVITY_00                           0xFFFF0000
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t number_of_sets                                        : 32;
#define CPUID_ECX_NUMBER_OF_SETS                                     0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t translation_cache_type_field                          : 5;
#define CPUID_EDX_TRANSLATION_CACHE_TYPE_FIELD                       0x1F
      uint32_t translation_cache_level                               : 3;
#define CPUID_EDX_TRANSLATION_CACHE_LEVEL                            0xE0
      uint32_t fully_associative_structure                           : 1;
#define CPUID_EDX_FULLY_ASSOCIATIVE_STRUCTURE                        0x100
      uint32_t reserved_1                                            : 5;
      uint32_t max_addressable_ids_for_logical_processors            : 12;
#define CPUID_EDX_MAX_ADDRESSABLE_IDS_FOR_LOGICAL_PROCESSORS         0x3FFC000
      uint32_t reserved_2                                            : 6;
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_18_ecx_00;

typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EAX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t page_entries_4kb_supported                            : 1;
#define CPUID_EBX_PAGE_ENTRIES_4KB_SUPPORTED                         0x01
      uint32_t page_entries_2mb_supported                            : 1;
#define CPUID_EBX_PAGE_ENTRIES_2MB_SUPPORTED                         0x02
      uint32_t page_entries_4mb_supported                            : 1;
#define CPUID_EBX_PAGE_ENTRIES_4MB_SUPPORTED                         0x04
      uint32_t page_entries_1gb_supported                            : 1;
#define CPUID_EBX_PAGE_ENTRIES_1GB_SUPPORTED                         0x08
      uint32_t reserved_1                                            : 4;
      uint32_t partitioning                                          : 3;
#define CPUID_EBX_PARTITIONING                                       0x700
      uint32_t reserved_2                                            : 5;
      uint32_t ways_of_associativity_01                              : 16;
#define CPUID_EBX_WAYS_OF_ASSOCIATIVITY_01                           0xFFFF0000
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t number_of_sets                                        : 32;
#define CPUID_ECX_NUMBER_OF_SETS                                     0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t translation_cache_type_field                          : 5;
#define CPUID_EDX_TRANSLATION_CACHE_TYPE_FIELD                       0x1F
      uint32_t translation_cache_level                               : 3;
#define CPUID_EDX_TRANSLATION_CACHE_LEVEL                            0xE0
      uint32_t fully_associative_structure                           : 1;
#define CPUID_EDX_FULLY_ASSOCIATIVE_STRUCTURE                        0x100
      uint32_t reserved_1                                            : 5;
      uint32_t max_addressable_ids_for_logical_processors            : 12;
#define CPUID_EDX_MAX_ADDRESSABLE_IDS_FOR_LOGICAL_PROCESSORS         0x3FFC000
      uint32_t reserved_2                                            : 6;
    };

    uint32_t Flags;
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
#define CPUID_EAX_MAX_EXTENDED_FUNCTIONS                             0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EBX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_ECX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_80000000;

#define CPUID_EXTENDED_CPU_SIGNATURE                                 0x80000001
typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EAX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EBX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t lahf_sahf_available_in_64_bit_mode                    : 1;
#define CPUID_ECX_LAHF_SAHF_AVAILABLE_IN_64_BIT_MODE                 0x01
      uint32_t reserved_1                                            : 4;
      uint32_t lzcnt                                                 : 1;
#define CPUID_ECX_LZCNT                                              0x20
      uint32_t reserved_2                                            : 2;
      uint32_t prefetchw                                             : 1;
#define CPUID_ECX_PREFETCHW                                          0x100
      uint32_t reserved_3                                            : 23;
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved_1                                            : 11;
      uint32_t syscall_sysret_available_in_64_bit_mode               : 1;
#define CPUID_EDX_SYSCALL_SYSRET_AVAILABLE_IN_64_BIT_MODE            0x800
      uint32_t reserved_2                                            : 8;
      uint32_t execute_disable_bit_available                         : 1;
#define CPUID_EDX_EXECUTE_DISABLE_BIT_AVAILABLE                      0x100000
      uint32_t reserved_3                                            : 5;
      uint32_t pages_1gb_available                                   : 1;
#define CPUID_EDX_PAGES_1GB_AVAILABLE                                0x4000000
      uint32_t rdtscp_available                                      : 1;
#define CPUID_EDX_RDTSCP_AVAILABLE                                   0x8000000
      uint32_t reserved_4                                            : 1;
      uint32_t ia64_available                                        : 1;
#define CPUID_EDX_IA64_AVAILABLE                                     0x20000000
      uint32_t reserved_5                                            : 2;
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_80000001;

#define CPUID_BRAND_STRING1                                          0x80000002
#define CPUID_BRAND_STRING2                                          0x80000003
#define CPUID_BRAND_STRING3                                          0x80000004
typedef struct {
  union {
    struct {
      uint32_t processor_brand_string_1                              : 32;
#define CPUID_EAX_PROCESSOR_BRAND_STRING_1                           0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t processor_brand_string_2                              : 32;
#define CPUID_EBX_PROCESSOR_BRAND_STRING_2                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t processor_brand_string_3                              : 32;
#define CPUID_ECX_PROCESSOR_BRAND_STRING_3                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t processor_brand_string_4                              : 32;
#define CPUID_EDX_PROCESSOR_BRAND_STRING_4                           0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_80000002;

typedef struct {
  union {
    struct {
      uint32_t processor_brand_string_5                              : 32;
#define CPUID_EAX_PROCESSOR_BRAND_STRING_5                           0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t processor_brand_string_6                              : 32;
#define CPUID_EBX_PROCESSOR_BRAND_STRING_6                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t processor_brand_string_7                              : 32;
#define CPUID_ECX_PROCESSOR_BRAND_STRING_7                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t processor_brand_string_8                              : 32;
#define CPUID_EDX_PROCESSOR_BRAND_STRING_8                           0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_80000003;

typedef struct {
  union {
    struct {
      uint32_t processor_brand_string_9                              : 32;
#define CPUID_EAX_PROCESSOR_BRAND_STRING_9                           0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t processor_brand_string_10                             : 32;
#define CPUID_EBX_PROCESSOR_BRAND_STRING_10                          0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t processor_brand_string_11                             : 32;
#define CPUID_ECX_PROCESSOR_BRAND_STRING_11                          0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t processor_brand_string_12                             : 32;
#define CPUID_EDX_PROCESSOR_BRAND_STRING_12                          0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_80000004;

typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EAX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EBX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_ECX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_80000005;

#define CPUID_EXTENDED_CACHE_INFO                                    0x80000006
typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EAX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EBX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t cache_line_size_in_bytes                              : 8;
#define CPUID_ECX_CACHE_LINE_SIZE_IN_BYTES                           0xFF
      uint32_t reserved_1                                            : 4;
      uint32_t l2_associativity_field                                : 4;
#define CPUID_ECX_L2_ASSOCIATIVITY_FIELD                             0xF000
      uint32_t cache_size_in_1k_units                                : 16;
#define CPUID_ECX_CACHE_SIZE_IN_1K_UNITS                             0xFFFF0000
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EDX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } edx;

} cpuid_eax_80000006;

#define CPUID_EXTENDED_TIME_STAMP_COUNTER                            0x80000007
typedef struct {
  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EAX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } eax;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_EBX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ebx;

  union {
    struct {
      uint32_t reserved                                              : 32;
#define CPUID_ECX_RESERVED                                           0xFFFFFFFF
    };

    uint32_t Flags;
  } ecx;

  union {
    struct {
      uint32_t reserved_1                                            : 8;
      uint32_t invariant_tsc_available                               : 1;
#define CPUID_EDX_INVARIANT_TSC_AVAILABLE                            0x100
      uint32_t reserved_2                                            : 23;
    };

    uint32_t Flags;
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
#define IA32_PLATFORM_ID_PLATFORM_ID                                 0x1C000000000000
    uint64_t reserved_2                                              : 11;
  };

  uint64_t Flags;
} ia32_platform_id_register;

#define IA32_APIC_BASE                                               0x0000001B
typedef union {
  struct {
    uint64_t reserved_1                                              : 8;
    uint64_t bsp_flag                                                : 1;
#define IA32_APIC_BASE_BSP_FLAG                                      0x100
    uint64_t reserved_2                                              : 1;
    uint64_t enable_x2apic_mode                                      : 1;
#define IA32_APIC_BASE_ENABLE_X2APIC_MODE                            0x400
    uint64_t apic_global_enable                                      : 1;
#define IA32_APIC_BASE_APIC_GLOBAL_ENABLE                            0x800
    uint64_t apic_base                                               : 36;
#define IA32_APIC_BASE_APIC_BASE                                     0xFFFFFFFFF000
    uint64_t reserved_3                                              : 16;
  };

  uint64_t Flags;
} ia32_apic_base_register;

#define IA32_FEATURE_CONTROL                                         0x0000003A
typedef union {
  struct {
    uint64_t lock_bit                                                : 1;
#define IA32_FEATURE_CONTROL_LOCK_BIT                                0x01
    uint64_t enable_vmx_inside_smx                                   : 1;
#define IA32_FEATURE_CONTROL_ENABLE_VMX_INSIDE_SMX                   0x02
    uint64_t enable_vmx_outside_smx                                  : 1;
#define IA32_FEATURE_CONTROL_ENABLE_VMX_OUTSIDE_SMX                  0x04
    uint64_t reserved_1                                              : 5;
    uint64_t senter_local_function_enables                           : 7;
#define IA32_FEATURE_CONTROL_SENTER_LOCAL_FUNCTION_ENABLES           0x7F00
    uint64_t senter_global_enable                                    : 1;
#define IA32_FEATURE_CONTROL_SENTER_GLOBAL_ENABLE                    0x8000
    uint64_t reserved_2                                              : 1;
    uint64_t sgx_launch_control_enable                               : 1;
#define IA32_FEATURE_CONTROL_SGX_LAUNCH_CONTROL_ENABLE               0x20000
    uint64_t sgx_global_enable                                       : 1;
#define IA32_FEATURE_CONTROL_SGX_GLOBAL_ENABLE                       0x40000
    uint64_t reserved_3                                              : 1;
    uint64_t lmce_on                                                 : 1;
#define IA32_FEATURE_CONTROL_LMCE_ON                                 0x100000
    uint64_t reserved_4                                              : 43;
  };

  uint64_t Flags;
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
#define IA32_BIOS_SIGN_ID_RESERVED                                   0xFFFFFFFF
    uint64_t microcode_update_signature                              : 32;
#define IA32_BIOS_SIGN_ID_MICROCODE_UPDATE_SIGNATURE                 0xFFFFFFFF00000000
  };

  uint64_t Flags;
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
#define IA32_SMM_MONITOR_CTL_VALID                                   0x01
    uint64_t reserved_1                                              : 1;
    uint64_t smi_unblocking_by_vmxoff                                : 1;
#define IA32_SMM_MONITOR_CTL_SMI_UNBLOCKING_BY_VMXOFF                0x04
    uint64_t reserved_2                                              : 9;
    uint64_t mseg_base                                               : 20;
#define IA32_SMM_MONITOR_CTL_MSEG_BASE                               0xFFFFF000
    uint64_t reserved_3                                              : 32;
  };

  uint64_t Flags;
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
#define IA32_MTRRCAP_VARIABLE_RANGE_REGISTERS_COUNT                  0xFF
    uint64_t fixed_range_registers_supported                         : 1;
#define IA32_MTRRCAP_FIXED_RANGE_REGISTERS_SUPPORTED                 0x100
    uint64_t reserved_1                                              : 1;
    uint64_t write_combining                                         : 1;
#define IA32_MTRRCAP_WRITE_COMBINING                                 0x400
    uint64_t system_management_range_register                        : 1;
#define IA32_MTRRCAP_SYSTEM_MANAGEMENT_RANGE_REGISTER                0x800
    uint64_t reserved_2                                              : 52;
  };

  uint64_t Flags;
} ia32_mtrrcap_register;

#define IA32_SYSENTER_CS                                             0x00000174
typedef union {
  struct {
    uint64_t cs_selector                                             : 16;
#define IA32_SYSENTER_CS_CS_SELECTOR                                 0xFFFF
    uint64_t not_used_1                                              : 16;
#define IA32_SYSENTER_CS_NOT_USED_1                                  0xFFFF0000
    uint64_t not_used_2                                              : 32;
#define IA32_SYSENTER_CS_NOT_USED_2                                  0xFFFFFFFF00000000
  };

  uint64_t Flags;
} ia32_sysenter_cs_register;

#define IA32_SYSENTER_ESP                                            0x00000175
#define IA32_SYSENTER_EIP                                            0x00000176
#define IA32_MCG_CAP                                                 0x00000179
typedef union {
  struct {
    uint64_t count                                                   : 8;
#define IA32_MCG_CAP_COUNT                                           0xFF
    uint64_t mcg_ctl_p                                               : 1;
#define IA32_MCG_CAP_MCG_CTL_P                                       0x100
    uint64_t mcg_ext_p                                               : 1;
#define IA32_MCG_CAP_MCG_EXT_P                                       0x200
    uint64_t mcp_cmci_p                                              : 1;
#define IA32_MCG_CAP_MCP_CMCI_P                                      0x400
    uint64_t mcg_tes_p                                               : 1;
#define IA32_MCG_CAP_MCG_TES_P                                       0x800
    uint64_t reserved_1                                              : 4;
    uint64_t mcg_ext_cnt                                             : 8;
#define IA32_MCG_CAP_MCG_EXT_CNT                                     0xFF0000
    uint64_t mcg_ser_p                                               : 1;
#define IA32_MCG_CAP_MCG_SER_P                                       0x1000000
    uint64_t reserved_2                                              : 1;
    uint64_t mcg_elog_p                                              : 1;
#define IA32_MCG_CAP_MCG_ELOG_P                                      0x4000000
    uint64_t mcg_lmce_p                                              : 1;
#define IA32_MCG_CAP_MCG_LMCE_P                                      0x8000000
    uint64_t reserved_3                                              : 36;
  };

  uint64_t Flags;
} ia32_mcg_cap_register;

#define IA32_MCG_STATUS                                              0x0000017A
typedef union {
  struct {
    uint64_t ripv                                                    : 1;
#define IA32_MCG_STATUS_RIPV                                         0x01
    uint64_t eipv                                                    : 1;
#define IA32_MCG_STATUS_EIPV                                         0x02
    uint64_t mcip                                                    : 1;
#define IA32_MCG_STATUS_MCIP                                         0x04
    uint64_t lmce_s                                                  : 1;
#define IA32_MCG_STATUS_LMCE_S                                       0x08
    uint64_t reserved_1                                              : 60;
  };

  uint64_t Flags;
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
#define IA32_PERFEVTSEL_EVENT_SELECT                                 0xFF
    uint64_t u_mask                                                  : 8;
#define IA32_PERFEVTSEL_U_MASK                                       0xFF00
    uint64_t usr                                                     : 1;
#define IA32_PERFEVTSEL_USR                                          0x10000
    uint64_t os                                                      : 1;
#define IA32_PERFEVTSEL_OS                                           0x20000
    uint64_t edge                                                    : 1;
#define IA32_PERFEVTSEL_EDGE                                         0x40000
    uint64_t pc                                                      : 1;
#define IA32_PERFEVTSEL_PC                                           0x80000
    uint64_t intr                                                    : 1;
#define IA32_PERFEVTSEL_INTR                                         0x100000
    uint64_t any_thread                                              : 1;
#define IA32_PERFEVTSEL_ANY_THREAD                                   0x200000
    uint64_t en                                                      : 1;
#define IA32_PERFEVTSEL_EN                                           0x400000
    uint64_t inv                                                     : 1;
#define IA32_PERFEVTSEL_INV                                          0x800000
    uint64_t cmask                                                   : 8;
#define IA32_PERFEVTSEL_CMASK                                        0xFF000000
    uint64_t reserved_1                                              : 32;
  };

  uint64_t Flags;
} ia32_perfevtsel_register;

/**
 * @}
 */

#define IA32_PERF_STATUS                                             0x00000198
typedef union {
  struct {
    uint64_t current_performance_state_value                         : 16;
#define IA32_PERF_STATUS_CURRENT_PERFORMANCE_STATE_VALUE             0xFFFF
    uint64_t reserved_1                                              : 48;
  };

  uint64_t Flags;
} ia32_perf_status_register;

#define IA32_PERF_CTL                                                0x00000199
typedef union {
  struct {
    uint64_t target_performance_state_value                          : 16;
#define IA32_PERF_CTL_TARGET_PERFORMANCE_STATE_VALUE                 0xFFFF
    uint64_t reserved_1                                              : 16;
    uint64_t ida_engage                                              : 1;
#define IA32_PERF_CTL_IDA_ENGAGE                                     0x100000000
    uint64_t reserved_2                                              : 31;
  };

  uint64_t Flags;
} ia32_perf_ctl_register;

#define IA32_CLOCK_MODULATION                                        0x0000019A
typedef union {
  struct {
    uint64_t extended_on_demand_clock_modulation_duty_cycle          : 1;
#define IA32_CLOCK_MODULATION_EXTENDED_ON_DEMAND_CLOCK_MODULATION_DUTY_CYCLE 0x01
    uint64_t on_demand_clock_modulation_duty_cycle                   : 3;
#define IA32_CLOCK_MODULATION_ON_DEMAND_CLOCK_MODULATION_DUTY_CYCLE  0x0E
    uint64_t on_demand_clock_modulation_enable                       : 1;
#define IA32_CLOCK_MODULATION_ON_DEMAND_CLOCK_MODULATION_ENABLE      0x10
    uint64_t reserved_1                                              : 59;
  };

  uint64_t Flags;
} ia32_clock_modulation_register;

#define IA32_THERM_INTERRUPT                                         0x0000019B
typedef union {
  struct {
    uint64_t high_temperature_interrupt_enable                       : 1;
#define IA32_THERM_INTERRUPT_HIGH_TEMPERATURE_INTERRUPT_ENABLE       0x01
    uint64_t low_temperature_interrupt_enable                        : 1;
#define IA32_THERM_INTERRUPT_LOW_TEMPERATURE_INTERRUPT_ENABLE        0x02
    uint64_t prochot_interrupt_enable                                : 1;
#define IA32_THERM_INTERRUPT_PROCHOT_INTERRUPT_ENABLE                0x04
    uint64_t forcepr_interrupt_enable                                : 1;
#define IA32_THERM_INTERRUPT_FORCEPR_INTERRUPT_ENABLE                0x08
    uint64_t critical_temperature_interrupt_enable                   : 1;
#define IA32_THERM_INTERRUPT_CRITICAL_TEMPERATURE_INTERRUPT_ENABLE   0x10
    uint64_t reserved_1                                              : 3;
    uint64_t threshold1_value                                        : 7;
#define IA32_THERM_INTERRUPT_THRESHOLD1_VALUE                        0x7F00
    uint64_t threshold1_interrupt_enable                             : 1;
#define IA32_THERM_INTERRUPT_THRESHOLD1_INTERRUPT_ENABLE             0x8000
    uint64_t threshold2_value                                        : 7;
#define IA32_THERM_INTERRUPT_THRESHOLD2_VALUE                        0x7F0000
    uint64_t threshold2_interrupt_enable                             : 1;
#define IA32_THERM_INTERRUPT_THRESHOLD2_INTERRUPT_ENABLE             0x800000
    uint64_t power_limit_notification_enable                         : 1;
#define IA32_THERM_INTERRUPT_POWER_LIMIT_NOTIFICATION_ENABLE         0x1000000
    uint64_t reserved_2                                              : 39;
  };

  uint64_t Flags;
} ia32_therm_interrupt_register;

#define IA32_THERM_STATUS                                            0x0000019C
typedef union {
  struct {
    uint64_t thermal_status                                          : 1;
#define IA32_THERM_STATUS_THERMAL_STATUS                             0x01
    uint64_t thermal_status_log                                      : 1;
#define IA32_THERM_STATUS_THERMAL_STATUS_LOG                         0x02
    uint64_t prochot_forcepr_event                                   : 1;
#define IA32_THERM_STATUS_PROCHOT_FORCEPR_EVENT                      0x04
    uint64_t prochot_forcepr_log                                     : 1;
#define IA32_THERM_STATUS_PROCHOT_FORCEPR_LOG                        0x08
    uint64_t critical_temperature_status                             : 1;
#define IA32_THERM_STATUS_CRITICAL_TEMPERATURE_STATUS                0x10
    uint64_t critical_temperature_status_log                         : 1;
#define IA32_THERM_STATUS_CRITICAL_TEMPERATURE_STATUS_LOG            0x20
    uint64_t thermal_threshold1_status                               : 1;
#define IA32_THERM_STATUS_THERMAL_THRESHOLD1_STATUS                  0x40
    uint64_t thermal_threshold1_log                                  : 1;
#define IA32_THERM_STATUS_THERMAL_THRESHOLD1_LOG                     0x80
    uint64_t thermal_threshold2_status                               : 1;
#define IA32_THERM_STATUS_THERMAL_THRESHOLD2_STATUS                  0x100
    uint64_t thermal_threshold2_log                                  : 1;
#define IA32_THERM_STATUS_THERMAL_THRESHOLD2_LOG                     0x200
    uint64_t power_limitation_status                                 : 1;
#define IA32_THERM_STATUS_POWER_LIMITATION_STATUS                    0x400
    uint64_t power_limitation_log                                    : 1;
#define IA32_THERM_STATUS_POWER_LIMITATION_LOG                       0x800
    uint64_t current_limit_status                                    : 1;
#define IA32_THERM_STATUS_CURRENT_LIMIT_STATUS                       0x1000
    uint64_t current_limit_log                                       : 1;
#define IA32_THERM_STATUS_CURRENT_LIMIT_LOG                          0x2000
    uint64_t cross_domain_limit_status                               : 1;
#define IA32_THERM_STATUS_CROSS_DOMAIN_LIMIT_STATUS                  0x4000
    uint64_t cross_domain_limit_log                                  : 1;
#define IA32_THERM_STATUS_CROSS_DOMAIN_LIMIT_LOG                     0x8000
    uint64_t digital_readout                                         : 7;
#define IA32_THERM_STATUS_DIGITAL_READOUT                            0x7F0000
    uint64_t reserved_1                                              : 4;
    uint64_t resolution_in_degrees_celsius                           : 4;
#define IA32_THERM_STATUS_RESOLUTION_IN_DEGREES_CELSIUS              0x78000000
    uint64_t reading_valid                                           : 1;
#define IA32_THERM_STATUS_READING_VALID                              0x80000000
    uint64_t reserved_2                                              : 32;
  };

  uint64_t Flags;
} ia32_therm_status_register;

#define IA32_MISC_ENABLE                                             0x000001A0
typedef union {
  struct {
    uint64_t fast_strings_enable                                     : 1;
#define IA32_MISC_ENABLE_FAST_STRINGS_ENABLE                         0x01
    uint64_t reserved_1                                              : 2;
    uint64_t automatic_thermal_control_circuit_enable                : 1;
#define IA32_MISC_ENABLE_AUTOMATIC_THERMAL_CONTROL_CIRCUIT_ENABLE    0x08
    uint64_t reserved_2                                              : 3;
    uint64_t performance_monitoring_available                        : 1;
#define IA32_MISC_ENABLE_PERFORMANCE_MONITORING_AVAILABLE            0x80
    uint64_t reserved_3                                              : 3;
    uint64_t branch_trace_storage_unavailable                        : 1;
#define IA32_MISC_ENABLE_BRANCH_TRACE_STORAGE_UNAVAILABLE            0x800
    uint64_t processor_event_based_sampling_unavailable              : 1;
#define IA32_MISC_ENABLE_PROCESSOR_EVENT_BASED_SAMPLING_UNAVAILABLE  0x1000
    uint64_t reserved_4                                              : 3;
    uint64_t enhanced_intel_speedstep_technology_enable              : 1;
#define IA32_MISC_ENABLE_ENHANCED_INTEL_SPEEDSTEP_TECHNOLOGY_ENABLE  0x10000
    uint64_t reserved_5                                              : 1;
    uint64_t enable_monitor_fsm                                      : 1;
#define IA32_MISC_ENABLE_ENABLE_MONITOR_FSM                          0x40000
    uint64_t reserved_6                                              : 3;
    uint64_t limit_cpuid_maxval                                      : 1;
#define IA32_MISC_ENABLE_LIMIT_CPUID_MAXVAL                          0x400000
    uint64_t xtpr_message_disable                                    : 1;
#define IA32_MISC_ENABLE_XTPR_MESSAGE_DISABLE                        0x800000
    uint64_t reserved_7                                              : 10;
    uint64_t xd_bit_disable                                          : 1;
#define IA32_MISC_ENABLE_XD_BIT_DISABLE                              0x400000000
    uint64_t reserved_8                                              : 29;
  };

  uint64_t Flags;
} ia32_misc_enable_register;

#define IA32_ENERGY_PERF_BIAS                                        0x000001B0
typedef union {
  struct {
    uint64_t power_policy_preference                                 : 4;
#define IA32_ENERGY_PERF_BIAS_POWER_POLICY_PREFERENCE                0x0F
    uint64_t reserved_1                                              : 60;
  };

  uint64_t Flags;
} ia32_energy_perf_bias_register;

#define IA32_PACKAGE_THERM_STATUS                                    0x000001B1
typedef union {
  struct {
    uint64_t thermal_status                                          : 1;
#define IA32_PACKAGE_THERM_STATUS_THERMAL_STATUS                     0x01
    uint64_t thermal_status_log                                      : 1;
#define IA32_PACKAGE_THERM_STATUS_THERMAL_STATUS_LOG                 0x02
    uint64_t prochot_event                                           : 1;
#define IA32_PACKAGE_THERM_STATUS_PROCHOT_EVENT                      0x04
    uint64_t prochot_log                                             : 1;
#define IA32_PACKAGE_THERM_STATUS_PROCHOT_LOG                        0x08
    uint64_t critical_temperature_status                             : 1;
#define IA32_PACKAGE_THERM_STATUS_CRITICAL_TEMPERATURE_STATUS        0x10
    uint64_t critical_temperature_status_log                         : 1;
#define IA32_PACKAGE_THERM_STATUS_CRITICAL_TEMPERATURE_STATUS_LOG    0x20
    uint64_t thermal_threshold1_status                               : 1;
#define IA32_PACKAGE_THERM_STATUS_THERMAL_THRESHOLD1_STATUS          0x40
    uint64_t thermal_threshold1_log                                  : 1;
#define IA32_PACKAGE_THERM_STATUS_THERMAL_THRESHOLD1_LOG             0x80
    uint64_t thermal_threshold2_status                               : 1;
#define IA32_PACKAGE_THERM_STATUS_THERMAL_THRESHOLD2_STATUS          0x100
    uint64_t thermal_threshold2_log                                  : 1;
#define IA32_PACKAGE_THERM_STATUS_THERMAL_THRESHOLD2_LOG             0x200
    uint64_t power_limitation_status                                 : 1;
#define IA32_PACKAGE_THERM_STATUS_POWER_LIMITATION_STATUS            0x400
    uint64_t power_limitation_log                                    : 1;
#define IA32_PACKAGE_THERM_STATUS_POWER_LIMITATION_LOG               0x800
    uint64_t reserved_1                                              : 4;
    uint64_t digital_readout                                         : 7;
#define IA32_PACKAGE_THERM_STATUS_DIGITAL_READOUT                    0x7F0000
    uint64_t reserved_2                                              : 41;
  };

  uint64_t Flags;
} ia32_package_therm_status_register;

#define IA32_PACKAGE_THERM_INTERRUPT                                 0x000001B2
typedef union {
  struct {
    uint64_t high_temperature_interrupt_enable                       : 1;
#define IA32_PACKAGE_THERM_INTERRUPT_HIGH_TEMPERATURE_INTERRUPT_ENABLE 0x01
    uint64_t low_temperature_interrupt_enable                        : 1;
#define IA32_PACKAGE_THERM_INTERRUPT_LOW_TEMPERATURE_INTERRUPT_ENABLE 0x02
    uint64_t prochot_interrupt_enable                                : 1;
#define IA32_PACKAGE_THERM_INTERRUPT_PROCHOT_INTERRUPT_ENABLE        0x04
    uint64_t reserved_1                                              : 1;
    uint64_t overheat_interrupt_enable                               : 1;
#define IA32_PACKAGE_THERM_INTERRUPT_OVERHEAT_INTERRUPT_ENABLE       0x10
    uint64_t reserved_2                                              : 3;
    uint64_t threshold1_value                                        : 7;
#define IA32_PACKAGE_THERM_INTERRUPT_THRESHOLD1_VALUE                0x7F00
    uint64_t threshold1_interrupt_enable                             : 1;
#define IA32_PACKAGE_THERM_INTERRUPT_THRESHOLD1_INTERRUPT_ENABLE     0x8000
    uint64_t threshold2_value                                        : 7;
#define IA32_PACKAGE_THERM_INTERRUPT_THRESHOLD2_VALUE                0x7F0000
    uint64_t threshold2_interrupt_enable                             : 1;
#define IA32_PACKAGE_THERM_INTERRUPT_THRESHOLD2_INTERRUPT_ENABLE     0x800000
    uint64_t power_limit_notification_enable                         : 1;
#define IA32_PACKAGE_THERM_INTERRUPT_POWER_LIMIT_NOTIFICATION_ENABLE 0x1000000
    uint64_t reserved_3                                              : 39;
  };

  uint64_t Flags;
} ia32_package_therm_interrupt_register;

#define IA32_DEBUGCTL                                                0x000001D9
typedef union {
  struct {
    uint64_t lbr                                                     : 1;
#define IA32_DEBUGCTL_LBR                                            0x01
    uint64_t btf                                                     : 1;
#define IA32_DEBUGCTL_BTF                                            0x02
    uint64_t reserved_1                                              : 4;
    uint64_t tr                                                      : 1;
#define IA32_DEBUGCTL_TR                                             0x40
    uint64_t bts                                                     : 1;
#define IA32_DEBUGCTL_BTS                                            0x80
    uint64_t btint                                                   : 1;
#define IA32_DEBUGCTL_BTINT                                          0x100
    uint64_t bts_off_os                                              : 1;
#define IA32_DEBUGCTL_BTS_OFF_OS                                     0x200
    uint64_t bts_off_usr                                             : 1;
#define IA32_DEBUGCTL_BTS_OFF_USR                                    0x400
    uint64_t freeze_lbrs_on_pmi                                      : 1;
#define IA32_DEBUGCTL_FREEZE_LBRS_ON_PMI                             0x800
    uint64_t freeze_perfmon_on_pmi                                   : 1;
#define IA32_DEBUGCTL_FREEZE_PERFMON_ON_PMI                          0x1000
    uint64_t enable_uncore_pmi                                       : 1;
#define IA32_DEBUGCTL_ENABLE_UNCORE_PMI                              0x2000
    uint64_t freeze_while_smm                                        : 1;
#define IA32_DEBUGCTL_FREEZE_WHILE_SMM                               0x4000
    uint64_t rtm_debug                                               : 1;
#define IA32_DEBUGCTL_RTM_DEBUG                                      0x8000
    uint64_t reserved_2                                              : 48;
  };

  uint64_t Flags;
} ia32_debugctl_register;

#define IA32_SMRR_PHYSBASE                                           0x000001F2
typedef union {
  struct {
    uint64_t type                                                    : 8;
#define IA32_SMRR_PHYSBASE_TYPE                                      0xFF
    uint64_t reserved_1                                              : 4;
    uint64_t smrr_physical_base_address                              : 20;
#define IA32_SMRR_PHYSBASE_SMRR_PHYSICAL_BASE_ADDRESS                0xFFFFF000
    uint64_t reserved_2                                              : 32;
  };

  uint64_t Flags;
} ia32_smrr_physbase_register;

#define IA32_SMRR_PHYSMASK                                           0x000001F3
typedef union {
  struct {
    uint64_t reserved_1                                              : 11;
    uint64_t enable_range_mask                                       : 1;
#define IA32_SMRR_PHYSMASK_ENABLE_RANGE_MASK                         0x800
    uint64_t smrr_address_range_mask                                 : 20;
#define IA32_SMRR_PHYSMASK_SMRR_ADDRESS_RANGE_MASK                   0xFFFFF000
    uint64_t reserved_2                                              : 32;
  };

  uint64_t Flags;
} ia32_smrr_physmask_register;

#define IA32_PLATFORM_DCA_CAP                                        0x000001F8
#define IA32_CPU_DCA_CAP                                             0x000001F9
#define IA32_DCA_0_CAP                                               0x000001FA
typedef union {
  struct {
    uint64_t dca_active                                              : 1;
#define IA32_DCA_0_CAP_DCA_ACTIVE                                    0x01
    uint64_t transaction                                             : 2;
#define IA32_DCA_0_CAP_TRANSACTION                                   0x06
    uint64_t dca_type                                                : 4;
#define IA32_DCA_0_CAP_DCA_TYPE                                      0x78
    uint64_t dca_queue_size                                          : 4;
#define IA32_DCA_0_CAP_DCA_QUEUE_SIZE                                0x780
    uint64_t reserved_1                                              : 2;
    uint64_t dca_delay                                               : 4;
#define IA32_DCA_0_CAP_DCA_DELAY                                     0x1E000
    uint64_t reserved_2                                              : 7;
    uint64_t sw_block                                                : 1;
#define IA32_DCA_0_CAP_SW_BLOCK                                      0x1000000
    uint64_t reserved_3                                              : 1;
    uint64_t hw_block                                                : 1;
#define IA32_DCA_0_CAP_HW_BLOCK                                      0x4000000
    uint64_t reserved_4                                              : 37;
  };

  uint64_t Flags;
} ia32_dca_0_cap_register;

/**
 * @defgroup ia32_mtrr_physbase \
 *           IA32_MTRR_PHYSBASE(n)
 * @{
 */
typedef union {
  struct {
    uint64_t type                                                    : 8;
#define IA32_MTRR_PHYSBASE_TYPE                                      0xFF
    uint64_t reserved_1                                              : 4;
    uint64_t physical_addres_base                                    : 36;
#define IA32_MTRR_PHYSBASE_PHYSICAL_ADDRES_BASE                      0xFFFFFFFFF000
    uint64_t reserved_2                                              : 16;
  };

  uint64_t Flags;
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
#define IA32_MTRR_PHYSMASK_TYPE                                      0xFF
    uint64_t reserved_1                                              : 3;
    uint64_t valid                                                   : 1;
#define IA32_MTRR_PHYSMASK_VALID                                     0x800
    uint64_t physical_addres_mask                                    : 36;
#define IA32_MTRR_PHYSMASK_PHYSICAL_ADDRES_MASK                      0xFFFFFFFFF000
    uint64_t reserved_2                                              : 16;
  };

  uint64_t Flags;
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
#define IA32_PAT_PA0                                                 0x07
    uint64_t reserved_1                                              : 5;
    uint64_t pa1                                                     : 3;
#define IA32_PAT_PA1                                                 0x700
    uint64_t reserved_2                                              : 5;
    uint64_t pa2                                                     : 3;
#define IA32_PAT_PA2                                                 0x70000
    uint64_t reserved_3                                              : 5;
    uint64_t pa3                                                     : 3;
#define IA32_PAT_PA3                                                 0x7000000
    uint64_t reserved_4                                              : 5;
    uint64_t pa4                                                     : 3;
#define IA32_PAT_PA4                                                 0x700000000
    uint64_t reserved_5                                              : 5;
    uint64_t pa5                                                     : 3;
#define IA32_PAT_PA5                                                 0x70000000000
    uint64_t reserved_6                                              : 5;
    uint64_t pa6                                                     : 3;
#define IA32_PAT_PA6                                                 0x7000000000000
    uint64_t reserved_7                                              : 5;
    uint64_t pa7                                                     : 3;
#define IA32_PAT_PA7                                                 0x700000000000000
    uint64_t reserved_8                                              : 5;
  };

  uint64_t Flags;
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
#define IA32_MC_CTL2_CORRECTED_ERROR_COUNT_THRESHOLD                 0x7FFF
    uint64_t reserved_1                                              : 15;
    uint64_t cmci_en                                                 : 1;
#define IA32_MC_CTL2_CMCI_EN                                         0x40000000
    uint64_t reserved_2                                              : 33;
  };

  uint64_t Flags;
} ia32_mc_ctl2_register;

/**
 * @}
 */

#define IA32_MTRR_DEF_TYPE                                           0x000002FF
typedef union {
  struct {
    uint64_t default_memory_type                                     : 3;
#define IA32_MTRR_DEF_TYPE_DEFAULT_MEMORY_TYPE                       0x07
    uint64_t reserved_1                                              : 7;
    uint64_t fixed_range_mtrr_enable                                 : 1;
#define IA32_MTRR_DEF_TYPE_FIXED_RANGE_MTRR_ENABLE                   0x400
    uint64_t mtrr_enable                                             : 1;
#define IA32_MTRR_DEF_TYPE_MTRR_ENABLE                               0x800
    uint64_t reserved_2                                              : 52;
  };

  uint64_t Flags;
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
#define IA32_PERF_CAPABILITIES_LBR_FORMAT                            0x3F
    uint64_t pebs_trap                                               : 1;
#define IA32_PERF_CAPABILITIES_PEBS_TRAP                             0x40
    uint64_t pebs_save_arch_regs                                     : 1;
#define IA32_PERF_CAPABILITIES_PEBS_SAVE_ARCH_REGS                   0x80
    uint64_t pebs_record_format                                      : 4;
#define IA32_PERF_CAPABILITIES_PEBS_RECORD_FORMAT                    0xF00
    uint64_t freeze_while_smm_is_supported                           : 1;
#define IA32_PERF_CAPABILITIES_FREEZE_WHILE_SMM_IS_SUPPORTED         0x1000
    uint64_t full_width_counter_write                                : 1;
#define IA32_PERF_CAPABILITIES_FULL_WIDTH_COUNTER_WRITE              0x2000
    uint64_t reserved_1                                              : 50;
  };

  uint64_t Flags;
} ia32_perf_capabilities_register;

#define IA32_FIXED_CTR_CTRL                                          0x0000038D
typedef union {
  struct {
    uint64_t en0_os                                                  : 1;
#define IA32_FIXED_CTR_CTRL_EN0_OS                                   0x01
    uint64_t en0_usr                                                 : 1;
#define IA32_FIXED_CTR_CTRL_EN0_USR                                  0x02
    uint64_t any_thread0                                             : 1;
#define IA32_FIXED_CTR_CTRL_ANY_THREAD0                              0x04
    uint64_t en0_pmi                                                 : 1;
#define IA32_FIXED_CTR_CTRL_EN0_PMI                                  0x08
    uint64_t en1_os                                                  : 1;
#define IA32_FIXED_CTR_CTRL_EN1_OS                                   0x10
    uint64_t en1_usr                                                 : 1;
#define IA32_FIXED_CTR_CTRL_EN1_USR                                  0x20
    uint64_t any_thread1                                             : 1;
#define IA32_FIXED_CTR_CTRL_ANY_THREAD1                              0x40
    uint64_t en1_pmi                                                 : 1;
#define IA32_FIXED_CTR_CTRL_EN1_PMI                                  0x80
    uint64_t en2_os                                                  : 1;
#define IA32_FIXED_CTR_CTRL_EN2_OS                                   0x100
    uint64_t en2_usr                                                 : 1;
#define IA32_FIXED_CTR_CTRL_EN2_USR                                  0x200
    uint64_t any_thread2                                             : 1;
#define IA32_FIXED_CTR_CTRL_ANY_THREAD2                              0x400
    uint64_t en2_pmi                                                 : 1;
#define IA32_FIXED_CTR_CTRL_EN2_PMI                                  0x800
    uint64_t reserved_1                                              : 52;
  };

  uint64_t Flags;
} ia32_fixed_ctr_ctrl_register;

#define IA32_PERF_GLOBAL_STATUS                                      0x0000038E
typedef union {
  struct {
    uint64_t ovf_pmc0                                                : 1;
#define IA32_PERF_GLOBAL_STATUS_OVF_PMC0                             0x01
    uint64_t ovf_pmc1                                                : 1;
#define IA32_PERF_GLOBAL_STATUS_OVF_PMC1                             0x02
    uint64_t ovf_pmc2                                                : 1;
#define IA32_PERF_GLOBAL_STATUS_OVF_PMC2                             0x04
    uint64_t ovf_pmc3                                                : 1;
#define IA32_PERF_GLOBAL_STATUS_OVF_PMC3                             0x08
    uint64_t reserved_1                                              : 28;
    uint64_t ovf_fixedctr0                                           : 1;
#define IA32_PERF_GLOBAL_STATUS_OVF_FIXEDCTR0                        0x100000000
    uint64_t ovf_fixedctr1                                           : 1;
#define IA32_PERF_GLOBAL_STATUS_OVF_FIXEDCTR1                        0x200000000
    uint64_t ovf_fixedctr2                                           : 1;
#define IA32_PERF_GLOBAL_STATUS_OVF_FIXEDCTR2                        0x400000000
    uint64_t reserved_2                                              : 20;
    uint64_t trace_topa_pmi                                          : 1;
#define IA32_PERF_GLOBAL_STATUS_TRACE_TOPA_PMI                       0x80000000000000
    uint64_t reserved_3                                              : 2;
    uint64_t lbr_frz                                                 : 1;
#define IA32_PERF_GLOBAL_STATUS_LBR_FRZ                              0x400000000000000
    uint64_t ctr_frz                                                 : 1;
#define IA32_PERF_GLOBAL_STATUS_CTR_FRZ                              0x800000000000000
    uint64_t asci                                                    : 1;
#define IA32_PERF_GLOBAL_STATUS_ASCI                                 0x1000000000000000
    uint64_t ovf_uncore                                              : 1;
#define IA32_PERF_GLOBAL_STATUS_OVF_UNCORE                           0x2000000000000000
    uint64_t ovf_buf                                                 : 1;
#define IA32_PERF_GLOBAL_STATUS_OVF_BUF                              0x4000000000000000
    uint64_t cond_chgd                                               : 1;
#define IA32_PERF_GLOBAL_STATUS_COND_CHGD                            0x8000000000000000
  };

  uint64_t Flags;
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
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_OVF_PMCN                 0xFFFFFFFF
    uint64_t clear_ovf_fixed_ctrn                                    : 3;
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_OVF_FIXED_CTRN           0x700000000
    uint64_t reserved_1                                              : 20;
    uint64_t clear_trace_topa_pmi                                    : 1;
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_TRACE_TOPA_PMI           0x80000000000000
    uint64_t reserved_2                                              : 2;
    uint64_t clear_lbr_frz                                           : 1;
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_LBR_FRZ                  0x400000000000000
    uint64_t clear_ctr_frz                                           : 1;
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_CTR_FRZ                  0x800000000000000
    uint64_t clear_asci                                              : 1;
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_ASCI                     0x1000000000000000
    uint64_t clear_ovf_uncore                                        : 1;
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_OVF_UNCORE               0x2000000000000000
    uint64_t clear_ovf_buf                                           : 1;
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_OVF_BUF                  0x4000000000000000
    uint64_t clear_cond_chgd                                         : 1;
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_COND_CHGD                0x8000000000000000
  };

  uint64_t Flags;
} ia32_perf_global_status_reset_register;

#define IA32_PERF_GLOBAL_STATUS_SET                                  0x00000391
typedef union {
  struct {
    uint64_t ovf_pmcn                                                : 32;
#define IA32_PERF_GLOBAL_STATUS_SET_OVF_PMCN                         0xFFFFFFFF
    uint64_t ovf_fixed_ctrn                                          : 3;
#define IA32_PERF_GLOBAL_STATUS_SET_OVF_FIXED_CTRN                   0x700000000
    uint64_t reserved_1                                              : 20;
    uint64_t trace_topa_pmi                                          : 1;
#define IA32_PERF_GLOBAL_STATUS_SET_TRACE_TOPA_PMI                   0x80000000000000
    uint64_t reserved_2                                              : 2;
    uint64_t lbr_frz                                                 : 1;
#define IA32_PERF_GLOBAL_STATUS_SET_LBR_FRZ                          0x400000000000000
    uint64_t ctr_frz                                                 : 1;
#define IA32_PERF_GLOBAL_STATUS_SET_CTR_FRZ                          0x800000000000000
    uint64_t asci                                                    : 1;
#define IA32_PERF_GLOBAL_STATUS_SET_ASCI                             0x1000000000000000
    uint64_t ovf_uncore                                              : 1;
#define IA32_PERF_GLOBAL_STATUS_SET_OVF_UNCORE                       0x2000000000000000
    uint64_t ovf_buf                                                 : 1;
#define IA32_PERF_GLOBAL_STATUS_SET_OVF_BUF                          0x4000000000000000
    uint64_t reserved_3                                              : 1;
  };

  uint64_t Flags;
} ia32_perf_global_status_set_register;

#define IA32_PERF_GLOBAL_INUSE                                       0x00000392
typedef union {
  struct {
    uint64_t ia32_perfevtseln_in_use                                 : 32;
#define IA32_PERF_GLOBAL_INUSE_IA32_PERFEVTSELN_IN_USE               0xFFFFFFFF
    uint64_t ia32_fixed_ctrn_in_use                                  : 3;
#define IA32_PERF_GLOBAL_INUSE_IA32_FIXED_CTRN_IN_USE                0x700000000
    uint64_t reserved_1                                              : 28;
    uint64_t pmi_in_use                                              : 1;
#define IA32_PERF_GLOBAL_INUSE_PMI_IN_USE                            0x8000000000000000
  };

  uint64_t Flags;
} ia32_perf_global_inuse_register;

#define IA32_PEBS_ENABLE                                             0x000003F1
typedef union {
  struct {
    uint64_t enable_pebs                                             : 1;
#define IA32_PEBS_ENABLE_ENABLE_PEBS                                 0x01
    uint64_t reservedormodelspecific1                                : 3;
#define IA32_PEBS_ENABLE_RESERVEDORMODELSPECIFIC1                    0x0E
    uint64_t reserved_1                                              : 28;
    uint64_t reservedormodelspecific2                                : 4;
#define IA32_PEBS_ENABLE_RESERVEDORMODELSPECIFIC2                    0xF00000000
    uint64_t reserved_2                                              : 28;
  };

  uint64_t Flags;
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
#define IA32_VMX_BASIC_VMCS_REVISION_ID                              0x7FFFFFFF
    uint64_t must_be_zero                                            : 1;
#define IA32_VMX_BASIC_MUST_BE_ZERO                                  0x80000000
    uint64_t vmcs_size_in_bytes                                      : 13;
#define IA32_VMX_BASIC_VMCS_SIZE_IN_BYTES                            0x1FFF00000000
    uint64_t reserved_1                                              : 3;
    uint64_t vmcs_physical_address_width                             : 1;
#define IA32_VMX_BASIC_VMCS_PHYSICAL_ADDRESS_WIDTH                   0x1000000000000
    uint64_t dual_monitor                                            : 1;
#define IA32_VMX_BASIC_DUAL_MONITOR                                  0x2000000000000
    uint64_t memory_type                                             : 4;
#define IA32_VMX_BASIC_MEMORY_TYPE                                   0x3C000000000000
    uint64_t ins_outs_vmexit_information                             : 1;
#define IA32_VMX_BASIC_INS_OUTS_VMEXIT_INFORMATION                   0x40000000000000
    uint64_t true_controls                                           : 1;
#define IA32_VMX_BASIC_TRUE_CONTROLS                                 0x80000000000000
    uint64_t reserved_2                                              : 8;
  };

  uint64_t Flags;
} ia32_vmx_basic_register;

#define IA32_VMX_PINBASED_CTLS                                       0x00000481
typedef union {
  struct {
    uint64_t external_interrupt_exiting                              : 1;
#define IA32_VMX_PINBASED_CTLS_EXTERNAL_INTERRUPT_EXITING            0x01
    uint64_t reserved_1                                              : 2;
    uint64_t nmi_exiting                                             : 1;
#define IA32_VMX_PINBASED_CTLS_NMI_EXITING                           0x08
    uint64_t reserved_2                                              : 1;
    uint64_t virtual_nmis                                            : 1;
#define IA32_VMX_PINBASED_CTLS_VIRTUAL_NMIS                          0x20
    uint64_t activate_vmx_preemption_timer                           : 1;
#define IA32_VMX_PINBASED_CTLS_ACTIVATE_VMX_PREEMPTION_TIMER         0x40
    uint64_t process_posted_interrupts                               : 1;
#define IA32_VMX_PINBASED_CTLS_PROCESS_POSTED_INTERRUPTS             0x80
    uint64_t reserved_3                                              : 56;
  };

  uint64_t Flags;
} ia32_vmx_pinbased_ctls_register;

#define IA32_VMX_PROCBASED_CTLS                                      0x00000482
typedef union {
  struct {
    uint64_t reserved_1                                              : 2;
    uint64_t interrupt_window_exiting                                : 1;
#define IA32_VMX_PROCBASED_CTLS_INTERRUPT_WINDOW_EXITING             0x04
    uint64_t use_tsc_offsetting                                      : 1;
#define IA32_VMX_PROCBASED_CTLS_USE_TSC_OFFSETTING                   0x08
    uint64_t reserved_2                                              : 3;
    uint64_t hlt_exiting                                             : 1;
#define IA32_VMX_PROCBASED_CTLS_HLT_EXITING                          0x80
    uint64_t reserved_3                                              : 1;
    uint64_t invlpg_exiting                                          : 1;
#define IA32_VMX_PROCBASED_CTLS_INVLPG_EXITING                       0x200
    uint64_t mwait_exiting                                           : 1;
#define IA32_VMX_PROCBASED_CTLS_MWAIT_EXITING                        0x400
    uint64_t rdpmc_exiting                                           : 1;
#define IA32_VMX_PROCBASED_CTLS_RDPMC_EXITING                        0x800
    uint64_t rdtsc_exiting                                           : 1;
#define IA32_VMX_PROCBASED_CTLS_RDTSC_EXITING                        0x1000
    uint64_t reserved_4                                              : 2;
    uint64_t cr3_load_exiting                                        : 1;
#define IA32_VMX_PROCBASED_CTLS_CR3_LOAD_EXITING                     0x8000
    uint64_t cr3_store_exiting                                       : 1;
#define IA32_VMX_PROCBASED_CTLS_CR3_STORE_EXITING                    0x10000
    uint64_t reserved_5                                              : 2;
    uint64_t cr8_load_exiting                                        : 1;
#define IA32_VMX_PROCBASED_CTLS_CR8_LOAD_EXITING                     0x80000
    uint64_t cr8_store_exiting                                       : 1;
#define IA32_VMX_PROCBASED_CTLS_CR8_STORE_EXITING                    0x100000
    uint64_t use_tpr_shadow                                          : 1;
#define IA32_VMX_PROCBASED_CTLS_USE_TPR_SHADOW                       0x200000
    uint64_t nmi_window_exiting                                      : 1;
#define IA32_VMX_PROCBASED_CTLS_NMI_WINDOW_EXITING                   0x400000
    uint64_t mov_dr_exiting                                          : 1;
#define IA32_VMX_PROCBASED_CTLS_MOV_DR_EXITING                       0x800000
    uint64_t unconditional_io_exiting                                : 1;
#define IA32_VMX_PROCBASED_CTLS_UNCONDITIONAL_IO_EXITING             0x1000000
    uint64_t use_io_bitmaps                                          : 1;
#define IA32_VMX_PROCBASED_CTLS_USE_IO_BITMAPS                       0x2000000
    uint64_t reserved_6                                              : 1;
    uint64_t monitor_trap_flag                                       : 1;
#define IA32_VMX_PROCBASED_CTLS_MONITOR_TRAP_FLAG                    0x8000000
    uint64_t use_msr_bitmaps                                         : 1;
#define IA32_VMX_PROCBASED_CTLS_USE_MSR_BITMAPS                      0x10000000
    uint64_t monitor_exiting                                         : 1;
#define IA32_VMX_PROCBASED_CTLS_MONITOR_EXITING                      0x20000000
    uint64_t pause_exiting                                           : 1;
#define IA32_VMX_PROCBASED_CTLS_PAUSE_EXITING                        0x40000000
    uint64_t activate_secondary_controls                             : 1;
#define IA32_VMX_PROCBASED_CTLS_ACTIVATE_SECONDARY_CONTROLS          0x80000000
    uint64_t reserved_7                                              : 32;
  };

  uint64_t Flags;
} ia32_vmx_procbased_ctls_register;

#define IA32_VMX_EXIT_CTLS                                           0x00000483
typedef union {
  struct {
    uint64_t reserved_1                                              : 2;
    uint64_t save_debug_controls                                     : 1;
#define IA32_VMX_EXIT_CTLS_SAVE_DEBUG_CONTROLS                       0x04
    uint64_t reserved_2                                              : 6;
    uint64_t host_address_space_size                                 : 1;
#define IA32_VMX_EXIT_CTLS_HOST_ADDRESS_SPACE_SIZE                   0x200
    uint64_t reserved_3                                              : 2;
    uint64_t load_ia32_perf_global_ctrl                              : 1;
#define IA32_VMX_EXIT_CTLS_LOAD_IA32_PERF_GLOBAL_CTRL                0x1000
    uint64_t reserved_4                                              : 2;
    uint64_t acknowledge_interrupt_on_exit                           : 1;
#define IA32_VMX_EXIT_CTLS_ACKNOWLEDGE_INTERRUPT_ON_EXIT             0x8000
    uint64_t reserved_5                                              : 2;
    uint64_t save_ia32_pat                                           : 1;
#define IA32_VMX_EXIT_CTLS_SAVE_IA32_PAT                             0x40000
    uint64_t load_ia32_pat                                           : 1;
#define IA32_VMX_EXIT_CTLS_LOAD_IA32_PAT                             0x80000
    uint64_t save_ia32_efer                                          : 1;
#define IA32_VMX_EXIT_CTLS_SAVE_IA32_EFER                            0x100000
    uint64_t load_ia32_efer                                          : 1;
#define IA32_VMX_EXIT_CTLS_LOAD_IA32_EFER                            0x200000
    uint64_t save_vmx_preemption_timer_value                         : 1;
#define IA32_VMX_EXIT_CTLS_SAVE_VMX_PREEMPTION_TIMER_VALUE           0x400000
    uint64_t clear_ia32_bndcfgs                                      : 1;
#define IA32_VMX_EXIT_CTLS_CLEAR_IA32_BNDCFGS                        0x800000
    uint64_t conceal_vmx_from_pt                                     : 1;
#define IA32_VMX_EXIT_CTLS_CONCEAL_VMX_FROM_PT                       0x1000000
    uint64_t reserved_6                                              : 39;
  };

  uint64_t Flags;
} ia32_vmx_exit_ctls_register;

#define IA32_VMX_ENTRY_CTLS                                          0x00000484
typedef union {
  struct {
    uint64_t reserved_1                                              : 2;
    uint64_t load_debug_controls                                     : 1;
#define IA32_VMX_ENTRY_CTLS_LOAD_DEBUG_CONTROLS                      0x04
    uint64_t reserved_2                                              : 6;
    uint64_t ia32e_mode_guest                                        : 1;
#define IA32_VMX_ENTRY_CTLS_IA32E_MODE_GUEST                         0x200
    uint64_t entry_to_smm                                            : 1;
#define IA32_VMX_ENTRY_CTLS_ENTRY_TO_SMM                             0x400
    uint64_t deactivate_dual_monitor_treatment                       : 1;
#define IA32_VMX_ENTRY_CTLS_DEACTIVATE_DUAL_MONITOR_TREATMENT        0x800
    uint64_t reserved_3                                              : 1;
    uint64_t load_ia32_perf_global_ctrl                              : 1;
#define IA32_VMX_ENTRY_CTLS_LOAD_IA32_PERF_GLOBAL_CTRL               0x2000
    uint64_t load_ia32_pat                                           : 1;
#define IA32_VMX_ENTRY_CTLS_LOAD_IA32_PAT                            0x4000
    uint64_t load_ia32_efer                                          : 1;
#define IA32_VMX_ENTRY_CTLS_LOAD_IA32_EFER                           0x8000
    uint64_t load_ia32_bndcfgs                                       : 1;
#define IA32_VMX_ENTRY_CTLS_LOAD_IA32_BNDCFGS                        0x10000
    uint64_t conceal_vmx_from_pt                                     : 1;
#define IA32_VMX_ENTRY_CTLS_CONCEAL_VMX_FROM_PT                      0x20000
    uint64_t reserved_4                                              : 46;
  };

  uint64_t Flags;
} ia32_vmx_entry_ctls_register;

#define IA32_VMX_MISC                                                0x00000485
typedef union {
  struct {
    uint64_t preemption_timer_tsc_relationship                       : 5;
#define IA32_VMX_MISC_PREEMPTION_TIMER_TSC_RELATIONSHIP              0x1F
    uint64_t store_efer_lma_on_vmexit                                : 1;
#define IA32_VMX_MISC_STORE_EFER_LMA_ON_VMEXIT                       0x20
    uint64_t activity_states                                         : 3;
#define IA32_VMX_MISC_ACTIVITY_STATES                                0x1C0
    uint64_t reserved_1                                              : 5;
    uint64_t intel_pt_available_in_vmx                               : 1;
#define IA32_VMX_MISC_INTEL_PT_AVAILABLE_IN_VMX                      0x4000
    uint64_t rdmsr_can_read_ia32_smbase_msr_in_smm                   : 1;
#define IA32_VMX_MISC_RDMSR_CAN_READ_IA32_SMBASE_MSR_IN_SMM          0x8000
    uint64_t cr3_target_count                                        : 9;
#define IA32_VMX_MISC_CR3_TARGET_COUNT                               0x1FF0000
    uint64_t max_number_of_msr                                       : 3;
#define IA32_VMX_MISC_MAX_NUMBER_OF_MSR                              0xE000000
    uint64_t smm_monitor_ctl_b2                                      : 1;
#define IA32_VMX_MISC_SMM_MONITOR_CTL_B2                             0x10000000
    uint64_t vmwrite_vmexit_info                                     : 1;
#define IA32_VMX_MISC_VMWRITE_VMEXIT_INFO                            0x20000000
    uint64_t zero_length_instruction_vmentry_injection               : 1;
#define IA32_VMX_MISC_ZERO_LENGTH_INSTRUCTION_VMENTRY_INJECTION      0x40000000
    uint64_t reserved_2                                              : 1;
    uint64_t mseg_id                                                 : 32;
#define IA32_VMX_MISC_MSEG_ID                                        0xFFFFFFFF00000000
  };

  uint64_t Flags;
} ia32_vmx_misc_register;

#define IA32_VMX_CR0_FIXED0                                          0x00000486
#define IA32_VMX_CR0_FIXED1                                          0x00000487
#define IA32_VMX_CR4_FIXED0                                          0x00000488
#define IA32_VMX_CR4_FIXED1                                          0x00000489
#define IA32_VMX_VMCS_ENUM                                           0x0000048A
typedef union {
  struct {
    uint64_t access_type                                             : 1;
#define IA32_VMX_VMCS_ENUM_ACCESS_TYPE                               0x01
    uint64_t highest_index_value                                     : 9;
#define IA32_VMX_VMCS_ENUM_HIGHEST_INDEX_VALUE                       0x3FE
    uint64_t field_type                                              : 2;
#define IA32_VMX_VMCS_ENUM_FIELD_TYPE                                0xC00
    uint64_t reserved_1                                              : 1;
    uint64_t field_width                                             : 2;
#define IA32_VMX_VMCS_ENUM_FIELD_WIDTH                               0x6000
    uint64_t reserved_2                                              : 49;
  };

  uint64_t Flags;
} ia32_vmx_vmcs_enum_register;

#define IA32_VMX_PROCBASED_CTLS2                                     0x0000048B
typedef union {
  struct {
    uint64_t virtualize_apic_accesses                                : 1;
#define IA32_VMX_PROCBASED_CTLS2_VIRTUALIZE_APIC_ACCESSES            0x01
    uint64_t enable_ept                                              : 1;
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_EPT                          0x02
    uint64_t descriptor_table_exiting                                : 1;
#define IA32_VMX_PROCBASED_CTLS2_DESCRIPTOR_TABLE_EXITING            0x04
    uint64_t enable_rdtscp                                           : 1;
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_RDTSCP                       0x08
    uint64_t virtualize_x2apic_mode                                  : 1;
#define IA32_VMX_PROCBASED_CTLS2_VIRTUALIZE_X2APIC_MODE              0x10
    uint64_t enable_vpid                                             : 1;
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_VPID                         0x20
    uint64_t wbinvd_exiting                                          : 1;
#define IA32_VMX_PROCBASED_CTLS2_WBINVD_EXITING                      0x40
    uint64_t unrestricted_guest                                      : 1;
#define IA32_VMX_PROCBASED_CTLS2_UNRESTRICTED_GUEST                  0x80
    uint64_t apic_register_virtualization                            : 1;
#define IA32_VMX_PROCBASED_CTLS2_APIC_REGISTER_VIRTUALIZATION        0x100
    uint64_t virtual_interrupt_delivery                              : 1;
#define IA32_VMX_PROCBASED_CTLS2_VIRTUAL_INTERRUPT_DELIVERY          0x200
    uint64_t pause_loop_exiting                                      : 1;
#define IA32_VMX_PROCBASED_CTLS2_PAUSE_LOOP_EXITING                  0x400
    uint64_t rdrand_exiting                                          : 1;
#define IA32_VMX_PROCBASED_CTLS2_RDRAND_EXITING                      0x800
    uint64_t enable_invpcid                                          : 1;
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_INVPCID                      0x1000
    uint64_t enable_vm_functions                                     : 1;
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_VM_FUNCTIONS                 0x2000
    uint64_t vmcs_shadowing                                          : 1;
#define IA32_VMX_PROCBASED_CTLS2_VMCS_SHADOWING                      0x4000
    uint64_t enable_encls_exiting                                    : 1;
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_ENCLS_EXITING                0x8000
    uint64_t rdseed_exiting                                          : 1;
#define IA32_VMX_PROCBASED_CTLS2_RDSEED_EXITING                      0x10000
    uint64_t enable_pml                                              : 1;
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_PML                          0x20000
    uint64_t ept_violation                                           : 1;
#define IA32_VMX_PROCBASED_CTLS2_EPT_VIOLATION                       0x40000
    uint64_t conceal_vmx_from_pt                                     : 1;
#define IA32_VMX_PROCBASED_CTLS2_CONCEAL_VMX_FROM_PT                 0x80000
    uint64_t enable_xsaves                                           : 1;
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_XSAVES                       0x100000
    uint64_t reserved_1                                              : 1;
    uint64_t mode_based_execute_control_for_ept                      : 1;
#define IA32_VMX_PROCBASED_CTLS2_MODE_BASED_EXECUTE_CONTROL_FOR_EPT  0x400000
    uint64_t reserved_2                                              : 2;
    uint64_t use_tsc_scaling                                         : 1;
#define IA32_VMX_PROCBASED_CTLS2_USE_TSC_SCALING                     0x2000000
    uint64_t reserved_3                                              : 38;
  };

  uint64_t Flags;
} ia32_vmx_procbased_ctls2_register;

#define IA32_VMX_EPT_VPID_CAP                                        0x0000048C
typedef union {
  struct {
    uint64_t execute_only_pages                                      : 1;
#define IA32_VMX_EPT_VPID_CAP_EXECUTE_ONLY_PAGES                     0x01
    uint64_t reserved_1                                              : 5;
    uint64_t page_walk_length_4                                      : 1;
#define IA32_VMX_EPT_VPID_CAP_PAGE_WALK_LENGTH_4                     0x40
    uint64_t reserved_2                                              : 1;
    uint64_t memory_type_uncacheable                                 : 1;
#define IA32_VMX_EPT_VPID_CAP_MEMORY_TYPE_UNCACHEABLE                0x100
    uint64_t reserved_3                                              : 5;
    uint64_t memory_type_write_back                                  : 1;
#define IA32_VMX_EPT_VPID_CAP_MEMORY_TYPE_WRITE_BACK                 0x4000
    uint64_t reserved_4                                              : 1;
    uint64_t pde_2mb_pages                                           : 1;
#define IA32_VMX_EPT_VPID_CAP_PDE_2MB_PAGES                          0x10000
    uint64_t pdpte_1gb_pages                                         : 1;
#define IA32_VMX_EPT_VPID_CAP_PDPTE_1GB_PAGES                        0x20000
    uint64_t reserved_5                                              : 2;
    uint64_t invept                                                  : 1;
#define IA32_VMX_EPT_VPID_CAP_INVEPT                                 0x100000
    uint64_t ept_accessed_and_dirty_flags                            : 1;
#define IA32_VMX_EPT_VPID_CAP_EPT_ACCESSED_AND_DIRTY_FLAGS           0x200000
    uint64_t advanced_vmexit_ept_violations_information              : 1;
#define IA32_VMX_EPT_VPID_CAP_ADVANCED_VMEXIT_EPT_VIOLATIONS_INFORMATION 0x400000
    uint64_t reserved_6                                              : 2;
    uint64_t invept_single_context                                   : 1;
#define IA32_VMX_EPT_VPID_CAP_INVEPT_SINGLE_CONTEXT                  0x2000000
    uint64_t invept_all_contexts                                     : 1;
#define IA32_VMX_EPT_VPID_CAP_INVEPT_ALL_CONTEXTS                    0x4000000
    uint64_t reserved_7                                              : 5;
    uint64_t invvpid                                                 : 1;
#define IA32_VMX_EPT_VPID_CAP_INVVPID                                0x100000000
    uint64_t reserved_8                                              : 7;
    uint64_t invvpid_individual_address                              : 1;
#define IA32_VMX_EPT_VPID_CAP_INVVPID_INDIVIDUAL_ADDRESS             0x10000000000
    uint64_t invvpid_single_context                                  : 1;
#define IA32_VMX_EPT_VPID_CAP_INVVPID_SINGLE_CONTEXT                 0x20000000000
    uint64_t invvpid_all_contexts                                    : 1;
#define IA32_VMX_EPT_VPID_CAP_INVVPID_ALL_CONTEXTS                   0x40000000000
    uint64_t invvpid_single_context_retain_globals                   : 1;
#define IA32_VMX_EPT_VPID_CAP_INVVPID_SINGLE_CONTEXT_RETAIN_GLOBALS  0x80000000000
    uint64_t reserved_9                                              : 20;
  };

  uint64_t Flags;
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
#define IA32_VMX_TRUE_CTLS_ALLOWED_0_SETTINGS                        0xFFFFFFFF
    uint64_t allowed_1_settings                                      : 32;
#define IA32_VMX_TRUE_CTLS_ALLOWED_1_SETTINGS                        0xFFFFFFFF00000000
  };

  uint64_t Flags;
} ia32_vmx_true_ctls_register;

/**
 * @}
 */

#define IA32_VMX_VMFUNC                                              0x00000491
typedef union {
  struct {
    uint64_t eptp_switching                                          : 1;
#define IA32_VMX_VMFUNC_EPTP_SWITCHING                               0x01
    uint64_t reserved_1                                              : 63;
  };

  uint64_t Flags;
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
#define IA32_MCG_EXT_CTL_LMCE_EN                                     0x01
    uint64_t reserved_1                                              : 63;
  };

  uint64_t Flags;
} ia32_mcg_ext_ctl_register;

#define IA32_SGX_SVN_STATUS                                          0x00000500
typedef union {
  struct {
    uint64_t lock                                                    : 1;
#define IA32_SGX_SVN_STATUS_LOCK                                     0x01
    uint64_t reserved_1                                              : 15;
    uint64_t sgx_svn_sinit                                           : 8;
#define IA32_SGX_SVN_STATUS_SGX_SVN_SINIT                            0xFF0000
    uint64_t reserved_2                                              : 40;
  };

  uint64_t Flags;
} ia32_sgx_svn_status_register;

#define IA32_RTIT_OUTPUT_BASE                                        0x00000560
typedef union {
  struct {
    uint64_t reserved_1                                              : 7;
    uint64_t base_physical_address                                   : 41;
#define IA32_RTIT_OUTPUT_BASE_BASE_PHYSICAL_ADDRESS                  0xFFFFFFFFFF80
    uint64_t reserved_2                                              : 16;
  };

  uint64_t Flags;
} ia32_rtit_output_base_register;

#define IA32_RTIT_OUTPUT_MASK_PTRS                                   0x00000561
typedef union {
  struct {
    uint64_t lower_mask                                              : 7;
#define IA32_RTIT_OUTPUT_MASK_PTRS_LOWER_MASK                        0x7F
    uint64_t mask_or_table_offset                                    : 25;
#define IA32_RTIT_OUTPUT_MASK_PTRS_MASK_OR_TABLE_OFFSET              0xFFFFFF80
    uint64_t output_offset                                           : 32;
#define IA32_RTIT_OUTPUT_MASK_PTRS_OUTPUT_OFFSET                     0xFFFFFFFF00000000
  };

  uint64_t Flags;
} ia32_rtit_output_mask_ptrs_register;

#define IA32_RTIT_CTL                                                0x00000570
typedef union {
  struct {
    uint64_t trace_en                                                : 1;
#define IA32_RTIT_CTL_TRACE_EN                                       0x01
    uint64_t cyc_en                                                  : 1;
#define IA32_RTIT_CTL_CYC_EN                                         0x02
    uint64_t os                                                      : 1;
#define IA32_RTIT_CTL_OS                                             0x04
    uint64_t user                                                    : 1;
#define IA32_RTIT_CTL_USER                                           0x08
    uint64_t pwr_evt_en                                              : 1;
#define IA32_RTIT_CTL_PWR_EVT_EN                                     0x10
    uint64_t fup_on_ptw                                              : 1;
#define IA32_RTIT_CTL_FUP_ON_PTW                                     0x20
    uint64_t fabric_en                                               : 1;
#define IA32_RTIT_CTL_FABRIC_EN                                      0x40
    uint64_t cr3_filter                                              : 1;
#define IA32_RTIT_CTL_CR3_FILTER                                     0x80
    uint64_t topa                                                    : 1;
#define IA32_RTIT_CTL_TOPA                                           0x100
    uint64_t mtc_en                                                  : 1;
#define IA32_RTIT_CTL_MTC_EN                                         0x200
    uint64_t tsc_en                                                  : 1;
#define IA32_RTIT_CTL_TSC_EN                                         0x400
    uint64_t dis_retc                                                : 1;
#define IA32_RTIT_CTL_DIS_RETC                                       0x800
    uint64_t ptw_en                                                  : 1;
#define IA32_RTIT_CTL_PTW_EN                                         0x1000
    uint64_t branch_en                                               : 1;
#define IA32_RTIT_CTL_BRANCH_EN                                      0x2000
    uint64_t mtc_freq                                                : 4;
#define IA32_RTIT_CTL_MTC_FREQ                                       0x3C000
    uint64_t reserved_1                                              : 1;
    uint64_t cyc_thresh                                              : 4;
#define IA32_RTIT_CTL_CYC_THRESH                                     0x780000
    uint64_t reserved_2                                              : 1;
    uint64_t psb_freq                                                : 4;
#define IA32_RTIT_CTL_PSB_FREQ                                       0xF000000
    uint64_t reserved_3                                              : 4;
    uint64_t addr0_cfg                                               : 4;
#define IA32_RTIT_CTL_ADDR0_CFG                                      0xF00000000
    uint64_t addr1_cfg                                               : 4;
#define IA32_RTIT_CTL_ADDR1_CFG                                      0xF000000000
    uint64_t addr2_cfg                                               : 4;
#define IA32_RTIT_CTL_ADDR2_CFG                                      0xF0000000000
    uint64_t addr3_cfg                                               : 4;
#define IA32_RTIT_CTL_ADDR3_CFG                                      0xF00000000000
    uint64_t reserved_4                                              : 8;
    uint64_t inject_psb_pmi_on_enable                                : 1;
#define IA32_RTIT_CTL_INJECT_PSB_PMI_ON_ENABLE                       0x100000000000000
    uint64_t reserved_5                                              : 7;
  };

  uint64_t Flags;
} ia32_rtit_ctl_register;

#define IA32_RTIT_STATUS                                             0x00000571
typedef union {
  struct {
    uint64_t filter_en                                               : 1;
#define IA32_RTIT_STATUS_FILTER_EN                                   0x01
    uint64_t contex_en                                               : 1;
#define IA32_RTIT_STATUS_CONTEX_EN                                   0x02
    uint64_t trigger_en                                              : 1;
#define IA32_RTIT_STATUS_TRIGGER_EN                                  0x04
    uint64_t reserved_1                                              : 1;
    uint64_t error                                                   : 1;
#define IA32_RTIT_STATUS_ERROR                                       0x10
    uint64_t stopped                                                 : 1;
#define IA32_RTIT_STATUS_STOPPED                                     0x20
    uint64_t pend_psb                                                : 1;
#define IA32_RTIT_STATUS_PEND_PSB                                    0x40
    uint64_t pend_topa_pmi                                           : 1;
#define IA32_RTIT_STATUS_PEND_TOPA_PMI                               0x80
    uint64_t reserved_2                                              : 24;
    uint64_t packet_byte_cnt                                         : 17;
#define IA32_RTIT_STATUS_PACKET_BYTE_CNT                             0x1FFFF00000000
    uint64_t reserved_3                                              : 15;
  };

  uint64_t Flags;
} ia32_rtit_status_register;

#define IA32_RTIT_CR3_MATCH                                          0x00000572
typedef union {
  struct {
    uint64_t reserved_1                                              : 5;
    uint64_t cr3_value_to_match                                      : 59;
#define IA32_RTIT_CR3_MATCH_CR3_VALUE_TO_MATCH                       0xFFFFFFFFFFFFFFE0
  };

  uint64_t Flags;
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
#define IA32_RTIT_ADDR_VIRTUAL_ADDRESS                               0xFFFFFFFFFFFF
    uint64_t sign_ext_va                                             : 16;
#define IA32_RTIT_ADDR_SIGN_EXT_VA                                   0xFFFF000000000000
  };

  uint64_t Flags;
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
#define IA32_PM_ENABLE_HWP_ENABLE                                    0x01
    uint64_t reserved_1                                              : 63;
  };

  uint64_t Flags;
} ia32_pm_enable_register;

#define IA32_HWP_CAPABILITIES                                        0x00000771
typedef union {
  struct {
    uint64_t highest_performance                                     : 8;
#define IA32_HWP_CAPABILITIES_HIGHEST_PERFORMANCE                    0xFF
    uint64_t guaranteed_performance                                  : 8;
#define IA32_HWP_CAPABILITIES_GUARANTEED_PERFORMANCE                 0xFF00
    uint64_t most_efficient_performance                              : 8;
#define IA32_HWP_CAPABILITIES_MOST_EFFICIENT_PERFORMANCE             0xFF0000
    uint64_t lowest_performance                                      : 8;
#define IA32_HWP_CAPABILITIES_LOWEST_PERFORMANCE                     0xFF000000
    uint64_t reserved_1                                              : 32;
  };

  uint64_t Flags;
} ia32_hwp_capabilities_register;

#define IA32_HWP_REQUEST_PKG                                         0x00000772
typedef union {
  struct {
    uint64_t minimum_performance                                     : 8;
#define IA32_HWP_REQUEST_PKG_MINIMUM_PERFORMANCE                     0xFF
    uint64_t maximum_performance                                     : 8;
#define IA32_HWP_REQUEST_PKG_MAXIMUM_PERFORMANCE                     0xFF00
    uint64_t desired_performance                                     : 8;
#define IA32_HWP_REQUEST_PKG_DESIRED_PERFORMANCE                     0xFF0000
    uint64_t energy_performance_preference                           : 8;
#define IA32_HWP_REQUEST_PKG_ENERGY_PERFORMANCE_PREFERENCE           0xFF000000
    uint64_t activity_window                                         : 10;
#define IA32_HWP_REQUEST_PKG_ACTIVITY_WINDOW                         0x3FF00000000
    uint64_t reserved_1                                              : 22;
  };

  uint64_t Flags;
} ia32_hwp_request_pkg_register;

#define IA32_HWP_INTERRUPT                                           0x00000773
typedef union {
  struct {
    uint64_t en_guaranteed_performance_change                        : 1;
#define IA32_HWP_INTERRUPT_EN_GUARANTEED_PERFORMANCE_CHANGE          0x01
    uint64_t en_excursion_minimum                                    : 1;
#define IA32_HWP_INTERRUPT_EN_EXCURSION_MINIMUM                      0x02
    uint64_t reserved_1                                              : 62;
  };

  uint64_t Flags;
} ia32_hwp_interrupt_register;

#define IA32_HWP_REQUEST                                             0x00000774
typedef union {
  struct {
    uint64_t minimum_performance                                     : 8;
#define IA32_HWP_REQUEST_MINIMUM_PERFORMANCE                         0xFF
    uint64_t maximum_performance                                     : 8;
#define IA32_HWP_REQUEST_MAXIMUM_PERFORMANCE                         0xFF00
    uint64_t desired_performance                                     : 8;
#define IA32_HWP_REQUEST_DESIRED_PERFORMANCE                         0xFF0000
    uint64_t energy_performance_preference                           : 8;
#define IA32_HWP_REQUEST_ENERGY_PERFORMANCE_PREFERENCE               0xFF000000
    uint64_t activity_window                                         : 10;
#define IA32_HWP_REQUEST_ACTIVITY_WINDOW                             0x3FF00000000
    uint64_t package_control                                         : 1;
#define IA32_HWP_REQUEST_PACKAGE_CONTROL                             0x40000000000
    uint64_t reserved_1                                              : 21;
  };

  uint64_t Flags;
} ia32_hwp_request_register;

#define IA32_HWP_STATUS                                              0x00000777
typedef union {
  struct {
    uint64_t guaranteed_performance_change                           : 1;
#define IA32_HWP_STATUS_GUARANTEED_PERFORMANCE_CHANGE                0x01
    uint64_t reserved_1                                              : 1;
    uint64_t excursion_to_minimum                                    : 1;
#define IA32_HWP_STATUS_EXCURSION_TO_MINIMUM                         0x04
    uint64_t reserved_2                                              : 61;
  };

  uint64_t Flags;
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
#define IA32_DEBUG_INTERFACE_ENABLE                                  0x01
    uint64_t reserved_1                                              : 29;
    uint64_t lock                                                    : 1;
#define IA32_DEBUG_INTERFACE_LOCK                                    0x40000000
    uint64_t debug_occurred                                          : 1;
#define IA32_DEBUG_INTERFACE_DEBUG_OCCURRED                          0x80000000
    uint64_t reserved_2                                              : 32;
  };

  uint64_t Flags;
} ia32_debug_interface_register;

#define IA32_L3_QOS_CFG                                              0x00000C81
typedef union {
  struct {
    uint64_t enable                                                  : 1;
#define IA32_L3_QOS_CFG_ENABLE                                       0x01
    uint64_t reserved_1                                              : 63;
  };

  uint64_t Flags;
} ia32_l3_qos_cfg_register;

#define IA32_L2_QOS_CFG                                              0x00000C82
typedef union {
  struct {
    uint64_t enable                                                  : 1;
#define IA32_L2_QOS_CFG_ENABLE                                       0x01
    uint64_t reserved_1                                              : 63;
  };

  uint64_t Flags;
} ia32_l2_qos_cfg_register;

#define IA32_QM_EVTSEL                                               0x00000C8D
typedef union {
  struct {
    uint64_t event_id                                                : 8;
#define IA32_QM_EVTSEL_EVENT_ID                                      0xFF
    uint64_t reserved_1                                              : 24;
    uint64_t resource_monitoring_id                                  : 32;
#define IA32_QM_EVTSEL_RESOURCE_MONITORING_ID                        0xFFFFFFFF00000000
  };

  uint64_t Flags;
} ia32_qm_evtsel_register;

#define IA32_QM_CTR                                                  0x00000C8E
typedef union {
  struct {
    uint64_t resource_monitored_data                                 : 62;
#define IA32_QM_CTR_RESOURCE_MONITORED_DATA                          0x3FFFFFFFFFFFFFFF
    uint64_t unavailable                                             : 1;
#define IA32_QM_CTR_UNAVAILABLE                                      0x4000000000000000
    uint64_t error                                                   : 1;
#define IA32_QM_CTR_ERROR                                            0x8000000000000000
  };

  uint64_t Flags;
} ia32_qm_ctr_register;

#define IA32_PQR_ASSOC                                               0x00000C8F
typedef union {
  struct {
    uint64_t resource_monitoring_id                                  : 32;
#define IA32_PQR_ASSOC_RESOURCE_MONITORING_ID                        0xFFFFFFFF
    uint64_t cos                                                     : 32;
#define IA32_PQR_ASSOC_COS                                           0xFFFFFFFF00000000
  };

  uint64_t Flags;
} ia32_pqr_assoc_register;

#define IA32_BNDCFGS                                                 0x00000D90
typedef union {
  struct {
    uint64_t enable                                                  : 1;
#define IA32_BNDCFGS_ENABLE                                          0x01
    uint64_t bnd_preserve                                            : 1;
#define IA32_BNDCFGS_BND_PRESERVE                                    0x02
    uint64_t reserved_1                                              : 10;
    uint64_t bound_directory_base_address                            : 52;
#define IA32_BNDCFGS_BOUND_DIRECTORY_BASE_ADDRESS                    0xFFFFFFFFFFFFF000
  };

  uint64_t Flags;
} ia32_bndcfgs_register;

#define IA32_XSS                                                     0x00000DA0
typedef union {
  struct {
    uint64_t reserved_1                                              : 8;
    uint64_t trace_packet_configuration_state                        : 1;
#define IA32_XSS_TRACE_PACKET_CONFIGURATION_STATE                    0x100
    uint64_t reserved_2                                              : 55;
  };

  uint64_t Flags;
} ia32_xss_register;

#define IA32_PKG_HDC_CTL                                             0x00000DB0
typedef union {
  struct {
    uint64_t hdc_pkg_enable                                          : 1;
#define IA32_PKG_HDC_CTL_HDC_PKG_ENABLE                              0x01
    uint64_t reserved_1                                              : 63;
  };

  uint64_t Flags;
} ia32_pkg_hdc_ctl_register;

#define IA32_PM_CTL1                                                 0x00000DB1
typedef union {
  struct {
    uint64_t hdc_allow_block                                         : 1;
#define IA32_PM_CTL1_HDC_ALLOW_BLOCK                                 0x01
    uint64_t reserved_1                                              : 63;
  };

  uint64_t Flags;
} ia32_pm_ctl1_register;

#define IA32_THREAD_STALL                                            0x00000DB2
typedef struct {
  uint64_t stall_cycle_cnt;
} ia32_thread_stall_register;

#define IA32_EFER                                                    0xC0000080
typedef union {
  struct {
    uint64_t syscall_enable                                          : 1;
#define IA32_EFER_SYSCALL_ENABLE                                     0x01
    uint64_t reserved_1                                              : 7;
    uint64_t ia32e_mode_enable                                       : 1;
#define IA32_EFER_IA32E_MODE_ENABLE                                  0x100
    uint64_t reserved_2                                              : 1;
    uint64_t ia32e_mode_active                                       : 1;
#define IA32_EFER_IA32E_MODE_ACTIVE                                  0x400
    uint64_t execute_disable_bit_enable                              : 1;
#define IA32_EFER_EXECUTE_DISABLE_BIT_ENABLE                         0x800
    uint64_t reserved_3                                              : 52;
  };

  uint64_t Flags;
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
#define IA32_TSC_AUX_TSC_AUXILIARY_SIGNATURE                         0xFFFFFFFF
    uint64_t reserved_1                                              : 32;
  };

  uint64_t Flags;
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
#define PDE_4MB_32_PRESENT                                           0x01
    uint32_t write                                                   : 1;
#define PDE_4MB_32_WRITE                                             0x02
    uint32_t supervisor                                              : 1;
#define PDE_4MB_32_SUPERVISOR                                        0x04
    uint32_t page_level_write_through                                : 1;
#define PDE_4MB_32_PAGE_LEVEL_WRITE_THROUGH                          0x08
    uint32_t page_level_cache_disable                                : 1;
#define PDE_4MB_32_PAGE_LEVEL_CACHE_DISABLE                          0x10
    uint32_t accessed                                                : 1;
#define PDE_4MB_32_ACCESSED                                          0x20
    uint32_t dirty                                                   : 1;
#define PDE_4MB_32_DIRTY                                             0x40
    uint32_t large_page                                              : 1;
#define PDE_4MB_32_LARGE_PAGE                                        0x80
    uint32_t global                                                  : 1;
#define PDE_4MB_32_GLOBAL                                            0x100
    uint32_t ignored_1                                               : 3;
#define PDE_4MB_32_IGNORED_1                                         0xE00
    uint32_t pat                                                     : 1;
#define PDE_4MB_32_PAT                                               0x1000
    uint32_t page_frame_number_low                                   : 8;
#define PDE_4MB_32_PAGE_FRAME_NUMBER_LOW                             0x1FE000
    uint32_t reserved_1                                              : 1;
    uint32_t page_frame_number_high                                  : 10;
#define PDE_4MB_32_PAGE_FRAME_NUMBER_HIGH                            0xFFC00000
  };

  uint32_t Flags;
} pde_4mb_32;

typedef union {
  struct {
    uint32_t present                                                 : 1;
#define PDE_32_PRESENT                                               0x01
    uint32_t write                                                   : 1;
#define PDE_32_WRITE                                                 0x02
    uint32_t supervisor                                              : 1;
#define PDE_32_SUPERVISOR                                            0x04
    uint32_t page_level_write_through                                : 1;
#define PDE_32_PAGE_LEVEL_WRITE_THROUGH                              0x08
    uint32_t page_level_cache_disable                                : 1;
#define PDE_32_PAGE_LEVEL_CACHE_DISABLE                              0x10
    uint32_t accessed                                                : 1;
#define PDE_32_ACCESSED                                              0x20
    uint32_t ignored_1                                               : 1;
#define PDE_32_IGNORED_1                                             0x40
    uint32_t large_page                                              : 1;
#define PDE_32_LARGE_PAGE                                            0x80
    uint32_t ignored_2                                               : 4;
#define PDE_32_IGNORED_2                                             0xF00
    uint32_t page_frame_number                                       : 20;
#define PDE_32_PAGE_FRAME_NUMBER                                     0xFFFFF000
  };

  uint32_t Flags;
} pde_32;

typedef union {
  struct {
    uint32_t present                                                 : 1;
#define PTE_32_PRESENT                                               0x01
    uint32_t write                                                   : 1;
#define PTE_32_WRITE                                                 0x02
    uint32_t supervisor                                              : 1;
#define PTE_32_SUPERVISOR                                            0x04
    uint32_t page_level_write_through                                : 1;
#define PTE_32_PAGE_LEVEL_WRITE_THROUGH                              0x08
    uint32_t page_level_cache_disable                                : 1;
#define PTE_32_PAGE_LEVEL_CACHE_DISABLE                              0x10
    uint32_t accessed                                                : 1;
#define PTE_32_ACCESSED                                              0x20
    uint32_t dirty                                                   : 1;
#define PTE_32_DIRTY                                                 0x40
    uint32_t pat                                                     : 1;
#define PTE_32_PAT                                                   0x80
    uint32_t global                                                  : 1;
#define PTE_32_GLOBAL                                                0x100
    uint32_t ignored_1                                               : 3;
#define PTE_32_IGNORED_1                                             0xE00
    uint32_t page_frame_number                                       : 20;
#define PTE_32_PAGE_FRAME_NUMBER                                     0xFFFFF000
  };

  uint32_t Flags;
} pte_32;

typedef union {
  struct {
    uint32_t present                                                 : 1;
#define PT_ENTRY_32_PRESENT                                          0x01
    uint32_t write                                                   : 1;
#define PT_ENTRY_32_WRITE                                            0x02
    uint32_t supervisor                                              : 1;
#define PT_ENTRY_32_SUPERVISOR                                       0x04
    uint32_t page_level_write_through                                : 1;
#define PT_ENTRY_32_PAGE_LEVEL_WRITE_THROUGH                         0x08
    uint32_t page_level_cache_disable                                : 1;
#define PT_ENTRY_32_PAGE_LEVEL_CACHE_DISABLE                         0x10
    uint32_t accessed                                                : 1;
#define PT_ENTRY_32_ACCESSED                                         0x20
    uint32_t dirty                                                   : 1;
#define PT_ENTRY_32_DIRTY                                            0x40
    uint32_t large_page                                              : 1;
#define PT_ENTRY_32_LARGE_PAGE                                       0x80
    uint32_t global                                                  : 1;
#define PT_ENTRY_32_GLOBAL                                           0x100
    uint32_t ignored_1                                               : 3;
#define PT_ENTRY_32_IGNORED_1                                        0xE00
    uint32_t page_frame_number                                       : 20;
#define PT_ENTRY_32_PAGE_FRAME_NUMBER                                0xFFFFF000
  };

  uint32_t Flags;
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
#define PML4E_64_PRESENT                                             0x01
    uint64_t write                                                   : 1;
#define PML4E_64_WRITE                                               0x02
    uint64_t supervisor                                              : 1;
#define PML4E_64_SUPERVISOR                                          0x04
    uint64_t page_level_write_through                                : 1;
#define PML4E_64_PAGE_LEVEL_WRITE_THROUGH                            0x08
    uint64_t page_level_cache_disable                                : 1;
#define PML4E_64_PAGE_LEVEL_CACHE_DISABLE                            0x10
    uint64_t accessed                                                : 1;
#define PML4E_64_ACCESSED                                            0x20
    uint64_t reserved_1                                              : 1;
    uint64_t must_be_zero                                            : 1;
#define PML4E_64_MUST_BE_ZERO                                        0x80
    uint64_t ignored_1                                               : 4;
#define PML4E_64_IGNORED_1                                           0xF00
    uint64_t page_frame_number                                       : 36;
#define PML4E_64_PAGE_FRAME_NUMBER                                   0xFFFFFFFFF000
    uint64_t reserved_2                                              : 4;
    uint64_t ignored_2                                               : 11;
#define PML4E_64_IGNORED_2                                           0x7FF0000000000000
    uint64_t execute_disable                                         : 1;
#define PML4E_64_EXECUTE_DISABLE                                     0x8000000000000000
  };

  uint64_t Flags;
} pml4e_64;

typedef union {
  struct {
    uint64_t present                                                 : 1;
#define PDPTE_1GB_64_PRESENT                                         0x01
    uint64_t write                                                   : 1;
#define PDPTE_1GB_64_WRITE                                           0x02
    uint64_t supervisor                                              : 1;
#define PDPTE_1GB_64_SUPERVISOR                                      0x04
    uint64_t page_level_write_through                                : 1;
#define PDPTE_1GB_64_PAGE_LEVEL_WRITE_THROUGH                        0x08
    uint64_t page_level_cache_disable                                : 1;
#define PDPTE_1GB_64_PAGE_LEVEL_CACHE_DISABLE                        0x10
    uint64_t accessed                                                : 1;
#define PDPTE_1GB_64_ACCESSED                                        0x20
    uint64_t dirty                                                   : 1;
#define PDPTE_1GB_64_DIRTY                                           0x40
    uint64_t large_page                                              : 1;
#define PDPTE_1GB_64_LARGE_PAGE                                      0x80
    uint64_t global                                                  : 1;
#define PDPTE_1GB_64_GLOBAL                                          0x100
    uint64_t ignored_1                                               : 3;
#define PDPTE_1GB_64_IGNORED_1                                       0xE00
    uint64_t pat                                                     : 1;
#define PDPTE_1GB_64_PAT                                             0x1000
    uint64_t reserved_1                                              : 17;
    uint64_t page_frame_number                                       : 18;
#define PDPTE_1GB_64_PAGE_FRAME_NUMBER                               0xFFFFC0000000
    uint64_t reserved_2                                              : 4;
    uint64_t ignored_2                                               : 7;
#define PDPTE_1GB_64_IGNORED_2                                       0x7F0000000000000
    uint64_t protection_key                                          : 4;
#define PDPTE_1GB_64_PROTECTION_KEY                                  0x7800000000000000
    uint64_t execute_disable                                         : 1;
#define PDPTE_1GB_64_EXECUTE_DISABLE                                 0x8000000000000000
  };

  uint64_t Flags;
} pdpte_1gb_64;

typedef union {
  struct {
    uint64_t present                                                 : 1;
#define PDPTE_64_PRESENT                                             0x01
    uint64_t write                                                   : 1;
#define PDPTE_64_WRITE                                               0x02
    uint64_t supervisor                                              : 1;
#define PDPTE_64_SUPERVISOR                                          0x04
    uint64_t page_level_write_through                                : 1;
#define PDPTE_64_PAGE_LEVEL_WRITE_THROUGH                            0x08
    uint64_t page_level_cache_disable                                : 1;
#define PDPTE_64_PAGE_LEVEL_CACHE_DISABLE                            0x10
    uint64_t accessed                                                : 1;
#define PDPTE_64_ACCESSED                                            0x20
    uint64_t reserved_1                                              : 1;
    uint64_t large_page                                              : 1;
#define PDPTE_64_LARGE_PAGE                                          0x80
    uint64_t ignored_1                                               : 4;
#define PDPTE_64_IGNORED_1                                           0xF00
    uint64_t page_frame_number                                       : 36;
#define PDPTE_64_PAGE_FRAME_NUMBER                                   0xFFFFFFFFF000
    uint64_t reserved_2                                              : 4;
    uint64_t ignored_2                                               : 11;
#define PDPTE_64_IGNORED_2                                           0x7FF0000000000000
    uint64_t execute_disable                                         : 1;
#define PDPTE_64_EXECUTE_DISABLE                                     0x8000000000000000
  };

  uint64_t Flags;
} pdpte_64;

typedef union {
  struct {
    uint64_t present                                                 : 1;
#define PDE_2MB_64_PRESENT                                           0x01
    uint64_t write                                                   : 1;
#define PDE_2MB_64_WRITE                                             0x02
    uint64_t supervisor                                              : 1;
#define PDE_2MB_64_SUPERVISOR                                        0x04
    uint64_t page_level_write_through                                : 1;
#define PDE_2MB_64_PAGE_LEVEL_WRITE_THROUGH                          0x08
    uint64_t page_level_cache_disable                                : 1;
#define PDE_2MB_64_PAGE_LEVEL_CACHE_DISABLE                          0x10
    uint64_t accessed                                                : 1;
#define PDE_2MB_64_ACCESSED                                          0x20
    uint64_t dirty                                                   : 1;
#define PDE_2MB_64_DIRTY                                             0x40
    uint64_t large_page                                              : 1;
#define PDE_2MB_64_LARGE_PAGE                                        0x80
    uint64_t global                                                  : 1;
#define PDE_2MB_64_GLOBAL                                            0x100
    uint64_t ignored_1                                               : 3;
#define PDE_2MB_64_IGNORED_1                                         0xE00
    uint64_t pat                                                     : 1;
#define PDE_2MB_64_PAT                                               0x1000
    uint64_t reserved_1                                              : 8;
    uint64_t page_frame_number                                       : 27;
#define PDE_2MB_64_PAGE_FRAME_NUMBER                                 0xFFFFFFE00000
    uint64_t reserved_2                                              : 4;
    uint64_t ignored_2                                               : 7;
#define PDE_2MB_64_IGNORED_2                                         0x7F0000000000000
    uint64_t protection_key                                          : 4;
#define PDE_2MB_64_PROTECTION_KEY                                    0x7800000000000000
    uint64_t execute_disable                                         : 1;
#define PDE_2MB_64_EXECUTE_DISABLE                                   0x8000000000000000
  };

  uint64_t Flags;
} pde_2mb_64;

typedef union {
  struct {
    uint64_t present                                                 : 1;
#define PDE_64_PRESENT                                               0x01
    uint64_t write                                                   : 1;
#define PDE_64_WRITE                                                 0x02
    uint64_t supervisor                                              : 1;
#define PDE_64_SUPERVISOR                                            0x04
    uint64_t page_level_write_through                                : 1;
#define PDE_64_PAGE_LEVEL_WRITE_THROUGH                              0x08
    uint64_t page_level_cache_disable                                : 1;
#define PDE_64_PAGE_LEVEL_CACHE_DISABLE                              0x10
    uint64_t accessed                                                : 1;
#define PDE_64_ACCESSED                                              0x20
    uint64_t reserved_1                                              : 1;
    uint64_t large_page                                              : 1;
#define PDE_64_LARGE_PAGE                                            0x80
    uint64_t ignored_1                                               : 4;
#define PDE_64_IGNORED_1                                             0xF00
    uint64_t page_frame_number                                       : 36;
#define PDE_64_PAGE_FRAME_NUMBER                                     0xFFFFFFFFF000
    uint64_t reserved_2                                              : 4;
    uint64_t ignored_2                                               : 11;
#define PDE_64_IGNORED_2                                             0x7FF0000000000000
    uint64_t execute_disable                                         : 1;
#define PDE_64_EXECUTE_DISABLE                                       0x8000000000000000
  };

  uint64_t Flags;
} pde_64;

typedef union {
  struct {
    uint64_t present                                                 : 1;
#define PTE_64_PRESENT                                               0x01
    uint64_t write                                                   : 1;
#define PTE_64_WRITE                                                 0x02
    uint64_t supervisor                                              : 1;
#define PTE_64_SUPERVISOR                                            0x04
    uint64_t page_level_write_through                                : 1;
#define PTE_64_PAGE_LEVEL_WRITE_THROUGH                              0x08
    uint64_t page_level_cache_disable                                : 1;
#define PTE_64_PAGE_LEVEL_CACHE_DISABLE                              0x10
    uint64_t accessed                                                : 1;
#define PTE_64_ACCESSED                                              0x20
    uint64_t dirty                                                   : 1;
#define PTE_64_DIRTY                                                 0x40
    uint64_t pat                                                     : 1;
#define PTE_64_PAT                                                   0x80
    uint64_t global                                                  : 1;
#define PTE_64_GLOBAL                                                0x100
    uint64_t ignored_1                                               : 3;
#define PTE_64_IGNORED_1                                             0xE00
    uint64_t page_frame_number                                       : 36;
#define PTE_64_PAGE_FRAME_NUMBER                                     0xFFFFFFFFF000
    uint64_t reserved_1                                              : 4;
    uint64_t ignored_2                                               : 7;
#define PTE_64_IGNORED_2                                             0x7F0000000000000
    uint64_t protection_key                                          : 4;
#define PTE_64_PROTECTION_KEY                                        0x7800000000000000
    uint64_t execute_disable                                         : 1;
#define PTE_64_EXECUTE_DISABLE                                       0x8000000000000000
  };

  uint64_t Flags;
} pte_64;

typedef union {
  struct {
    uint64_t present                                                 : 1;
#define PT_ENTRY_64_PRESENT                                          0x01
    uint64_t write                                                   : 1;
#define PT_ENTRY_64_WRITE                                            0x02
    uint64_t supervisor                                              : 1;
#define PT_ENTRY_64_SUPERVISOR                                       0x04
    uint64_t page_level_write_through                                : 1;
#define PT_ENTRY_64_PAGE_LEVEL_WRITE_THROUGH                         0x08
    uint64_t page_level_cache_disable                                : 1;
#define PT_ENTRY_64_PAGE_LEVEL_CACHE_DISABLE                         0x10
    uint64_t accessed                                                : 1;
#define PT_ENTRY_64_ACCESSED                                         0x20
    uint64_t dirty                                                   : 1;
#define PT_ENTRY_64_DIRTY                                            0x40
    uint64_t large_page                                              : 1;
#define PT_ENTRY_64_LARGE_PAGE                                       0x80
    uint64_t global                                                  : 1;
#define PT_ENTRY_64_GLOBAL                                           0x100
    uint64_t ignored_1                                               : 3;
#define PT_ENTRY_64_IGNORED_1                                        0xE00
    uint64_t page_frame_number                                       : 36;
#define PT_ENTRY_64_PAGE_FRAME_NUMBER                                0xFFFFFFFFF000
    uint64_t reserved_1                                              : 4;
    uint64_t ignored_2                                               : 7;
#define PT_ENTRY_64_IGNORED_2                                        0x7F0000000000000
    uint64_t protection_key                                          : 4;
#define PT_ENTRY_64_PROTECTION_KEY                                   0x7800000000000000
    uint64_t execute_disable                                         : 1;
#define PT_ENTRY_64_EXECUTE_DISABLE                                  0x8000000000000000
  };

  uint64_t Flags;
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
#define SEGMENT_ACCESS_RIGHTS_TYPE                                   0xF00
    uint32_t descriptor_type                                         : 1;
#define SEGMENT_ACCESS_RIGHTS_DESCRIPTOR_TYPE                        0x1000
    uint32_t descriptor_privilege_level                              : 2;
#define SEGMENT_ACCESS_RIGHTS_DESCRIPTOR_PRIVILEGE_LEVEL             0x6000
    uint32_t present                                                 : 1;
#define SEGMENT_ACCESS_RIGHTS_PRESENT                                0x8000
    uint32_t reserved_2                                              : 4;
    uint32_t available_bit                                           : 1;
#define SEGMENT_ACCESS_RIGHTS_AVAILABLE_BIT                          0x100000
    uint32_t long_mode                                               : 1;
#define SEGMENT_ACCESS_RIGHTS_LONG_MODE                              0x200000
    uint32_t default_big                                             : 1;
#define SEGMENT_ACCESS_RIGHTS_DEFAULT_BIG                            0x400000
    uint32_t granularity                                             : 1;
#define SEGMENT_ACCESS_RIGHTS_GRANULARITY                            0x800000
    uint32_t reserved_3                                              : 8;
  };

  uint32_t Flags;
} segment_access_rights;

typedef struct {
  uint16_t segment_limit_low;
  uint16_t base_address_low;
  union {
    struct {
      uint32_t base_address_middle                                   : 8;
#define SEGMENT__BASE_ADDRESS_MIDDLE                                 0xFF
      uint32_t type                                                  : 4;
#define SEGMENT__TYPE                                                0xF00
      uint32_t descriptor_type                                       : 1;
#define SEGMENT__DESCRIPTOR_TYPE                                     0x1000
      uint32_t descriptor_privilege_level                            : 2;
#define SEGMENT__DESCRIPTOR_PRIVILEGE_LEVEL                          0x6000
      uint32_t present                                               : 1;
#define SEGMENT__PRESENT                                             0x8000
      uint32_t segment_limit_high                                    : 4;
#define SEGMENT__SEGMENT_LIMIT_HIGH                                  0xF0000
      uint32_t available_bit                                         : 1;
#define SEGMENT__AVAILABLE_BIT                                       0x100000
      uint32_t long_mode                                             : 1;
#define SEGMENT__LONG_MODE                                           0x200000
      uint32_t default_big                                           : 1;
#define SEGMENT__DEFAULT_BIG                                         0x400000
      uint32_t granularity                                           : 1;
#define SEGMENT__GRANULARITY                                         0x800000
      uint32_t base_address_high                                     : 8;
#define SEGMENT__BASE_ADDRESS_HIGH                                   0xFF000000
    };

    uint32_t Flags;
  } ;

} segment_descriptor_32;

typedef struct {
  uint16_t segment_limit_low;
  uint16_t base_address_low;
  union {
    struct {
      uint32_t base_address_middle                                   : 8;
#define SEGMENT__BASE_ADDRESS_MIDDLE                                 0xFF
      uint32_t type                                                  : 4;
#define SEGMENT__TYPE                                                0xF00
      uint32_t descriptor_type                                       : 1;
#define SEGMENT__DESCRIPTOR_TYPE                                     0x1000
      uint32_t descriptor_privilege_level                            : 2;
#define SEGMENT__DESCRIPTOR_PRIVILEGE_LEVEL                          0x6000
      uint32_t present                                               : 1;
#define SEGMENT__PRESENT                                             0x8000
      uint32_t segment_limit_high                                    : 4;
#define SEGMENT__SEGMENT_LIMIT_HIGH                                  0xF0000
      uint32_t available_bit                                         : 1;
#define SEGMENT__AVAILABLE_BIT                                       0x100000
      uint32_t long_mode                                             : 1;
#define SEGMENT__LONG_MODE                                           0x200000
      uint32_t default_big                                           : 1;
#define SEGMENT__DEFAULT_BIG                                         0x400000
      uint32_t granularity                                           : 1;
#define SEGMENT__GRANULARITY                                         0x800000
      uint32_t base_address_high                                     : 8;
#define SEGMENT__BASE_ADDRESS_HIGH                                   0xFF000000
    };

    uint32_t Flags;
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
#define SEGMENT_SELECTOR_REQUEST_PRIVILEGE_LEVEL                     0x03
    uint16_t table_indicator                                         : 1;
#define SEGMENT_SELECTOR_TABLE_INDICATOR                             0x04
    uint16_t index                                                   : 13;
#define SEGMENT_SELECTOR_INDEX                                       0xFFF8
  };

  uint16_t Flags;
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
#define VMX_EXIT_QUALIFICATION_DEBUG_EXCEPTION_BREAKPOINT_CONDITION  0x0F
    uint64_t reserved_1                                              : 9;
    uint64_t debug_register_access_detected                          : 1;
#define VMX_EXIT_QUALIFICATION_DEBUG_EXCEPTION_DEBUG_REGISTER_ACCESS_DETECTED 0x2000
    uint64_t single_instruction                                      : 1;
#define VMX_EXIT_QUALIFICATION_DEBUG_EXCEPTION_SINGLE_INSTRUCTION    0x4000
    uint64_t reserved_2                                              : 49;
  };

  uint64_t Flags;
} vmx_exit_qualification_debug_exception;

typedef union {
  struct {
    uint64_t selector                                                : 16;
#define VMX_EXIT_QUALIFICATION_TASK_SWITCH_SELECTOR                  0xFFFF
    uint64_t reserved_1                                              : 14;
    uint64_t type                                                    : 2;
#define VMX_EXIT_QUALIFICATION_TASK_SWITCH_TYPE                      0xC0000000
#define VMX_EXIT_QUALIFICATION_TYPE_CALL                             0x00000000
#define VMX_EXIT_QUALIFICATION_TYPE_IRET                             0x00000001
#define VMX_EXIT_QUALIFICATION_TYPE_JMP                              0x00000002
#define VMX_EXIT_QUALIFICATION_TYPE_IDT                              0x00000003
    uint64_t reserved_2                                              : 32;
  };

  uint64_t Flags;
} vmx_exit_qualification_task_switch;

typedef union {
  struct {
    uint64_t cr_number                                               : 4;
#define VMX_EXIT_QUALIFICATION_CR_ACCESS_CR_NUMBER                   0x0F
#define VMX_EXIT_QUALIFICATION_REGISTER_CR0                          0x00000000
#define VMX_EXIT_QUALIFICATION_REGISTER_CR2                          0x00000002
#define VMX_EXIT_QUALIFICATION_REGISTER_CR3                          0x00000003
#define VMX_EXIT_QUALIFICATION_REGISTER_CR4                          0x00000004
#define VMX_EXIT_QUALIFICATION_REGISTER_CR8                          0x00000008
    uint64_t access_type                                             : 2;
#define VMX_EXIT_QUALIFICATION_CR_ACCESS_ACCESS_TYPE                 0x30
#define VMX_EXIT_QUALIFICATION_ACCESS_MOV_TO_CR                      0x00000000
#define VMX_EXIT_QUALIFICATION_ACCESS_MOV_FROM_CR                    0x00000001
#define VMX_EXIT_QUALIFICATION_ACCESS_CLTS                           0x00000002
#define VMX_EXIT_QUALIFICATION_ACCESS_LMSW                           0x00000003
    uint64_t lmsw_operand_type                                       : 1;
#define VMX_EXIT_QUALIFICATION_CR_ACCESS_LMSW_OPERAND_TYPE           0x40
#define VMX_EXIT_QUALIFICATION_LMSW_OP_REGISTER                      0x00000000
#define VMX_EXIT_QUALIFICATION_LMSW_OP_MEMORY                        0x00000001
    uint64_t reserved_1                                              : 1;
    uint64_t gp_register                                             : 4;
#define VMX_EXIT_QUALIFICATION_CR_ACCESS_GP_REGISTER                 0xF00
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
#define VMX_EXIT_QUALIFICATION_CR_ACCESS_LMSW_SOURCE_DATA            0xFFFF0000
    uint64_t reserved_3                                              : 32;
  };

  uint64_t Flags;
} vmx_exit_qualification_cr_access;

typedef union {
  struct {
    uint64_t dr_number                                               : 3;
#define VMX_EXIT_QUALIFICATION_DR_ACCESS_DR_NUMBER                   0x07
#define VMX_EXIT_QUALIFICATION_REGISTER_DR0                          0x00000000
#define VMX_EXIT_QUALIFICATION_REGISTER_DR1                          0x00000001
#define VMX_EXIT_QUALIFICATION_REGISTER_DR2                          0x00000002
#define VMX_EXIT_QUALIFICATION_REGISTER_DR3                          0x00000003
#define VMX_EXIT_QUALIFICATION_REGISTER_DR6                          0x00000006
#define VMX_EXIT_QUALIFICATION_REGISTER_DR7                          0x00000007
    uint64_t reserved_1                                              : 1;
    uint64_t direction_of_access                                     : 1;
#define VMX_EXIT_QUALIFICATION_DR_ACCESS_DIRECTION_OF_ACCESS         0x10
#define VMX_EXIT_QUALIFICATION_DIRECTION_MOV_TO_DR                   0x00000000
#define VMX_EXIT_QUALIFICATION_DIRECTION_MOV_FROM_DR                 0x00000001
    uint64_t reserved_2                                              : 3;
    uint64_t gp_register                                             : 4;
#define VMX_EXIT_QUALIFICATION_DR_ACCESS_GP_REGISTER                 0xF00
    uint64_t reserved_3                                              : 52;
  };

  uint64_t Flags;
} vmx_exit_qualification_dr_access;

typedef union {
  struct {
    uint64_t size_of_access                                          : 3;
#define VMX_EXIT_QUALIFICATION_IO_INST_SIZE_OF_ACCESS                0x07
#define VMX_EXIT_QUALIFICATION_WIDTH_1B                              0x00000000
#define VMX_EXIT_QUALIFICATION_WIDTH_2B                              0x00000001
#define VMX_EXIT_QUALIFICATION_WIDTH_4B                              0x00000003
    uint64_t direction_of_access                                     : 1;
#define VMX_EXIT_QUALIFICATION_IO_INST_DIRECTION_OF_ACCESS           0x08
#define VMX_EXIT_QUALIFICATION_DIRECTION_OUT                         0x00000000
#define VMX_EXIT_QUALIFICATION_DIRECTION_IN                          0x00000001
    uint64_t string_instruction                                      : 1;
#define VMX_EXIT_QUALIFICATION_IO_INST_STRING_INSTRUCTION            0x10
#define VMX_EXIT_QUALIFICATION_IS_STRING_NOT_STRING                  0x00000000
#define VMX_EXIT_QUALIFICATION_IS_STRING_STRING                      0x00000001
    uint64_t rep_prefixed                                            : 1;
#define VMX_EXIT_QUALIFICATION_IO_INST_REP_PREFIXED                  0x20
#define VMX_EXIT_QUALIFICATION_IS_REP_NOT_REP                        0x00000000
#define VMX_EXIT_QUALIFICATION_IS_REP_REP                            0x00000001
    uint64_t operand_encoding                                        : 1;
#define VMX_EXIT_QUALIFICATION_IO_INST_OPERAND_ENCODING              0x40
#define VMX_EXIT_QUALIFICATION_ENCODING_DX                           0x00000000
#define VMX_EXIT_QUALIFICATION_ENCODING_IMM                          0x00000001
    uint64_t reserved_1                                              : 9;
    uint64_t port_number                                             : 16;
#define VMX_EXIT_QUALIFICATION_IO_INST_PORT_NUMBER                   0xFFFF0000
    uint64_t reserved_2                                              : 32;
  };

  uint64_t Flags;
} vmx_exit_qualification_io_inst;

typedef union {
  struct {
    uint64_t page_offset                                             : 12;
#define VMX_EXIT_QUALIFICATION_APIC_ACCESS_PAGE_OFFSET               0xFFF
    uint64_t access_type                                             : 4;
#define VMX_EXIT_QUALIFICATION_APIC_ACCESS_ACCESS_TYPE               0xF000
#define VMX_EXIT_QUALIFICATION_TYPE_LINEAR_READ                      0x00000000
#define VMX_EXIT_QUALIFICATION_TYPE_LINEAR_WRITE                     0x00000001
#define VMX_EXIT_QUALIFICATION_TYPE_LINEAR_INSTR_FETCH               0x00000002
#define VMX_EXIT_QUALIFICATION_TYPE_LINEAR_EVENT_DELIVERY            0x00000003
#define VMX_EXIT_QUALIFICATION_TYPE_PHYSICAL_EVENT_DELIVERY          0x0000000A
#define VMX_EXIT_QUALIFICATION_TYPE_PHYSICAL_INSTR                   0x0000000F
    uint64_t reserved_1                                              : 48;
  };

  uint64_t Flags;
} vmx_exit_qualification_apic_access;

typedef union {
  struct {
    uint64_t data_read                                               : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_DATA_READ               0x01
    uint64_t data_write                                              : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_DATA_WRITE              0x02
    uint64_t instruction_fetch                                       : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_INSTRUCTION_FETCH       0x04
    uint64_t entry_present                                           : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_ENTRY_PRESENT           0x08
    uint64_t entry_write                                             : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_ENTRY_WRITE             0x10
    uint64_t entry_execute                                           : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_ENTRY_EXECUTE           0x20
    uint64_t entry_execute_for_user_mode                             : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_ENTRY_EXECUTE_FOR_USER_MODE 0x40
    uint64_t valid_guest_linear_address                              : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_VALID_GUEST_LINEAR_ADDRESS 0x80
    uint64_t ept_translated_access                                   : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_EPT_TRANSLATED_ACCESS   0x100
    uint64_t user_mode_linear_address                                : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_USER_MODE_LINEAR_ADDRESS 0x200
    uint64_t readable_writable_page                                  : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_READABLE_WRITABLE_PAGE  0x400
    uint64_t execute_disable_page                                    : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_EXECUTE_DISABLE_PAGE    0x800
    uint64_t nmi_unblocking                                          : 1;
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_NMI_UNBLOCKING          0x1000
    uint64_t reserved_1                                              : 51;
  };

  uint64_t Flags;
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
#define VMX_VMEXIT_INSTRUCTION_INFO_INS_OUTS_ADDRESS_SIZE            0x380
    uint64_t reserved_2                                              : 5;
    uint64_t segment_register                                        : 3;
#define VMX_VMEXIT_INSTRUCTION_INFO_INS_OUTS_SEGMENT_REGISTER        0x38000
    uint64_t reserved_3                                              : 46;
  };

  uint64_t Flags;
} vmx_vmexit_instruction_info_ins_outs;

typedef union {
  struct {
    uint64_t scaling                                                 : 2;
#define VMX_VMEXIT_INSTRUCTION_INFO_INVALIDATE_SCALING               0x03
    uint64_t reserved_1                                              : 5;
    uint64_t address_size                                            : 3;
#define VMX_VMEXIT_INSTRUCTION_INFO_INVALIDATE_ADDRESS_SIZE          0x380
    uint64_t reserved_2                                              : 5;
    uint64_t segment_register                                        : 3;
#define VMX_VMEXIT_INSTRUCTION_INFO_INVALIDATE_SEGMENT_REGISTER      0x38000
    uint64_t gp_register                                             : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_INVALIDATE_GP_REGISTER           0x3C0000
    uint64_t gp_register_invalid                                     : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_INVALIDATE_GP_REGISTER_INVALID   0x400000
    uint64_t base_register                                           : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_INVALIDATE_BASE_REGISTER         0x7800000
    uint64_t base_register_invalid                                   : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_INVALIDATE_BASE_REGISTER_INVALID 0x8000000
    uint64_t register_2                                              : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_INVALIDATE_REGISTER_2            0xF0000000
    uint64_t reserved_3                                              : 32;
  };

  uint64_t Flags;
} vmx_vmexit_instruction_info_invalidate;

typedef union {
  struct {
    uint64_t scaling                                                 : 2;
#define VMX_VMEXIT_INSTRUCTION_INFO_GDTR_IDTR_ACCESS_SCALING         0x03
    uint64_t reserved_1                                              : 5;
    uint64_t address_size                                            : 3;
#define VMX_VMEXIT_INSTRUCTION_INFO_GDTR_IDTR_ACCESS_ADDRESS_SIZE    0x380
    uint64_t reserved_2                                              : 1;
    uint64_t operand_size                                            : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_GDTR_IDTR_ACCESS_OPERAND_SIZE    0x800
    uint64_t reserved_3                                              : 3;
    uint64_t segment_register                                        : 3;
#define VMX_VMEXIT_INSTRUCTION_INFO_GDTR_IDTR_ACCESS_SEGMENT_REGISTER 0x38000
    uint64_t gp_register                                             : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_GDTR_IDTR_ACCESS_GP_REGISTER     0x3C0000
    uint64_t gp_register_invalid                                     : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_GDTR_IDTR_ACCESS_GP_REGISTER_INVALID 0x400000
    uint64_t base_register                                           : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_GDTR_IDTR_ACCESS_BASE_REGISTER   0x7800000
    uint64_t base_register_invalid                                   : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_GDTR_IDTR_ACCESS_BASE_REGISTER_INVALID 0x8000000
    uint64_t instruction_identity                                    : 2;
#define VMX_VMEXIT_INSTRUCTION_INFO_GDTR_IDTR_ACCESS_INSTRUCTION_IDENTITY 0x30000000
    uint64_t reserved_4                                              : 34;
  };

  uint64_t Flags;
} vmx_vmexit_instruction_info_gdtr_idtr_access;

typedef union {
  struct {
    uint64_t scaling                                                 : 2;
#define VMX_VMEXIT_INSTRUCTION_INFO_LDTR_TR_ACCESS_SCALING           0x03
    uint64_t reserved_1                                              : 1;
    uint64_t reg_1                                                   : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_LDTR_TR_ACCESS_REG_1             0x78
    uint64_t address_size                                            : 3;
#define VMX_VMEXIT_INSTRUCTION_INFO_LDTR_TR_ACCESS_ADDRESS_SIZE      0x380
    uint64_t memory_register                                         : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_LDTR_TR_ACCESS_MEMORY_REGISTER   0x400
    uint64_t reserved_2                                              : 4;
    uint64_t segment_register                                        : 3;
#define VMX_VMEXIT_INSTRUCTION_INFO_LDTR_TR_ACCESS_SEGMENT_REGISTER  0x38000
    uint64_t gp_register                                             : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_LDTR_TR_ACCESS_GP_REGISTER       0x3C0000
    uint64_t gp_register_invalid                                     : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_LDTR_TR_ACCESS_GP_REGISTER_INVALID 0x400000
    uint64_t base_register                                           : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_LDTR_TR_ACCESS_BASE_REGISTER     0x7800000
    uint64_t base_register_invalid                                   : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_LDTR_TR_ACCESS_BASE_REGISTER_INVALID 0x8000000
    uint64_t instruction_identity                                    : 2;
#define VMX_VMEXIT_INSTRUCTION_INFO_LDTR_TR_ACCESS_INSTRUCTION_IDENTITY 0x30000000
    uint64_t reserved_3                                              : 34;
  };

  uint64_t Flags;
} vmx_vmexit_instruction_info_ldtr_tr_access;

typedef union {
  struct {
    uint64_t reserved_1                                              : 3;
    uint64_t destination_register                                    : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_RDRAND_RDSEED_DESTINATION_REGISTER 0x78
    uint64_t reserved_2                                              : 4;
    uint64_t operand_size                                            : 2;
#define VMX_VMEXIT_INSTRUCTION_INFO_RDRAND_RDSEED_OPERAND_SIZE       0x1800
    uint64_t reserved_3                                              : 51;
  };

  uint64_t Flags;
} vmx_vmexit_instruction_info_rdrand_rdseed;

typedef union {
  struct {
    uint64_t scaling                                                 : 2;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMX_AND_XSAVES_SCALING           0x03
    uint64_t reserved_1                                              : 5;
    uint64_t address_size                                            : 3;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMX_AND_XSAVES_ADDRESS_SIZE      0x380
    uint64_t reserved_2                                              : 5;
    uint64_t segment_register                                        : 3;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMX_AND_XSAVES_SEGMENT_REGISTER  0x38000
    uint64_t gp_register                                             : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMX_AND_XSAVES_GP_REGISTER       0x3C0000
    uint64_t gp_register_invalid                                     : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMX_AND_XSAVES_GP_REGISTER_INVALID 0x400000
    uint64_t base_register                                           : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMX_AND_XSAVES_BASE_REGISTER     0x7800000
    uint64_t base_register_invalid                                   : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMX_AND_XSAVES_BASE_REGISTER_INVALID 0x8000000
    uint64_t reserved_3                                              : 36;
  };

  uint64_t Flags;
} vmx_vmexit_instruction_info_vmx_and_xsaves;

typedef union {
  struct {
    uint64_t scaling                                                 : 2;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMREAD_VMWRITE_SCALING           0x03
    uint64_t reserved_1                                              : 1;
    uint64_t register_1                                              : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMREAD_VMWRITE_REGISTER_1        0x78
    uint64_t address_size                                            : 3;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMREAD_VMWRITE_ADDRESS_SIZE      0x380
    uint64_t memory_register                                         : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMREAD_VMWRITE_MEMORY_REGISTER   0x400
    uint64_t reserved_2                                              : 4;
    uint64_t segment_register                                        : 3;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMREAD_VMWRITE_SEGMENT_REGISTER  0x38000
    uint64_t gp_register                                             : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMREAD_VMWRITE_GP_REGISTER       0x3C0000
    uint64_t gp_register_invalid                                     : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMREAD_VMWRITE_GP_REGISTER_INVALID 0x400000
    uint64_t base_register                                           : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMREAD_VMWRITE_BASE_REGISTER     0x7800000
    uint64_t base_register_invalid                                   : 1;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMREAD_VMWRITE_BASE_REGISTER_INVALID 0x8000000
    uint64_t register_2                                              : 4;
#define VMX_VMEXIT_INSTRUCTION_INFO_VMREAD_VMWRITE_REGISTER_2        0xF0000000
    uint64_t reserved_3                                              : 32;
  };

  uint64_t Flags;
} vmx_vmexit_instruction_info_vmread_vmwrite;

/**
 * @}
 */

typedef union {
  struct {
    uint32_t type                                                    : 4;
#define VMX_SEGMENT_ACCESS_RIGHTS_TYPE                               0x0F
    uint32_t descriptor_type                                         : 1;
#define VMX_SEGMENT_ACCESS_RIGHTS_DESCRIPTOR_TYPE                    0x10
    uint32_t descriptor_privilege_level                              : 2;
#define VMX_SEGMENT_ACCESS_RIGHTS_DESCRIPTOR_PRIVILEGE_LEVEL         0x60
    uint32_t present                                                 : 1;
#define VMX_SEGMENT_ACCESS_RIGHTS_PRESENT                            0x80
    uint32_t reserved_1                                              : 4;
    uint32_t available_bit                                           : 1;
#define VMX_SEGMENT_ACCESS_RIGHTS_AVAILABLE_BIT                      0x1000
    uint32_t long_mode                                               : 1;
#define VMX_SEGMENT_ACCESS_RIGHTS_LONG_MODE                          0x2000
    uint32_t default_big                                             : 1;
#define VMX_SEGMENT_ACCESS_RIGHTS_DEFAULT_BIG                        0x4000
    uint32_t granularity                                             : 1;
#define VMX_SEGMENT_ACCESS_RIGHTS_GRANULARITY                        0x8000
    uint32_t unusable                                                : 1;
#define VMX_SEGMENT_ACCESS_RIGHTS_UNUSABLE                           0x10000
    uint32_t reserved_2                                              : 15;
  };

  uint32_t Flags;
} vmx_segment_access_rights;

typedef union {
  struct {
    uint32_t blocking_by_sti                                         : 1;
#define VMX_INTERRUPTIBILITY_STATE_BLOCKING_BY_STI                   0x01
    uint32_t blocking_by_mov_ss                                      : 1;
#define VMX_INTERRUPTIBILITY_STATE_BLOCKING_BY_MOV_SS                0x02
    uint32_t blocking_by_smi                                         : 1;
#define VMX_INTERRUPTIBILITY_STATE_BLOCKING_BY_SMI                   0x04
    uint32_t blocking_by_nmi                                         : 1;
#define VMX_INTERRUPTIBILITY_STATE_BLOCKING_BY_NMI                   0x08
    uint32_t enclave_interruption                                    : 1;
#define VMX_INTERRUPTIBILITY_STATE_ENCLAVE_INTERRUPTION              0x10
    uint32_t reserved_1                                              : 27;
  };

  uint32_t Flags;
} vmx_interruptibility_state;

#define VMX_ACTIVE                                                   0x00000000
#define VMX_HLT                                                      0x00000001
#define VMX_SHUTDOWN                                                 0x00000002
#define VMX_WAIT_FOR_SIPI                                            0x00000003
/**
 * @}
 */

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
#define EPTP_MEMORY_TYPE                                             0x07
    uint64_t page_walk_length                                        : 3;
#define EPTP_PAGE_WALK_LENGTH                                        0x38
#define EPT_PAGE_WALK_LENGTH_4                                       0x00000003
    uint64_t enable_access_and_dirty_flags                           : 1;
#define EPTP_ENABLE_ACCESS_AND_DIRTY_FLAGS                           0x40
    uint64_t reserved_1                                              : 5;
    uint64_t page_frame_number                                       : 36;
#define EPTP_PAGE_FRAME_NUMBER                                       0xFFFFFFFFF000
    uint64_t reserved_2                                              : 16;
  };

  uint64_t Flags;
} eptp;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
#define EPML4E_READ_ACCESS                                           0x01
    uint64_t write_access                                            : 1;
#define EPML4E_WRITE_ACCESS                                          0x02
    uint64_t execute_access                                          : 1;
#define EPML4E_EXECUTE_ACCESS                                        0x04
    uint64_t reserved_1                                              : 5;
    uint64_t accessed                                                : 1;
#define EPML4E_ACCESSED                                              0x100
    uint64_t reserved_2                                              : 1;
    uint64_t user_mode_execute                                       : 1;
#define EPML4E_USER_MODE_EXECUTE                                     0x400
    uint64_t reserved_3                                              : 1;
    uint64_t page_frame_number                                       : 36;
#define EPML4E_PAGE_FRAME_NUMBER                                     0xFFFFFFFFF000
    uint64_t reserved_4                                              : 16;
  };

  uint64_t Flags;
} epml4e;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
#define EPT_PDPTE_1GB_READ_ACCESS                                    0x01
    uint64_t write_access                                            : 1;
#define EPT_PDPTE_1GB_WRITE_ACCESS                                   0x02
    uint64_t execute_access                                          : 1;
#define EPT_PDPTE_1GB_EXECUTE_ACCESS                                 0x04
    uint64_t memory_type                                             : 3;
#define EPT_PDPTE_1GB_MEMORY_TYPE                                    0x38
    uint64_t ignore_pat                                              : 1;
#define EPT_PDPTE_1GB_IGNORE_PAT                                     0x40
    uint64_t large_page                                              : 1;
#define EPT_PDPTE_1GB_LARGE_PAGE                                     0x80
    uint64_t accessed                                                : 1;
#define EPT_PDPTE_1GB_ACCESSED                                       0x100
    uint64_t dirty                                                   : 1;
#define EPT_PDPTE_1GB_DIRTY                                          0x200
    uint64_t user_mode_execute                                       : 1;
#define EPT_PDPTE_1GB_USER_MODE_EXECUTE                              0x400
    uint64_t reserved_1                                              : 19;
    uint64_t page_frame_number                                       : 18;
#define EPT_PDPTE_1GB_PAGE_FRAME_NUMBER                              0xFFFFC0000000
    uint64_t reserved_2                                              : 15;
    uint64_t suppress_ve                                             : 1;
#define EPT_PDPTE_1GB_SUPPRESS_VE                                    0x8000000000000000
  };

  uint64_t Flags;
} ept_pdpte_1gb;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
#define EPT_PDPTE_READ_ACCESS                                        0x01
    uint64_t write_access                                            : 1;
#define EPT_PDPTE_WRITE_ACCESS                                       0x02
    uint64_t execute_access                                          : 1;
#define EPT_PDPTE_EXECUTE_ACCESS                                     0x04
    uint64_t reserved_1                                              : 5;
    uint64_t accessed                                                : 1;
#define EPT_PDPTE_ACCESSED                                           0x100
    uint64_t reserved_2                                              : 1;
    uint64_t user_mode_execute                                       : 1;
#define EPT_PDPTE_USER_MODE_EXECUTE                                  0x400
    uint64_t reserved_3                                              : 1;
    uint64_t page_frame_number                                       : 36;
#define EPT_PDPTE_PAGE_FRAME_NUMBER                                  0xFFFFFFFFF000
    uint64_t reserved_4                                              : 16;
  };

  uint64_t Flags;
} ept_pdpte;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
#define EPT_PDE_2MB_READ_ACCESS                                      0x01
    uint64_t write_access                                            : 1;
#define EPT_PDE_2MB_WRITE_ACCESS                                     0x02
    uint64_t execute_access                                          : 1;
#define EPT_PDE_2MB_EXECUTE_ACCESS                                   0x04
    uint64_t memory_type                                             : 3;
#define EPT_PDE_2MB_MEMORY_TYPE                                      0x38
    uint64_t ignore_pat                                              : 1;
#define EPT_PDE_2MB_IGNORE_PAT                                       0x40
    uint64_t large_page                                              : 1;
#define EPT_PDE_2MB_LARGE_PAGE                                       0x80
    uint64_t accessed                                                : 1;
#define EPT_PDE_2MB_ACCESSED                                         0x100
    uint64_t dirty                                                   : 1;
#define EPT_PDE_2MB_DIRTY                                            0x200
    uint64_t user_mode_execute                                       : 1;
#define EPT_PDE_2MB_USER_MODE_EXECUTE                                0x400
    uint64_t reserved_1                                              : 10;
    uint64_t page_frame_number                                       : 27;
#define EPT_PDE_2MB_PAGE_FRAME_NUMBER                                0xFFFFFFE00000
    uint64_t reserved_2                                              : 15;
    uint64_t suppress_ve                                             : 1;
#define EPT_PDE_2MB_SUPPRESS_VE                                      0x8000000000000000
  };

  uint64_t Flags;
} ept_pde_2mb;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
#define EPT_PDE_READ_ACCESS                                          0x01
    uint64_t write_access                                            : 1;
#define EPT_PDE_WRITE_ACCESS                                         0x02
    uint64_t execute_access                                          : 1;
#define EPT_PDE_EXECUTE_ACCESS                                       0x04
    uint64_t reserved_1                                              : 5;
    uint64_t accessed                                                : 1;
#define EPT_PDE_ACCESSED                                             0x100
    uint64_t reserved_2                                              : 1;
    uint64_t user_mode_execute                                       : 1;
#define EPT_PDE_USER_MODE_EXECUTE                                    0x400
    uint64_t reserved_3                                              : 1;
    uint64_t page_frame_number                                       : 36;
#define EPT_PDE_PAGE_FRAME_NUMBER                                    0xFFFFFFFFF000
    uint64_t reserved_4                                              : 16;
  };

  uint64_t Flags;
} ept_pde;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
#define EPT_PTE_READ_ACCESS                                          0x01
    uint64_t write_access                                            : 1;
#define EPT_PTE_WRITE_ACCESS                                         0x02
    uint64_t execute_access                                          : 1;
#define EPT_PTE_EXECUTE_ACCESS                                       0x04
    uint64_t memory_type                                             : 3;
#define EPT_PTE_MEMORY_TYPE                                          0x38
    uint64_t ignore_pat                                              : 1;
#define EPT_PTE_IGNORE_PAT                                           0x40
    uint64_t reserved_1                                              : 1;
    uint64_t accessed                                                : 1;
#define EPT_PTE_ACCESSED                                             0x100
    uint64_t dirty                                                   : 1;
#define EPT_PTE_DIRTY                                                0x200
    uint64_t user_mode_execute                                       : 1;
#define EPT_PTE_USER_MODE_EXECUTE                                    0x400
    uint64_t reserved_2                                              : 1;
    uint64_t page_frame_number                                       : 36;
#define EPT_PTE_PAGE_FRAME_NUMBER                                    0xFFFFFFFFF000
    uint64_t reserved_3                                              : 15;
    uint64_t suppress_ve                                             : 1;
#define EPT_PTE_SUPPRESS_VE                                          0x8000000000000000
  };

  uint64_t Flags;
} ept_pte;

typedef union {
  struct {
    uint64_t read_access                                             : 1;
#define EPT_ENTRY_READ_ACCESS                                        0x01
    uint64_t write_access                                            : 1;
#define EPT_ENTRY_WRITE_ACCESS                                       0x02
    uint64_t execute_access                                          : 1;
#define EPT_ENTRY_EXECUTE_ACCESS                                     0x04
    uint64_t memory_type                                             : 3;
#define EPT_ENTRY_MEMORY_TYPE                                        0x38
    uint64_t ignore_pat                                              : 1;
#define EPT_ENTRY_IGNORE_PAT                                         0x40
    uint64_t large_page                                              : 1;
#define EPT_ENTRY_LARGE_PAGE                                         0x80
    uint64_t accessed                                                : 1;
#define EPT_ENTRY_ACCESSED                                           0x100
    uint64_t dirty                                                   : 1;
#define EPT_ENTRY_DIRTY                                              0x200
    uint64_t user_mode_execute                                       : 1;
#define EPT_ENTRY_USER_MODE_EXECUTE                                  0x400
    uint64_t reserved_1                                              : 1;
    uint64_t page_frame_number                                       : 36;
#define EPT_ENTRY_PAGE_FRAME_NUMBER                                  0xFFFFFFFFF000
    uint64_t reserved_2                                              : 15;
    uint64_t suppress_ve                                             : 1;
#define EPT_ENTRY_SUPPRESS_VE                                        0x8000000000000000
  };

  uint64_t Flags;
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

#define INVEPT_SINGLE_CONTEXT                                        0x00000001
#define INVEPT_ALL_CONTEXT                                           0x00000002
/**
 * @}
 */

#define INVVPID_INDIVIDUAL_ADDRESS                                   0x00000000
#define INVVPID_SINGLE_CONTEXT                                       0x00000001
#define INVVPID_ALL_CONTEXT                                          0x00000002
#define INVVPID_SINGLE_CONTEXT_RETAINING_GLOBALS                     0x00000003
/**
 * @}
 */

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
#define VMCS_COMPONENT_ENCODING_ACCESS_TYPE                          0x01
    uint16_t index                                                   : 9;
#define VMCS_COMPONENT_ENCODING_INDEX                                0x3FE
    uint16_t type                                                    : 2;
#define VMCS_COMPONENT_ENCODING_TYPE                                 0xC00
    uint16_t must_be_zero                                            : 1;
#define VMCS_COMPONENT_ENCODING_MUST_BE_ZERO                         0x1000
    uint16_t width                                                   : 2;
#define VMCS_COMPONENT_ENCODING_WIDTH                                0x6000
    uint16_t reserved_1                                              : 1;
  };

  uint16_t Flags;
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

#define EXTERNAL_INTERRUPT                                           0x00000000
#define NON_MASKABLE_INTERRUPT                                       0x00000002
#define HARDWARE_EXCEPTION                                           0x00000003
#define SOFTWARE_INTERRUPT                                           0x00000004
#define PRIVILEGED_SOFTWARE_EXCEPTION                                0x00000005
#define SOFTWARE_EXCEPTION                                           0x00000006
#define OTHER_EVENT                                                  0x00000007
/**
 * @}
 */

typedef union {
  struct {
    uint32_t vector                                                  : 8;
#define VMENTRY_INTERRUPT_INFO_VECTOR                                0xFF
    uint32_t interruption_type                                       : 3;
#define VMENTRY_INTERRUPT_INFO_INTERRUPTION_TYPE                     0x700
    uint32_t deliver_error_code                                      : 1;
#define VMENTRY_INTERRUPT_INFO_DELIVER_ERROR_CODE                    0x800
    uint32_t reserved_1                                              : 19;
    uint32_t valid                                                   : 1;
#define VMENTRY_INTERRUPT_INFO_VALID                                 0x80000000
  };

  uint32_t Flags;
} vmentry_interrupt_info;

typedef union {
  struct {
    uint32_t vector                                                  : 8;
#define VMEXIT_INTERRUPT_INFO_VECTOR                                 0xFF
    uint32_t interruption_type                                       : 3;
#define VMEXIT_INTERRUPT_INFO_INTERRUPTION_TYPE                      0x700
    uint32_t error_code_valid                                        : 1;
#define VMEXIT_INTERRUPT_INFO_ERROR_CODE_VALID                       0x800
    uint32_t nmi_unblocking                                          : 1;
#define VMEXIT_INTERRUPT_INFO_NMI_UNBLOCKING                         0x1000
    uint32_t reserved_1                                              : 18;
    uint32_t valid                                                   : 1;
#define VMEXIT_INTERRUPT_INFO_VALID                                  0x80000000
  };

  uint32_t Flags;
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
#define EFL_CARRY_FLAG                                               0x01
    uint32_t read_as_1                                               : 1;
#define EFL_READ_AS_1                                                0x02
    uint32_t parity_flag                                             : 1;
#define EFL_PARITY_FLAG                                              0x04
    uint32_t reserved_1                                              : 1;
    uint32_t auxiliary_carry_flag                                    : 1;
#define EFL_AUXILIARY_CARRY_FLAG                                     0x10
    uint32_t reserved_2                                              : 1;
    uint32_t zero_flag                                               : 1;
#define EFL_ZERO_FLAG                                                0x40
    uint32_t sign_flag                                               : 1;
#define EFL_SIGN_FLAG                                                0x80
    uint32_t trap_flag                                               : 1;
#define EFL_TRAP_FLAG                                                0x100
    uint32_t interrupt_enable_flag                                   : 1;
#define EFL_INTERRUPT_ENABLE_FLAG                                    0x200
    uint32_t direction_flag                                          : 1;
#define EFL_DIRECTION_FLAG                                           0x400
    uint32_t overflow_flag                                           : 1;
#define EFL_OVERFLOW_FLAG                                            0x800
    uint32_t io_privilege_level                                      : 2;
#define EFL_IO_PRIVILEGE_LEVEL                                       0x3000
    uint32_t nested_task_flag                                        : 1;
#define EFL_NESTED_TASK_FLAG                                         0x4000
    uint32_t reserved_3                                              : 1;
    uint32_t resume_flag                                             : 1;
#define EFL_RESUME_FLAG                                              0x10000
    uint32_t virtual_8086_mode_flag                                  : 1;
#define EFL_VIRTUAL_8086_MODE_FLAG                                   0x20000
    uint32_t alignment_check_flag                                    : 1;
#define EFL_ALIGNMENT_CHECK_FLAG                                     0x40000
    uint32_t virtual_interrupt_flag                                  : 1;
#define EFL_VIRTUAL_INTERRUPT_FLAG                                   0x80000
    uint32_t virtual_interrupt_pending_flag                          : 1;
#define EFL_VIRTUAL_INTERRUPT_PENDING_FLAG                           0x100000
    uint32_t identification_flag                                     : 1;
#define EFL_IDENTIFICATION_FLAG                                      0x200000
    uint32_t reserved_4                                              : 10;
  };

  uint32_t Flags;
} efl;

/**
 * @defgroup exceptions \
 *           Exceptions
 * @{
 */
#define DIVIDE_ERROR                                                 0x00000000
#define DEBUG                                                        0x00000001
#define BREAKPOINT                                                   0x00000003
#define OVERFLOW                                                     0x00000004
#define BOUND_RANGE_EXCEEDED                                         0x00000005
#define INVALID_OPCODE                                               0x00000006
#define DEVICE_NOT_AVAILABLE                                         0x00000007
#define DOUBLE_FAULT                                                 0x00000008
#define COPROCESSOR_SEGMENT_OVERRUN                                  0x00000009
#define INVALID_TSS                                                  0x0000000A
#define SEGMENT_NOT_PRESENT                                          0x0000000B
#define STACK_SEGMENT_FAULT                                          0x0000000C
#define GENERAL_PROTECTION                                           0x0000000D
#define PAGE_FAULT                                                   0x0000000E
#define X87_FLOATING_POINT_ERROR                                     0x00000010
#define ALIGNMENT_CHECK                                              0x00000011
#define MACHINE_CHECK                                                0x00000012
#define SIMD_FLOATING_POINT_ERROR                                    0x00000013
#define VIRTUALIZATION_EXCEPTION                                     0x00000014
/**
 * @}
 */

typedef union {
  struct {
    uint32_t external_event                                          : 1;
#define EXCEPTION_ERROR_CODE_EXTERNAL_EVENT                          0x01
    uint32_t descriptor_location                                     : 1;
#define EXCEPTION_ERROR_CODE_DESCRIPTOR_LOCATION                     0x02
    uint32_t gdt_ldt                                                 : 1;
#define EXCEPTION_ERROR_CODE_GDT_LDT                                 0x04
    uint32_t index                                                   : 13;
#define EXCEPTION_ERROR_CODE_INDEX                                   0xFFF8
    uint32_t reserved_1                                              : 16;
  };

  uint32_t Flags;
} exception_error_code;

typedef union {
  struct {
    uint32_t present                                                 : 1;
#define PAGE_FAULT_EXCEPTION_PRESENT                                 0x01
    uint32_t write                                                   : 1;
#define PAGE_FAULT_EXCEPTION_WRITE                                   0x02
    uint32_t user_mode_access                                        : 1;
#define PAGE_FAULT_EXCEPTION_USER_MODE_ACCESS                        0x04
    uint32_t reserved_bit_violation                                  : 1;
#define PAGE_FAULT_EXCEPTION_RESERVED_BIT_VIOLATION                  0x08
    uint32_t execute                                                 : 1;
#define PAGE_FAULT_EXCEPTION_EXECUTE                                 0x10
    uint32_t protection_key_violation                                : 1;
#define PAGE_FAULT_EXCEPTION_PROTECTION_KEY_VIOLATION                0x20
    uint32_t reserved_1                                              : 9;
    uint32_t sgx                                                     : 1;
#define PAGE_FAULT_EXCEPTION_SGX                                     0x8000
    uint32_t reserved_2                                              : 16;
  };

  uint32_t Flags;
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


