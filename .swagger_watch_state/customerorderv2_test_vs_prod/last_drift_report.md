# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-09-27T15:51:15Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ada51aa3d3155a08f309c8199a2f8233118b61baae704d8a372c6060239d1e0a`
- PROD hash: `ea93db0e8f716bad147d6f03ddb22e3270170313f6d6a50a13c29b39313b9c09`

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
