# Benchmark Comparison Report

## Configuration

### Baseline
- **File**: `baseline-results.json`
- **Timestamp**: 2025-12-06T01:18:18.230145
- **Device**: Unknown
- **Driver**: Unknown
- **Iterations**: 10

### Comparison
- **File**: `lazy-init-results.json`
- **Timestamp**: 2025-12-06T01:29:19.681505
- **Device**: Unknown
- **Driver**: Unknown
- **Iterations**: 10

---

## Executive Summary

**Overall Performance Change**: -8.2%

### 🚀 Top Improvements (62 tests >10% faster)

- **+71.4%** - ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCompletion=1 BarrierSynchro=1 KernelExecTime=1 EventSync=0 ioq=0) (api_overhead_benchmark_l0/ExecuteCommandList)
- **+69.0%** - UsmMemoryAllocation(api=l0 type=Shared size=4 measureMode=Both) (api_overhead_benchmark_l0/UsmMemoryAllocation)
- **+67.9%** - UsmMemoryAllocation(api=l0 type=Shared size=4 measureMode=Free) (api_overhead_benchmark_l0/UsmMemoryAllocation)
- **+66.9%** - EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=none wait=none eventCount=1000) (api_overhead_benchmark_l0/EventCreation)
- **+64.0%** - ExecuteCommandListForCopyEngine(api=l0 UseFence=1 measureCompletionTime=0) (api_overhead_benchmark_l0/ExecuteCommandList)
- **+63.5%** - ExecuteCommandListForCopyEngine(api=l0 UseFence=0 measureCompletionTime=0) (api_overhead_benchmark_l0/ExecuteCommandList)
- **+59.9%** - EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=device wait=device eventCount=1000) (api_overhead_benchmark_l0/EventCreation)
- **+58.2%** - DriverGet(api=l0 getDriverCount=1) (api_overhead_benchmark_l0/DriverGet)
- **+57.0%** - EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=none wait=subdevice eventCount=1000) (api_overhead_benchmark_l0/EventCreation)
- **+55.7%** - ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCompletion=1 BarrierSynchro=0 KernelExecTime=1 EventSync=1 ioq=0) (api_overhead_benchmark_l0/ExecuteCommandList)

### ⚠️ Regressions (161 tests >10% slower)

- **-241.5%** - UsmMemoryAllocation(api=l0 type=Host size=64MB measureMode=Allocate) (api_overhead_benchmark_l0/UsmMemoryAllocation)
- **-225.3%** - EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=host wait=host eventCount=1000) (api_overhead_benchmark_l0/EventCreation)
- **-210.0%** - EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=device wait=subdevice eventCount=1000) (api_overhead_benchmark_l0/EventCreation)
- **-186.0%** - ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureCompletionTime=0 src=Device dst=Device size=64MB ioq=1 withCopyOffload=1) (api_overhead_benchmark_l0/ExecuteCommandList)
- **-170.1%** - EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=subdevice wait=none eventCount=1000) (api_overhead_benchmark_l0/EventCreation)
- **-156.1%** - EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=host wait=device eventCount=1000) (api_overhead_benchmark_l0/EventCreation)
- **-154.8%** - UsmMemoryAllocation(api=l0 type=Device size=512MB measureMode=Allocate) (api_overhead_benchmark_l0/UsmMemoryAllocation)
- **-123.6%** - EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=subdevice wait=none eventCount=1000) (api_overhead_benchmark_l0/EventCreation)
- **-120.0%** - ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIndirectAllocations=100 placement=Host) (api_overhead_benchmark_l0/ExecuteCommandList)
- **-117.9%** - EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=subdevice wait=host eventCount=1000) (api_overhead_benchmark_l0/EventCreation)

---


## api_overhead_benchmark_l0/AppendLaunchKernel

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| AppendLaunchKernel(api=l0 wgc=1 wgs=1 event=1 appendCount... | 4.731 µs | 3.034 µs | +35.9% | 🚀 |
| AppendLaunchKernel(api=l0 wgc=1 wgs=256 event=0 appendCou... | 5.598 µs | 4.386 µs | +21.7% | 🚀 |
| AppendLaunchKernel(api=l0 wgc=1 wgs=256 event=1 appendCou... | 5.987 µs | 5.730 µs | +4.3% | ✓ |
| AppendLaunchKernel(api=l0 wgc=1000 wgs=1 event=0 appendCo... | 5.634 µs | 5.655 µs | -0.4% | ≈ |
| AppendLaunchKernel(api=l0 wgc=1 wgs=1 event=0 appendCount... | 1.885 µs | 1.912 µs | -1.4% | ↓ |
| AppendLaunchKernel(api=l0 wgc=1000 wgs=1 event=1 appendCo... | 6.127 µs | 6.222 µs | -1.6% | ↓ |
| AppendLaunchKernel(api=l0 wgc=1000 wgs=256 event=0 append... | 5.473 µs | 5.662 µs | -3.5% | ↓ |
| AppendLaunchKernel(api=l0 wgc=1000 wgs=256 event=1 append... | 4.700 µs | 6.213 µs | -32.2% | 🔴 |

**Category Average**: +2.9% change

---

## api_overhead_benchmark_l0/CreateCommandList

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| CreateCommandListImmediate(api=l0 CmdListCount=1000 ioq=0) | 3479.478 µs | 2861.089 µs | +17.8% | ✅ |
| CreateCommandListImmediate(api=l0 CmdListCount=1000 ioq=1) | 3969.081 µs | 3373.599 µs | +15.0% | ✅ |
| CreateCommandListImmediate(api=l0 CmdListCount=100 ioq=0) | 361.192 µs | 339.524 µs | +6.0% | ✓ |
| CreateCommandList(api=l0 CmdListCount=100 CopyOnly=0) | 181.439 µs | 215.924 µs | -19.0% | ⚠️ |
| CreateCommandListImmediate(api=l0 CmdListCount=100 ioq=1) | 420.362 µs | 559.293 µs | -33.1% | 🔴 |
| CreateCommandList(api=l0 CmdListCount=100 CopyOnly=1) | 131.989 µs | 189.343 µs | -43.5% | 🔴 |

**Category Average**: -9.5% change

---

## api_overhead_benchmark_l0/DriverGet

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| DriverGet(api=l0 getDriverCount=1) | 0.141 µs | 0.059 µs | +58.2% | 🚀 |
| DriverGet(api=l0 getDriverCount=1) | 0.089 µs | 0.059 µs | +33.7% | 🚀 |
| DriverGetProperties(api=l0) | 0.142 µs | 0.140 µs | +1.4% | ✓ |
| DriverGetApiVersion(api=l0) | 0.132 µs | 0.132 µs | +0.0% | ≈ |
| DriverGet(api=l0 getDriverCount=0) | 0.067 µs | 0.068 µs | -1.5% | ↓ |

**Category Average**: +18.4% change

---

## api_overhead_benchmark_l0/EventCreation

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 2.409 µs | 0.797 µs | +66.9% | 🚀 |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 2.578 µs | 1.034 µs | +59.9% | 🚀 |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 2.309 µs | 0.994 µs | +57.0% | 🚀 |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 1.534 µs | 0.866 µs | +43.5% | 🚀 |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 1.564 µs | 0.930 µs | +40.5% | 🚀 |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 1.429 µs | 0.891 µs | +37.6% | 🚀 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.992 µs | 0.675 µs | +32.0% | 🚀 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 1.134 µs | 0.841 µs | +25.8% | 🚀 |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 1.027 µs | 0.771 µs | +24.9% | 🚀 |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 1.415 µs | 1.069 µs | +24.5% | 🚀 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.871 µs | 0.683 µs | +21.6% | 🚀 |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 1.304 µs | 1.037 µs | +20.5% | 🚀 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 1.077 µs | 0.901 µs | +16.3% | ✅ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.980 µs | 0.842 µs | +14.1% | ✅ |
| EventQueryStatus(api=l0 eventSignaled=1) | 0.085 µs | 0.075 µs | +11.8% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 1.157 µs | 1.026 µs | +11.3% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.926 µs | 0.833 µs | +10.0% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 1.093 µs | 0.999 µs | +8.6% | ✓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.995 µs | 0.917 µs | +7.8% | ✓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.837 µs | 0.786 µs | +6.1% | ✓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.844 µs | 0.811 µs | +3.9% | ✓ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 1.035 µs | 1.007 µs | +2.7% | ✓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.848 µs | 0.831 µs | +2.0% | ✓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.904 µs | 0.893 µs | +1.2% | ✓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.882 µs | 0.881 µs | +0.1% | ≈ |
| EventQueryStatus(api=l0 eventSignaled=0) | 1.545 µs | 1.550 µs | -0.3% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.859 µs | 0.871 µs | -1.4% | ↓ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.849 µs | 0.877 µs | -3.3% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.911 µs | 0.942 µs | -3.4% | ↓ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 1.008 µs | 1.043 µs | -3.5% | ↓ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 1.227 µs | 1.289 µs | -5.1% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.818 µs | 0.865 µs | -5.7% | ↓ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.950 µs | 1.006 µs | -5.9% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.875 µs | 0.929 µs | -6.2% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.869 µs | 0.932 µs | -7.2% | ↓ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.852 µs | 0.916 µs | -7.5% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.834 µs | 0.909 µs | -9.0% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.760 µs | 0.833 µs | -9.6% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.819 µs | 0.903 µs | -10.3% | ⚠️ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.929 µs | 1.050 µs | -13.0% | ⚠️ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.814 µs | 0.928 µs | -14.0% | ⚠️ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.835 µs | 0.953 µs | -14.1% | ⚠️ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.801 µs | 0.944 µs | -17.9% | ⚠️ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.840 µs | 1.000 µs | -19.0% | ⚠️ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.927 µs | 1.112 µs | -20.0% | ⚠️ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 1.001 µs | 1.208 µs | -20.7% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.708 µs | 0.856 µs | -20.9% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.832 µs | 1.027 µs | -23.4% | 🔴 |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.691 µs | 0.856 µs | -23.9% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.710 µs | 0.883 µs | -24.4% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.798 µs | 1.015 µs | -27.2% | 🔴 |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.735 µs | 0.940 µs | -27.9% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.910 µs | 1.168 µs | -28.4% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.712 µs | 0.916 µs | -28.7% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.778 µs | 1.006 µs | -29.3% | 🔴 |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.948 µs | 1.240 µs | -30.8% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.715 µs | 0.942 µs | -31.7% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.736 µs | 1.030 µs | -39.9% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.772 µs | 1.168 µs | -51.3% | 🔴 |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.875 µs | 1.489 µs | -70.2% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.845 µs | 1.841 µs | -117.9% | 🔴 |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.818 µs | 1.829 µs | -123.6% | 🔴 |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.880 µs | 2.254 µs | -156.1% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.722 µs | 1.950 µs | -170.1% | 🔴 |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.793 µs | 2.458 µs | -210.0% | 🔴 |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.691 µs | 2.248 µs | -225.3% | 🔴 |

**Category Average**: -16.8% change

---

## api_overhead_benchmark_l0/ExecuteCommandList

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 124.643 µs | 35.597 µs | +71.4% | 🚀 |
| ExecuteCommandListForCopyEngine(api=l0 UseFence=1 measure... | 4.991 µs | 1.799 µs | +64.0% | 🚀 |
| ExecuteCommandListForCopyEngine(api=l0 UseFence=0 measure... | 6.832 µs | 2.494 µs | +63.5% | 🚀 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 90.730 µs | 40.236 µs | +55.7% | 🚀 |
| ExecuteCommandList(api=l0 UseFence=0 measureCompletionTim... | 4.828 µs | 2.152 µs | +55.4% | 🚀 |
| ExecuteCommandListForCopyEngine(api=l0 UseFence=1 measure... | 9.476 µs | 4.876 µs | +48.5% | 🚀 |
| ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndir... | 4.595 µs | 3.463 µs | +24.6% | 🚀 |
| ExecuteCommandListForCopyEngine(api=l0 UseFence=0 measure... | 9.296 µs | 7.083 µs | +23.8% | 🚀 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 11.175 µs | 8.838 µs | +20.9% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 123.286 µs | 97.609 µs | +20.8% | 🚀 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 21738.993 µs | 17988.238 µs | +17.3% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2.461 µs | 2.050 µs | +16.7% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2.412 µs | 2.044 µs | +15.3% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 37.873 µs | 32.175 µs | +15.0% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 21027.468 µs | 18026.499 µs | +14.3% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6.158 µs | 5.296 µs | +14.0% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7528.891 µs | 6588.710 µs | +12.5% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2.560 µs | 2.262 µs | +11.6% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7469.255 µs | 6611.796 µs | +11.5% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7757.628 µs | 6868.164 µs | +11.5% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7725.313 µs | 6894.064 µs | +10.8% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 35.486 µs | 31.731 µs | +10.6% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 8329.388 µs | 7453.758 µs | +10.5% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 8380.322 µs | 7501.916 µs | +10.5% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 95.023 µs | 85.108 µs | +10.4% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7168.966 µs | 6444.052 µs | +10.1% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 35.591 µs | 32.025 µs | +10.0% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6.174 µs | 5.580 µs | +9.6% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7207.130 µs | 6524.533 µs | +9.5% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7391.287 µs | 6725.680 µs | +9.0% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 19.615 µs | 17.996 µs | +8.3% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 12.463 µs | 11.480 µs | +7.9% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 17.126 µs | 15.841 µs | +7.5% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 44676.730 µs | 41565.647 µs | +7.0% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7147.317 µs | 6650.060 µs | +7.0% | ✓ |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=10... | 641.409 µs | 606.955 µs | +5.4% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 3.159 µs | 2.990 µs | +5.3% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 96.773 µs | 91.702 µs | +5.2% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 12.055 µs | 11.456 µs | +5.0% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 96.153 µs | 91.573 µs | +4.8% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2.640 µs | 2.515 µs | +4.7% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 43008.834 µs | 41006.576 µs | +4.7% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 209.770 µs | 201.031 µs | +4.2% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 18509.884 µs | 17790.522 µs | +3.9% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7480.441 µs | 7193.131 µs | +3.8% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 9.545 µs | 9.192 µs | +3.7% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 13.939 µs | 13.427 µs | +3.7% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 12.239 µs | 11.790 µs | +3.7% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 115.135 µs | 111.061 µs | +3.5% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 14.775 µs | 14.270 µs | +3.4% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 14.808 µs | 14.307 µs | +3.4% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2.607 µs | 2.526 µs | +3.1% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2.516 µs | 2.441 µs | +3.0% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 18134.498 µs | 17698.870 µs | +2.4% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2421.131 µs | 2365.135 µs | +2.3% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 94.422 µs | 92.440 µs | +2.1% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2.974 µs | 2.918 µs | +1.9% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 3.186 µs | 3.128 µs | +1.8% | ✓ |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=10... | 618.882 µs | 607.750 µs | +1.8% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7617.565 µs | 7481.653 µs | +1.8% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 197.460 µs | 194.002 µs | +1.8% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6849.153 µs | 6729.547 µs | +1.7% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6938.155 µs | 6823.677 µs | +1.6% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 18357.577 µs | 18054.736 µs | +1.6% | ✓ |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 5.001 µs | 4.925 µs | +1.5% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 95.250 µs | 93.808 µs | +1.5% | ✓ |
| ExecuteCommandListWithFenceUsage(api=l0) | 7.457 µs | 7.346 µs | +1.5% | ✓ |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 5.061 µs | 4.990 µs | +1.4% | ✓ |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=1 ... | 618.378 µs | 609.986 µs | +1.4% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 92.676 µs | 91.495 µs | +1.3% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 92.626 µs | 91.573 µs | +1.1% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7153.200 µs | 7077.497 µs | +1.1% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 3.249 µs | 3.215 µs | +1.0% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6965.223 µs | 6893.292 µs | +1.0% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 92.414 µs | 91.492 µs | +1.0% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 30.075 µs | 29.787 µs | +1.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 40823.672 µs | 40472.866 µs | +0.9% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 6521.022 µs | 6467.381 µs | +0.8% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6606.984 µs | 6553.261 µs | +0.8% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6860.074 µs | 6808.193 µs | +0.8% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 6449.135 µs | 6404.388 µs | +0.7% | ≈ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=1 B... | 38.088 µs | 37.829 µs | +0.7% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 41419.231 µs | 41150.640 µs | +0.6% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 9.200 µs | 9.149 µs | +0.6% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 9.814 µs | 9.768 µs | +0.5% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6906.917 µs | 6879.288 µs | +0.4% | ≈ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=100... | 40.345 µs | 40.187 µs | +0.4% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 9.511 µs | 9.475 µs | +0.4% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7580.277 µs | 7553.402 µs | +0.4% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7393.433 µs | 7368.620 µs | +0.3% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 199.892 µs | 199.225 µs | +0.3% | ≈ |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 1.826 µs | 1.820 µs | +0.3% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2438.458 µs | 2430.569 µs | +0.3% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 31.729 µs | 31.627 µs | +0.3% | ≈ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=100... | 19.687 µs | 19.625 µs | +0.3% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2438.753 µs | 2432.322 µs | +0.3% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2720.426 µs | 2713.498 µs | +0.3% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2363.693 µs | 2357.866 µs | +0.2% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2422.015 µs | 2416.119 µs | +0.2% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2437.664 µs | 2431.793 µs | +0.2% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 10.235 µs | 10.213 µs | +0.2% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 9.597 µs | 9.578 µs | +0.2% | ≈ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=1 B... | 19.360 µs | 19.323 µs | +0.2% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7379.435 µs | 7366.168 µs | +0.2% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 91.562 µs | 91.414 µs | +0.2% | ≈ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=1 B... | 8.001 µs | 7.989 µs | +0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 13.944 µs | 13.924 µs | +0.1% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 44201.111 µs | 44144.727 µs | +0.1% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2975.625 µs | 2972.148 µs | +0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 89.250 µs | 89.148 µs | +0.1% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2438.796 µs | 2436.036 µs | +0.1% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2363.787 µs | 2361.896 µs | +0.1% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 6478.396 µs | 6476.113 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 6521.390 µs | 6519.233 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2713.609 µs | 2712.809 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2714.325 µs | 2713.606 µs | +0.0% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 112.044 µs | 112.024 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 3270.899 µs | 3270.514 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7858.432 µs | 7857.689 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2965.809 µs | 2965.548 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 3270.097 µs | 3269.882 µs | +0.0% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 91.505 µs | 91.499 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2357.132 µs | 2357.204 µs | -0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7736.938 µs | 7738.233 µs | -0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2715.856 µs | 2716.593 µs | -0.0% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 14.800 µs | 14.809 µs | -0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 92.084 µs | 92.157 µs | -0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 91.404 µs | 91.492 µs | -0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 32.901 µs | 32.934 µs | -0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 198.978 µs | 199.200 µs | -0.1% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7465.072 µs | 7473.677 µs | -0.1% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2416.320 µs | 2419.790 µs | -0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 30.493 µs | 30.538 µs | -0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 9.338 µs | 9.352 µs | -0.1% | ≈ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=100... | 19.145 µs | 19.175 µs | -0.2% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 206.827 µs | 207.216 µs | -0.2% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 6868.784 µs | 6883.963 µs | -0.2% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6591.387 µs | 6607.551 µs | -0.2% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 41090.060 µs | 41193.064 µs | -0.3% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6827.126 µs | 6844.338 µs | -0.3% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 91.570 µs | 91.818 µs | -0.3% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 92.869 µs | 93.138 µs | -0.3% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 90.995 µs | 91.276 µs | -0.3% | ≈ |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=10... | 295.769 µs | 296.685 µs | -0.3% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 9.320 µs | 9.350 µs | -0.3% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 9.538 µs | 9.573 µs | -0.4% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 88.309 µs | 88.741 µs | -0.5% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7007.297 µs | 7042.260 µs | -0.5% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6648.374 µs | 6681.648 µs | -0.5% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 32.067 µs | 32.231 µs | -0.5% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 108.308 µs | 108.915 µs | -0.6% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 18150.825 µs | 18270.059 µs | -0.7% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6601.650 µs | 6646.195 µs | -0.7% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6694.260 µs | 6740.036 µs | -0.7% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 92.280 µs | 92.918 µs | -0.7% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 97.245 µs | 97.930 µs | -0.7% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 88.593 µs | 89.234 µs | -0.7% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7490.721 µs | 7547.018 µs | -0.8% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 211.864 µs | 213.642 µs | -0.8% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6361.682 µs | 6416.944 µs | -0.9% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 91.350 µs | 92.166 µs | -0.9% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 17.116 µs | 17.281 µs | -1.0% | ≈ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=1 B... | 39.610 µs | 40.021 µs | -1.0% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7566.967 µs | 7647.234 µs | -1.1% | ↓ |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=10... | 310.964 µs | 314.464 µs | -1.1% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 9.396 µs | 9.502 µs | -1.1% | ↓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 87.913 µs | 88.982 µs | -1.2% | ↓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 11.617 µs | 11.771 µs | -1.3% | ↓ |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 5.043 µs | 5.118 µs | -1.5% | ↓ |
| ExecuteCommandList(api=l0 UseFence=1 measureCompletionTim... | 8.248 µs | 8.376 µs | -1.6% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6453.448 µs | 6562.451 µs | -1.7% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 14.340 µs | 14.590 µs | -1.7% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 200.838 µs | 204.598 µs | -1.9% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 12.036 µs | 12.264 µs | -1.9% | ↓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 199.092 µs | 202.889 µs | -1.9% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6704.261 µs | 6835.376 µs | -2.0% | ↓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 18.165 µs | 18.546 µs | -2.1% | ↓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 14.414 µs | 14.718 µs | -2.1% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7565.881 µs | 7777.948 µs | -2.8% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6748.390 µs | 6940.422 µs | -2.8% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 199.812 µs | 206.080 µs | -3.1% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 5.953 µs | 6.156 µs | -3.4% | ↓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 109.149 µs | 113.157 µs | -3.7% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6341.105 µs | 6578.984 µs | -3.8% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2.977 µs | 3.128 µs | -5.1% | ↓ |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 5.068 µs | 5.332 µs | -5.2% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 33.410 µs | 35.210 µs | -5.4% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7511.183 µs | 7989.634 µs | -6.4% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6.079 µs | 6.500 µs | -6.9% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 31.570 µs | 33.770 µs | -7.0% | ↓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 109.964 µs | 117.792 µs | -7.1% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7688.518 µs | 8244.472 µs | -7.2% | ↓ |
| ExecuteCommandListWithFenceDestroy(api=l0) | 0.157 µs | 0.169 µs | -7.6% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 31.684 µs | 34.126 µs | -7.7% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 31.588 µs | 34.193 µs | -8.2% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 31.950 µs | 34.602 µs | -8.3% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 200.317 µs | 219.476 µs | -9.6% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 5.135 µs | 5.631 µs | -9.7% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 31.684 µs | 34.768 µs | -9.7% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2.571 µs | 2.842 µs | -10.5% | ⚠️ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7469.376 µs | 8289.985 µs | -11.0% | ⚠️ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 108.347 µs | 120.380 µs | -11.1% | ⚠️ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 13.503 µs | 15.097 µs | -11.8% | ⚠️ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7436.311 µs | 8673.080 µs | -16.6% | ⚠️ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 19.557 µs | 23.137 µs | -18.3% | ⚠️ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 14.468 µs | 17.338 µs | -19.8% | ⚠️ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 111.949 µs | 134.281 µs | -19.9% | ⚠️ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 96.222 µs | 115.802 µs | -20.3% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 92.475 µs | 111.740 µs | -20.8% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 14.360 µs | 17.380 µs | -21.0% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 5.093 µs | 6.169 µs | -21.1% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 10.357 µs | 12.548 µs | -21.2% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 7.652 µs | 9.302 µs | -21.6% | 🔴 |
| ExecuteCommandList(api=l0 UseFence=0 measureCompletionTim... | 1.768 µs | 2.152 µs | -21.7% | 🔴 |
| ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndir... | 7.518 µs | 9.152 µs | -21.7% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 17.011 µs | 20.709 µs | -21.7% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 94.371 µs | 115.168 µs | -22.0% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 110.892 µs | 135.599 µs | -22.3% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 9.504 µs | 11.622 µs | -22.3% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 9.407 µs | 11.549 µs | -22.8% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 95.125 µs | 116.849 µs | -22.8% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 12.667 µs | 15.561 µs | -22.8% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 99.311 µs | 122.191 µs | -23.0% | 🔴 |
| ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndir... | 5.462 µs | 6.721 µs | -23.1% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 91.606 µs | 112.888 µs | -23.2% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 9.367 µs | 11.549 µs | -23.3% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=100... | 77.093 µs | 95.073 µs | -23.3% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=1 B... | 77.067 µs | 95.119 µs | -23.4% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 91.566 µs | 113.128 µs | -23.5% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=100... | 151.331 µs | 186.998 µs | -23.6% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=100... | 158.447 µs | 195.805 µs | -23.6% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=1 B... | 158.200 µs | 195.583 µs | -23.6% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 92.783 µs | 114.724 µs | -23.6% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 96.811 µs | 119.730 µs | -23.7% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 98.559 µs | 121.897 µs | -23.7% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 12.351 µs | 15.282 µs | -23.7% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 12.142 µs | 15.027 µs | -23.8% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 91.918 µs | 113.841 µs | -23.9% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 9.596 µs | 11.887 µs | -23.9% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 92.135 µs | 114.179 µs | -23.9% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=100... | 38.039 µs | 47.180 µs | -24.0% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 91.291 µs | 113.239 µs | -24.0% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 92.645 µs | 114.969 µs | -24.1% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 9.182 µs | 11.395 µs | -24.1% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 5.285 µs | 6.561 µs | -24.1% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 88.695 µs | 110.456 µs | -24.5% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=100... | 74.554 µs | 92.982 µs | -24.7% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=1 ... | 302.091 µs | 376.778 µs | -24.7% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 92.377 µs | 115.380 µs | -24.9% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 112.123 µs | 140.115 µs | -25.0% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=1 B... | 149.575 µs | 187.173 µs | -25.1% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 91.447 µs | 114.453 µs | -25.2% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 87.942 µs | 110.077 µs | -25.2% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 87.947 µs | 110.163 µs | -25.3% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 97.295 µs | 121.919 µs | -25.3% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 9.563 µs | 12.019 µs | -25.7% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 17.834 µs | 22.591 µs | -26.7% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=1 ... | 639.882 µs | 812.474 µs | -27.0% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=1 ... | 309.574 µs | 393.260 µs | -27.0% | 🔴 |
| ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndir... | 3.067 µs | 3.921 µs | -27.8% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 108.398 µs | 140.270 µs | -29.4% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 94.142 µs | 122.828 µs | -30.5% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 97.282 µs | 128.243 µs | -31.8% | 🔴 |
| ExecuteCommandListWithFenceCreate(api=l0) | 0.147 µs | 0.196 µs | -33.3% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 91.877 µs | 122.684 µs | -33.5% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 93.050 µs | 124.675 µs | -34.0% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 30.041 µs | 40.461 µs | -34.7% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 30.322 µs | 41.049 µs | -35.4% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2.601 µs | 3.611 µs | -38.8% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 4.273 µs | 6.040 µs | -41.4% | 🔴 |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 3.635 µs | 5.473 µs | -50.6% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 95.142 µs | 146.477 µs | -54.0% | 🔴 |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 1.839 µs | 2.887 µs | -57.0% | 🔴 |
| ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndir... | 5.960 µs | 9.874 µs | -65.7% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 12.305 µs | 20.395 µs | -65.7% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 17.149 µs | 28.934 µs | -68.7% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=1 B... | 74.244 µs | 125.518 µs | -69.1% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 9.703 µs | 16.731 µs | -72.4% | 🔴 |
| ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndir... | 2.054 µs | 3.561 µs | -73.4% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 9.753 µs | 16.970 µs | -74.0% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 13.970 µs | 25.185 µs | -80.3% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7.998 µs | 14.914 µs | -86.5% | 🔴 |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 2.699 µs | 5.937 µs | -120.0% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 5.397 µs | 15.433 µs | -186.0% | 🔴 |

**Category Average**: -7.6% change

---

## api_overhead_benchmark_l0/ModuleCreate

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| ModuleCreateSpv(api=l0 kernelName=api_overhead_benchmark_... | 360.254 µs | 400.784 µs | -11.3% | ⚠️ |
| ModuleCreateSpv(api=l0 kernelName=api_overhead_benchmark_... | 71.011 µs | 86.182 µs | -21.4% | 🔴 |

**Category Average**: -16.3% change

---

## api_overhead_benchmark_l0/UsmMemoryAllocation

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| UsmMemoryAllocation(api=l0 type=Shared size=4 measureMode... | 690.718 µs | 214.207 µs | +69.0% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=4 measureMode... | 102.531 µs | 32.937 µs | +67.9% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=4MB measureMo... | 205.601 µs | 133.445 µs | +35.1% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=64 measureMod... | 123.014 µs | 93.457 µs | +24.0% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=4 measureMode=B... | 0.997 µs | 0.778 µs | +22.0% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Device size=64KB measureM... | 0.816 µs | 0.651 µs | +20.2% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=64MB measureM... | 152.502 µs | 125.080 µs | +18.0% | ✅ |
| UsmMemoryAllocation(api=l0 type=Shared size=64 measureMod... | 781.641 µs | 658.841 µs | +15.7% | ✅ |
| UsmMemoryAllocation(api=l0 type=Shared size=4MB measureMo... | 883.190 µs | 764.396 µs | +13.5% | ✅ |
| UsmMemoryAllocation(api=l0 type=Host size=64MB measureMod... | 0.834 µs | 0.726 µs | +12.9% | ✅ |
| UsmMemoryAllocation(api=l0 type=Device size=4 measureMode... | 0.734 µs | 0.644 µs | +12.3% | ✅ |
| UsmMemoryAllocation(api=l0 type=Host size=64 measureMode=... | 0.366 µs | 0.322 µs | +12.0% | ✅ |
| UsmMemoryAllocation(api=l0 type=Host size=1GB measureMode... | 1564.818 µs | 1454.083 µs | +7.1% | ✓ |
| UsmMemoryAllocation(api=l0 type=Device size=512MB measure... | 1707.477 µs | 1592.497 µs | +6.7% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=4 measureMode... | 197.730 µs | 184.921 µs | +6.5% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=512 measureMo... | 99.290 µs | 92.916 µs | +6.4% | ✓ |
| UsmMemoryAllocation(api=l0 type=Device size=512KB measure... | 0.692 µs | 0.652 µs | +5.8% | ✓ |
| UsmMemoryAllocation(api=l0 type=Host size=4 measureMode=A... | 0.129 µs | 0.122 µs | +5.4% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=512KB measure... | 526.942 µs | 498.647 µs | +5.4% | ✓ |
| UsmMemoryAllocation(api=l0 type=Device size=1GB measureMo... | 3382.733 µs | 3237.756 µs | +4.3% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=4KB measureMo... | 96.061 µs | 92.671 µs | +3.5% | ✓ |
| UsmMemoryAllocation(api=l0 type=Host size=512 measureMode... | 0.429 µs | 0.417 µs | +2.8% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=512MB measure... | 43431.484 µs | 42278.913 µs | +2.7% | ✓ |
| UsmMemoryAllocation(api=l0 type=Host size=512KB measureMo... | 0.427 µs | 0.417 µs | +2.3% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=64MB measureM... | 5310.435 µs | 5210.845 µs | +1.9% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=512 measureMo... | 579.010 µs | 569.042 µs | +1.7% | ✓ |
| UsmMemoryAllocation(api=l0 type=Host size=4KB measureMode... | 0.998 µs | 0.984 µs | +1.4% | ✓ |
| UsmMemoryAllocation(api=l0 type=Host size=64KB measureMod... | 1.005 µs | 0.995 µs | +1.0% | ≈ |
| UsmMemoryAllocation(api=l0 type=Shared size=512MB measure... | 42328.643 µs | 41949.399 µs | +0.9% | ≈ |
| UsmMemoryAllocation(api=l0 type=Host size=512MB measureMo... | 42416.852 µs | 42132.637 µs | +0.7% | ≈ |
| UsmMemoryAllocation(api=l0 type=Host size=1GB measureMode... | 80954.718 µs | 80629.874 µs | +0.4% | ≈ |
| UsmMemoryAllocation(api=l0 type=Host size=512MB measureMo... | 41444.637 µs | 41289.749 µs | +0.4% | ≈ |
| UsmMemoryAllocation(api=l0 type=Shared size=1GB measureMo... | 85003.348 µs | 84702.976 µs | +0.4% | ≈ |
| UsmMemoryAllocation(api=l0 type=Device size=1GB measureMo... | 10.496 µs | 10.477 µs | +0.2% | ≈ |
| UsmMemoryAllocation(api=l0 type=Shared size=64 measureMod... | 567.844 µs | 567.135 µs | +0.1% | ≈ |
| UsmMemoryAllocation(api=l0 type=Host size=1GB measureMode... | 82559.833 µs | 82751.357 µs | -0.2% | ≈ |
| UsmMemoryAllocation(api=l0 type=Device size=64MB measureM... | 0.645 µs | 0.651 µs | -0.9% | ≈ |
| UsmMemoryAllocation(api=l0 type=Device size=64 measureMod... | 0.641 µs | 0.647 µs | -0.9% | ≈ |
| UsmMemoryAllocation(api=l0 type=Device size=512 measureMo... | 1.053 µs | 1.063 µs | -0.9% | ≈ |
| UsmMemoryAllocation(api=l0 type=Device size=64 measureMod... | 1.044 µs | 1.056 µs | -1.1% | ↓ |
| UsmMemoryAllocation(api=l0 type=Device size=512 measureMo... | 0.637 µs | 0.645 µs | -1.3% | ↓ |
| UsmMemoryAllocation(api=l0 type=Host size=512KB measureMo... | 0.703 µs | 0.712 µs | -1.3% | ↓ |
| UsmMemoryAllocation(api=l0 type=Shared size=1GB measureMo... | 83385.984 µs | 84492.503 µs | -1.3% | ↓ |
| UsmMemoryAllocation(api=l0 type=Shared size=64MB measureM... | 5035.282 µs | 5123.326 µs | -1.7% | ↓ |
| UsmMemoryAllocation(api=l0 type=Host size=512MB measureMo... | 968.896 µs | 991.394 µs | -2.3% | ↓ |
| UsmMemoryAllocation(api=l0 type=Device size=4MB measureMo... | 0.641 µs | 0.661 µs | -3.1% | ↓ |
| UsmMemoryAllocation(api=l0 type=Shared size=512MB measure... | 367.748 µs | 379.451 µs | -3.2% | ↓ |
| UsmMemoryAllocation(api=l0 type=Device size=512KB measure... | 1.102 µs | 1.152 µs | -4.5% | ↓ |
| UsmMemoryAllocation(api=l0 type=Device size=64MB measureM... | 1.556 µs | 1.653 µs | -6.2% | ↓ |
| UsmMemoryAllocation(api=l0 type=Device size=4MB measureMo... | 1.554 µs | 1.679 µs | -8.0% | ↓ |
| UsmMemoryAllocation(api=l0 type=Device size=64MB measureM... | 0.999 µs | 1.104 µs | -10.5% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Device size=512KB measure... | 1.465 µs | 1.653 µs | -12.8% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Device size=4KB measureMo... | 0.811 µs | 0.919 µs | -13.3% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Device size=4MB measureMo... | 1.017 µs | 1.158 µs | -13.9% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Shared size=4KB measureMo... | 483.036 µs | 554.686 µs | -14.8% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Device size=4 measureMode... | 1.379 µs | 1.592 µs | -15.4% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Host size=4MB measureMode... | 0.893 µs | 1.041 µs | -16.6% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Shared size=4MB measureMo... | 1041.053 µs | 1215.657 µs | -16.8% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Device size=64 measureMod... | 1.372 µs | 1.613 µs | -17.6% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Host size=4MB measureMode... | 0.370 µs | 0.436 µs | -17.8% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Shared size=512 measureMo... | 560.709 µs | 661.234 µs | -17.9% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Shared size=1GB measureMo... | 800.809 µs | 945.844 µs | -18.1% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Device size=64KB measureM... | 1.421 µs | 1.679 µs | -18.2% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Device size=4KB measureMo... | 1.392 µs | 1.678 µs | -20.5% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=4MB measureMode... | 0.599 µs | 0.723 µs | -20.7% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=64MB measureMod... | 0.864 µs | 1.046 µs | -21.1% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=64KB measureMod... | 0.340 µs | 0.414 µs | -21.8% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Shared size=4KB measureMo... | 538.993 µs | 661.823 µs | -22.8% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=512 measureMode... | 0.728 µs | 0.903 µs | -24.0% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Shared size=512KB measure... | 623.810 µs | 784.637 µs | -25.8% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=64KB measureM... | 0.878 µs | 1.112 µs | -26.7% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=512KB measureMo... | 0.805 µs | 1.026 µs | -27.5% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=64 measureMode=... | 0.778 µs | 0.997 µs | -28.1% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Shared size=64KB measureM... | 438.147 µs | 562.870 µs | -28.5% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=4KB measureMode... | 0.528 µs | 0.681 µs | -29.0% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=64 measureMode=... | 0.530 µs | 0.688 µs | -29.8% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=512 measureMode... | 0.528 µs | 0.687 µs | -30.1% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=4KB measureMode... | 0.477 µs | 0.635 µs | -33.1% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=4KB measureMo... | 0.847 µs | 1.152 µs | -36.0% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=512MB measure... | 6.583 µs | 9.111 µs | -38.4% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=64KB measureMod... | 0.474 µs | 0.684 µs | -44.3% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=1GB measureMo... | 4563.223 µs | 6771.155 µs | -48.4% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=512 measureMo... | 1.767 µs | 2.804 µs | -58.7% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Shared size=64KB measureM... | 559.779 µs | 903.371 µs | -61.4% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=4 measureMode=F... | 0.323 µs | 0.540 µs | -67.2% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Shared size=512KB measure... | 96.817 µs | 171.517 µs | -77.2% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=4 measureMode... | 0.415 µs | 0.756 µs | -82.2% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Shared size=64KB measureM... | 94.556 µs | 175.851 µs | -86.0% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=512MB measure... | 1846.703 µs | 4705.778 µs | -154.8% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=64MB measureMod... | 0.135 µs | 0.461 µs | -241.5% | 🔴 |

**Category Average**: -13.7% change

---

## gpu_cmds_benchmark_l0/Execution

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|

---

## gpu_cmds_benchmark_l0/Walker

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| WaitOnEventFromWalker(api=l0 measuredCommands=500) | 0.104 µs | 0.114 µs | -9.6% | ↓ |
| WaitOnEventFromWalker(api=l0 measuredCommands=1000) | 0.092 µs | 0.104 µs | -13.0% | ⚠️ |

**Category Average**: -11.3% change

---

## memory_benchmark_l0/CopyBuffer

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| CopyBufferToImage(api=l0 region=512:512:1 src=Device size... | 336.082 µs | 334.693 µs | +0.4% | ≈ |
| CopyBufferToImage(api=l0 region=512:512:1 src=Host size=5... | 27.680 µs | 27.623 µs | +0.2% | ≈ |
| CopyBufferToImage(api=l0 region=512:512:64 src=Device siz... | 340.718 µs | 340.583 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=512:512:64 src=Host size=... | 27.921 µs | 27.918 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=8192:1:1 src=Device size=... | 63.015 µs | 63.015 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=16384:1:1 src=Device size... | 157.538 µs | 157.538 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=16384:1:1 src=Host size=5... | 24.006 µs | 24.006 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=256:512:1 src=Device size... | 242.951 µs | 242.951 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=512:512:2 src=Device size... | 329.898 µs | 329.898 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=512:512:2 src=Host size=5... | 27.756 µs | 27.766 µs | -0.0% | ≈ |
| CopyBufferToImage(api=l0 region=256:512:1 src=Host size=5... | 27.380 µs | 27.473 µs | -0.3% | ≈ |
| CopyBufferToImage(api=l0 region=8192:1:1 src=Host size=51... | 19.692 µs | 19.849 µs | -0.8% | ≈ |

**Category Average**: -0.0% change

---

## memory_benchmark_l0/FillBuffer

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=0 p... | 20.336 µs | 18.408 µs | +9.5% | ✓ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=0 p... | 20.261 µs | 18.346 µs | +9.5% | ✓ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=1 p... | 20.205 µs | 18.424 µs | +8.8% | ✓ |
| UsmFill(api=l0 memory=Shared size=128MB contents=Zeros pa... | 715.386 µs | 712.620 µs | +0.4% | ≈ |
| UsmFill(api=l0 memory=Device size=128MB contents=Zeros pa... | 711.442 µs | 708.903 µs | +0.4% | ≈ |
| UsmFill(api=l0 memory=Shared size=512MB contents=Zeros pa... | 656.522 µs | 654.523 µs | +0.3% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=1 p... | 22.612 µs | 22.546 µs | +0.3% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=0 p... | 18.747 µs | 18.709 µs | +0.2% | ≈ |
| UsmFillSpecificPattern(api=l0 memory=Shared size=512MB co... | 656.604 µs | 655.895 µs | +0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=0 p... | 18.723 µs | 18.704 µs | +0.1% | ≈ |
| UsmFill(api=l0 memory=Shared size=512MB contents=Zeros pa... | 686.192 µs | 685.508 µs | +0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=1 p... | 22.603 µs | 22.584 µs | +0.1% | ≈ |
| UsmFillImmediate(api=l0 memory=Device size=512MB contents... | 688.250 µs | 687.700 µs | +0.1% | ≈ |
| UsmFillImmediate(api=l0 memory=Shared size=512MB contents... | 687.334 µs | 686.785 µs | +0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=0 p... | 18.415 µs | 18.404 µs | +0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=0 p... | 22.590 µs | 22.577 µs | +0.1% | ≈ |
| UsmFillSpecificPattern(api=l0 memory=Shared size=128MB co... | 677.102 µs | 676.748 µs | +0.1% | ≈ |
| UsmFill(api=l0 memory=Device size=512MB contents=Zeros pa... | 447.507 µs | 447.352 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Shared size=512MB contents... | 447.478 µs | 447.342 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Host size=512MB contents=Z... | 22.725 µs | 22.720 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Host size=512MB contents=Z... | 22.725 µs | 22.721 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Device size=128MB contents=Zeros pa... | 447.100 µs | 447.023 µs | +0.0% | ≈ |
| UsmFillMultipleBlits(api=l0 memory=Device size=512MB patt... | 447.488 µs | 447.468 µs | +0.0% | ≈ |
| UsmFillMultipleBlits(api=l0 memory=Device size=512MB patt... | 447.488 µs | 447.468 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Host size=512MB contents=Z... | 22.722 µs | 22.721 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Host size=512MB contents=Z... | 28.363 µs | 28.362 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=128MB contents=Zeros patt... | 28.386 µs | 28.385 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Device size=128MB contents=Zeros pa... | 677.460 µs | 677.457 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=128MB contents=Zeros patt... | 22.770 µs | 22.770 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=128MB contents=Zeros patt... | 22.770 µs | 22.770 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=512MB contents=Zeros patt... | 22.772 µs | 22.772 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=512MB contents=Zeros patt... | 22.772 µs | 22.772 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=512MB contents=Zeros patt... | 22.771 µs | 22.771 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Device size=512MB contents=Zeros pa... | 554.541 µs | 554.541 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Device size=512MB contents... | 555.018 µs | 555.018 µs | +0.0% | ≈ |
| UsmFillSpecificPattern(api=l0 memory=Host size=128MB cont... | 22.770 µs | 22.770 µs | +0.0% | ≈ |
| UsmFillSpecificPattern(api=l0 memory=Host size=512MB cont... | 22.772 µs | 22.772 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=512MB contents=Zeros patt... | 28.386 µs | 28.387 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Shared size=512MB contents=Zeros pa... | 447.401 µs | 447.420 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=128MB contents=Zeros patt... | 22.766 µs | 22.767 µs | -0.0% | ≈ |
| UsmFillMultipleBlits(api=l0 memory=Device size=512MB patt... | 447.391 µs | 447.420 µs | -0.0% | ≈ |
| UsmFillMultipleBlits(api=l0 memory=Device size=512MB patt... | 447.391 µs | 447.420 µs | -0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Shared size=512MB contents... | 555.018 µs | 555.077 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Shared size=512MB contents=Zeros pa... | 554.541 µs | 554.600 µs | -0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Device size=512MB contents... | 447.352 µs | 447.430 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Shared size=128MB contents=Zeros pa... | 446.984 µs | 447.062 µs | -0.0% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=1 p... | 18.717 µs | 18.721 µs | -0.0% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=0 p... | 18.108 µs | 18.112 µs | -0.0% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=1 p... | 18.737 µs | 18.744 µs | -0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Device size=512MB contents... | 657.733 µs | 657.985 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Shared size=128MB contents=Zeros pa... | 550.578 µs | 550.813 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Device size=128MB contents=Zeros pa... | 550.226 µs | 550.578 µs | -0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=1 p... | 18.105 µs | 18.122 µs | -0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=1 p... | 22.635 µs | 22.661 µs | -0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=1 p... | 18.714 µs | 18.737 µs | -0.1% | ≈ |
| UsmFillImmediate(api=l0 memory=Shared size=512MB contents... | 655.478 µs | 656.479 µs | -0.2% | ≈ |
| UsmFillSpecificPattern(api=l0 memory=Device size=512MB co... | 654.939 µs | 656.020 µs | -0.2% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=1 p... | 18.053 µs | 18.093 µs | -0.2% | ≈ |
| UsmFill(api=l0 memory=Shared size=128MB contents=Zeros pa... | 678.704 µs | 680.326 µs | -0.2% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=1 p... | 18.041 µs | 18.088 µs | -0.3% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=1 p... | 18.386 µs | 18.434 µs | -0.3% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=0 p... | 22.557 µs | 22.618 µs | -0.3% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=0 p... | 22.535 µs | 22.599 µs | -0.3% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=0 p... | 18.084 µs | 18.149 µs | -0.4% | ≈ |
| UsmFill(api=l0 memory=Device size=512MB contents=Zeros pa... | 686.010 µs | 688.617 µs | -0.4% | ≈ |
| UsmFill(api=l0 memory=Device size=512MB contents=Zeros pa... | 655.562 µs | 658.783 µs | -0.5% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=0 p... | 18.691 µs | 18.795 µs | -0.6% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=0 p... | 17.990 µs | 18.132 µs | -0.8% | ≈ |
| UsmFillMultipleBlits(api=l0 memory=Device size=512MB patt... | 442.479 µs | 447.468 µs | -1.1% | ↓ |
| UsmFillMultipleBlits(api=l0 memory=Device size=512MB patt... | 442.012 µs | 447.420 µs | -1.2% | ↓ |
| UsmFillSpecificPattern(api=l0 memory=Device size=128MB co... | 665.249 µs | 677.991 µs | -1.9% | ↓ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=1 p... | 18.417 µs | 20.273 µs | -10.1% | ⚠️ |

**Category Average**: +0.1% change

---
