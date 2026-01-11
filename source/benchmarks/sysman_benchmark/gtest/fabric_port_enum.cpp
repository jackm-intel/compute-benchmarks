/*
 * Copyright (C) 2022-2023 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#include "definitions/fabric_port_enum.h"

#include "framework/test_case/register_test_case.h"

#include <gtest/gtest.h>

[[maybe_unused]] static const inline RegisterTestCase<FabricPortEnum> registerTestCase{};

class FabricPortEnumTest : public ::testing::TestWithParam<size_t> {
};

TEST_P(FabricPortEnumTest, Test) {
    FabricPortEnumArguments args{};
    args.api = Api::L0;
    args.iterations = GetParam();
    FabricPortEnum test;
    test.run(args);
}

INSTANTIATE_TEST_SUITE_P(
    FabricPortEnumTest,
    FabricPortEnumTest,
    ::testing::Values(100, 1000));
