# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-26T10:21:09Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `aee5ee2760430407ac02bc2f5de4971820682f63d2fb8b0e1f00796274d58d0b`
- PROD hash: `41298d4857b79af35ca4b457d8c75a37002ef3056b531e92952e13774afa50a2`

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
