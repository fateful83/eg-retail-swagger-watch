# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-24T18:55:03Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `849d5fdf23abd823b8b11fc2bc594aa6c94b627028a413cbc90cdd6100e9013e`
- PROD hash: `e8d087b85d87a6b6cab2b40e7622a972173e8f4b20c521e156d1f76deed8f9fa`

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
