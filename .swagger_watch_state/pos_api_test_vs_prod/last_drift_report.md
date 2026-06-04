# TEST vs PROD drift detected: POS API

- Time: 2026-06-04T09:37:18Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `d47a1498b2e881de9fc80af51b064c5c94cf030779ce169d33a93b0aabe85960`
- PROD hash: `be0c9bfa2bd80f38b719ebfc60a3c7409d3c04ff012635a09ce1f1c169d9bddb`

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
