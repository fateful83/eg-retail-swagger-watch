# TEST vs PROD drift detected: POS API

- Time: 2026-06-09T01:46:30Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `f881f2ca854c1be82ce23b3f1969fbb0f82a5be61127bdd9c51e681ab6a36746`
- PROD hash: `4e1bfa2d02b3efd5a122db48b93df2a83dad2080d7916ef5e2eb6c4e21c78608`

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
