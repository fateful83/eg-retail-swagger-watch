# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-26T20:14:45Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a24894cfc40d4f93dd6d08817aab1ec1003f03c4bf60615ae68df7aa4c6ed4e8`
- PROD hash: `886e820623ef011fe449f56bfe2956c93068f388d263966539c1f9bef66b4e5b`

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
