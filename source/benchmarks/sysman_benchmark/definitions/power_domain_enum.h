/*
 * Copyright (C) 2022 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#pragma once

#include "framework/argument/basic_argument.h"
#include "framework/test_case/test_case.h"

struct PowerDomainEnumArguments : TestCaseArgumentContainer {
    PositiveIntegerArgument iterations;

    PowerDomainEnumArguments()
        : iterations(*this, "iterations", "Number of iterations to measure") {}
};

struct PowerDomainEnum : TestCase<PowerDomainEnumArguments> {
    using TestCase<PowerDomainEnumArguments>::TestCase;

    std::string getTestCaseName() const override {
        return "PowerDomainEnum";
    }

    std::string getHelp() const override {
        return "measures time spent enumerating Sysman power domains on CPU.";
    }
};
