# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-28T01:12:05Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `2dd1b505d343a6dc70617f0a095096fe8279d48c1a6845108a40ab949a4ceb97`
- PROD hash: `f9264fd83ad60c5cceaf4314912135f371a7b6b70dd1eca56c597c938b5e16c2`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 1

## Only in TEST
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in PROD
- None

## Different in TEST and PROD
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
