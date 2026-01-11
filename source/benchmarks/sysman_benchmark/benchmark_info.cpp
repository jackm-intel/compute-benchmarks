/*
 * Copyright (C) 2022-2023 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#include "framework/benchmark_info.h"

#include "framework/utility/execute_at_app_init.h"

EXECUTE_AT_APP_INIT {
    const std::string name = "sysman_benchmark";
    const std::string description = "Benchmarks for Level Zero Sysman (System Management) enumeration APIs.";
    const int testCaseColumnWidth = 130;
    BenchmarkInfo::initialize(name, description, testCaseColumnWidth);
};
