# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-01T10:34:06Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d99d6ac9f5593501ddf84396b3a1ac788ce6eb39f021e5a6b1bf043bb3c5e071`
- PROD hash: `52eb5a616f8cf7e069b6f9800765a14a321593358029ae5ff65c5c2bd0aa5cda`

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
