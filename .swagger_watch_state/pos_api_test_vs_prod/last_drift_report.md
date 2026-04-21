# TEST vs PROD drift detected: POS API

- Time: 2026-04-21T01:13:12Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `03d37381532945d272c0b4d0b3208f48fb56b1c1ea85a45da27a0db1912dd6dc`
- PROD hash: `e32fb042837252ae0f787a04bc4163ed1e22118d8641decab27166e40115a6bf`

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
