# TEST vs PROD drift detected: POS API

- Time: 2026-06-02T15:49:36Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f85b545ee255b77004dcb68d85ef87edd5056b661c99d186d5fa8426d0a1aa15`
- PROD hash: `23ada680640070fd0b8fbeb93fc9f19af2069102e03bfd4003e624ed1347b0cc`

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
