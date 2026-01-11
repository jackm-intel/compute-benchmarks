/*
 * Copyright (C) 2022 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#pragma once

#include "framework/argument/basic_argument.h"
#include "framework/test_case/test_case.h"

struct MemoryModuleEnumArguments : TestCaseArgumentContainer {
    PositiveIntegerArgument iterations;

    MemoryModuleEnumArguments()
        : iterations(*this, "iterations", "Number of iterations to measure") {}
};

struct MemoryModuleEnum : TestCase<MemoryModuleEnumArguments> {
    using TestCase<MemoryModuleEnumArguments>::TestCase;

    std::string getTestCaseName() const override {
        return "MemoryModuleEnum";
    }

    std::string getHelp() const override {
        return "measures time spent enumerating Sysman memory modules on CPU.";
    }
};
