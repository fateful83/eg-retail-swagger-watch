# TEST vs PROD drift detected: POS API

- Time: 2026-04-17T01:14:01Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f09ecc7bd9e5b0fd32e58bf2cf273ee67f264764fad9d7038cc4358063adab91`
- PROD hash: `23d292fe23534f27c2ef5e8f1bc93109e82caeaab3f2e5f1cfdba0744e19fc62`

## Summary
- Only in TEST: 1
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- POST /api/Payment/AddBonusPaymentToCart

## Only in PROD
- None

## Different in TEST and PROD
- None
