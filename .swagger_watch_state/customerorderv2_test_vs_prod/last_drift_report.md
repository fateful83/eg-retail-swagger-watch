# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-12T00:46:37Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ebd30ec759a6d79b476d684bcbf3c8399f3fa30c5b664d8d9c36c38c5acde7bc`
- PROD hash: `555d607b8f3fe2b59938b2bd9270c121fba01c4848fee270bcf19d7b6b82bd1c`

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
