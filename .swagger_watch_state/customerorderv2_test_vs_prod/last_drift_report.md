# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-07-04T01:23:56Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `76200f8594676f6109425f1c9a392874c4bdf7a11a7ae1929011f2966d53f7a6`
- PROD hash: `8a0b549e8615b9fcc24f0d056912f9dd344030aae6ff9cc2ec2131014b302755`

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
