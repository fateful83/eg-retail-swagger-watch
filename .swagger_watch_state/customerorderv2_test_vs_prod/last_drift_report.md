# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-30T18:53:44Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b9124cd100c70f6d221d7e732cb6eff94ea50df39543c8413e6bbe226c08579c`
- PROD hash: `8b54fb2f896623bdb2f2bea4fcdb301d03c65f88d6e48472613a7133ddba3541`

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
