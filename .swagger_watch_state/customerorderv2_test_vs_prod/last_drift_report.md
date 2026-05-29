# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-29T20:01:45Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9d53651d7fa259fcbe798758f34789c5c7389e08761bba06b94d34eaf4b8288c`
- PROD hash: `16737a4f5df09786f0547df876deb4308b71d09c9606b3efbfb6ed78eb7a7604`

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
