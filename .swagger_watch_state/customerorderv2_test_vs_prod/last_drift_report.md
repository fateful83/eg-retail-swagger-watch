# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-22T19:18:28Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d4951479f86ccadd9ed322e0662a06a2352fd6edcde4dfb4e7f99ecd99aef81c`
- PROD hash: `5ef8b06c4e8b42b9a2a476e220d13a182bd3018050ee88c4322ba911e7140497`

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
