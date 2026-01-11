/*
 * Copyright (C) 2022-2023 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#include "definitions/power_domain_enum.h"

#include "framework/test_case/register_test_case.h"

#include <gtest/gtest.h>

[[maybe_unused]] static const inline RegisterTestCase<PowerDomainEnum> registerTestCase{};

class PowerDomainEnumTest : public ::testing::TestWithParam<size_t> {
};

TEST_P(PowerDomainEnumTest, Test) {
    PowerDomainEnumArguments args{};
    args.api = Api::L0;
    args.iterations = GetParam();
    PowerDomainEnum test;
    test.run(args);
}

INSTANTIATE_TEST_SUITE_P(
    PowerDomainEnumTest,
    PowerDomainEnumTest,
    ::testing::Values(100, 1000));
