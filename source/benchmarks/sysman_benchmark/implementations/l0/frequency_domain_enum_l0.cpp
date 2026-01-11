/*
 * Copyright (C) 2022-2023 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#include "framework/l0/levelzero.h"
#include "framework/test_case/register_test_case.h"
#include "framework/utility/timer.h"
#include "framework/configuration.h"

#include "definitions/frequency_domain_enum.h"

#include <gtest/gtest.h>
#include <level_zero/zes_api.h>
#include <vector>

static TestResult run(const FrequencyDomainEnumArguments &arguments, Statistics &statistics) {
    MeasurementFields typeSelector(MeasurementUnit::Microseconds, MeasurementType::Cpu);

    if (isNoopRun()) {
        statistics.pushUnitAndType(typeSelector.getUnit(), typeSelector.getType());
        return TestResult::Nooped;
    }

    // Setup - Initialize Sysman
    ze_result_t result = zesInit(0);
    if (result != ZE_RESULT_SUCCESS) {
        return TestResult::DeviceNotCapable;
    }

    // Get driver
    uint32_t driverCount = 0;
    result = zesDriverGet(&driverCount, nullptr);
    if (result != ZE_RESULT_SUCCESS || driverCount == 0) {
        return TestResult::DeviceNotCapable;
    }

    std::vector<zes_driver_handle_t> drivers(driverCount);
    result = zesDriverGet(&driverCount, drivers.data());
    if (result != ZE_RESULT_SUCCESS) {
        return TestResult::DeviceNotCapable;
    }

    uint32_t driverIndex = Configuration::get().l0DriverIndex;
    if (driverIndex >= driverCount) {
        driverIndex = 0;
    }
    zes_driver_handle_t driver = drivers[driverIndex];

    // Get device
    uint32_t deviceCount = 0;
    result = zesDeviceGet(driver, &deviceCount, nullptr);
    if (result != ZE_RESULT_SUCCESS || deviceCount == 0) {
        return TestResult::DeviceNotCapable;
    }

    std::vector<zes_device_handle_t> devices(deviceCount);
    result = zesDeviceGet(driver, &deviceCount, devices.data());
    if (result != ZE_RESULT_SUCCESS) {
        return TestResult::DeviceNotCapable;
    }

    uint32_t deviceIndex = Configuration::get().l0DeviceIndex;
    if (deviceIndex >= deviceCount) {
        deviceIndex = 0;
    }
    zes_device_handle_t device = devices[deviceIndex];

    Timer timer;

    // Benchmark
    for (auto j = 0u; j < arguments.iterations; j++) {
        uint32_t count = 0;
        timer.measureStart();
        result = zesDeviceEnumFrequencyDomains(device, &count, nullptr);
        if (result != ZE_RESULT_SUCCESS) {
            return TestResult::DeviceNotCapable;
        }
        std::vector<zes_freq_handle_t> handles(count);
        if (count > 0) {
            result = zesDeviceEnumFrequencyDomains(device, &count, handles.data());
            if (result != ZE_RESULT_SUCCESS) {
                return TestResult::DeviceNotCapable;
            }
        }
        timer.measureEnd();
        statistics.pushValue(timer.get(), typeSelector.getUnit(), typeSelector.getType());
    }

    return TestResult::Success;
}

static RegisterTestCaseImplementation<FrequencyDomainEnum> registerTestCase(run, Api::L0);
