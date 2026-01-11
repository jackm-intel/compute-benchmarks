/*
 * Copyright (C) 2022-2023 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#include "definitions/full_sysman_enum.h"

#include "framework/test_case/register_test_case.h"

#include <gtest/gtest.h>

[[maybe_unused]] static const inline RegisterTestCase<FullSysmanEnum> registerTestCase{};

class FullSysmanEnumTest : public ::testing::TestWithParam<size_t> {
};

TEST_P(FullSysmanEnumTest, Test) {
    FullSysmanEnumArguments args{};
    args.api = Api::L0;
    args.iterations = GetParam();
    FullSysmanEnum test;
    test.run(args);
}

INSTANTIATE_TEST_SUITE_P(
    FullSysmanEnumTest,
    FullSysmanEnumTest,
    ::testing::Values(100, 1000));
