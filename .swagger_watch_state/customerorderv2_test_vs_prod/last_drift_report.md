# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-08-19T18:14:05Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e320cf64ed4bfa8bb215721b4debf7953fed402d762b6eac7a58f940c0b36ad3`
- PROD hash: `7fa8a9be06f35431ea5f720fd43bc25ca6a83ba1248c6391b3f292d04ba53b63`

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
