# DEV vs TEST drift detected: POS API

- Time: 2026-04-17T01:14:01Z
- Severity: breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `84f8d8f58227c5e01f4a7dee3be9bc6d9a05bea92446c1e5c3e2cdf16e4b901d`
- TEST hash: `f09ecc7bd9e5b0fd32e58bf2cf273ee67f264764fad9d7038cc4358063adab91`

## Summary
- Only in DEV: 0
- Only in TEST: 1
- Present in both but different: 0

## Only in DEV
- None

## Only in TEST
- POST /api/Payment/AddBonusPaymentToCart

## Different in DEV and TEST
- None
