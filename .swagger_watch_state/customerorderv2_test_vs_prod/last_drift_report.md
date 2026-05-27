# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-27T19:53:45Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `317e89cd126078babde94358ac41ac81c261f1a3cb21ffa63579adcb727f1267`
- PROD hash: `3777842c1015a2d38cace42b5563c744bc3494857707547aa7857dd820edc743`

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
