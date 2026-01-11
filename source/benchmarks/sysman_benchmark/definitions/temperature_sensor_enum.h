/*
 * Copyright (C) 2022 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#pragma once

#include "framework/argument/basic_argument.h"
#include "framework/test_case/test_case.h"

struct TemperatureSensorEnumArguments : TestCaseArgumentContainer {
    PositiveIntegerArgument iterations;

    TemperatureSensorEnumArguments()
        : iterations(*this, "iterations", "Number of iterations to measure") {}
};

struct TemperatureSensorEnum : TestCase<TemperatureSensorEnumArguments> {
    using TestCase<TemperatureSensorEnumArguments>::TestCase;

    std::string getTestCaseName() const override {
        return "TemperatureSensorEnum";
    }

    std::string getHelp() const override {
        return "measures time spent enumerating Sysman temperature sensors on CPU.";
    }
};
