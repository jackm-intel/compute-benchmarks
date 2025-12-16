# Benchmark Comparison Report

## Configuration

### Baseline
- **File**: `baseline-results.json`
- **Timestamp**: 2025-12-16T00:35:00.424927
- **Device**: Unknown
- **Driver**: Unknown
- **Iterations**: 30

### Comparison
- **File**: `lazy-init-v2-results.json`
- **Timestamp**: 2025-12-16T00:38:32.132772
- **Device**: Unknown
- **Driver**: Unknown
- **Iterations**: 30

---

## Executive Summary

**Overall Performance Change**: +1.7%

### 🚀 Top Improvements (170 tests >10% faster)

- **+78.9%** - ExecuteCommandList(api=l0 UseFence=0 measureCompletionTime=0) (api_overhead_benchmark_l0/ExecuteCommandList)
- **+71.0%** - ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIndirectAllocations=1000 placement=Host) (api_overhead_benchmark_l0/ExecuteCommandList)
- **+68.4%** - UsmMemoryAllocation(api=l0 type=Host size=64MB measureMode=Allocate) (api_overhead_benchmark_l0/UsmMemoryAllocation)
- **+62.5%** - UsmMemoryAllocation(api=l0 type=Shared size=4KB measureMode=Free) (api_overhead_benchmark_l0/UsmMemoryAllocation)
- **+55.0%** - UsmMemoryAllocation(api=l0 type=Device size=4KB measureMode=Free) (api_overhead_benchmark_l0/UsmMemoryAllocation)
- **+50.8%** - ExecuteCommandList(api=l0 UseFence=0 measureCompletionTime=0) (api_overhead_benchmark_l0/ExecuteCommandList)
- **+50.3%** - DriverGet(api=l0 getDriverCount=1) (api_overhead_benchmark_l0/DriverGet)
- **+50.2%** - ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndirectAllocations=10 AllocateMemory=0) (api_overhead_benchmark_l0/ExecuteCommandList)
- **+49.7%** - UsmMemoryAllocation(api=l0 type=Shared size=64KB measureMode=Free) (api_overhead_benchmark_l0/UsmMemoryAllocation)
- **+48.8%** - ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndirectAllocations=1000 AllocateMemory=0) (api_overhead_benchmark_l0/ExecuteCommandList)

### ⚠️ Regressions (52 tests >10% slower)

- **-260.0%** - ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureCompletionTime=0 src=Device dst=Device size=64MB ioq=1 withCopyOffload=1) (api_overhead_benchmark_l0/ExecuteCommandList)
- **-248.6%** - ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureCompletionTime=0 src=Device dst=Device size=64MB ioq=1 withCopyOffload=0) (api_overhead_benchmark_l0/ExecuteCommandList)
- **-220.7%** - ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureCompletionTime=0 src=Device dst=Device size=64MB ioq=0 withCopyOffload=1) (api_overhead_benchmark_l0/ExecuteCommandList)
- **-208.3%** - ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIndirectAllocations=1000 placement=Shared) (api_overhead_benchmark_l0/ExecuteCommandList)
- **-153.9%** - AppendLaunchKernel(api=l0 wgc=1000 wgs=256 event=1 appendCount=100) (api_overhead_benchmark_l0/AppendLaunchKernel)
- **-149.5%** - ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureCompletionTime=0 src=Device dst=Device size=64MB ioq=1 withCopyOffload=0) (api_overhead_benchmark_l0/ExecuteCommandList)
- **-143.7%** - UsmMemoryAllocation(api=l0 type=Device size=64 measureMode=Allocate) (api_overhead_benchmark_l0/UsmMemoryAllocation)
- **-135.7%** - UsmMemoryAllocation(api=l0 type=Device size=4 measureMode=Free) (api_overhead_benchmark_l0/UsmMemoryAllocation)
- **-130.9%** - ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureCompletion=0 BarrierSynchro=0 KernelExecTime=100 EventSync=0 ioq=1) (api_overhead_benchmark_l0/ExecuteCommandList)
- **-124.2%** - UsmMemoryAllocation(api=l0 type=Host size=512KB measureMode=Both) (api_overhead_benchmark_l0/UsmMemoryAllocation)

---


## api_overhead_benchmark_l0/AppendLaunchKernel

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| AppendLaunchKernel(api=l0 wgc=1 wgs=1 event=0 appendCount... | 1.981 µs | 1.611 µs | +18.7% | ✅ |
| AppendLaunchKernel(api=l0 wgc=1000 wgs=256 event=0 append... | 4.783 µs | 4.341 µs | +9.2% | ✓ |
| AppendLaunchKernel(api=l0 wgc=1 wgs=256 event=1 appendCou... | 5.136 µs | 4.678 µs | +8.9% | ✓ |
| AppendLaunchKernel(api=l0 wgc=1 wgs=256 event=0 appendCou... | 4.385 µs | 4.077 µs | +7.0% | ✓ |
| AppendLaunchKernel(api=l0 wgc=1000 wgs=1 event=0 appendCo... | 3.995 µs | 3.961 µs | +0.9% | ≈ |
| AppendLaunchKernel(api=l0 wgc=1000 wgs=1 event=1 appendCo... | 4.368 µs | 4.380 µs | -0.3% | ≈ |
| AppendLaunchKernel(api=l0 wgc=1 wgs=1 event=1 appendCount... | 2.643 µs | 2.688 µs | -1.7% | ↓ |
| AppendLaunchKernel(api=l0 wgc=1000 wgs=256 event=1 append... | 1.662 µs | 4.219 µs | -153.9% | 🔴 |

**Category Average**: -13.9% change

---

## api_overhead_benchmark_l0/CreateCommandList

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| CreateCommandListImmediate(api=l0 CmdListCount=1000 ioq=1) | 3958.545 µs | 3240.130 µs | +18.1% | ✅ |
| CreateCommandList(api=l0 CmdListCount=100 CopyOnly=1) | 200.470 µs | 167.326 µs | +16.5% | ✅ |
| CreateCommandListImmediate(api=l0 CmdListCount=1000 ioq=0) | 3311.205 µs | 2801.997 µs | +15.4% | ✅ |
| CreateCommandList(api=l0 CmdListCount=100 CopyOnly=0) | 217.422 µs | 204.668 µs | +5.9% | ✓ |
| CreateCommandListImmediate(api=l0 CmdListCount=100 ioq=1) | 375.567 µs | 377.312 µs | -0.5% | ≈ |
| CreateCommandListImmediate(api=l0 CmdListCount=100 ioq=0) | 326.125 µs | 342.127 µs | -4.9% | ↓ |

**Category Average**: +8.4% change

---

## api_overhead_benchmark_l0/DriverGet

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| DriverGet(api=l0 getDriverCount=1) | 0.195 µs | 0.097 µs | +50.3% | 🚀 |
| DriverGetProperties(api=l0) | 0.141 µs | 0.139 µs | +1.4% | ✓ |
| DriverGetApiVersion(api=l0) | 0.131 µs | 0.132 µs | -0.8% | ≈ |
| DriverGet(api=l0 getDriverCount=0) | 0.069 µs | 0.070 µs | -1.4% | ↓ |
| DriverGet(api=l0 getDriverCount=1) | 0.091 µs | 0.097 µs | -6.6% | ↓ |

**Category Average**: +8.6% change

---

## api_overhead_benchmark_l0/EventCreation

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| EventQueryStatus(api=l0 eventSignaled=1) | 0.141 µs | 0.074 µs | +47.5% | 🚀 |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.809 µs | 0.666 µs | +17.7% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.804 µs | 0.665 µs | +17.3% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.804 µs | 0.665 µs | +17.3% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.809 µs | 0.670 µs | +17.2% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.800 µs | 0.665 µs | +16.9% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.801 µs | 0.666 µs | +16.9% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.802 µs | 0.667 µs | +16.8% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.802 µs | 0.668 µs | +16.7% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.798 µs | 0.665 µs | +16.7% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.799 µs | 0.667 µs | +16.5% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.803 µs | 0.671 µs | +16.4% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.798 µs | 0.667 µs | +16.4% | ✅ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.802 µs | 0.678 µs | +15.5% | ✅ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.802 µs | 0.742 µs | +7.5% | ✓ |
| EventQueryStatus(api=l0 eventSignaled=0) | 1.695 µs | 1.601 µs | +5.5% | ✓ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.826 µs | 0.802 µs | +2.9% | ✓ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.802 µs | 0.799 µs | +0.4% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.802 µs | 0.799 µs | +0.4% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.803 µs | 0.800 µs | +0.4% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.803 µs | 0.800 µs | +0.4% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.804 µs | 0.802 µs | +0.2% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.801 µs | 0.800 µs | +0.1% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.802 µs | 0.801 µs | +0.1% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.802 µs | 0.801 µs | +0.1% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.800 µs | 0.800 µs | +0.0% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.800 µs | 0.800 µs | +0.0% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.802 µs | 0.803 µs | -0.1% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.800 µs | 0.801 µs | -0.1% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.798 µs | 0.799 µs | -0.1% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.806 µs | 0.808 µs | -0.2% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.805 µs | 0.807 µs | -0.2% | ≈ |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.802 µs | 0.804 µs | -0.2% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.804 µs | 0.807 µs | -0.4% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.804 µs | 0.808 µs | -0.5% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.804 µs | 0.808 µs | -0.5% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.803 µs | 0.807 µs | -0.5% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.803 µs | 0.807 µs | -0.5% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.804 µs | 0.809 µs | -0.6% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.803 µs | 0.808 µs | -0.6% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.802 µs | 0.807 µs | -0.6% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.802 µs | 0.807 µs | -0.6% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.802 µs | 0.807 µs | -0.6% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.804 µs | 0.810 µs | -0.7% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.803 µs | 0.809 µs | -0.7% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.803 µs | 0.809 µs | -0.7% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.801 µs | 0.807 µs | -0.7% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.804 µs | 0.811 µs | -0.9% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.803 µs | 0.810 µs | -0.9% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.802 µs | 0.809 µs | -0.9% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.801 µs | 0.808 µs | -0.9% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.801 µs | 0.808 µs | -0.9% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.801 µs | 0.808 µs | -0.9% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.802 µs | 0.810 µs | -1.0% | ≈ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.800 µs | 0.808 µs | -1.0% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.800 µs | 0.808 µs | -1.0% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.803 µs | 0.812 µs | -1.1% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.802 µs | 0.811 µs | -1.1% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.800 µs | 0.809 µs | -1.1% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.804 µs | 0.814 µs | -1.2% | ↓ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.802 µs | 0.812 µs | -1.2% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=1 signal=... | 0.803 µs | 0.817 µs | -1.7% | ↓ |
| EventCreation(api=l0 useProfiling=1 hostVisible=0 signal=... | 0.803 µs | 0.833 µs | -3.7% | ↓ |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.668 µs | 0.802 µs | -20.1% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=0 signal=... | 0.668 µs | 0.802 µs | -20.1% | 🔴 |
| EventCreation(api=l0 useProfiling=0 hostVisible=1 signal=... | 0.665 µs | 0.803 µs | -20.8% | 🔴 |

**Category Average**: +2.9% change

---

## api_overhead_benchmark_l0/ExecuteCommandList

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| ExecuteCommandList(api=l0 UseFence=0 measureCompletionTim... | 7.830 µs | 1.653 µs | +78.9% | 🚀 |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 6.487 µs | 1.882 µs | +71.0% | 🚀 |
| ExecuteCommandList(api=l0 UseFence=0 measureCompletionTim... | 3.361 µs | 1.653 µs | +50.8% | 🚀 |
| ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndir... | 3.939 µs | 1.962 µs | +50.2% | 🚀 |
| ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndir... | 4.032 µs | 2.064 µs | +48.8% | 🚀 |
| ExecuteCommandList(api=l0 UseFence=1 measureCompletionTim... | 14.063 µs | 8.066 µs | +42.6% | 🚀 |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=1 B... | 24.066 µs | 14.056 µs | +41.6% | 🚀 |
| ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndir... | 9.445 µs | 5.564 µs | +41.1% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 20.066 µs | 12.065 µs | +39.9% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 15.087 µs | 9.165 µs | +39.3% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 11.402 µs | 7.014 µs | +38.5% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 5.207 µs | 3.223 µs | +38.1% | 🚀 |
| ExecuteCommandListForCopyEngine(api=l0 UseFence=1 measure... | 7.866 µs | 4.902 µs | +37.7% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 22.030 µs | 13.938 µs | +36.7% | 🚀 |
| ExecuteCommandListForCopyEngine(api=l0 UseFence=0 measure... | 7.710 µs | 4.879 µs | +36.7% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 25.112 µs | 16.874 µs | +32.8% | 🚀 |
| ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndir... | 3.234 µs | 2.312 µs | +28.5% | 🚀 |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=10... | 448.345 µs | 333.452 µs | +25.6% | 🚀 |
| ExecuteCommandListForCopyEngine(api=l0 UseFence=0 measure... | 12.274 µs | 9.134 µs | +25.6% | 🚀 |
| ExecuteCommandListForCopyEngine(api=l0 UseFence=1 measure... | 12.481 µs | 9.350 µs | +25.1% | 🚀 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 14.971 µs | 11.326 µs | +24.3% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 118.934 µs | 90.389 µs | +24.0% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 115.183 µs | 87.546 µs | +24.0% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 115.905 µs | 88.596 µs | +23.6% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 121.538 µs | 92.960 µs | +23.5% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 118.802 µs | 91.191 µs | +23.2% | 🚀 |
| ExecuteCommandListWithFenceDestroy(api=l0) | 0.197 µs | 0.153 µs | +22.3% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 11.563 µs | 9.147 µs | +20.9% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 114.585 µs | 90.659 µs | +20.9% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 11.752 µs | 9.306 µs | +20.8% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 12.263 µs | 9.714 µs | +20.8% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 114.432 µs | 90.659 µs | +20.8% | 🚀 |
| ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndir... | 7.114 µs | 5.638 µs | +20.7% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 114.031 µs | 90.506 µs | +20.6% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 113.986 µs | 90.471 µs | +20.6% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 113.650 µs | 90.233 µs | +20.6% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 11.949 µs | 9.518 µs | +20.3% | 🚀 |
| ExecuteCommandListWithFenceCreate(api=l0) | 0.184 µs | 0.147 µs | +20.1% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 11.434 µs | 9.140 µs | +20.1% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 37.621 µs | 30.087 µs | +20.0% | 🚀 |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 6.123 µs | 4.897 µs | +20.0% | 🚀 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 110.048 µs | 88.074 µs | +20.0% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=100... | 24.243 µs | 19.406 µs | +20.0% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 114.456 µs | 91.629 µs | +19.9% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=1 B... | 187.607 µs | 150.341 µs | +19.9% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 113.693 µs | 91.162 µs | +19.8% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 114.987 µs | 92.270 µs | +19.8% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 114.335 µs | 91.829 µs | +19.7% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=1 B... | 47.120 µs | 37.849 µs | +19.7% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 11.863 µs | 9.530 µs | +19.7% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=100... | 23.550 µs | 18.948 µs | +19.5% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=100... | 47.208 µs | 38.026 µs | +19.5% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=1 B... | 95.575 µs | 77.035 µs | +19.4% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 11.659 µs | 9.401 µs | +19.4% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=10... | 379.036 µs | 305.731 µs | +19.3% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=1 B... | 8.252 µs | 6.664 µs | +19.2% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=1 B... | 92.287 µs | 74.544 µs | +19.2% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=100... | 92.099 µs | 74.471 µs | +19.1% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 114.062 µs | 92.275 µs | +19.1% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 110.296 µs | 89.288 µs | +19.0% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=1 B... | 194.981 µs | 158.140 µs | +18.9% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=100... | 49.334 µs | 40.016 µs | +18.9% | ✅ |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 6.072 µs | 4.931 µs | +18.8% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 13.950 µs | 11.344 µs | +18.7% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 15.684 µs | 12.802 µs | +18.4% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 17.210 µs | 14.090 µs | +18.1% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 15.439 µs | 12.644 µs | +18.1% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 17.231 µs | 14.130 µs | +18.0% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 115.895 µs | 95.324 µs | +17.7% | ✅ |
| ExecuteCommandListWithFenceUsage(api=l0) | 8.976 µs | 7.395 µs | +17.6% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 14.326 µs | 11.809 µs | +17.6% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 35.803 µs | 29.603 µs | +17.3% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 20659.963 µs | 17147.064 µs | +17.0% | ✅ |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 6.014 µs | 5.010 µs | +16.7% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 20579.537 µs | 17196.361 µs | +16.4% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 5.059 µs | 4.265 µs | +15.7% | ✅ |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 5.961 µs | 5.029 µs | +15.6% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7512.230 µs | 6345.436 µs | +15.5% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7591.510 µs | 6430.013 µs | +15.3% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7440.211 µs | 6328.283 µs | +14.9% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7569.155 µs | 6464.530 µs | +14.6% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7868.948 µs | 6734.744 µs | +14.4% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7565.594 µs | 6483.570 µs | +14.3% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7752.743 µs | 6644.229 µs | +14.3% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2.490 µs | 2.146 µs | +13.8% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7604.431 µs | 6556.505 µs | +13.8% | ✅ |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 2.090 µs | 1.802 µs | +13.8% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=1 ExecTime=1 B... | 49.022 µs | 42.483 µs | +13.3% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 8367.509 µs | 7257.989 µs | +13.3% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 8222.765 µs | 7224.293 µs | +12.1% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7179.180 µs | 6319.878 µs | +12.0% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7606.241 µs | 6698.763 µs | +11.9% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7398.579 µs | 6520.604 µs | +11.9% | ✅ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 103.105 µs | 91.037 µs | +11.7% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7080.986 µs | 6258.872 µs | +11.6% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 8106.186 µs | 7212.408 µs | +11.0% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7608.290 µs | 6779.706 µs | +10.9% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 8158.446 µs | 7273.056 µs | +10.9% | ✅ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 8267.775 µs | 7397.190 µs | +10.5% | ✅ |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=10... | 505.856 µs | 456.752 µs | +9.7% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 35.074 µs | 31.789 µs | +9.4% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 35.737 µs | 32.419 µs | +9.3% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7081.388 µs | 6444.619 µs | +9.0% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7053.120 µs | 6419.418 µs | +9.0% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6844.379 µs | 6232.519 µs | +8.9% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 34.507 µs | 31.515 µs | +8.7% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 34.085 µs | 31.146 µs | +8.6% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 34.817 µs | 31.846 µs | +8.5% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 34.151 µs | 31.248 µs | +8.5% | ✓ |
| ExecuteCommandListWithIndirectAccess(api=l0 AmountOfIndir... | 4.058 µs | 3.716 µs | +8.4% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7176.343 µs | 6573.849 µs | +8.4% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7219.352 µs | 6643.177 µs | +8.0% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7218.484 µs | 6645.199 µs | +7.9% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 8014.238 µs | 7388.236 µs | +7.8% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7310.341 µs | 6743.132 µs | +7.8% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7942.272 µs | 7332.249 µs | +7.7% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7941.119 µs | 7334.787 µs | +7.6% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7206.390 µs | 6661.532 µs | +7.6% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 6826.256 µs | 6311.158 µs | +7.5% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7918.939 µs | 7348.105 µs | +7.2% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7952.941 µs | 7385.648 µs | +7.1% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7176.247 µs | 6666.236 µs | +7.1% | ✓ |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=10... | 311.557 µs | 292.648 µs | +6.1% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 119.261 µs | 113.386 µs | +4.9% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 115.419 µs | 110.078 µs | +4.6% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 119.082 µs | 113.624 µs | +4.6% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 95.887 µs | 91.534 µs | +4.5% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 95.903 µs | 92.322 µs | +3.7% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 34.940 µs | 33.674 µs | +3.6% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2.621 µs | 2.529 µs | +3.5% | ✓ |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=1 ... | 381.153 µs | 368.162 µs | +3.4% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 9.511 µs | 9.239 µs | +2.9% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 94.314 µs | 91.630 µs | +2.8% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 85.729 µs | 83.529 µs | +2.6% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 17726.480 µs | 17363.471 µs | +2.0% | ✓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 12.327 µs | 12.106 µs | +1.8% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 17255.470 µs | 16975.704 µs | +1.6% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7373.959 µs | 7268.140 µs | +1.4% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 11.937 µs | 11.768 µs | +1.4% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 35.095 µs | 34.630 µs | +1.3% | ✓ |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=1 ... | 371.382 µs | 366.913 µs | +1.2% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 40259.571 µs | 39779.310 µs | +1.2% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 17.312 µs | 17.106 µs | +1.2% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 14.309 µs | 14.145 µs | +1.1% | ✓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 8203.031 µs | 8110.498 µs | +1.1% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 113.784 µs | 112.549 µs | +1.1% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 13.890 µs | 13.748 µs | +1.0% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 116.047 µs | 114.864 µs | +1.0% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 134.406 µs | 133.048 µs | +1.0% | ✓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 120.543 µs | 119.486 µs | +0.9% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 122.881 µs | 121.814 µs | +0.9% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 114.376 µs | 113.428 µs | +0.8% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 40375.486 µs | 40072.389 µs | +0.8% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7346.485 µs | 7295.071 µs | +0.7% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 114.201 µs | 113.433 µs | +0.7% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 114.885 µs | 114.116 µs | +0.7% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 116.276 µs | 115.510 µs | +0.7% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 115.856 µs | 115.118 µs | +0.6% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 115.095 µs | 114.374 µs | +0.6% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 17.498 µs | 17.392 µs | +0.6% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 17.645 µs | 17.548 µs | +0.5% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 20.492 µs | 20.381 µs | +0.5% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 11.696 µs | 11.639 µs | +0.5% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 11.401 µs | 11.348 µs | +0.5% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 15.082 µs | 15.013 µs | +0.5% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 34.117 µs | 33.971 µs | +0.4% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 115.225 µs | 114.772 µs | +0.4% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 11.581 µs | 11.540 µs | +0.4% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 116.553 µs | 116.178 µs | +0.3% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 119.485 µs | 119.126 µs | +0.3% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 110.635 µs | 110.303 µs | +0.3% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 133.688 µs | 133.313 µs | +0.3% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 18.047 µs | 18.000 µs | +0.3% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 117.272 µs | 117.010 µs | +0.2% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 34.095 µs | 34.023 µs | +0.2% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 5.284 µs | 5.274 µs | +0.2% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 200.967 µs | 200.590 µs | +0.2% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 200.660 µs | 200.320 µs | +0.2% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2.398 µs | 2.394 µs | +0.2% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 201.371 µs | 201.071 µs | +0.1% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 17508.694 µs | 17484.755 µs | +0.1% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2969.278 µs | 2965.952 µs | +0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 200.820 µs | 200.644 µs | +0.1% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2714.103 µs | 2712.027 µs | +0.1% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2711.966 µs | 2709.936 µs | +0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 114.722 µs | 114.637 µs | +0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 201.082 µs | 200.966 µs | +0.1% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2429.927 µs | 2428.962 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2712.488 µs | 2711.444 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2713.762 µs | 2712.770 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2357.412 µs | 2356.680 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 3271.055 µs | 3270.110 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 3269.801 µs | 3268.870 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2416.461 µs | 2415.799 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2357.527 µs | 2356.884 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2430.060 µs | 2429.443 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2416.559 µs | 2416.034 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2965.822 µs | 2965.638 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2430.112 µs | 2429.974 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2429.922 µs | 2429.860 µs | +0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 43708.371 µs | 43707.560 µs | +0.0% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 12.554 µs | 12.555 µs | -0.0% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 133.267 µs | 133.292 µs | -0.0% | ≈ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 201.983 µs | 202.031 µs | -0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2358.145 µs | 2358.793 µs | -0.0% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2357.298 µs | 2358.465 µs | -0.0% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 114.588 µs | 114.701 µs | -0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 201.185 µs | 201.389 µs | -0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 112.344 µs | 112.479 µs | -0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 121.260 µs | 121.422 µs | -0.1% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 22.942 µs | 22.986 µs | -0.2% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 39567.222 µs | 39645.487 µs | -0.2% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7693.485 µs | 7718.748 µs | -0.3% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 193.971 µs | 194.782 µs | -0.4% | ≈ |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=100... | 186.752 µs | 187.620 µs | -0.5% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2.520 µs | 2.532 µs | -0.5% | ≈ |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=100... | 76.976 µs | 77.343 µs | -0.5% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 8204.454 µs | 8248.454 µs | -0.5% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7514.858 µs | 7560.751 µs | -0.6% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 138.197 µs | 139.238 µs | -0.8% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7082.811 µs | 7139.511 µs | -0.8% | ≈ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 108.871 µs | 109.814 µs | -0.9% | ≈ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7404.649 µs | 7485.055 µs | -1.1% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 17446.646 µs | 17648.575 µs | -1.2% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 137.596 µs | 139.206 µs | -1.2% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 5.022 µs | 5.082 µs | -1.2% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 197.693 µs | 200.205 µs | -1.3% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 44847.780 µs | 45470.666 µs | -1.4% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 5.058 µs | 5.131 µs | -1.4% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7631.393 µs | 7742.722 µs | -1.5% | ↓ |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=1 ... | 479.432 µs | 486.759 µs | -1.5% | ↓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 136.513 µs | 139.006 µs | -1.8% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 121.392 µs | 123.805 µs | -2.0% | ↓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 130.935 µs | 133.560 µs | -2.0% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 194.782 µs | 198.771 µs | -2.0% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2.496 µs | 2.550 µs | -2.2% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 124.801 µs | 127.799 µs | -2.4% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 40703.437 µs | 41720.111 µs | -2.5% | ↓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 14.139 µs | 14.537 µs | -2.8% | ↓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 135.911 µs | 139.964 µs | -3.0% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2.497 µs | 2.574 µs | -3.1% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7324.075 µs | 7721.043 µs | -5.4% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7061.075 µs | 7484.047 µs | -6.0% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7094.670 µs | 7522.917 µs | -6.0% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 7027.165 µs | 7476.438 µs | -6.4% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7337.604 µs | 7807.663 µs | -6.4% | ↓ |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 107.482 µs | 115.062 µs | -7.1% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 31.428 µs | 33.824 µs | -7.6% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2.224 µs | 2.399 µs | -7.9% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 7085.766 µs | 7682.179 µs | -8.4% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 31.605 µs | 34.326 µs | -8.6% | ↓ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 5.332 µs | 5.797 µs | -8.7% | ↓ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 26.075 µs | 28.684 µs | -10.0% | ⚠️ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2.469 µs | 2.763 µs | -11.9% | ⚠️ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 35.812 µs | 40.292 µs | -12.5% | ⚠️ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 36.218 µs | 41.014 µs | -13.2% | ⚠️ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 22.130 µs | 25.116 µs | -13.5% | ⚠️ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 5.092 µs | 5.812 µs | -14.1% | ⚠️ |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2.527 µs | 2.922 µs | -15.6% | ⚠️ |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 9.389 µs | 11.321 µs | -20.6% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 2.521 µs | 3.054 µs | -21.1% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 13.366 µs | 16.212 µs | -21.3% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2.330 µs | 2.829 µs | -21.4% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 10.239 µs | 12.492 µs | -22.0% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 13.244 µs | 16.187 µs | -22.2% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 12.171 µs | 14.934 µs | -22.7% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 9.358 µs | 11.540 µs | -23.3% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 12.093 µs | 14.980 µs | -23.9% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=4 ExecTime=100... | 156.147 µs | 194.825 µs | -24.8% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 87.681 µs | 109.650 µs | -25.1% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 4.281 µs | 5.686 µs | -32.8% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=10 MeasureCom... | 95.495 µs | 126.969 µs | -33.0% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=1 MeasureComp... | 11.136 µs | 15.460 µs | -38.8% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 3.316 µs | 4.687 µs | -41.3% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 2.124 µs | 3.058 µs | -44.0% | 🔴 |
| ExecImmediate(api=l0 Profiling=1 CallsCount=10 MeasureCom... | 90.987 µs | 137.491 µs | -51.1% | 🔴 |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 4.003 µs | 6.071 µs | -51.7% | 🔴 |
| ExecImmediateMultiKernel(api=l0 CallsCount=16 ExecTime=1 ... | 392.952 µs | 602.905 µs | -53.4% | 🔴 |
| ExecImmediate(api=l0 Profiling=0 CallsCount=1 MeasureComp... | 4.004 µs | 9.246 µs | -130.9% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=1 MeasureComplet... | 3.011 µs | 7.512 µs | -149.5% | 🔴 |
| ExecuteCommandListWithIndirectArguments(api=l0 AmountOfIn... | 2.073 µs | 6.392 µs | -208.3% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 4.765 µs | 15.280 µs | -220.7% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 4.302 µs | 14.998 µs | -248.6% | 🔴 |
| ExecImmediateCopyQueue(api=l0 IsCopyOnly=0 MeasureComplet... | 4.251 µs | 15.303 µs | -260.0% | 🔴 |

**Category Average**: +1.7% change

---

## api_overhead_benchmark_l0/ModuleCreate

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| ModuleCreateSpv(api=l0 kernelName=api_overhead_benchmark_... | 350.550 µs | 344.624 µs | +1.7% | ✓ |
| ModuleCreateSpv(api=l0 kernelName=api_overhead_benchmark_... | 84.801 µs | 83.447 µs | +1.6% | ✓ |

**Category Average**: +1.6% change

---

## api_overhead_benchmark_l0/UsmMemoryAllocation

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| UsmMemoryAllocation(api=l0 type=Host size=64MB measureMod... | 0.376 µs | 0.119 µs | +68.4% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=4KB measureMo... | 129.924 µs | 48.668 µs | +62.5% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Device size=4KB measureMo... | 1.164 µs | 0.524 µs | +55.0% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=64KB measureM... | 93.067 µs | 46.846 µs | +49.7% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=512 measureMo... | 508.774 µs | 282.333 µs | +44.5% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=4MB measureMo... | 102.670 µs | 59.306 µs | +42.2% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=512 measureMo... | 337.337 µs | 199.127 µs | +41.0% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=64KB measureM... | 504.418 µs | 299.692 µs | +40.6% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Device size=512KB measure... | 0.880 µs | 0.523 µs | +40.6% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=64 measureMod... | 136.558 µs | 82.197 µs | +39.8% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Device size=64KB measureM... | 0.851 µs | 0.523 µs | +38.5% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=512MB measureMo... | 2287.272 µs | 1438.306 µs | +37.1% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Device size=4MB measureMo... | 0.815 µs | 0.524 µs | +35.7% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Device size=4MB measureMo... | 1.934 µs | 1.309 µs | +32.3% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Device size=512KB measure... | 1.841 µs | 1.305 µs | +29.1% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Device size=4MB measureMo... | 1.226 µs | 0.876 µs | +28.5% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=64KB measureMod... | 0.743 µs | 0.534 µs | +28.1% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=4KB measureMo... | 343.815 µs | 247.438 µs | +28.0% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Device size=64KB measureM... | 1.815 µs | 1.309 µs | +27.9% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=512KB measureMo... | 0.759 µs | 0.553 µs | +27.1% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=64KB measureMod... | 1.057 µs | 0.772 µs | +27.0% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=4KB measureMode... | 0.732 µs | 0.538 µs | +26.5% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=64 measureMode=... | 0.733 µs | 0.542 µs | +26.1% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=512 measureMode... | 0.733 µs | 0.543 µs | +25.9% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=4 measureMode=B... | 1.046 µs | 0.777 µs | +25.7% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=4KB measureMode... | 1.038 µs | 0.774 µs | +25.4% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=64 measureMode=... | 1.046 µs | 0.780 µs | +25.4% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=512KB measure... | 331.452 µs | 248.165 µs | +25.1% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=512 measureMode... | 1.046 µs | 0.784 µs | +25.0% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=64MB measureMod... | 1.091 µs | 0.819 µs | +24.9% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=512 measureMode... | 0.427 µs | 0.321 µs | +24.8% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Shared size=512MB measure... | 528.546 µs | 398.046 µs | +24.7% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=64 measureMode=... | 0.424 µs | 0.322 µs | +24.1% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=64KB measureMod... | 0.422 µs | 0.324 µs | +23.2% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=64MB measureMod... | 0.736 µs | 0.567 µs | +23.0% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=4MB measureMode... | 1.054 µs | 0.812 µs | +23.0% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=4MB measureMode... | 0.430 µs | 0.333 µs | +22.6% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=512KB measureMo... | 0.415 µs | 0.322 µs | +22.4% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=4MB measureMode... | 0.727 µs | 0.566 µs | +22.1% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Host size=4 measureMode=A... | 0.147 µs | 0.116 µs | +21.1% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Device size=512KB measure... | 1.089 µs | 0.871 µs | +20.0% | 🚀 |
| UsmMemoryAllocation(api=l0 type=Device size=64KB measureM... | 1.066 µs | 0.859 µs | +19.4% | ✅ |
| UsmMemoryAllocation(api=l0 type=Shared size=512 measureMo... | 127.915 µs | 103.669 µs | +19.0% | ✅ |
| UsmMemoryAllocation(api=l0 type=Shared size=1GB measureMo... | 915.705 µs | 745.006 µs | +18.6% | ✅ |
| UsmMemoryAllocation(api=l0 type=Device size=512MB measure... | 2455.758 µs | 2000.810 µs | +18.5% | ✅ |
| UsmMemoryAllocation(api=l0 type=Shared size=64KB measureM... | 243.772 µs | 199.819 µs | +18.0% | ✅ |
| UsmMemoryAllocation(api=l0 type=Host size=512MB measureMo... | 52872.673 µs | 43473.697 µs | +17.8% | ✅ |
| UsmMemoryAllocation(api=l0 type=Device size=64MB measureM... | 0.637 µs | 0.528 µs | +17.1% | ✅ |
| UsmMemoryAllocation(api=l0 type=Device size=64MB measureM... | 1.568 µs | 1.310 µs | +16.5% | ✅ |
| UsmMemoryAllocation(api=l0 type=Device size=64MB measureM... | 1.018 µs | 0.863 µs | +15.2% | ✅ |
| UsmMemoryAllocation(api=l0 type=Host size=1GB measureMode... | 97327.777 µs | 82987.492 µs | +14.7% | ✅ |
| UsmMemoryAllocation(api=l0 type=Host size=512MB measureMo... | 49298.378 µs | 44156.470 µs | +10.4% | ✅ |
| UsmMemoryAllocation(api=l0 type=Shared size=1GB measureMo... | 94581.700 µs | 85448.838 µs | +9.7% | ✓ |
| UsmMemoryAllocation(api=l0 type=Device size=1GB measureMo... | 13.035 µs | 11.985 µs | +8.1% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=64MB measureM... | 131.322 µs | 120.903 µs | +7.9% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=4 measureMode... | 93.943 µs | 86.874 µs | +7.5% | ✓ |
| UsmMemoryAllocation(api=l0 type=Device size=512MB measure... | 7.874 µs | 7.321 µs | +7.0% | ✓ |
| UsmMemoryAllocation(api=l0 type=Device size=4 measureMode... | 0.447 µs | 0.416 µs | +6.9% | ✓ |
| UsmMemoryAllocation(api=l0 type=Host size=4 measureMode=F... | 0.475 µs | 0.444 µs | +6.5% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=4 measureMode... | 252.868 µs | 237.448 µs | +6.1% | ✓ |
| UsmMemoryAllocation(api=l0 type=Host size=1GB measureMode... | 2984.943 µs | 2839.206 µs | +4.9% | ✓ |
| UsmMemoryAllocation(api=l0 type=Host size=1GB measureMode... | 85006.322 µs | 81127.530 µs | +4.6% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=512KB measure... | 373.043 µs | 356.358 µs | +4.5% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=4MB measureMo... | 467.803 µs | 452.165 µs | +3.3% | ✓ |
| UsmMemoryAllocation(api=l0 type=Host size=4KB measureMode... | 0.423 µs | 0.415 µs | +1.9% | ✓ |
| UsmMemoryAllocation(api=l0 type=Shared size=4KB measureMo... | 235.019 µs | 233.275 µs | +0.7% | ≈ |
| UsmMemoryAllocation(api=l0 type=Shared size=1GB measureMo... | 88209.853 µs | 87604.641 µs | +0.7% | ≈ |
| UsmMemoryAllocation(api=l0 type=Shared size=512MB measure... | 45193.278 µs | 44959.879 µs | +0.5% | ≈ |
| UsmMemoryAllocation(api=l0 type=Device size=512MB measure... | 1668.644 µs | 1688.981 µs | -1.2% | ↓ |
| UsmMemoryAllocation(api=l0 type=Shared size=64MB measureM... | 5235.557 µs | 5410.138 µs | -3.3% | ↓ |
| UsmMemoryAllocation(api=l0 type=Device size=1GB measureMo... | 4684.060 µs | 4900.446 µs | -4.6% | ↓ |
| UsmMemoryAllocation(api=l0 type=Shared size=512MB measure... | 41769.115 µs | 43766.882 µs | -4.8% | ↓ |
| UsmMemoryAllocation(api=l0 type=Shared size=64MB measureM... | 5137.737 µs | 5407.990 µs | -5.3% | ↓ |
| UsmMemoryAllocation(api=l0 type=Shared size=64 measureMod... | 471.499 µs | 504.425 µs | -7.0% | ↓ |
| UsmMemoryAllocation(api=l0 type=Device size=1GB measureMo... | 4840.313 µs | 5190.534 µs | -7.2% | ↓ |
| UsmMemoryAllocation(api=l0 type=Device size=4KB measureMo... | 1.221 µs | 1.314 µs | -7.6% | ↓ |
| UsmMemoryAllocation(api=l0 type=Shared size=4MB measureMo... | 393.927 µs | 428.880 µs | -8.9% | ↓ |
| UsmMemoryAllocation(api=l0 type=Shared size=4 measureMode... | 438.981 µs | 485.833 µs | -10.7% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Shared size=64 measureMod... | 317.106 µs | 373.149 µs | -17.7% | ⚠️ |
| UsmMemoryAllocation(api=l0 type=Device size=64 measureMod... | 0.324 µs | 0.520 µs | -60.5% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=64 measureMod... | 0.796 µs | 1.283 µs | -61.2% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=512 measureMo... | 0.283 µs | 0.520 µs | -83.7% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=512 measureMo... | 0.447 µs | 0.822 µs | -83.9% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=4KB measureMo... | 0.477 µs | 0.885 µs | -85.5% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=4 measureMode... | 0.584 µs | 1.268 µs | -117.1% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=512 measureMo... | 0.586 µs | 1.281 µs | -118.6% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Shared size=512KB measure... | 42.988 µs | 94.334 µs | -119.4% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Host size=512KB measureMo... | 0.356 µs | 0.798 µs | -124.2% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=4 measureMode... | 0.280 µs | 0.660 µs | -135.7% | 🔴 |
| UsmMemoryAllocation(api=l0 type=Device size=64 measureMod... | 0.341 µs | 0.831 µs | -143.7% | 🔴 |

**Category Average**: +4.0% change

---

## gpu_cmds_benchmark_l0/Execution

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|

---

## gpu_cmds_benchmark_l0/Walker

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| WaitOnEventFromWalker(api=l0 measuredCommands=500) | 0.081 µs | 0.110 µs | -35.8% | 🔴 |
| WaitOnEventFromWalker(api=l0 measuredCommands=1000) | 0.052 µs | 0.073 µs | -40.4% | 🔴 |

**Category Average**: -38.1% change

---

## memory_benchmark_l0/CopyBuffer

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| CopyBufferToImage(api=l0 region=8192:1:1 src=Device size=... | 66.332 µs | 63.015 µs | +5.0% | ✓ |
| CopyBufferToImage(api=l0 region=256:512:1 src=Device size... | 261.882 µs | 256.888 µs | +1.9% | ✓ |
| CopyBufferToImage(api=l0 region=512:512:2 src=Device size... | 317.558 µs | 316.313 µs | +0.4% | ≈ |
| CopyBufferToImage(api=l0 region=512:512:1 src=Host size=5... | 27.595 µs | 27.567 µs | +0.1% | ≈ |
| CopyBufferToImage(api=l0 region=256:512:1 src=Host size=5... | 27.268 µs | 27.250 µs | +0.1% | ≈ |
| CopyBufferToImage(api=l0 region=512:512:64 src=Host size=... | 27.922 µs | 27.913 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=8192:1:1 src=Host size=51... | 20.005 µs | 20.005 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=16384:1:1 src=Device size... | 157.538 µs | 157.538 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=16384:1:1 src=Host size=5... | 24.006 µs | 24.006 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=512:512:1 src=Device size... | 315.077 µs | 315.077 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=512:512:64 src=Device siz... | 340.561 µs | 340.561 µs | +0.0% | ≈ |
| CopyBufferToImage(api=l0 region=512:512:2 src=Host size=5... | 27.747 µs | 27.756 µs | -0.0% | ≈ |

**Category Average**: +0.6% change

---

## memory_benchmark_l0/FillBuffer

| Test | Baseline (Median) | Comparison (Median) | Change | Status |
|------|-------------------|---------------------|--------|--------|
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=0 p... | 20.314 µs | 18.424 µs | +9.3% | ✓ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=1 p... | 18.215 µs | 18.085 µs | +0.7% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=1 p... | 18.178 µs | 18.106 µs | +0.4% | ≈ |
| UsmFill(api=l0 memory=Shared size=128MB contents=Zeros pa... | 680.314 µs | 677.813 µs | +0.4% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=1 p... | 18.770 µs | 18.707 µs | +0.3% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=0 p... | 20.357 µs | 20.304 µs | +0.3% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=1 p... | 22.665 µs | 22.611 µs | +0.2% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=0 p... | 18.160 µs | 18.118 µs | +0.2% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=0 p... | 18.154 µs | 18.117 µs | +0.2% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=1 p... | 18.767 µs | 18.730 µs | +0.2% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=1 p... | 18.764 µs | 18.736 µs | +0.1% | ≈ |
| UsmFill(api=l0 memory=Shared size=128MB contents=Zeros pa... | 714.198 µs | 713.408 µs | +0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=0 p... | 18.769 µs | 18.749 µs | +0.1% | ≈ |
| UsmFillSpecificPattern(api=l0 memory=Device size=512MB co... | 656.646 µs | 656.020 µs | +0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=1 p... | 18.141 µs | 18.127 µs | +0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=0 p... | 18.136 µs | 18.123 µs | +0.1% | ≈ |
| UsmFill(api=l0 memory=Device size=512MB contents=Zeros pa... | 655.895 µs | 655.520 µs | +0.1% | ≈ |
| UsmFillImmediate(api=l0 memory=Device size=512MB contents... | 688.204 µs | 687.883 µs | +0.0% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=0 p... | 22.632 µs | 22.625 µs | +0.0% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=0 p... | 22.660 µs | 22.655 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Shared size=512MB contents... | 687.380 µs | 687.242 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Device size=512MB contents... | 657.398 µs | 657.273 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Host size=512MB contents=Z... | 22.725 µs | 22.721 µs | +0.0% | ≈ |
| UsmFillMultipleBlits(api=l0 memory=Device size=512MB patt... | 447.488 µs | 447.410 µs | +0.0% | ≈ |
| UsmFillMultipleBlits(api=l0 memory=Device size=512MB patt... | 447.488 µs | 447.410 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Device size=128MB contents=Zeros pa... | 447.100 µs | 447.023 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Host size=512MB contents=Z... | 22.724 µs | 22.721 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Host size=512MB contents=Z... | 22.725 µs | 22.724 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=128MB contents=Zeros patt... | 22.770 µs | 22.770 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=128MB contents=Zeros patt... | 28.386 µs | 28.386 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=128MB contents=Zeros patt... | 22.770 µs | 22.770 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=128MB contents=Zeros patt... | 22.766 µs | 22.766 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=512MB contents=Zeros patt... | 22.772 µs | 22.772 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=512MB contents=Zeros patt... | 22.772 µs | 22.772 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=512MB contents=Zeros patt... | 22.771 µs | 22.771 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Device size=128MB contents=Zeros pa... | 677.279 µs | 677.279 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Device size=128MB contents=Zeros pa... | 550.578 µs | 550.578 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Host size=512MB contents=Z... | 28.364 µs | 28.364 µs | +0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Device size=512MB contents... | 555.018 µs | 555.018 µs | +0.0% | ≈ |
| UsmFillMultipleBlits(api=l0 memory=Device size=512MB patt... | 447.449 µs | 447.449 µs | +0.0% | ≈ |
| UsmFillMultipleBlits(api=l0 memory=Device size=512MB patt... | 447.449 µs | 447.449 µs | +0.0% | ≈ |
| UsmFillSpecificPattern(api=l0 memory=Host size=128MB cont... | 22.770 µs | 22.770 µs | +0.0% | ≈ |
| UsmFillSpecificPattern(api=l0 memory=Host size=512MB cont... | 22.772 µs | 22.772 µs | +0.0% | ≈ |
| UsmFill(api=l0 memory=Host size=512MB contents=Zeros patt... | 28.386 µs | 28.387 µs | -0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Device size=512MB contents... | 447.391 µs | 447.410 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Device size=512MB contents=Zeros pa... | 447.391 µs | 447.430 µs | -0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Shared size=512MB contents... | 555.018 µs | 555.077 µs | -0.0% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=0 p... | 22.653 µs | 22.656 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Shared size=512MB contents=Zeros pa... | 656.187 µs | 656.312 µs | -0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Shared size=512MB contents... | 656.103 µs | 656.228 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Shared size=512MB contents=Zeros pa... | 554.422 µs | 554.541 µs | -0.0% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=1 p... | 22.650 µs | 22.655 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Shared size=512MB contents=Zeros pa... | 447.313 µs | 447.420 µs | -0.0% | ≈ |
| UsmFillImmediate(api=l0 memory=Shared size=512MB contents... | 447.284 µs | 447.410 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Device size=512MB contents=Zeros pa... | 554.362 µs | 554.541 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Shared size=128MB contents=Zeros pa... | 550.578 µs | 550.813 µs | -0.0% | ≈ |
| UsmFill(api=l0 memory=Shared size=128MB contents=Zeros pa... | 446.791 µs | 447.023 µs | -0.1% | ≈ |
| UsmFill(api=l0 memory=Shared size=512MB contents=Zeros pa... | 686.648 µs | 687.014 µs | -0.1% | ≈ |
| UsmFillSpecificPattern(api=l0 memory=Shared size=512MB co... | 655.562 µs | 656.103 µs | -0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=0 p... | 18.739 µs | 18.756 µs | -0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=0 p... | 18.726 µs | 18.747 µs | -0.1% | ≈ |
| UsmFill(api=l0 memory=Device size=512MB contents=Zeros pa... | 687.197 µs | 688.067 µs | -0.1% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=1 p... | 20.308 µs | 20.335 µs | -0.1% | ≈ |
| UsmFillSpecificPattern(api=l0 memory=Device size=128MB co... | 675.330 µs | 676.392 µs | -0.2% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=128MB prefetch=1 p... | 22.619 µs | 22.661 µs | -0.2% | ≈ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=1 p... | 18.433 µs | 18.473 µs | -0.2% | ≈ |
| UsmFillSpecificPattern(api=l0 memory=Shared size=128MB co... | 679.240 µs | 680.852 µs | -0.2% | ≈ |
| UsmFill(api=l0 memory=Device size=128MB contents=Zeros pa... | 711.442 µs | 714.989 µs | -0.5% | ≈ |
| UsmFillMultipleBlits(api=l0 memory=Device size=512MB patt... | 443.070 µs | 447.410 µs | -1.0% | ≈ |
| UsmFillMultipleBlits(api=l0 memory=Device size=512MB patt... | 442.790 µs | 447.449 µs | -1.1% | ↓ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=1 p... | 18.534 µs | 20.293 µs | -9.5% | ↓ |
| UsmSharedMigrateGpuForFill(api=l0 size=256MB prefetch=0 p... | 18.364 µs | 20.318 µs | -10.6% | ⚠️ |

**Category Average**: -0.2% change

---
