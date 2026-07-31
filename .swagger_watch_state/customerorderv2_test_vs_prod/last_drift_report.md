# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-31T08:24:48Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `149e3990f67c24a315cc317065c7e34650fc0375651184931d6e42992f399aa6`
- PROD hash: `cd6a47d4ec2ef73957562d8fb6a6440aa880dc5cc0e94154bc98512cbe55f42b`

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
