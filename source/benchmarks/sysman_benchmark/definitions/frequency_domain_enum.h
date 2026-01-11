/*
 * Copyright (C) 2022 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#pragma once

#include "framework/argument/basic_argument.h"
#include "framework/test_case/test_case.h"

struct FrequencyDomainEnumArguments : TestCaseArgumentContainer {
    PositiveIntegerArgument iterations;

    FrequencyDomainEnumArguments()
        : iterations(*this, "iterations", "Number of iterations to measure") {}
};

struct FrequencyDomainEnum : TestCase<FrequencyDomainEnumArguments> {
    using TestCase<FrequencyDomainEnumArguments>::TestCase;

    std::string getTestCaseName() const override {
        return "FrequencyDomainEnum";
    }

    std::string getHelp() const override {
        return "measures time spent enumerating Sysman frequency domains on CPU.";
    }
};
