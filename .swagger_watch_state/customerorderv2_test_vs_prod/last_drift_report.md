# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-17T18:46:38Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cbd4fe979e96931c261b59d575407bda3553d59538d289bd80c46af099454096`
- PROD hash: `78ec274dd88be497dc280a026e34ae2698d32e9ad1a191eebc3de2c72f66c470`

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
