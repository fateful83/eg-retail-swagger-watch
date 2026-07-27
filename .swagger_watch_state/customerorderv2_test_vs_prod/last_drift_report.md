# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-27T19:05:23Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `894bb1445fef9406907ec16f92b7a1fc08fbb17fc768830664b0e7a8c00c7287`
- PROD hash: `bdf897e07ec506617235a77375aed66f135dc53afd2a3c994f7f2a32ec876f9b`

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
