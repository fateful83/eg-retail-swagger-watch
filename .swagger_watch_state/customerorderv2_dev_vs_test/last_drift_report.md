# DEV vs TEST drift detected: CustomerOrderV2

- Time: 2026-06-10T14:44:35Z
- Severity: breaking
- DEV Swagger URL: https://customerorderv2service.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `935d89c7c450390fb29e05ac808644a5d970e83e259eedf122fdaa1091eb1ff4`
- TEST hash: `9c5a347241a3139e575cb15eec61ff9b07a0cdc892b2f83e559182d7b480b876`

## Summary
- Only in DEV: 1
- Only in TEST: 0
- Present in both but different: 1

## Only in DEV
- PATCH /api/gateway/ServiceOrders/{orderNumber}/orderStatus

## Only in TEST
- None

## Different in DEV and TEST
- POST /api/gateway/ServiceOrders/{storeNumber}/{orderNumber}/payment
