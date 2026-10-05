# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-05T23:23:23Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `eb706f2511b5e78a9e5c5a654e2d486f6fcba458393b3c18178987c8e83f2d76`
- PROD hash: `c33a5927b7e0607749e627ef34011a9f23fa00f6ba5297afe1e10304214186d1`

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
