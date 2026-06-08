# TEST vs PROD drift detected: POS API

- Time: 2026-06-08T10:09:18Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `dab002b54a915a065f612688be2cd607e284f3844568dd67b34f7de0cacd676d`
- PROD hash: `b0e014d368404e2bfa506c0456569618563d365ce511edc1dfcd27aa6eb79454`

## Summary
- Only in TEST: 2
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- POST /api/Payment/BeginKlarnaPayment
- POST /api/Payment/EndKlarnaPayment

## Only in PROD
- None

## Different in TEST and PROD
- None
