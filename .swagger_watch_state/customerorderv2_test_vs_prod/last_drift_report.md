# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-23T18:48:38Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2a62e318a3e805cb4d8409679a51a221ca5d15a2de75c094c4c007f34e05bd8d`
- PROD hash: `b60b8af4854d43a7cc74dbbc7d062613f36eaa633b3fee0fed4c2abde077b6c1`

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
