# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-07T13:12:18Z
- Severity: non_breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `0cc11671ab15d20475e0d0864f27d497c4d5999a974c8f4b7afa8b53511fac91`
- TEST hash: `e3bd6b6d37017feed2e497583dcbe40ee4f9d296a4679ca434e136a62b26b073`

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
