/*
 * Copyright (C) 2022 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#pragma once

#include "framework/argument/basic_argument.h"
#include "framework/test_case/test_case.h"

struct FullSysmanEnumArguments : TestCaseArgumentContainer {
    PositiveIntegerArgument iterations;

    FullSysmanEnumArguments()
        : iterations(*this, "iterations", "Number of iterations to measure") {}
};

struct FullSysmanEnum : TestCase<FullSysmanEnumArguments> {
    using TestCase<FullSysmanEnumArguments>::TestCase;

    std::string getTestCaseName() const override {
        return "FullSysmanEnum";
    }

    std::string getHelp() const override {
        return "measures time spent enumerating all Sysman domains (power, frequency, memory, fabric, temperature) on CPU.";
    }
};
