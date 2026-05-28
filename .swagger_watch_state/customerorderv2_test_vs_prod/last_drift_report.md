# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-28T20:00:02Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `91ffd80a821a743b45c4a3b09d7cd7259ea93b9935a7f540d57107755f5819d9`
- PROD hash: `fbbcba18b08ccc9d28af4fe0ba725bd2babe6071ac926c6b34c8ef9aadfd8c87`

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
