# TEST vs PROD drift detected: CustomerOrderV2

- Time: 2026-05-29T14:30:24Z
- Severity: non_breaking
- TEST Swagger URL: https://customerorderv2service.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://customerorderv2service.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `fba201f4f8451d27df5190c6dfbe7b65f2eaeb61be5c3879d4b13db06661dfcd`
- PROD hash: `bce64458bc3d9c2fc293d0dabd9692fa8522c7a57324ab5ed310e9602b816ed3`

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
