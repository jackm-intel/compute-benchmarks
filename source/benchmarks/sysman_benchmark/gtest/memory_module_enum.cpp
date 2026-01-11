/*
 * Copyright (C) 2022-2023 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#include "definitions/memory_module_enum.h"

#include "framework/test_case/register_test_case.h"

#include <gtest/gtest.h>

[[maybe_unused]] static const inline RegisterTestCase<MemoryModuleEnum> registerTestCase{};

class MemoryModuleEnumTest : public ::testing::TestWithParam<size_t> {
};

TEST_P(MemoryModuleEnumTest, Test) {
    MemoryModuleEnumArguments args{};
    args.api = Api::L0;
    args.iterations = GetParam();
    MemoryModuleEnum test;
    test.run(args);
}

INSTANTIATE_TEST_SUITE_P(
    MemoryModuleEnumTest,
    MemoryModuleEnumTest,
    ::testing::Values(100, 1000));
