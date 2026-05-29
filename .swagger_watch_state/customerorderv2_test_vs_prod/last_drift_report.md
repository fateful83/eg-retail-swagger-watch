# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-29T01:50:43Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `68fd6e93ce1c2a7be286e77ecdaa4d391ee7199a3ca35f81a6187bcc17d40af5`
- PROD hash: `d34ea0d52c9cf2ac518e942e20fd762a500e3f209bb8688c04684cb81d307b8c`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- GET /api/gateway/ServiceOrders/{storeNumber}

## Only in PROD
- None

## Different in TEST and PROD
- None
