# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-02T21:28:34Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `ee12b98e48533767c90488a24e6f32b459bd719c6984457ec2bf6c240a610afb`
- PROD hash: `13656d45633a6856adc0e6fbe0256edc4f189b0bc3badae5fb23c0a2eced7c30`

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
