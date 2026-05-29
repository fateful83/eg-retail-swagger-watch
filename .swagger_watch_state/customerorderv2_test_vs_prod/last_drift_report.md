# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-29T08:59:05Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `9add0346eb078b2fa87f69cb516a05c09d4652f2cfb6714625c2399e811d2205`
- PROD hash: `b644776cc3dca3e05c35c5ff2fd8302c615fccb2b8f46ad1793b933ba1d9d24a`

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
