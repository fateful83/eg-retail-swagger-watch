# TEST vs PROD drift detected: POS API

- Time: 2026-06-05T08:58:49Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `98da52acccb11f1dfbc777fe307f200dea380e8e17d6015065b8affd3dbc3e2a`
- PROD hash: `847775097d8573c404b6d3f4ff74961927b2248f18093ce504d18306407e41f1`

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
