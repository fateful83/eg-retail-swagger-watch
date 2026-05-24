# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-24T08:10:52Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `40ad49d6e9146fd91dd7b58780d970195fe1cd413b36e2d436adb457ab684596`
- PROD hash: `fb29e9a8c9991c969c405e3e528ac34aabee6a3597bc5e2feea1913a0326e970`

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
