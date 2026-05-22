# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-22T01:53:40Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b3269912f371eb54f570bdfe76c06c76c192a94d38e5beff3e5c0d83cc14fa4c`
- PROD hash: `0ca2a860b84dbd2b2113d2c7b9d45f94275bfc21cae88f1cc8fe14abae81c5c6`

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
