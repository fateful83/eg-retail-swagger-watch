# TEST vs PROD drift detected: POS API

- Time: 2026-05-09T07:28:05Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `4dacebb1788698fa135fdd5a11dcf97f289a427135214a80ed0dbb74694a6a19`
- PROD hash: `94f56d96d4b1d68267bee9ea1a04401041c6f46cd5f0caa5f4f452775509191a`

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
