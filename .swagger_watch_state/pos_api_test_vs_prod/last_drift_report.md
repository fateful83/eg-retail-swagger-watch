# TEST vs PROD drift detected: POS API

- Time: 2026-05-08T13:02:25Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `463ff7091460703fbffd0a9adfcbf1c463d2d3fe9e82e5084b0c66f9860f5a45`
- PROD hash: `8d42e642341e1ee80f5c34c9358425f1ea123e7e39372202de5c81460c319c2b`

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
