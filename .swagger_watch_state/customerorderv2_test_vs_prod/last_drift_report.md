# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-14T01:47:52Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f7948da4ceeedd91fc9e629479276cad7c8108edef8a37b222a7f705fec412dc`
- PROD hash: `999ee6b09754a96e988560ee46a7a3d45a086e638b505c914f520eb2cc9415aa`

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
