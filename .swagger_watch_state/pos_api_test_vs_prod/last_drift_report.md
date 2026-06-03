# TEST vs PROD drift detected: POS API

- Time: 2026-06-03T16:08:33Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `b908160bd5bfdfe661d8c5c7415aa2600e877f37bbd93fb27ce0d04549c84aa9`
- PROD hash: `c83433cbcead32fe706536959ef19dc59c22dc82d37b0c9d4dc48c34694969f1`

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
