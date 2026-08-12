# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-12T07:01:19Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `cc4ab85cdc1a9b896e09a0b216a62748aef3a9398a4df76055dbad1b4f1084b9`
- PROD hash: `53fdef14286826b71d48a46f24f9a5dc41fb66dc7a459b251230f99bbc8373e6`

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
