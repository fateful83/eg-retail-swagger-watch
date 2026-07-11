# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-11T07:27:44Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `87751123b854e81f5f6657e86ef791fe8df44c7b17626d7ab623c5fa0ebfe8d5`
- PROD hash: `411c0f1f2c03ab910a3018010d73abce1fe767dbfd3e110e7da21aa6c154b007`

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
