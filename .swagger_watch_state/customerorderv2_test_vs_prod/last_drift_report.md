# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-30T08:11:28Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `939ffd7b179ceda7f9fc6084ed256f52baa3bc291f7b9aaed95dfb112276ab6d`
- PROD hash: `fbfe68b1d3b9b869ef5520b73c21d6740fa93f45ec062cfc112d5bc859906c6b`

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
