# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-14T21:05:22Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8c57c130364854842901d74f52bc1f5cc58f8cece4d69ff86159c1a77fe7eb59`
- PROD hash: `46baf825d9530a996a76bf51461867a56cc0e73909263d86bf65ce27e527c192`

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
