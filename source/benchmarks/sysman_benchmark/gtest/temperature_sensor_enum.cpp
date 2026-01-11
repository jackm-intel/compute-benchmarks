/*
 * Copyright (C) 2022-2023 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#include "definitions/temperature_sensor_enum.h"

#include "framework/test_case/register_test_case.h"

#include <gtest/gtest.h>

[[maybe_unused]] static const inline RegisterTestCase<TemperatureSensorEnum> registerTestCase{};

class TemperatureSensorEnumTest : public ::testing::TestWithParam<size_t> {
};

TEST_P(TemperatureSensorEnumTest, Test) {
    TemperatureSensorEnumArguments args{};
    args.api = Api::L0;
    args.iterations = GetParam();
    TemperatureSensorEnum test;
    test.run(args);
}

INSTANTIATE_TEST_SUITE_P(
    TemperatureSensorEnumTest,
    TemperatureSensorEnumTest,
    ::testing::Values(100, 1000));
