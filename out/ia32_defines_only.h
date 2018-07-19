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
#define CR0_PROTECTION_ENABLE                                        0x01
#define CR0_MONITOR_COPROCESSOR                                      0x02
#define CR0_EMULATE_FPU                                              0x04
#define CR0_TASK_SWITCHED                                            0x08
#define CR0_EXTENSION_TYPE                                           0x10
#define CR0_NUMERIC_ERROR                                            0x20
#define CR0_WRITE_PROTECT                                            0x10000
#define CR0_ALIGNMENT_MASK                                           0x40000
#define CR0_NOT_WRITE_THROUGH                                        0x20000000
#define CR0_CACHE_DISABLE                                            0x40000000
#define CR0_PAGING_ENABLE                                            0x80000000

#define CR3_PAGE_LEVEL_WRITE_THROUGH                                 0x08
#define CR3_PAGE_LEVEL_CACHE_DISABLE                                 0x10
#define CR3_ADDRESS_OF_PAGE_DIRECTORY                                0xFFFFFFFFF000

#define CR4_VIRTUAL_MODE_EXTENSIONS                                  0x01
#define CR4_PROTECTED_MODE_VIRTUAL_INTERRUPTS                        0x02
#define CR4_TIMESTAMP_DISABLE                                        0x04
#define CR4_DEBUGGING_EXTENSIONS                                     0x08
#define CR4_PAGE_SIZE_EXTENSIONS                                     0x10
#define CR4_PHYSICAL_ADDRESS_EXTENSION                               0x20
#define CR4_MACHINE_CHECK_ENABLE                                     0x40
#define CR4_PAGE_GLOBAL_ENABLE                                       0x80
#define CR4_PERFORMANCE_MONITORING_COUNTER_ENABLE                    0x100
#define CR4_OS_FXSAVE_FXRSTOR_SUPPORT                                0x200
#define CR4_OS_XMM_EXCEPTION_SUPPORT                                 0x400
#define CR4_USERMODE_INSTRUCTION_PREVENTION                          0x800
#define CR4_VMX_ENABLE                                               0x2000
#define CR4_SMX_ENABLE                                               0x4000
#define CR4_FSGSBASE_ENABLE                                          0x10000
#define CR4_PCID_ENABLE                                              0x20000
#define CR4_OS_XSAVE                                                 0x40000
#define CR4_SMEP_ENABLE                                              0x100000
#define CR4_SMAP_ENABLE                                              0x200000
#define CR4_PROTECTION_KEY_ENABLE                                    0x400000

#define CR8_TASK_PRIORITY_LEVEL                                      0x0F
#define CR8_RESERVED                                                 0xFFFFFFFFFFFFFFF0

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
  uint32_t eax;
  struct {
    uint8_t brand_index;
    uint8_t clflush_line_size;
    uint8_t max_addressable_ids;
    uint8_t initial_apic_id;
  } ebx;

  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_01;

#define CPUID_CACHE_PARAMS                                           0x00000004
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_04;

#define CPUID_MONITOR_MWAIT                                          0x00000005
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_05;

#define CPUID_THERMAL_POWER_MANAGEMENT                               0x00000006
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_06;

#define CPUID_STRUCTURED_EXTENDED_FEATURE_FLAGS                      0x00000007
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_07;

#define CPUID_DIRECT_CACHE_ACCESS_INFO                               0x00000009
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_09;

#define CPUID_ARCHITECTURAL_PERFORMANCE_MONITORING                   0x0000000A
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_0a;

#define CPUID_EXTENDED_TOPOLOGY                                      0x0000000B
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_0b;

/**
 * @defgroup cpuid_eax_0d \
 *           EAX = 0x0D
 * @{
 */
#define CPUID_EXTENDED_STATE                                         0x0000000D
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_0d_ecx_00;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_0d_ecx_01;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
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
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_0f_ecx_00;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
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
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_10_ecx_00;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_10_ecx_01;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_10_ecx_02;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
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
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_12_ecx_00;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_12_ecx_01;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_12_ecx_02p_slt_0;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
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
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_14_ecx_00;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_14_ecx_01;

/**
 * @}
 */

#define CPUID_TIME_STAMP_COUNTER                                     0x00000015
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_15;

#define CPUID_PROCESSOR_FREQUENCY                                    0x00000016
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_16;

/**
 * @defgroup cpuid_eax_17 \
 *           EAX = 0x17
 * @{
 */
#define CPUID_SOC_VENDOR                                             0x00000017
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_17_ecx_00;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_17_ecx_01_03;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
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
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_18_ecx_00;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_18_ecx_01p;

/**
 * @}
 */

#define CPUID_EXTENDED_FUNCTION                                      0x80000000
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_80000000;

#define CPUID_EXTENDED_CPU_SIGNATURE                                 0x80000001
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_80000001;

#define CPUID_BRAND_STRING1                                          0x80000002
#define CPUID_BRAND_STRING2                                          0x80000003
#define CPUID_BRAND_STRING3                                          0x80000004
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_80000002;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_80000003;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_80000004;

typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_80000005;

#define CPUID_EXTENDED_CACHE_INFO                                    0x80000006
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
} cpuid_eax_80000006;

#define CPUID_EXTENDED_TIME_STAMP_COUNTER                            0x80000007
typedef struct {
  uint32_t eax;
  uint32_t ebx;
  uint32_t ecx;
  uint32_t edx;
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
#define IA32_PLATFORM_ID_PLATFORM_ID                                 0x1C000000000000

#define IA32_APIC_BASE                                               0x0000001B
#define IA32_APIC_BASE_BSP_FLAG                                      0x100
#define IA32_APIC_BASE_ENABLE_X2APIC_MODE                            0x400
#define IA32_APIC_BASE_APIC_GLOBAL_ENABLE                            0x800
#define IA32_APIC_BASE_APIC_BASE                                     0xFFFFFFFFF000

#define IA32_FEATURE_CONTROL                                         0x0000003A
#define IA32_FEATURE_CONTROL_LOCK_BIT                                0x01
#define IA32_FEATURE_CONTROL_ENABLE_VMX_INSIDE_SMX                   0x02
#define IA32_FEATURE_CONTROL_ENABLE_VMX_OUTSIDE_SMX                  0x04
#define IA32_FEATURE_CONTROL_SENTER_LOCAL_FUNCTION_ENABLES           0x7F00
#define IA32_FEATURE_CONTROL_SENTER_GLOBAL_ENABLE                    0x8000
#define IA32_FEATURE_CONTROL_SGX_LAUNCH_CONTROL_ENABLE               0x20000
#define IA32_FEATURE_CONTROL_SGX_GLOBAL_ENABLE                       0x40000
#define IA32_FEATURE_CONTROL_LMCE_ON                                 0x100000

#define IA32_TSC_ADJUST                                              0x0000003B
typedef struct {
  uint64_t thread_adjust;
} ia32_tsc_adjust_register;

#define IA32_BIOS_UPDT_TRIG                                          0x00000079
#define IA32_BIOS_SIGN_ID                                            0x0000008B
typedef struct {
  uint32_t reserved;
  uint32_t microcode_update_signature;
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
#define IA32_SMM_MONITOR_CTL_VALID                                   0x01
#define IA32_SMM_MONITOR_CTL_SMI_UNBLOCKING_BY_VMXOFF                0x04
#define IA32_SMM_MONITOR_CTL_MSEG_BASE                               0xFFFFF000

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
#define IA32_MTRRCAP_VARIABLE_RANGE_REGISTERS_COUNT                  0xFF
#define IA32_MTRRCAP_FIXED_RANGE_REGISTERS_SUPPORTED                 0x100
#define IA32_MTRRCAP_WRITE_COMBINING                                 0x400
#define IA32_MTRRCAP_SYSTEM_MANAGEMENT_RANGE_REGISTER                0x800

#define IA32_SYSENTER_CS                                             0x00000174
typedef struct {
  uint16_t cs_selector;
  uint16_t not_used_1;
  uint32_t not_used_2;
} ia32_sysenter_cs_register;

#define IA32_SYSENTER_ESP                                            0x00000175
#define IA32_SYSENTER_EIP                                            0x00000176
#define IA32_MCG_CAP                                                 0x00000179
#define IA32_MCG_CAP_COUNT                                           0xFF
#define IA32_MCG_CAP_MCG_CTL_P                                       0x100
#define IA32_MCG_CAP_MCG_EXT_P                                       0x200
#define IA32_MCG_CAP_MCP_CMCI_P                                      0x400
#define IA32_MCG_CAP_MCG_TES_P                                       0x800
#define IA32_MCG_CAP_MCG_EXT_CNT                                     0xFF0000
#define IA32_MCG_CAP_MCG_SER_P                                       0x1000000
#define IA32_MCG_CAP_MCG_ELOG_P                                      0x4000000
#define IA32_MCG_CAP_MCG_LMCE_P                                      0x8000000

#define IA32_MCG_STATUS                                              0x0000017A
#define IA32_MCG_STATUS_RIPV                                         0x01
#define IA32_MCG_STATUS_EIPV                                         0x02
#define IA32_MCG_STATUS_MCIP                                         0x04
#define IA32_MCG_STATUS_LMCE_S                                       0x08

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
#define IA32_PERFEVTSEL_EVENT_SELECT                                 0xFF
#define IA32_PERFEVTSEL_U_MASK                                       0xFF00
#define IA32_PERFEVTSEL_USR                                          0x10000
#define IA32_PERFEVTSEL_OS                                           0x20000
#define IA32_PERFEVTSEL_EDGE                                         0x40000
#define IA32_PERFEVTSEL_PC                                           0x80000
#define IA32_PERFEVTSEL_INTR                                         0x100000
#define IA32_PERFEVTSEL_ANY_THREAD                                   0x200000
#define IA32_PERFEVTSEL_EN                                           0x400000
#define IA32_PERFEVTSEL_INV                                          0x800000
#define IA32_PERFEVTSEL_CMASK                                        0xFF000000

/**
 * @}
 */

#define IA32_PERF_STATUS                                             0x00000198
typedef struct {
  uint16_t current_performance_state_value;
} ia32_perf_status_register;

#define IA32_PERF_CTL                                                0x00000199
#define IA32_PERF_CTL_TARGET_PERFORMANCE_STATE_VALUE                 0xFFFF
#define IA32_PERF_CTL_IDA_ENGAGE                                     0x100000000

#define IA32_CLOCK_MODULATION                                        0x0000019A
#define IA32_CLOCK_MODULATION_EXTENDED_ON_DEMAND_CLOCK_MODULATION_DUTY_CYCLE 0x01
#define IA32_CLOCK_MODULATION_ON_DEMAND_CLOCK_MODULATION_DUTY_CYCLE  0x0E
#define IA32_CLOCK_MODULATION_ON_DEMAND_CLOCK_MODULATION_ENABLE      0x10

#define IA32_THERM_INTERRUPT                                         0x0000019B
#define IA32_THERM_INTERRUPT_HIGH_TEMPERATURE_INTERRUPT_ENABLE       0x01
#define IA32_THERM_INTERRUPT_LOW_TEMPERATURE_INTERRUPT_ENABLE        0x02
#define IA32_THERM_INTERRUPT_PROCHOT_INTERRUPT_ENABLE                0x04
#define IA32_THERM_INTERRUPT_FORCEPR_INTERRUPT_ENABLE                0x08
#define IA32_THERM_INTERRUPT_CRITICAL_TEMPERATURE_INTERRUPT_ENABLE   0x10
#define IA32_THERM_INTERRUPT_THRESHOLD1_VALUE                        0x7F00
#define IA32_THERM_INTERRUPT_THRESHOLD1_INTERRUPT_ENABLE             0x8000
#define IA32_THERM_INTERRUPT_THRESHOLD2_VALUE                        0x7F0000
#define IA32_THERM_INTERRUPT_THRESHOLD2_INTERRUPT_ENABLE             0x800000
#define IA32_THERM_INTERRUPT_POWER_LIMIT_NOTIFICATION_ENABLE         0x1000000

#define IA32_THERM_STATUS                                            0x0000019C
#define IA32_THERM_STATUS_THERMAL_STATUS                             0x01
#define IA32_THERM_STATUS_THERMAL_STATUS_LOG                         0x02
#define IA32_THERM_STATUS_PROCHOT_FORCEPR_EVENT                      0x04
#define IA32_THERM_STATUS_PROCHOT_FORCEPR_LOG                        0x08
#define IA32_THERM_STATUS_CRITICAL_TEMPERATURE_STATUS                0x10
#define IA32_THERM_STATUS_CRITICAL_TEMPERATURE_STATUS_LOG            0x20
#define IA32_THERM_STATUS_THERMAL_THRESHOLD1_STATUS                  0x40
#define IA32_THERM_STATUS_THERMAL_THRESHOLD1_LOG                     0x80
#define IA32_THERM_STATUS_THERMAL_THRESHOLD2_STATUS                  0x100
#define IA32_THERM_STATUS_THERMAL_THRESHOLD2_LOG                     0x200
#define IA32_THERM_STATUS_POWER_LIMITATION_STATUS                    0x400
#define IA32_THERM_STATUS_POWER_LIMITATION_LOG                       0x800
#define IA32_THERM_STATUS_CURRENT_LIMIT_STATUS                       0x1000
#define IA32_THERM_STATUS_CURRENT_LIMIT_LOG                          0x2000
#define IA32_THERM_STATUS_CROSS_DOMAIN_LIMIT_STATUS                  0x4000
#define IA32_THERM_STATUS_CROSS_DOMAIN_LIMIT_LOG                     0x8000
#define IA32_THERM_STATUS_DIGITAL_READOUT                            0x7F0000
#define IA32_THERM_STATUS_RESOLUTION_IN_DEGREES_CELSIUS              0x78000000
#define IA32_THERM_STATUS_READING_VALID                              0x80000000

#define IA32_MISC_ENABLE                                             0x000001A0
#define IA32_MISC_ENABLE_FAST_STRINGS_ENABLE                         0x01
#define IA32_MISC_ENABLE_AUTOMATIC_THERMAL_CONTROL_CIRCUIT_ENABLE    0x08
#define IA32_MISC_ENABLE_PERFORMANCE_MONITORING_AVAILABLE            0x80
#define IA32_MISC_ENABLE_BRANCH_TRACE_STORAGE_UNAVAILABLE            0x800
#define IA32_MISC_ENABLE_PROCESSOR_EVENT_BASED_SAMPLING_UNAVAILABLE  0x1000
#define IA32_MISC_ENABLE_ENHANCED_INTEL_SPEEDSTEP_TECHNOLOGY_ENABLE  0x10000
#define IA32_MISC_ENABLE_ENABLE_MONITOR_FSM                          0x40000
#define IA32_MISC_ENABLE_LIMIT_CPUID_MAXVAL                          0x400000
#define IA32_MISC_ENABLE_XTPR_MESSAGE_DISABLE                        0x800000
#define IA32_MISC_ENABLE_XD_BIT_DISABLE                              0x400000000

#define IA32_ENERGY_PERF_BIAS                                        0x000001B0
#define IA32_ENERGY_PERF_BIAS_POWER_POLICY_PREFERENCE                0x0F

#define IA32_PACKAGE_THERM_STATUS                                    0x000001B1
#define IA32_PACKAGE_THERM_STATUS_THERMAL_STATUS                     0x01
#define IA32_PACKAGE_THERM_STATUS_THERMAL_STATUS_LOG                 0x02
#define IA32_PACKAGE_THERM_STATUS_PROCHOT_EVENT                      0x04
#define IA32_PACKAGE_THERM_STATUS_PROCHOT_LOG                        0x08
#define IA32_PACKAGE_THERM_STATUS_CRITICAL_TEMPERATURE_STATUS        0x10
#define IA32_PACKAGE_THERM_STATUS_CRITICAL_TEMPERATURE_STATUS_LOG    0x20
#define IA32_PACKAGE_THERM_STATUS_THERMAL_THRESHOLD1_STATUS          0x40
#define IA32_PACKAGE_THERM_STATUS_THERMAL_THRESHOLD1_LOG             0x80
#define IA32_PACKAGE_THERM_STATUS_THERMAL_THRESHOLD2_STATUS          0x100
#define IA32_PACKAGE_THERM_STATUS_THERMAL_THRESHOLD2_LOG             0x200
#define IA32_PACKAGE_THERM_STATUS_POWER_LIMITATION_STATUS            0x400
#define IA32_PACKAGE_THERM_STATUS_POWER_LIMITATION_LOG               0x800
#define IA32_PACKAGE_THERM_STATUS_DIGITAL_READOUT                    0x7F0000

#define IA32_PACKAGE_THERM_INTERRUPT                                 0x000001B2
#define IA32_PACKAGE_THERM_INTERRUPT_HIGH_TEMPERATURE_INTERRUPT_ENABLE 0x01
#define IA32_PACKAGE_THERM_INTERRUPT_LOW_TEMPERATURE_INTERRUPT_ENABLE 0x02
#define IA32_PACKAGE_THERM_INTERRUPT_PROCHOT_INTERRUPT_ENABLE        0x04
#define IA32_PACKAGE_THERM_INTERRUPT_OVERHEAT_INTERRUPT_ENABLE       0x10
#define IA32_PACKAGE_THERM_INTERRUPT_THRESHOLD1_VALUE                0x7F00
#define IA32_PACKAGE_THERM_INTERRUPT_THRESHOLD1_INTERRUPT_ENABLE     0x8000
#define IA32_PACKAGE_THERM_INTERRUPT_THRESHOLD2_VALUE                0x7F0000
#define IA32_PACKAGE_THERM_INTERRUPT_THRESHOLD2_INTERRUPT_ENABLE     0x800000
#define IA32_PACKAGE_THERM_INTERRUPT_POWER_LIMIT_NOTIFICATION_ENABLE 0x1000000

#define IA32_DEBUGCTL                                                0x000001D9
#define IA32_DEBUGCTL_LBR                                            0x01
#define IA32_DEBUGCTL_BTF                                            0x02
#define IA32_DEBUGCTL_TR                                             0x40
#define IA32_DEBUGCTL_BTS                                            0x80
#define IA32_DEBUGCTL_BTINT                                          0x100
#define IA32_DEBUGCTL_BTS_OFF_OS                                     0x200
#define IA32_DEBUGCTL_BTS_OFF_USR                                    0x400
#define IA32_DEBUGCTL_FREEZE_LBRS_ON_PMI                             0x800
#define IA32_DEBUGCTL_FREEZE_PERFMON_ON_PMI                          0x1000
#define IA32_DEBUGCTL_ENABLE_UNCORE_PMI                              0x2000
#define IA32_DEBUGCTL_FREEZE_WHILE_SMM                               0x4000
#define IA32_DEBUGCTL_RTM_DEBUG                                      0x8000

#define IA32_SMRR_PHYSBASE                                           0x000001F2
#define IA32_SMRR_PHYSBASE_TYPE                                      0xFF
#define IA32_SMRR_PHYSBASE_SMRR_PHYSICAL_BASE_ADDRESS                0xFFFFF000

#define IA32_SMRR_PHYSMASK                                           0x000001F3
#define IA32_SMRR_PHYSMASK_ENABLE_RANGE_MASK                         0x800
#define IA32_SMRR_PHYSMASK_SMRR_ADDRESS_RANGE_MASK                   0xFFFFF000

#define IA32_PLATFORM_DCA_CAP                                        0x000001F8
#define IA32_CPU_DCA_CAP                                             0x000001F9
#define IA32_DCA_0_CAP                                               0x000001FA
#define IA32_DCA_0_CAP_DCA_ACTIVE                                    0x01
#define IA32_DCA_0_CAP_TRANSACTION                                   0x06
#define IA32_DCA_0_CAP_DCA_TYPE                                      0x78
#define IA32_DCA_0_CAP_DCA_QUEUE_SIZE                                0x780
#define IA32_DCA_0_CAP_DCA_DELAY                                     0x1E000
#define IA32_DCA_0_CAP_SW_BLOCK                                      0x1000000
#define IA32_DCA_0_CAP_HW_BLOCK                                      0x4000000

/**
 * @defgroup ia32_mtrr_physbase \
 *           IA32_MTRR_PHYSBASE(n)
 * @{
 */
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

#define IA32_MTRR_FIX_COUNT                                          (1 + 2 + 8)
#define IA32_MTRR_VARIABLE_COUNT                                     0x000000FF
#define IA32_MTRR_COUNT                                              (IA32_MTRR_FIX_COUNT + IA32_MTRR_VARIABLE_COUNT)
/**
 * @}
 */

#define IA32_PAT                                                     0x00000277
#define IA32_PAT_PA0                                                 0x07
#define IA32_PAT_PA1                                                 0x700
#define IA32_PAT_PA2                                                 0x70000
#define IA32_PAT_PA3                                                 0x7000000
#define IA32_PAT_PA4                                                 0x700000000
#define IA32_PAT_PA5                                                 0x70000000000
#define IA32_PAT_PA6                                                 0x7000000000000
#define IA32_PAT_PA7                                                 0x700000000000000

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
#define IA32_MC_CTL2_CORRECTED_ERROR_COUNT_THRESHOLD                 0x7FFF
#define IA32_MC_CTL2_CMCI_EN                                         0x40000000

/**
 * @}
 */

#define IA32_MTRR_DEF_TYPE                                           0x000002FF
#define IA32_MTRR_DEF_TYPE_DEFAULT_MEMORY_TYPE                       0x07
#define IA32_MTRR_DEF_TYPE_FIXED_RANGE_MTRR_ENABLE                   0x400
#define IA32_MTRR_DEF_TYPE_MTRR_ENABLE                               0x800

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
#define IA32_PERF_CAPABILITIES_LBR_FORMAT                            0x3F
#define IA32_PERF_CAPABILITIES_PEBS_TRAP                             0x40
#define IA32_PERF_CAPABILITIES_PEBS_SAVE_ARCH_REGS                   0x80
#define IA32_PERF_CAPABILITIES_PEBS_RECORD_FORMAT                    0xF00
#define IA32_PERF_CAPABILITIES_FREEZE_WHILE_SMM_IS_SUPPORTED         0x1000
#define IA32_PERF_CAPABILITIES_FULL_WIDTH_COUNTER_WRITE              0x2000

#define IA32_FIXED_CTR_CTRL                                          0x0000038D
#define IA32_FIXED_CTR_CTRL_EN0_OS                                   0x01
#define IA32_FIXED_CTR_CTRL_EN0_USR                                  0x02
#define IA32_FIXED_CTR_CTRL_ANY_THREAD0                              0x04
#define IA32_FIXED_CTR_CTRL_EN0_PMI                                  0x08
#define IA32_FIXED_CTR_CTRL_EN1_OS                                   0x10
#define IA32_FIXED_CTR_CTRL_EN1_USR                                  0x20
#define IA32_FIXED_CTR_CTRL_ANY_THREAD1                              0x40
#define IA32_FIXED_CTR_CTRL_EN1_PMI                                  0x80
#define IA32_FIXED_CTR_CTRL_EN2_OS                                   0x100
#define IA32_FIXED_CTR_CTRL_EN2_USR                                  0x200
#define IA32_FIXED_CTR_CTRL_ANY_THREAD2                              0x400
#define IA32_FIXED_CTR_CTRL_EN2_PMI                                  0x800

#define IA32_PERF_GLOBAL_STATUS                                      0x0000038E
#define IA32_PERF_GLOBAL_STATUS_OVF_PMC0                             0x01
#define IA32_PERF_GLOBAL_STATUS_OVF_PMC1                             0x02
#define IA32_PERF_GLOBAL_STATUS_OVF_PMC2                             0x04
#define IA32_PERF_GLOBAL_STATUS_OVF_PMC3                             0x08
#define IA32_PERF_GLOBAL_STATUS_OVF_FIXEDCTR0                        0x100000000
#define IA32_PERF_GLOBAL_STATUS_OVF_FIXEDCTR1                        0x200000000
#define IA32_PERF_GLOBAL_STATUS_OVF_FIXEDCTR2                        0x400000000
#define IA32_PERF_GLOBAL_STATUS_TRACE_TOPA_PMI                       0x80000000000000
#define IA32_PERF_GLOBAL_STATUS_LBR_FRZ                              0x400000000000000
#define IA32_PERF_GLOBAL_STATUS_CTR_FRZ                              0x800000000000000
#define IA32_PERF_GLOBAL_STATUS_ASCI                                 0x1000000000000000
#define IA32_PERF_GLOBAL_STATUS_OVF_UNCORE                           0x2000000000000000
#define IA32_PERF_GLOBAL_STATUS_OVF_BUF                              0x4000000000000000
#define IA32_PERF_GLOBAL_STATUS_COND_CHGD                            0x8000000000000000

#define IA32_PERF_GLOBAL_CTRL                                        0x0000038F
typedef struct {
  uint32_t en_pmcn;
  uint32_t en_fixed_ctrn;
} ia32_perf_global_ctrl_register;

#define IA32_PERF_GLOBAL_STATUS_RESET                                0x00000390
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_OVF_PMCN                 0xFFFFFFFF
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_OVF_FIXED_CTRN           0x700000000
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_TRACE_TOPA_PMI           0x80000000000000
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_LBR_FRZ                  0x400000000000000
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_CTR_FRZ                  0x800000000000000
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_ASCI                     0x1000000000000000
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_OVF_UNCORE               0x2000000000000000
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_OVF_BUF                  0x4000000000000000
#define IA32_PERF_GLOBAL_STATUS_RESET_CLEAR_COND_CHGD                0x8000000000000000

#define IA32_PERF_GLOBAL_STATUS_SET                                  0x00000391
#define IA32_PERF_GLOBAL_STATUS_SET_OVF_PMCN                         0xFFFFFFFF
#define IA32_PERF_GLOBAL_STATUS_SET_OVF_FIXED_CTRN                   0x700000000
#define IA32_PERF_GLOBAL_STATUS_SET_TRACE_TOPA_PMI                   0x80000000000000
#define IA32_PERF_GLOBAL_STATUS_SET_LBR_FRZ                          0x400000000000000
#define IA32_PERF_GLOBAL_STATUS_SET_CTR_FRZ                          0x800000000000000
#define IA32_PERF_GLOBAL_STATUS_SET_ASCI                             0x1000000000000000
#define IA32_PERF_GLOBAL_STATUS_SET_OVF_UNCORE                       0x2000000000000000
#define IA32_PERF_GLOBAL_STATUS_SET_OVF_BUF                          0x4000000000000000

#define IA32_PERF_GLOBAL_INUSE                                       0x00000392
#define IA32_PERF_GLOBAL_INUSE_IA32_PERFEVTSELN_IN_USE               0xFFFFFFFF
#define IA32_PERF_GLOBAL_INUSE_IA32_FIXED_CTRN_IN_USE                0x700000000
#define IA32_PERF_GLOBAL_INUSE_PMI_IN_USE                            0x8000000000000000

#define IA32_PEBS_ENABLE                                             0x000003F1
#define IA32_PEBS_ENABLE_ENABLE_PEBS                                 0x01
#define IA32_PEBS_ENABLE_RESERVEDORMODELSPECIFIC1                    0x0E
#define IA32_PEBS_ENABLE_RESERVEDORMODELSPECIFIC2                    0xF00000000

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
#define IA32_VMX_BASIC_VMCS_REVISION_ID                              0x7FFFFFFF
#define IA32_VMX_BASIC_MUST_BE_ZERO                                  0x80000000
#define IA32_VMX_BASIC_VMCS_SIZE_IN_BYTES                            0x1FFF00000000
#define IA32_VMX_BASIC_VMCS_PHYSICAL_ADDRESS_WIDTH                   0x1000000000000
#define IA32_VMX_BASIC_DUAL_MONITOR                                  0x2000000000000
#define IA32_VMX_BASIC_MEMORY_TYPE                                   0x3C000000000000
#define IA32_VMX_BASIC_INS_OUTS_VMEXIT_INFORMATION                   0x40000000000000
#define IA32_VMX_BASIC_TRUE_CONTROLS                                 0x80000000000000

#define IA32_VMX_PINBASED_CTLS                                       0x00000481
#define IA32_VMX_PINBASED_CTLS_EXTERNAL_INTERRUPT_EXITING            0x01
#define IA32_VMX_PINBASED_CTLS_NMI_EXITING                           0x08
#define IA32_VMX_PINBASED_CTLS_VIRTUAL_NMIS                          0x20
#define IA32_VMX_PINBASED_CTLS_ACTIVATE_VMX_PREEMPTION_TIMER         0x40
#define IA32_VMX_PINBASED_CTLS_PROCESS_POSTED_INTERRUPTS             0x80

#define IA32_VMX_PROCBASED_CTLS                                      0x00000482
#define IA32_VMX_PROCBASED_CTLS_INTERRUPT_WINDOW_EXITING             0x04
#define IA32_VMX_PROCBASED_CTLS_USE_TSC_OFFSETTING                   0x08
#define IA32_VMX_PROCBASED_CTLS_HLT_EXITING                          0x80
#define IA32_VMX_PROCBASED_CTLS_INVLPG_EXITING                       0x200
#define IA32_VMX_PROCBASED_CTLS_MWAIT_EXITING                        0x400
#define IA32_VMX_PROCBASED_CTLS_RDPMC_EXITING                        0x800
#define IA32_VMX_PROCBASED_CTLS_RDTSC_EXITING                        0x1000
#define IA32_VMX_PROCBASED_CTLS_CR3_LOAD_EXITING                     0x8000
#define IA32_VMX_PROCBASED_CTLS_CR3_STORE_EXITING                    0x10000
#define IA32_VMX_PROCBASED_CTLS_CR8_LOAD_EXITING                     0x80000
#define IA32_VMX_PROCBASED_CTLS_CR8_STORE_EXITING                    0x100000
#define IA32_VMX_PROCBASED_CTLS_USE_TPR_SHADOW                       0x200000
#define IA32_VMX_PROCBASED_CTLS_NMI_WINDOW_EXITING                   0x400000
#define IA32_VMX_PROCBASED_CTLS_MOV_DR_EXITING                       0x800000
#define IA32_VMX_PROCBASED_CTLS_UNCONDITIONAL_IO_EXITING             0x1000000
#define IA32_VMX_PROCBASED_CTLS_USE_IO_BITMAPS                       0x2000000
#define IA32_VMX_PROCBASED_CTLS_MONITOR_TRAP_FLAG                    0x8000000
#define IA32_VMX_PROCBASED_CTLS_USE_MSR_BITMAPS                      0x10000000
#define IA32_VMX_PROCBASED_CTLS_MONITOR_EXITING                      0x20000000
#define IA32_VMX_PROCBASED_CTLS_PAUSE_EXITING                        0x40000000
#define IA32_VMX_PROCBASED_CTLS_ACTIVATE_SECONDARY_CONTROLS          0x80000000

#define IA32_VMX_EXIT_CTLS                                           0x00000483
#define IA32_VMX_EXIT_CTLS_SAVE_DEBUG_CONTROLS                       0x04
#define IA32_VMX_EXIT_CTLS_HOST_ADDRESS_SPACE_SIZE                   0x200
#define IA32_VMX_EXIT_CTLS_LOAD_IA32_PERF_GLOBAL_CTRL                0x1000
#define IA32_VMX_EXIT_CTLS_ACKNOWLEDGE_INTERRUPT_ON_EXIT             0x8000
#define IA32_VMX_EXIT_CTLS_SAVE_IA32_PAT                             0x40000
#define IA32_VMX_EXIT_CTLS_LOAD_IA32_PAT                             0x80000
#define IA32_VMX_EXIT_CTLS_SAVE_IA32_EFER                            0x100000
#define IA32_VMX_EXIT_CTLS_LOAD_IA32_EFER                            0x200000
#define IA32_VMX_EXIT_CTLS_SAVE_VMX_PREEMPTION_TIMER_VALUE           0x400000
#define IA32_VMX_EXIT_CTLS_CLEAR_IA32_BNDCFGS                        0x800000
#define IA32_VMX_EXIT_CTLS_CONCEAL_VMX_FROM_PT                       0x1000000

#define IA32_VMX_ENTRY_CTLS                                          0x00000484
#define IA32_VMX_ENTRY_CTLS_LOAD_DEBUG_CONTROLS                      0x04
#define IA32_VMX_ENTRY_CTLS_IA32E_MODE_GUEST                         0x200
#define IA32_VMX_ENTRY_CTLS_ENTRY_TO_SMM                             0x400
#define IA32_VMX_ENTRY_CTLS_DEACTIVATE_DUAL_MONITOR_TREATMENT        0x800
#define IA32_VMX_ENTRY_CTLS_LOAD_IA32_PERF_GLOBAL_CTRL               0x2000
#define IA32_VMX_ENTRY_CTLS_LOAD_IA32_PAT                            0x4000
#define IA32_VMX_ENTRY_CTLS_LOAD_IA32_EFER                           0x8000
#define IA32_VMX_ENTRY_CTLS_LOAD_IA32_BNDCFGS                        0x10000
#define IA32_VMX_ENTRY_CTLS_CONCEAL_VMX_FROM_PT                      0x20000

#define IA32_VMX_MISC                                                0x00000485
#define IA32_VMX_MISC_PREEMPTION_TIMER_TSC_RELATIONSHIP              0x1F
#define IA32_VMX_MISC_STORE_EFER_LMA_ON_VMEXIT                       0x20
#define IA32_VMX_MISC_ACTIVITY_STATES                                0x1C0
#define IA32_VMX_MISC_INTEL_PT_AVAILABLE_IN_VMX                      0x4000
#define IA32_VMX_MISC_RDMSR_CAN_READ_IA32_SMBASE_MSR_IN_SMM          0x8000
#define IA32_VMX_MISC_CR3_TARGET_COUNT                               0x1FF0000
#define IA32_VMX_MISC_MAX_NUMBER_OF_MSR                              0xE000000
#define IA32_VMX_MISC_SMM_MONITOR_CTL_B2                             0x10000000
#define IA32_VMX_MISC_VMWRITE_VMEXIT_INFO                            0x20000000
#define IA32_VMX_MISC_ZERO_LENGTH_INSTRUCTION_VMENTRY_INJECTION      0x40000000
#define IA32_VMX_MISC_MSEG_ID                                        0xFFFFFFFF00000000

#define IA32_VMX_CR0_FIXED0                                          0x00000486
#define IA32_VMX_CR0_FIXED1                                          0x00000487
#define IA32_VMX_CR4_FIXED0                                          0x00000488
#define IA32_VMX_CR4_FIXED1                                          0x00000489
#define IA32_VMX_VMCS_ENUM                                           0x0000048A
#define IA32_VMX_VMCS_ENUM_ACCESS_TYPE                               0x01
#define IA32_VMX_VMCS_ENUM_HIGHEST_INDEX_VALUE                       0x3FE
#define IA32_VMX_VMCS_ENUM_FIELD_TYPE                                0xC00
#define IA32_VMX_VMCS_ENUM_FIELD_WIDTH                               0x6000

#define IA32_VMX_PROCBASED_CTLS2                                     0x0000048B
#define IA32_VMX_PROCBASED_CTLS2_VIRTUALIZE_APIC_ACCESSES            0x01
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_EPT                          0x02
#define IA32_VMX_PROCBASED_CTLS2_DESCRIPTOR_TABLE_EXITING            0x04
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_RDTSCP                       0x08
#define IA32_VMX_PROCBASED_CTLS2_VIRTUALIZE_X2APIC_MODE              0x10
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_VPID                         0x20
#define IA32_VMX_PROCBASED_CTLS2_WBINVD_EXITING                      0x40
#define IA32_VMX_PROCBASED_CTLS2_UNRESTRICTED_GUEST                  0x80
#define IA32_VMX_PROCBASED_CTLS2_APIC_REGISTER_VIRTUALIZATION        0x100
#define IA32_VMX_PROCBASED_CTLS2_VIRTUAL_INTERRUPT_DELIVERY          0x200
#define IA32_VMX_PROCBASED_CTLS2_PAUSE_LOOP_EXITING                  0x400
#define IA32_VMX_PROCBASED_CTLS2_RDRAND_EXITING                      0x800
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_INVPCID                      0x1000
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_VM_FUNCTIONS                 0x2000
#define IA32_VMX_PROCBASED_CTLS2_VMCS_SHADOWING                      0x4000
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_ENCLS_EXITING                0x8000
#define IA32_VMX_PROCBASED_CTLS2_RDSEED_EXITING                      0x10000
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_PML                          0x20000
#define IA32_VMX_PROCBASED_CTLS2_EPT_VIOLATION                       0x40000
#define IA32_VMX_PROCBASED_CTLS2_CONCEAL_VMX_FROM_PT                 0x80000
#define IA32_VMX_PROCBASED_CTLS2_ENABLE_XSAVES                       0x100000
#define IA32_VMX_PROCBASED_CTLS2_MODE_BASED_EXECUTE_CONTROL_FOR_EPT  0x400000
#define IA32_VMX_PROCBASED_CTLS2_USE_TSC_SCALING                     0x2000000

#define IA32_VMX_EPT_VPID_CAP                                        0x0000048C
#define IA32_VMX_EPT_VPID_CAP_EXECUTE_ONLY_PAGES                     0x01
#define IA32_VMX_EPT_VPID_CAP_PAGE_WALK_LENGTH_4                     0x40
#define IA32_VMX_EPT_VPID_CAP_MEMORY_TYPE_UNCACHEABLE                0x100
#define IA32_VMX_EPT_VPID_CAP_MEMORY_TYPE_WRITE_BACK                 0x4000
#define IA32_VMX_EPT_VPID_CAP_PDE_2MB_PAGES                          0x10000
#define IA32_VMX_EPT_VPID_CAP_PDPTE_1GB_PAGES                        0x20000
#define IA32_VMX_EPT_VPID_CAP_INVEPT                                 0x100000
#define IA32_VMX_EPT_VPID_CAP_EPT_ACCESSED_AND_DIRTY_FLAGS           0x200000
#define IA32_VMX_EPT_VPID_CAP_ADVANCED_VMEXIT_EPT_VIOLATIONS_INFORMATION 0x400000
#define IA32_VMX_EPT_VPID_CAP_INVEPT_SINGLE_CONTEXT                  0x2000000
#define IA32_VMX_EPT_VPID_CAP_INVEPT_ALL_CONTEXTS                    0x4000000
#define IA32_VMX_EPT_VPID_CAP_INVVPID                                0x100000000
#define IA32_VMX_EPT_VPID_CAP_INVVPID_INDIVIDUAL_ADDRESS             0x10000000000
#define IA32_VMX_EPT_VPID_CAP_INVVPID_SINGLE_CONTEXT                 0x20000000000
#define IA32_VMX_EPT_VPID_CAP_INVVPID_ALL_CONTEXTS                   0x40000000000
#define IA32_VMX_EPT_VPID_CAP_INVVPID_SINGLE_CONTEXT_RETAIN_GLOBALS  0x80000000000

/**
 * @defgroup ia32_vmx_true_ctls \
 *           IA32_VMX_TRUE_(x)_CTLS
 * @{
 */
#define IA32_VMX_TRUE_PINBASED_CTLS                                  0x0000048D
#define IA32_VMX_TRUE_PROCBASED_CTLS                                 0x0000048E
#define IA32_VMX_TRUE_EXIT_CTLS                                      0x0000048F
#define IA32_VMX_TRUE_ENTRY_CTLS                                     0x00000490
typedef struct {
  uint32_t allowed_0_settings;
  uint32_t allowed_1_settings;
} ia32_vmx_true_ctls_register;

/**
 * @}
 */

#define IA32_VMX_VMFUNC                                              0x00000491
#define IA32_VMX_VMFUNC_EPTP_SWITCHING                               0x01

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
#define IA32_MCG_EXT_CTL_LMCE_EN                                     0x01

#define IA32_SGX_SVN_STATUS                                          0x00000500
#define IA32_SGX_SVN_STATUS_LOCK                                     0x01
#define IA32_SGX_SVN_STATUS_SGX_SVN_SINIT                            0xFF0000

#define IA32_RTIT_OUTPUT_BASE                                        0x00000560
#define IA32_RTIT_OUTPUT_BASE_BASE_PHYSICAL_ADDRESS                  0xFFFFFFFFFF80

#define IA32_RTIT_OUTPUT_MASK_PTRS                                   0x00000561
#define IA32_RTIT_OUTPUT_MASK_PTRS_LOWER_MASK                        0x7F
#define IA32_RTIT_OUTPUT_MASK_PTRS_MASK_OR_TABLE_OFFSET              0xFFFFFF80
#define IA32_RTIT_OUTPUT_MASK_PTRS_OUTPUT_OFFSET                     0xFFFFFFFF00000000

#define IA32_RTIT_CTL                                                0x00000570
#define IA32_RTIT_CTL_TRACE_EN                                       0x01
#define IA32_RTIT_CTL_CYC_EN                                         0x02
#define IA32_RTIT_CTL_OS                                             0x04
#define IA32_RTIT_CTL_USER                                           0x08
#define IA32_RTIT_CTL_PWR_EVT_EN                                     0x10
#define IA32_RTIT_CTL_FUP_ON_PTW                                     0x20
#define IA32_RTIT_CTL_FABRIC_EN                                      0x40
#define IA32_RTIT_CTL_CR3_FILTER                                     0x80
#define IA32_RTIT_CTL_TOPA                                           0x100
#define IA32_RTIT_CTL_MTC_EN                                         0x200
#define IA32_RTIT_CTL_TSC_EN                                         0x400
#define IA32_RTIT_CTL_DIS_RETC                                       0x800
#define IA32_RTIT_CTL_PTW_EN                                         0x1000
#define IA32_RTIT_CTL_BRANCH_EN                                      0x2000
#define IA32_RTIT_CTL_MTC_FREQ                                       0x3C000
#define IA32_RTIT_CTL_CYC_THRESH                                     0x780000
#define IA32_RTIT_CTL_PSB_FREQ                                       0xF000000
#define IA32_RTIT_CTL_ADDR0_CFG                                      0xF00000000
#define IA32_RTIT_CTL_ADDR1_CFG                                      0xF000000000
#define IA32_RTIT_CTL_ADDR2_CFG                                      0xF0000000000
#define IA32_RTIT_CTL_ADDR3_CFG                                      0xF00000000000
#define IA32_RTIT_CTL_INJECT_PSB_PMI_ON_ENABLE                       0x100000000000000

#define IA32_RTIT_STATUS                                             0x00000571
#define IA32_RTIT_STATUS_FILTER_EN                                   0x01
#define IA32_RTIT_STATUS_CONTEX_EN                                   0x02
#define IA32_RTIT_STATUS_TRIGGER_EN                                  0x04
#define IA32_RTIT_STATUS_ERROR                                       0x10
#define IA32_RTIT_STATUS_STOPPED                                     0x20
#define IA32_RTIT_STATUS_PEND_PSB                                    0x40
#define IA32_RTIT_STATUS_PEND_TOPA_PMI                               0x80
#define IA32_RTIT_STATUS_PACKET_BYTE_CNT                             0x1FFFF00000000

#define IA32_RTIT_CR3_MATCH                                          0x00000572
#define IA32_RTIT_CR3_MATCH_CR3_VALUE_TO_MATCH                       0xFFFFFFFFFFFFFFE0

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

#define IA32_RTIT_ADDR_VIRTUAL_ADDRESS                               0xFFFFFFFFFFFF
#define IA32_RTIT_ADDR_SIGN_EXT_VA                                   0xFFFF000000000000

/**
 * @}
 */

#define IA32_DS_AREA                                                 0x00000600
#define IA32_TSC_DEADLINE                                            0x000006E0
#define IA32_PM_ENABLE                                               0x00000770
#define IA32_PM_ENABLE_HWP_ENABLE                                    0x01

#define IA32_HWP_CAPABILITIES                                        0x00000771
#define IA32_HWP_CAPABILITIES_HIGHEST_PERFORMANCE                    0xFF
#define IA32_HWP_CAPABILITIES_GUARANTEED_PERFORMANCE                 0xFF00
#define IA32_HWP_CAPABILITIES_MOST_EFFICIENT_PERFORMANCE             0xFF0000
#define IA32_HWP_CAPABILITIES_LOWEST_PERFORMANCE                     0xFF000000

#define IA32_HWP_REQUEST_PKG                                         0x00000772
#define IA32_HWP_REQUEST_PKG_MINIMUM_PERFORMANCE                     0xFF
#define IA32_HWP_REQUEST_PKG_MAXIMUM_PERFORMANCE                     0xFF00
#define IA32_HWP_REQUEST_PKG_DESIRED_PERFORMANCE                     0xFF0000
#define IA32_HWP_REQUEST_PKG_ENERGY_PERFORMANCE_PREFERENCE           0xFF000000
#define IA32_HWP_REQUEST_PKG_ACTIVITY_WINDOW                         0x3FF00000000

#define IA32_HWP_INTERRUPT                                           0x00000773
#define IA32_HWP_INTERRUPT_EN_GUARANTEED_PERFORMANCE_CHANGE          0x01
#define IA32_HWP_INTERRUPT_EN_EXCURSION_MINIMUM                      0x02

#define IA32_HWP_REQUEST                                             0x00000774
#define IA32_HWP_REQUEST_MINIMUM_PERFORMANCE                         0xFF
#define IA32_HWP_REQUEST_MAXIMUM_PERFORMANCE                         0xFF00
#define IA32_HWP_REQUEST_DESIRED_PERFORMANCE                         0xFF0000
#define IA32_HWP_REQUEST_ENERGY_PERFORMANCE_PREFERENCE               0xFF000000
#define IA32_HWP_REQUEST_ACTIVITY_WINDOW                             0x3FF00000000
#define IA32_HWP_REQUEST_PACKAGE_CONTROL                             0x40000000000

#define IA32_HWP_STATUS                                              0x00000777
#define IA32_HWP_STATUS_GUARANTEED_PERFORMANCE_CHANGE                0x01
#define IA32_HWP_STATUS_EXCURSION_TO_MINIMUM                         0x04

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
#define IA32_DEBUG_INTERFACE_ENABLE                                  0x01
#define IA32_DEBUG_INTERFACE_LOCK                                    0x40000000
#define IA32_DEBUG_INTERFACE_DEBUG_OCCURRED                          0x80000000

#define IA32_L3_QOS_CFG                                              0x00000C81
#define IA32_L3_QOS_CFG_ENABLE                                       0x01

#define IA32_L2_QOS_CFG                                              0x00000C82
#define IA32_L2_QOS_CFG_ENABLE                                       0x01

#define IA32_QM_EVTSEL                                               0x00000C8D
#define IA32_QM_EVTSEL_EVENT_ID                                      0xFF
#define IA32_QM_EVTSEL_RESOURCE_MONITORING_ID                        0xFFFFFFFF00000000

#define IA32_QM_CTR                                                  0x00000C8E
#define IA32_QM_CTR_RESOURCE_MONITORED_DATA                          0x3FFFFFFFFFFFFFFF
#define IA32_QM_CTR_UNAVAILABLE                                      0x4000000000000000
#define IA32_QM_CTR_ERROR                                            0x8000000000000000

#define IA32_PQR_ASSOC                                               0x00000C8F
#define IA32_PQR_ASSOC_RESOURCE_MONITORING_ID                        0xFFFFFFFF
#define IA32_PQR_ASSOC_COS                                           0xFFFFFFFF00000000

#define IA32_BNDCFGS                                                 0x00000D90
#define IA32_BNDCFGS_ENABLE                                          0x01
#define IA32_BNDCFGS_BND_PRESERVE                                    0x02
#define IA32_BNDCFGS_BOUND_DIRECTORY_BASE_ADDRESS                    0xFFFFFFFFFFFFF000

#define IA32_XSS                                                     0x00000DA0
#define IA32_XSS_TRACE_PACKET_CONFIGURATION_STATE                    0x100

#define IA32_PKG_HDC_CTL                                             0x00000DB0
#define IA32_PKG_HDC_CTL_HDC_PKG_ENABLE                              0x01

#define IA32_PM_CTL1                                                 0x00000DB1
#define IA32_PM_CTL1_HDC_ALLOW_BLOCK                                 0x01

#define IA32_THREAD_STALL                                            0x00000DB2
typedef struct {
  uint64_t stall_cycle_cnt;
} ia32_thread_stall_register;

#define IA32_EFER                                                    0xC0000080
#define IA32_EFER_SYSCALL_ENABLE                                     0x01
#define IA32_EFER_IA32E_MODE_ENABLE                                  0x100
#define IA32_EFER_IA32E_MODE_ACTIVE                                  0x400
#define IA32_EFER_EXECUTE_DISABLE_BIT_ENABLE                         0x800

#define IA32_STAR                                                    0xC0000081
#define IA32_LSTAR                                                   0xC0000082
#define IA32_CSTAR                                                   0xC0000083
#define IA32_FMASK                                                   0xC0000084
#define IA32_FS_BASE                                                 0xC0000100
#define IA32_GS_BASE                                                 0xC0000101
#define IA32_KERNEL_GS_BASE                                          0xC0000102
#define IA32_TSC_AUX                                                 0xC0000103
#define IA32_TSC_AUX_TSC_AUXILIARY_SIGNATURE                         0xFFFFFFFF

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
#define PDE_4MB_32_PRESENT                                           0x01
#define PDE_4MB_32_WRITE                                             0x02
#define PDE_4MB_32_SUPERVISOR                                        0x04
#define PDE_4MB_32_PAGE_LEVEL_WRITE_THROUGH                          0x08
#define PDE_4MB_32_PAGE_LEVEL_CACHE_DISABLE                          0x10
#define PDE_4MB_32_ACCESSED                                          0x20
#define PDE_4MB_32_DIRTY                                             0x40
#define PDE_4MB_32_LARGE_PAGE                                        0x80
#define PDE_4MB_32_GLOBAL                                            0x100
#define PDE_4MB_32_IGNORED_1                                         0xE00
#define PDE_4MB_32_PAT                                               0x1000
#define PDE_4MB_32_PAGE_FRAME_NUMBER_LOW                             0x1FE000
#define PDE_4MB_32_PAGE_FRAME_NUMBER_HIGH                            0xFFC00000

#define PDE_32_PRESENT                                               0x01
#define PDE_32_WRITE                                                 0x02
#define PDE_32_SUPERVISOR                                            0x04
#define PDE_32_PAGE_LEVEL_WRITE_THROUGH                              0x08
#define PDE_32_PAGE_LEVEL_CACHE_DISABLE                              0x10
#define PDE_32_ACCESSED                                              0x20
#define PDE_32_IGNORED_1                                             0x40
#define PDE_32_LARGE_PAGE                                            0x80
#define PDE_32_IGNORED_2                                             0xF00
#define PDE_32_PAGE_FRAME_NUMBER                                     0xFFFFF000

#define PTE_32_PRESENT                                               0x01
#define PTE_32_WRITE                                                 0x02
#define PTE_32_SUPERVISOR                                            0x04
#define PTE_32_PAGE_LEVEL_WRITE_THROUGH                              0x08
#define PTE_32_PAGE_LEVEL_CACHE_DISABLE                              0x10
#define PTE_32_ACCESSED                                              0x20
#define PTE_32_DIRTY                                                 0x40
#define PTE_32_PAT                                                   0x80
#define PTE_32_GLOBAL                                                0x100
#define PTE_32_IGNORED_1                                             0xE00
#define PTE_32_PAGE_FRAME_NUMBER                                     0xFFFFF000

#define PT_ENTRY_32_PRESENT                                          0x01
#define PT_ENTRY_32_WRITE                                            0x02
#define PT_ENTRY_32_SUPERVISOR                                       0x04
#define PT_ENTRY_32_PAGE_LEVEL_WRITE_THROUGH                         0x08
#define PT_ENTRY_32_PAGE_LEVEL_CACHE_DISABLE                         0x10
#define PT_ENTRY_32_ACCESSED                                         0x20
#define PT_ENTRY_32_DIRTY                                            0x40
#define PT_ENTRY_32_LARGE_PAGE                                       0x80
#define PT_ENTRY_32_GLOBAL                                           0x100
#define PT_ENTRY_32_IGNORED_1                                        0xE00
#define PT_ENTRY_32_PAGE_FRAME_NUMBER                                0xFFFFF000

/**
 * @}
 */

/**
 * @defgroup paging_64 \
 *           64-Bit (4-Level Paging)
 * @{
 */
#define PML4E_64_PRESENT                                             0x01
#define PML4E_64_WRITE                                               0x02
#define PML4E_64_SUPERVISOR                                          0x04
#define PML4E_64_PAGE_LEVEL_WRITE_THROUGH                            0x08
#define PML4E_64_PAGE_LEVEL_CACHE_DISABLE                            0x10
#define PML4E_64_ACCESSED                                            0x20
#define PML4E_64_MUST_BE_ZERO                                        0x80
#define PML4E_64_IGNORED_1                                           0xF00
#define PML4E_64_PAGE_FRAME_NUMBER                                   0xFFFFFFFFF000
#define PML4E_64_IGNORED_2                                           0x7FF0000000000000
#define PML4E_64_EXECUTE_DISABLE                                     0x8000000000000000

#define PDPTE_1GB_64_PRESENT                                         0x01
#define PDPTE_1GB_64_WRITE                                           0x02
#define PDPTE_1GB_64_SUPERVISOR                                      0x04
#define PDPTE_1GB_64_PAGE_LEVEL_WRITE_THROUGH                        0x08
#define PDPTE_1GB_64_PAGE_LEVEL_CACHE_DISABLE                        0x10
#define PDPTE_1GB_64_ACCESSED                                        0x20
#define PDPTE_1GB_64_DIRTY                                           0x40
#define PDPTE_1GB_64_LARGE_PAGE                                      0x80
#define PDPTE_1GB_64_GLOBAL                                          0x100
#define PDPTE_1GB_64_IGNORED_1                                       0xE00
#define PDPTE_1GB_64_PAT                                             0x1000
#define PDPTE_1GB_64_PAGE_FRAME_NUMBER                               0xFFFFC0000000
#define PDPTE_1GB_64_IGNORED_2                                       0x7F0000000000000
#define PDPTE_1GB_64_PROTECTION_KEY                                  0x7800000000000000
#define PDPTE_1GB_64_EXECUTE_DISABLE                                 0x8000000000000000

#define PDPTE_64_PRESENT                                             0x01
#define PDPTE_64_WRITE                                               0x02
#define PDPTE_64_SUPERVISOR                                          0x04
#define PDPTE_64_PAGE_LEVEL_WRITE_THROUGH                            0x08
#define PDPTE_64_PAGE_LEVEL_CACHE_DISABLE                            0x10
#define PDPTE_64_ACCESSED                                            0x20
#define PDPTE_64_LARGE_PAGE                                          0x80
#define PDPTE_64_IGNORED_1                                           0xF00
#define PDPTE_64_PAGE_FRAME_NUMBER                                   0xFFFFFFFFF000
#define PDPTE_64_IGNORED_2                                           0x7FF0000000000000
#define PDPTE_64_EXECUTE_DISABLE                                     0x8000000000000000

#define PDE_2MB_64_PRESENT                                           0x01
#define PDE_2MB_64_WRITE                                             0x02
#define PDE_2MB_64_SUPERVISOR                                        0x04
#define PDE_2MB_64_PAGE_LEVEL_WRITE_THROUGH                          0x08
#define PDE_2MB_64_PAGE_LEVEL_CACHE_DISABLE                          0x10
#define PDE_2MB_64_ACCESSED                                          0x20
#define PDE_2MB_64_DIRTY                                             0x40
#define PDE_2MB_64_LARGE_PAGE                                        0x80
#define PDE_2MB_64_GLOBAL                                            0x100
#define PDE_2MB_64_IGNORED_1                                         0xE00
#define PDE_2MB_64_PAT                                               0x1000
#define PDE_2MB_64_PAGE_FRAME_NUMBER                                 0xFFFFC0000000
#define PDE_2MB_64_IGNORED_2                                         0x7F0000000000000
#define PDE_2MB_64_PROTECTION_KEY                                    0x7800000000000000
#define PDE_2MB_64_EXECUTE_DISABLE                                   0x8000000000000000

#define PDE_64_PRESENT                                               0x01
#define PDE_64_WRITE                                                 0x02
#define PDE_64_SUPERVISOR                                            0x04
#define PDE_64_PAGE_LEVEL_WRITE_THROUGH                              0x08
#define PDE_64_PAGE_LEVEL_CACHE_DISABLE                              0x10
#define PDE_64_ACCESSED                                              0x20
#define PDE_64_LARGE_PAGE                                            0x80
#define PDE_64_IGNORED_1                                             0xF00
#define PDE_64_PAGE_FRAME_NUMBER                                     0xFFFFFFFFF000
#define PDE_64_IGNORED_2                                             0x7FF0000000000000
#define PDE_64_EXECUTE_DISABLE                                       0x8000000000000000

#define PTE_64_PRESENT                                               0x01
#define PTE_64_WRITE                                                 0x02
#define PTE_64_SUPERVISOR                                            0x04
#define PTE_64_PAGE_LEVEL_WRITE_THROUGH                              0x08
#define PTE_64_PAGE_LEVEL_CACHE_DISABLE                              0x10
#define PTE_64_ACCESSED                                              0x20
#define PTE_64_DIRTY                                                 0x40
#define PTE_64_PAT                                                   0x80
#define PTE_64_GLOBAL                                                0x100
#define PTE_64_IGNORED_1                                             0xE00
#define PTE_64_PAGE_FRAME_NUMBER                                     0xFFFFFFFFF000
#define PTE_64_IGNORED_2                                             0x7F0000000000000
#define PTE_64_PROTECTION_KEY                                        0x7800000000000000
#define PTE_64_EXECUTE_DISABLE                                       0x8000000000000000

#define PT_ENTRY_64_PRESENT                                          0x01
#define PT_ENTRY_64_WRITE                                            0x02
#define PT_ENTRY_64_SUPERVISOR                                       0x04
#define PT_ENTRY_64_PAGE_LEVEL_WRITE_THROUGH                         0x08
#define PT_ENTRY_64_PAGE_LEVEL_CACHE_DISABLE                         0x10
#define PT_ENTRY_64_ACCESSED                                         0x20
#define PT_ENTRY_64_DIRTY                                            0x40
#define PT_ENTRY_64_LARGE_PAGE                                       0x80
#define PT_ENTRY_64_GLOBAL                                           0x100
#define PT_ENTRY_64_IGNORED_1                                        0xE00
#define PT_ENTRY_64_PAGE_FRAME_NUMBER                                0xFFFFFFFFF000
#define PT_ENTRY_64_IGNORED_2                                        0x7F0000000000000
#define PT_ENTRY_64_PROTECTION_KEY                                   0x7800000000000000
#define PT_ENTRY_64_EXECUTE_DISABLE                                  0x8000000000000000

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
} descriptor_32;
#pragma pack(pop)

#pragma pack(push, 1)
typedef struct {
  uint16_t limit;
  uint64_t base_address;
} descriptor_64;
#pragma pack(pop)

typedef struct {
  uint16_t segment_limit_low;
  uint16_t base_address_low;
  uint32_t bits;
} segment_descriptor_32;

typedef struct {
  uint16_t segment_limit_low;
  uint16_t base_address_low;
  uint32_t bits;
  uint32_t base_address_upper;
  uint32_t must_be_zero;
} segment_descriptor_64;

/**
 * @defgroup code_and_data_segment_descriptor_type \
 *           Code- and Data-Segment Descriptor Types
 * @{
 */
#define DESCRIPTOR_TYPE_DATA_R                                       0x00000000
#define DESCRIPTOR_TYPE_DATA_RA                                      0x00000001
#define DESCRIPTOR_TYPE_DATA_RW                                      0x00000002
#define DESCRIPTOR_TYPE_DATA_RWA                                     0x00000003
#define DESCRIPTOR_TYPE_DATA_RE                                      0x00000004
#define DESCRIPTOR_TYPE_DATA_REA                                     0x00000005
#define DESCRIPTOR_TYPE_DATA_RWE                                     0x00000006
#define DESCRIPTOR_TYPE_DATA_RWEA                                    0x00000007
#define DESCRIPTOR_TYPE_CODE_E                                       0x00000008
#define DESCRIPTOR_TYPE_CODE_EA                                      0x00000009
#define DESCRIPTOR_TYPE_CODE_ER                                      0x0000000A
#define DESCRIPTOR_TYPE_CODE_ERA                                     0x0000000B
#define DESCRIPTOR_TYPE_CODE_EC                                      0x0000000C
#define DESCRIPTOR_TYPE_CODE_ECA                                     0x0000000D
#define DESCRIPTOR_TYPE_CODE_ERC                                     0x0000000E
#define DESCRIPTOR_TYPE_CODE_ERCA                                    0x0000000F
/**
 * @}
 */

/**
 * @defgroup system_descriptor_type \
 *           System Descriptor Types
 * @{
 */
#define DESCRIPTOR_TYPE_RESERVED_1                                   0x00000000
#define DESCRIPTOR_TYPE_TSS_16_AVAILABLE                             0x00000001
#define DESCRIPTOR_TYPE_LDT                                          0x00000002
#define DESCRIPTOR_TYPE_TSS_16_BUSY                                  0x00000003
#define DESCRIPTOR_TYPE_CALL_GATE_16                                 0x00000004
#define DESCRIPTOR_TYPE_TASK_GATE                                    0x00000005
#define DESCRIPTOR_TYPE_INTERRUPT_GATE_16                            0x00000006
#define DESCRIPTOR_TYPE_TRAP_GATE_16                                 0x00000007
#define DESCRIPTOR_TYPE_RESERVED_2                                   0x00000008
#define DESCRIPTOR_TYPE_TSS_AVAILABLE                                0x00000009
#define DESCRIPTOR_TYPE_RESERVED_3                                   0x0000000A
#define DESCRIPTOR_TYPE_TSS_BUSY                                     0x0000000B
#define DESCRIPTOR_TYPE_CALL_GATE                                    0x0000000C
#define DESCRIPTOR_TYPE_RESERVED_4                                   0x0000000D
#define DESCRIPTOR_TYPE_INTERRUPT_GATE                               0x0000000E
#define DESCRIPTOR_TYPE_TRAP_GATE                                    0x0000000F
/**
 * @}
 */

#define SELECTOR_REQUEST_PRIVILEGE_LEVEL                             0x03
#define SELECTOR_TABLE_INDICATOR                                     0x04
#define SELECTOR_INDEX                                               0x1FFF8

/**
 * @}
 */

/**
 * @defgroup vmx \
 *           VMX
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
#define VMX_EXIT_QUALIFICATION_DEBUG_EXCEPTION_BREAKPOINT_CONDITION  0x0F
#define VMX_EXIT_QUALIFICATION_DEBUG_EXCEPTION_DEBUG_REGISTER_ACCESS_DETECTED 0x2000
#define VMX_EXIT_QUALIFICATION_DEBUG_EXCEPTION_SINGLE_INSTRUCTION    0x4000

#define VMX_EXIT_QUALIFICATION_TASK_SWITCH_SELECTOR                  0xFFFF
#define VMX_EXIT_QUALIFICATION_TASK_SWITCH_TYPE                      0xC0000000
#define VMX_EXIT_QUALIFICATION_TYPE_CALL                             0x00000000
#define VMX_EXIT_QUALIFICATION_TYPE_IRET                             0x00000001
#define VMX_EXIT_QUALIFICATION_TYPE_JMP                              0x00000002
#define VMX_EXIT_QUALIFICATION_TYPE_IDT                              0x00000003

#define VMX_EXIT_QUALIFICATION_CR_ACCESS_CR_NUMBER                   0x0F
#define VMX_EXIT_QUALIFICATION_REGISTER_CR0                          0x00000000
#define VMX_EXIT_QUALIFICATION_REGISTER_CR2                          0x00000002
#define VMX_EXIT_QUALIFICATION_REGISTER_CR3                          0x00000003
#define VMX_EXIT_QUALIFICATION_REGISTER_CR4                          0x00000004
#define VMX_EXIT_QUALIFICATION_REGISTER_CR8                          0x00000008
#define VMX_EXIT_QUALIFICATION_CR_ACCESS_ACCESS_TYPE                 0x30
#define VMX_EXIT_QUALIFICATION_ACCESS_MOV_TO_CR                      0x00000000
#define VMX_EXIT_QUALIFICATION_ACCESS_MOV_FROM_CR                    0x00000001
#define VMX_EXIT_QUALIFICATION_ACCESS_CLTS                           0x00000002
#define VMX_EXIT_QUALIFICATION_ACCESS_LMSW                           0x00000003
#define VMX_EXIT_QUALIFICATION_CR_ACCESS_LMSW_OPERAND_TYPE           0x40
#define VMX_EXIT_QUALIFICATION_LMSW_OP_REGISTER                      0x00000000
#define VMX_EXIT_QUALIFICATION_LMSW_OP_MEMORY                        0x00000001
#define VMX_EXIT_QUALIFICATION_CR_ACCESS_GENERAL_PURPOSE_REGISTER    0xF00
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
#define VMX_EXIT_QUALIFICATION_CR_ACCESS_LMSW_SOURCE_DATA            0xFFFF0000

#define VMX_EXIT_QUALIFICATION_DR_ACCESS_DR_NUMBER                   0x07
#define VMX_EXIT_QUALIFICATION_REGISTER_DR0                          0x00000000
#define VMX_EXIT_QUALIFICATION_REGISTER_DR1                          0x00000001
#define VMX_EXIT_QUALIFICATION_REGISTER_DR2                          0x00000002
#define VMX_EXIT_QUALIFICATION_REGISTER_DR3                          0x00000003
#define VMX_EXIT_QUALIFICATION_REGISTER_DR6                          0x00000006
#define VMX_EXIT_QUALIFICATION_REGISTER_DR7                          0x00000007
#define VMX_EXIT_QUALIFICATION_DR_ACCESS_DIRECTION_OF_ACCESS         0x10
#define VMX_EXIT_QUALIFICATION_DIRECTION_MOV_TO_DR                   0x00000000
#define VMX_EXIT_QUALIFICATION_DIRECTION_MOV_FROM_DR                 0x00000001
#define VMX_EXIT_QUALIFICATION_DR_ACCESS_GP_REGISTER                 0xF00
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

#define VMX_EXIT_QUALIFICATION_IO_INST_SIZE_OF_ACCESS                0x07
#define VMX_EXIT_QUALIFICATION_WIDTH_1B                              0x00000000
#define VMX_EXIT_QUALIFICATION_WIDTH_2B                              0x00000001
#define VMX_EXIT_QUALIFICATION_WIDTH_4B                              0x00000003
#define VMX_EXIT_QUALIFICATION_IO_INST_DIRECTION_OF_ACCESS           0x08
#define VMX_EXIT_QUALIFICATION_DIRECTION_OUT                         0x00000000
#define VMX_EXIT_QUALIFICATION_DIRECTION_IN                          0x00000001
#define VMX_EXIT_QUALIFICATION_IO_INST_STRING_INSTRUCTION            0x10
#define VMX_EXIT_QUALIFICATION_IS_STRING_NOT_STRING                  0x00000000
#define VMX_EXIT_QUALIFICATION_IS_STRING_STRING                      0x00000001
#define VMX_EXIT_QUALIFICATION_IO_INST_REP_PREFIXED                  0x20
#define VMX_EXIT_QUALIFICATION_IS_REP_NOT_REP                        0x00000000
#define VMX_EXIT_QUALIFICATION_IS_REP_REP                            0x00000001
#define VMX_EXIT_QUALIFICATION_IO_INST_OPERAND_ENCODING              0x40
#define VMX_EXIT_QUALIFICATION_ENCODING_DX                           0x00000000
#define VMX_EXIT_QUALIFICATION_ENCODING_IMM                          0x00000001
#define VMX_EXIT_QUALIFICATION_IO_INST_PORT_NUMBER                   0xFFFF0000

#define VMX_EXIT_QUALIFICATION_APIC_ACCESS_PAGE_OFFSET               0xFFF
#define VMX_EXIT_QUALIFICATION_APIC_ACCESS_ACCESS_TYPE               0xF000
#define VMX_EXIT_QUALIFICATION_TYPE_LINEAR_READ                      0x00000000
#define VMX_EXIT_QUALIFICATION_TYPE_LINEAR_WRITE                     0x00000001
#define VMX_EXIT_QUALIFICATION_TYPE_LINEAR_INSTR_FETCH               0x00000002
#define VMX_EXIT_QUALIFICATION_TYPE_LINEAR_EVENT_DELIVERY            0x00000003
#define VMX_EXIT_QUALIFICATION_TYPE_PHYSICAL_EVENT_DELIVERY          0x0000000A
#define VMX_EXIT_QUALIFICATION_TYPE_PHYSICAL_INSTR                   0x0000000F

#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_DATA_READ               0x01
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_DATA_WRITE              0x02
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_INSTRUCTION_FETCH       0x04
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_ENTRY_PRESENT           0x08
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_ENTRY_WRITE             0x10
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_ENTRY_EXECUTE           0x20
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_ENTRY_EXECUTE_FOR_USER_MODE 0x40
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_VALID_GUEST_LINEAR_ADDRESS 0x80
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_EPT_TRANSLATED_ACCESS   0x100
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_USER_MODE_LINEAR_ADDRESS 0x200
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_READABLE_WRITABLE_PAGE  0x400
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_EXECUTE_DISABLE_PAGE    0x800
#define VMX_EXIT_QUALIFICATION_EPT_VIOLATION_NMI_UNBLOCKING          0x1000

/**
 * @}
 */

#define VMX_ACCESS_RIGHTS_TYPE                                       0x0F
#define VMX_ACCESS_RIGHTS_DESCRIPTOR_TYPE                            0x10
#define VMX_ACCESS_RIGHTS_DESCRIPTOR_PRIVILEGE_LEVEL                 0x60
#define VMX_ACCESS_RIGHTS_PRESENT                                    0x80
#define VMX_ACCESS_RIGHTS_AVAILABLE_BIT                              0x1000
#define VMX_ACCESS_RIGHTS_LONG_MODE                                  0x2000
#define VMX_ACCESS_RIGHTS_DEFAULT_BIG                                0x4000
#define VMX_ACCESS_RIGHTS_GRANULARITY                                0x8000
#define VMX_ACCESS_RIGHTS_UNUSABLE                                   0x10000

#define VMX_INTERRUPTIBILITY_STATE_BLOCKING_BY_STI                   0x01
#define VMX_INTERRUPTIBILITY_STATE_BLOCKING_BY_MOV_SS                0x02
#define VMX_INTERRUPTIBILITY_STATE_BLOCKING_BY_SMI                   0x04
#define VMX_INTERRUPTIBILITY_STATE_BLOCKING_BY_NMI                   0x08
#define VMX_INTERRUPTIBILITY_STATE_ENCLAVE_INTERRUPTION              0x10

#define VMX_ACTIVE                                                   0x00000000
#define VMX_HLT                                                      0x00000001
#define VMX_SHUTDOWN                                                 0x00000002
#define VMX_WAIT_FOR_SIPI                                            0x00000003
/**
 * @}
 */

/**
 * @defgroup vmx_ept \
 *           The extended page-table mechanism
 * @{
 */
#define VMX_EPTP_MEMORY_TYPE                                         0x07
#define VMX_EPTP_PAGE_WALK_LENGTH                                    0x38
#define VMX_EPTP_ENABLE_ACCESS_AND_DIRTY_FLAGS                       0x40
#define VMX_EPTP_PAGE_FRAME_NUMBER                                   0xFFFFFFFFF000

#define VMX_EPML4E_READ_ACCESS                                       0x01
#define VMX_EPML4E_WRITE_ACCESS                                      0x02
#define VMX_EPML4E_EXECUTE_ACCESS                                    0x04
#define VMX_EPML4E_ACCESSED                                          0x100
#define VMX_EPML4E_USER_MODE_EXECUTE                                 0x400
#define VMX_EPML4E_PAGE_FRAME_NUMBER                                 0xFFFFFFFFF000

#define VMX_EPT_PDPTE_1GB_READ_ACCESS                                0x01
#define VMX_EPT_PDPTE_1GB_WRITE_ACCESS                               0x02
#define VMX_EPT_PDPTE_1GB_EXECUTE_ACCESS                             0x04
#define VMX_EPT_PDPTE_1GB_MEMORY_TYPE                                0x38
#define VMX_EPT_PDPTE_1GB_IGNORE_PAT                                 0x40
#define VMX_EPT_PDPTE_1GB_LARGE_PAGE                                 0x80
#define VMX_EPT_PDPTE_1GB_ACCESSED                                   0x100
#define VMX_EPT_PDPTE_1GB_DIRTY                                      0x200
#define VMX_EPT_PDPTE_1GB_USER_MODE_EXECUTE                          0x400
#define VMX_EPT_PDPTE_1GB_PAGE_FRAME_NUMBER                          0xFFFFC0000000
#define VMX_EPT_PDPTE_1GB_SUPPRESS_VE                                0x8000000000000000

#define VMX_EPT_PDPTE_READ_ACCESS                                    0x01
#define VMX_EPT_PDPTE_WRITE_ACCESS                                   0x02
#define VMX_EPT_PDPTE_EXECUTE_ACCESS                                 0x04
#define VMX_EPT_PDPTE_ACCESSED                                       0x100
#define VMX_EPT_PDPTE_USER_MODE_EXECUTE                              0x400
#define VMX_EPT_PDPTE_PAGE_FRAME_NUMBER                              0xFFFFFFFFF000

#define VMX_EPT_PDE_2MB_READ_ACCESS                                  0x01
#define VMX_EPT_PDE_2MB_WRITE_ACCESS                                 0x02
#define VMX_EPT_PDE_2MB_EXECUTE_ACCESS                               0x04
#define VMX_EPT_PDE_2MB_MEMORY_TYPE                                  0x38
#define VMX_EPT_PDE_2MB_IGNORE_PAT                                   0x40
#define VMX_EPT_PDE_2MB_LARGE_PAGE                                   0x80
#define VMX_EPT_PDE_2MB_ACCESSED                                     0x100
#define VMX_EPT_PDE_2MB_DIRTY                                        0x200
#define VMX_EPT_PDE_2MB_USER_MODE_EXECUTE                            0x400
#define VMX_EPT_PDE_2MB_PAGE_FRAME_NUMBER                            0xFFFFFFE00000
#define VMX_EPT_PDE_2MB_SUPPRESS_VE                                  0x8000000000000000

#define VMX_EPT_PDE_READ_ACCESS                                      0x01
#define VMX_EPT_PDE_WRITE_ACCESS                                     0x02
#define VMX_EPT_PDE_EXECUTE_ACCESS                                   0x04
#define VMX_EPT_PDE_ACCESSED                                         0x100
#define VMX_EPT_PDE_USER_MODE_EXECUTE                                0x400
#define VMX_EPT_PDE_PAGE_FRAME_NUMBER                                0xFFFFFFFFF000

#define VMX_EPT_PTE_READ_ACCESS                                      0x01
#define VMX_EPT_PTE_WRITE_ACCESS                                     0x02
#define VMX_EPT_PTE_EXECUTE_ACCESS                                   0x04
#define VMX_EPT_PTE_MEMORY_TYPE                                      0x38
#define VMX_EPT_PTE_IGNORE_PAT                                       0x40
#define VMX_EPT_PTE_ACCESSED                                         0x100
#define VMX_EPT_PTE_DIRTY                                            0x200
#define VMX_EPT_PTE_USER_MODE_EXECUTE                                0x400
#define VMX_EPT_PTE_PAGE_FRAME_NUMBER                                0xFFFFFFFFF000
#define VMX_EPT_PTE_SUPPRESS_VE                                      0x8000000000000000

#define VMX_EPT_ENTRY_READ_ACCESS                                    0x01
#define VMX_EPT_ENTRY_WRITE_ACCESS                                   0x02
#define VMX_EPT_ENTRY_EXECUTE_ACCESS                                 0x04
#define VMX_EPT_ENTRY_MEMORY_TYPE                                    0x38
#define VMX_EPT_ENTRY_IGNORE_PAT                                     0x40
#define VMX_EPT_ENTRY_LARGE_PAGE                                     0x80
#define VMX_EPT_ENTRY_ACCESSED                                       0x100
#define VMX_EPT_ENTRY_DIRTY                                          0x200
#define VMX_EPT_ENTRY_USER_MODE_EXECUTE                              0x400
#define VMX_EPT_ENTRY_PAGE_FRAME_NUMBER                              0xFFFFFFFFF000
#define VMX_EPT_ENTRY_SUPPRESS_VE                                    0x8000000000000000

/**
 * @defgroup vmx_ept_table_level \
 *           EPT Table level numbers
 * @{
 */
#define VMX_LEVEL_PML4E                                              0x00000003
#define VMX_LEVEL_PDPTE                                              0x00000002
#define VMX_LEVEL_PDE                                                0x00000001
#define VMX_LEVEL_PTE                                                0x00000000
/**
 * @}
 */

/**
 * @defgroup vmx_ept_entry_count \
 *           EPT Entry counts
 * @{
 */
#define VMX_PML4_ENTRY_COUNT                                         0x00000200
#define VMX_PDPTE_ENTRY_COUNT                                        0x00000200
#define VMX_PDE_ENTRY_COUNT                                          0x00000200
/**
 * @}
 */

/**
 * @defgroup vmx_ept_memory_type \
 *           EPT memory type
 * @{
 */
#define VMX_EPT_MEMORY_TYPE_UC                                       0x00000000
#define VMX_EPT_MEMORY_TYPE_WC                                       0x00000001
#define VMX_EPT_MEMORY_TYPE_WT                                       0x00000004
#define VMX_EPT_MEMORY_TYPE_WP                                       0x00000005
#define VMX_EPT_MEMORY_TYPE_WB                                       0x00000006
#define VMX_EPT_MEMORY_TYPE_UNCACHED                                 0x00000007
#define VMX_EPT_MEMORY_TYPE_INVALID                                  0x000000FF
/**
 * @}
 */

/**
 * @}
 */

#define VMX_INVEPT_SINGLE_CONTEXT                                    0x00000001
#define VMX_INVEPT_ALL_CONTEXT                                       0x00000002
/**
 * @}
 */

#define VMX_INVVPID_INDIVIDUAL_ADDRESS                               0x00000000
#define VMX_INVVPID_SINGLE_CONTEXT                                   0x00000001
#define VMX_INVVPID_ALL_CONTEXT                                      0x00000002
#define VMX_INVVPID_SINGLE_CONTEXT_RETAINING_GLOBALS                 0x00000003
/**
 * @}
 */

typedef struct {
  uint64_t ept_pointer;
  uint64_t reserved;
} vmx_invept_descriptor;

typedef struct {
  uint16_t vpid;
  uint16_t reserved1;
  uint32_t reserved2;
  uint64_t linear_address;
} vmx_invvpid_descriptor;

typedef struct {
  uint32_t revision_id;
  uint32_t abort_indicator;
  uint8_t data[4088];
} vmx_vmcs;

/**
 * @defgroup vmx_vmcs_group \
 *           VMCS (VM Control Structure)
 * @{
 */
#define VMX_VMCS_COMPONENT_ENCODING_ACCESS_TYPE                      0x01
#define VMX_VMCS_COMPONENT_ENCODING_INDEX                            0x3FE
#define VMX_VMCS_COMPONENT_ENCODING_TYPE                             0xC00
#define VMX_VMCS_COMPONENT_ENCODING_MUST_BE_ZERO                     0x1000
#define VMX_VMCS_COMPONENT_ENCODING_WIDTH                            0x6000

/**
 * @defgroup vmx_vmcs_16_bit \
 *           16-Bit Fields
 * @{
 */
/**
 * @defgroup vmx_vmcs_16_bit_control_fields \
 *           16-Bit Control Fields
 * @{
 */
#define VMX_VMCS_CTRL_VPID                                           0x00000000
#define VMX_VMCS_CTRL_POSTED_INTR_NOTIFY_VECTOR                      0x00000002
#define VMX_VMCS_CTRL_EPTP_INDEX                                     0x00000004
/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_16_bit_guest_state_fields \
 *           16-Bit Guest-State Fields
 * @{
 */
#define VMX_VMCS_GUEST_ES_SEL                                        0x00000800
#define VMX_VMCS_GUEST_CS_SEL                                        0x00000802
#define VMX_VMCS_GUEST_SS_SEL                                        0x00000804
#define VMX_VMCS_GUEST_DS_SEL                                        0x00000806
#define VMX_VMCS_GUEST_FS_SEL                                        0x00000808
#define VMX_VMCS_GUEST_GS_SEL                                        0x0000080A
#define VMX_VMCS_GUEST_LDTR_SEL                                      0x0000080C
#define VMX_VMCS_GUEST_TR_SEL                                        0x0000080E
#define VMX_VMCS_GUEST_INTR_STATUS                                   0x00000810
#define VMX_VMCS_GUEST_PML_INDEX                                     0x00000812
/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_16_bit_host_state_fields \
 *           16-Bit Host-State Fields
 * @{
 */
#define VMX_VMCS_HOST_ES_SEL                                         0x00000C00
#define VMX_VMCS_HOST_CS_SEL                                         0x00000C02
#define VMX_VMCS_HOST_SS_SEL                                         0x00000C04
#define VMX_VMCS_HOST_DS_SEL                                         0x00000C06
#define VMX_VMCS_HOST_FS_SEL                                         0x00000C08
#define VMX_VMCS_HOST_GS_SEL                                         0x00000C0A
#define VMX_VMCS_HOST_TR_SEL                                         0x00000C0C
/**
 * @}
 */

/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_64_bit \
 *           64-Bit Fields
 * @{
 */
/**
 * @defgroup vmx_vmcs_64_bit_control_fields \
 *           64-Bit Control Fields
 * @{
 */
#define VMX_VMCS_CTRL_IO_BITMAP_A                                    0x00002000
#define VMX_VMCS_CTRL_IO_BITMAP_B                                    0x00002002
#define VMX_VMCS_CTRL_MSR_BITMAP                                     0x00002004
#define VMX_VMCS_CTRL_VMEXIT_MSR_STORE                               0x00002006
#define VMX_VMCS_CTRL_VMEXIT_MSR_LOAD                                0x00002008
#define VMX_VMCS_CTRL_VMENTRY_MSR_LOAD                               0x0000200A
#define VMX_VMCS_CTRL_EXEC_VMCS_PTR                                  0x0000200C
#define VMX_VMCS_CTRL_PML_ADDR                                       0x0000200E
#define VMX_VMCS_CTRL_TSC_OFFSET                                     0x00002010
#define VMX_VMCS_CTRL_VAPIC_PAGEADDR                                 0x00002012
#define VMX_VMCS_CTRL_APIC_ACCESSADDR                                0x00002014
#define VMX_VMCS_CTRL_POSTED_INTR_DESC                               0x00002016
#define VMX_VMCS_CTRL_VMFUNC_CTRLS                                   0x00002018
#define VMX_VMCS_CTRL_EPTP                                           0x0000201A
#define VMX_VMCS_CTRL_EOI_BITMAP_0                                   0x0000201C
#define VMX_VMCS_CTRL_EOI_BITMAP_1                                   0x0000201E
#define VMX_VMCS_CTRL_EOI_BITMAP_2                                   0x00002020
#define VMX_VMCS_CTRL_EOI_BITMAP_3                                   0x00002022
#define VMX_VMCS_CTRL_EPTP_LIST                                      0x00002024
#define VMX_VMCS_CTRL_VMREAD_BITMAP                                  0x00002026
#define VMX_VMCS_CTRL_VMWRITE_BITMAP                                 0x00002028
#define VMX_VMCS_CTRL_VIRTXCPT_INFO_ADDR                             0x0000202A
#define VMX_VMCS_CTRL_XSS_EXITING_BITMAP                             0x0000202C
#define VMX_VMCS_CTRL_ENCLS_EXITING_BITMAP                           0x0000202E
#define VMX_VMCS_CTRL_TSC_MULTIPLIER                                 0x00002032
/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_64_bit_read_only_data_fields \
 *           64-Bit Read-Only Data Field
 * @{
 */
#define VMX_VMCS_GUEST_PHYS_ADDR                                     0x00002400
/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_64_bit_guest_state_fields \
 *           64-Bit Guest-State Fields
 * @{
 */
#define VMX_VMCS_GUEST_VMCS_LINK_PTR                                 0x00002800
#define VMX_VMCS_GUEST_DEBUGCTL                                      0x00002802
#define VMX_VMCS_GUEST_PAT                                           0x00002804
#define VMX_VMCS_GUEST_EFER                                          0x00002806
#define VMX_VMCS_GUEST_PERF_GLOBAL_CTRL                              0x00002808
#define VMX_VMCS_GUEST_PDPTE0                                        0x0000280A
#define VMX_VMCS_GUEST_PDPTE1                                        0x0000280C
#define VMX_VMCS_GUEST_PDPTE2                                        0x0000280E
#define VMX_VMCS_GUEST_PDPTE3                                        0x00002810
/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_64_bit_host_state_fields \
 *           64-Bit Host-State Fields
 * @{
 */
#define VMX_VMCS_HOST_PAT                                            0x00002C00
#define VMX_VMCS_HOST_EFER                                           0x00002C02
#define VMX_VMCS_HOST_PERF_GLOBAL_CTRL                               0x00002C04
/**
 * @}
 */

/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_32_bit \
 *           32-Bit Fields
 * @{
 */
/**
 * @defgroup vmx_vmcs_32_bit_control_fields \
 *           32-Bit Control Fields
 * @{
 */
#define VMX_VMCS_CTRL_PIN_EXEC                                       0x00004000
#define VMX_VMCS_CTRL_PROC_EXEC                                      0x00004002
#define VMX_VMCS_CTRL_EXCEPTION_BITMAP                               0x00004004
#define VMX_VMCS_CTRL_PAGEFAULT_ERROR_MASK                           0x00004006
#define VMX_VMCS_CTRL_PAGEFAULT_ERROR_MATCH                          0x00004008
#define VMX_VMCS_CTRL_CR3_TARGET_COUNT                               0x0000400A
#define VMX_VMCS_CTRL_EXIT                                           0x0000400C
#define VMX_VMCS_CTRL_EXIT_MSR_STORE_COUNT                           0x0000400E
#define VMX_VMCS_CTRL_EXIT_MSR_LOAD_COUNT                            0x00004010
#define VMX_VMCS_CTRL_ENTRY                                          0x00004012
#define VMX_VMCS_CTRL_ENTRY_MSR_LOAD_COUNT                           0x00004014
#define VMX_VMCS_CTRL_ENTRY_INTERRUPTION_INFO                        0x00004016
#define VMX_VMCS_CTRL_ENTRY_EXCEPTION_ERRCODE                        0x00004018
#define VMX_VMCS_CTRL_ENTRY_INSTR_LENGTH                             0x0000401A
#define VMX_VMCS_CTRL_TPR_THRESHOLD                                  0x0000401C
#define VMX_VMCS_CTRL_PROC_EXEC2                                     0x0000401E
#define VMX_VMCS_CTRL_PLE_GAP                                        0x00004020
#define VMX_VMCS_CTRL_PLE_WINDOW                                     0x00004022
/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_32_bit_read_only_data_fields \
 *           32-Bit Read-Only Data Fields
 * @{
 */
#define VMX_VMCS_VM_INSTR_ERROR                                      0x00004400
#define VMX_VMCS_EXIT_REASON                                         0x00004402
#define VMX_VMCS_EXIT_INTERRUPTION_INFO                              0x00004404
#define VMX_VMCS_EXIT_INTERRUPTION_ERROR_CODE                        0x00004406
#define VMX_VMCS_IDT_VECTORING_INFO                                  0x00004408
#define VMX_VMCS_IDT_VECTORING_ERROR_CODE                            0x0000440A
#define VMX_VMCS_EXIT_INSTR_LENGTH                                   0x0000440C
#define VMX_VMCS_EXIT_INSTR_INFO                                     0x0000440E
/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_32_bit_guest_state_fields \
 *           32-Bit Guest-State Fields
 * @{
 */
#define VMX_VMCS_GUEST_ES_LIMIT                                      0x00004800
#define VMX_VMCS_GUEST_CS_LIMIT                                      0x00004802
#define VMX_VMCS_GUEST_SS_LIMIT                                      0x00004804
#define VMX_VMCS_GUEST_DS_LIMIT                                      0x00004806
#define VMX_VMCS_GUEST_FS_LIMIT                                      0x00004808
#define VMX_VMCS_GUEST_GS_LIMIT                                      0x0000480A
#define VMX_VMCS_GUEST_LDTR_LIMIT                                    0x0000480C
#define VMX_VMCS_GUEST_TR_LIMIT                                      0x0000480E
#define VMX_VMCS_GUEST_GDTR_LIMIT                                    0x00004810
#define VMX_VMCS_GUEST_IDTR_LIMIT                                    0x00004812
#define VMX_VMCS_GUEST_ES_ACCESS_RIGHTS                              0x00004814
#define VMX_VMCS_GUEST_CS_ACCESS_RIGHTS                              0x00004816
#define VMX_VMCS_GUEST_SS_ACCESS_RIGHTS                              0x00004818
#define VMX_VMCS_GUEST_DS_ACCESS_RIGHTS                              0x0000481A
#define VMX_VMCS_GUEST_FS_ACCESS_RIGHTS                              0x0000481C
#define VMX_VMCS_GUEST_GS_ACCESS_RIGHTS                              0x0000481E
#define VMX_VMCS_GUEST_LDTR_ACCESS_RIGHTS                            0x00004820
#define VMX_VMCS_GUEST_TR_ACCESS_RIGHTS                              0x00004822
#define VMX_VMCS_GUEST_INTERRUPTIBILITY_STATE                        0x00004824
#define VMX_VMCS_GUEST_ACTIVITY_STATE                                0x00004826
#define VMX_VMCS_GUEST_SMBASE                                        0x00004828
#define VMX_VMCS_GUEST_SYSENTER_CS                                   0x0000482A
#define VMX_VMCS_GUEST_PREEMPT_TIMER_VALUE                           0x0000482E
/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_32_bit_host_state_fields \
 *           32-Bit Host-State Field
 * @{
 */
#define VMX_VMCS_SYSENTER_CS                                         0x00004C00
/**
 * @}
 */

/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_natural_width \
 *           Natural-Width Fields
 * @{
 */
/**
 * @defgroup vmx_vmcs_natural_width_control_fields \
 *           Natural-Width Control Fields
 * @{
 */
#define VMX_VMCS_CTRL_CR0_MASK                                       0x00006000
#define VMX_VMCS_CTRL_CR4_MASK                                       0x00006002
#define VMX_VMCS_CTRL_CR0_READ_SHADOW                                0x00006004
#define VMX_VMCS_CTRL_CR4_READ_SHADOW                                0x00006006
#define VMX_VMCS_CTRL_CR3_TARGET_VAL0                                0x00006008
#define VMX_VMCS_CTRL_CR3_TARGET_VAL1                                0x0000600A
#define VMX_VMCS_CTRL_CR3_TARGET_VAL2                                0x0000600C
#define VMX_VMCS_CTRL_CR3_TARGET_VAL3                                0x0000600E
/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_natural_width_read_only_data_fields \
 *           Natural-Width Read-Only Data Fields
 * @{
 */
#define VMX_VMCS_EXIT_QUALIFICATION                                  0x00006400
#define VMX_VMCS_IO_RCX                                              0x00006402
#define VMX_VMCS_IO_RSX                                              0x00006404
#define VMX_VMCS_IO_RDI                                              0x00006406
#define VMX_VMCS_IO_RIP                                              0x00006408
#define VMX_VMCS_EXIT_GUEST_LINEAR_ADDR                              0x0000640A
/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_natural_width_guest_state_fields \
 *           Natural-Width Guest-State Fields
 * @{
 */
#define VMX_VMCS_GUEST_CR0                                           0x00006800
#define VMX_VMCS_GUEST_CR3                                           0x00006802
#define VMX_VMCS_GUEST_CR4                                           0x00006804
#define VMX_VMCS_GUEST_ES_BASE                                       0x00006806
#define VMX_VMCS_GUEST_CS_BASE                                       0x00006808
#define VMX_VMCS_GUEST_SS_BASE                                       0x0000680A
#define VMX_VMCS_GUEST_DS_BASE                                       0x0000680C
#define VMX_VMCS_GUEST_FS_BASE                                       0x0000680E
#define VMX_VMCS_GUEST_GS_BASE                                       0x00006810
#define VMX_VMCS_GUEST_LDTR_BASE                                     0x00006812
#define VMX_VMCS_GUEST_TR_BASE                                       0x00006814
#define VMX_VMCS_GUEST_GDTR_BASE                                     0x00006816
#define VMX_VMCS_GUEST_IDTR_BASE                                     0x00006818
#define VMX_VMCS_GUEST_DR7                                           0x0000681A
#define VMX_VMCS_GUEST_RSP                                           0x0000681C
#define VMX_VMCS_GUEST_RIP                                           0x0000681E
#define VMX_VMCS_GUEST_RFLAGS                                        0x00006820
#define VMX_VMCS_GUEST_PENDING_DEBUG_EXCEPTIONS                      0x00006822
#define VMX_VMCS_GUEST_SYSENTER_ESP                                  0x00006824
#define VMX_VMCS_GUEST_SYSENTER_EIP                                  0x00006826
/**
 * @}
 */

/**
 * @defgroup vmx_vmcs_natural_width_host_state_fields \
 *           Natural-Width Host-State Fields
 * @{
 */
#define VMX_VMCS_HOST_CR0                                            0x00006C00
#define VMX_VMCS_HOST_CR3                                            0x00006C02
#define VMX_VMCS_HOST_CR4                                            0x00006C04
#define VMX_VMCS_HOST_FS_BASE                                        0x00006C06
#define VMX_VMCS_HOST_GS_BASE                                        0x00006C08
#define VMX_VMCS_HOST_TR_BASE                                        0x00006C0A
#define VMX_VMCS_HOST_GDTR_BASE                                      0x00006C0C
#define VMX_VMCS_HOST_IDTR_BASE                                      0x00006C0E
#define VMX_VMCS_HOST_SYSENTER_ESP                                   0x00006C10
#define VMX_VMCS_HOST_SYSENTER_EIP                                   0x00006C12
#define VMX_VMCS_HOST_RSP                                            0x00006C14
#define VMX_VMCS_HOST_RIP                                            0x00006C16
/**
 * @}
 */

/**
 * @}
 */

/**
 * @}
 */

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

#define EFL_CARRY_FLAG                                               0x01
#define EFL_READ_AS_1                                                0x02
#define EFL_PARITY_FLAG                                              0x04
#define EFL_AUXILIARY_CARRY_FLAG                                     0x10
#define EFL_ZERO_FLAG                                                0x40
#define EFL_SIGN_FLAG                                                0x80
#define EFL_TRAP_FLAG                                                0x100
#define EFL_INTERRUPT_ENABLE_FLAG                                    0x200
#define EFL_DIRECTION_FLAG                                           0x400
#define EFL_OVERFLOW_FLAG                                            0x800
#define EFL_IO_PRIVILEGE_LEVEL                                       0x3000
#define EFL_NESTED_TASK_FLAG                                         0x4000
#define EFL_RESUME_FLAG                                              0x10000
#define EFL_VIRTUAL_8086_MODE_FLAG                                   0x20000
#define EFL_ALIGNMENT_CHECK_FLAG                                     0x40000
#define EFL_VIRTUAL_INTERRUPT_FLAG                                   0x80000
#define EFL_VIRTUAL_INTERRUPT_PENDING_FLAG                           0x100000
#define EFL_IDENTIFICATION_FLAG                                      0x200000

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
#define MEMORY_TYPE_UNCACHED                                         0x00000007
#define MEMORY_TYPE_INVALID                                          0x000000FF
/**
 * @}
 */

/**
 * @}
 */


