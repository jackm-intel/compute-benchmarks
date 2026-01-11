/*
 * Copyright (C) 2022-2023 Intel Corporation
 *
 * SPDX-License-Identifier: MIT
 *
 */

#include "definitions/frequency_domain_enum.h"

#include "framework/test_case/register_test_case.h"

#include <gtest/gtest.h>

[[maybe_unused]] static const inline RegisterTestCase<FrequencyDomainEnum> registerTestCase{};

class FrequencyDomainEnumTest : public ::testing::TestWithParam<size_t> {
};

TEST_P(FrequencyDomainEnumTest, Test) {
    FrequencyDomainEnumArguments args{};
    args.api = Api::L0;
    args.iterations = GetParam();
    FrequencyDomainEnum test;
    test.run(args);
}

INSTANTIATE_TEST_SUITE_P(
    FrequencyDomainEnumTest,
    FrequencyDomainEnumTest,
    ::testing::Values(100, 1000));
