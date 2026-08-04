# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-04T08:11:39Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a1d015635ba5f957b37056c587424b56b2c5056d2ff7b5733fbc4f2fc99ef3cf`
- PROD hash: `f8027a02cc8fdb998a0bf6173329892e72ed32dfb801b4e0e414ed3e65e66482`

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
