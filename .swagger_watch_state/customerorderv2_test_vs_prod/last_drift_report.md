# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-31T01:57:48Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `e4bd95e223613c357d50ed8cd3ffc9325ba96190dcdec0f7929365fb4eafb70d`
- PROD hash: `850119d8847036f352257ad8ec7c4cb072a87925bcde338e4b4f89441160f10a`

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
