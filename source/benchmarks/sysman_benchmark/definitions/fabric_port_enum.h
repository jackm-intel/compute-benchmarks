/*
 * Copyright (C) 2022 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#pragma once

#include "framework/argument/basic_argument.h"
#include "framework/test_case/test_case.h"

struct FabricPortEnumArguments : TestCaseArgumentContainer {
    PositiveIntegerArgument iterations;

    FabricPortEnumArguments()
        : iterations(*this, "iterations", "Number of iterations to measure") {}
};

struct FabricPortEnum : TestCase<FabricPortEnumArguments> {
    using TestCase<FabricPortEnumArguments>::TestCase;

    std::string getTestCaseName() const override {
        return "FabricPortEnum";
    }

    std::string getHelp() const override {
        return "measures time spent enumerating Sysman fabric ports on CPU.";
    }
};
