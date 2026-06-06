# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-06T01:49:47Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `4fb35b40bbbdedda2c197e8722aa8524736dbd87c103647ea768cb6e0ab6aedc`
- TEST hash: `4411ec92063d9c6dfd465ac0a9a96264f5ddeb8580ce44d2e7501edd36ec531b`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- PATCH /api/gateway/ServiceOrders/{orderNumber}/order-status

## Only in TEST
- None

## Different in DEV and TEST
- None
