# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-27T14:47:05Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `3462f5290dcaadc5afd1fd32d453d46634b54622c317fba077bbcad018d35aab`
- PROD hash: `02f8236c02e1edc95936273948991639c1418eb4ce830dc91a115bcb5388e2d4`

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
