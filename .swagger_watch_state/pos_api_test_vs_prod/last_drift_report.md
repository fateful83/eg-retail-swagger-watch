# TEST vs PROD drift detected: POS API

- Time: 2026-05-10T12:44:51Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a43e22166792668481170aacb2917b2095b834b049ab9abe7b55096336e80622`
- PROD hash: `3e72a94461be44012be9b6b1f59950eccedb076fb8f13b4e4e737d52989f47e0`

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
