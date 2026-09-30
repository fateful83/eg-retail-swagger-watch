# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-30T11:26:55Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `0de54db5f5678c5c65cd5232a41372f9ac108f7884bfd10f8c8b3265bbb6e93f`
- PROD hash: `b709f887a7414e38a843ffed5d6ad99fefd60d52ab23329095384683f0721407`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 1

## Only in TEST
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in PROD
- None

## Different in TEST and PROD
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
