# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-10-06T03:24:36Z
- Severity: breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `8a3434b496507d1a064d6f0842dffc4f525b88026406cff6739883b5c614862f`
- PROD hash: `76049fc70a34acbadad7d5b73c42eda6757c6c560eb733db8cedf3d3e4746d11`

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
