# TEST vs PROD drift detected: POS API

- Time: 2026-10-30T03:02:57Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `80d22b327cd68261d78188e7640e7910976ea93abb031294be2a6d8ef39c03d8`
- PROD hash: `6cb3b565c9cce5789d9dbc636154dbbcc25e44c2b6e2683621e9924f7fc6a65e`

## Summary
- Only in TEST: 3
- Only in PROD: 0
- Present in both but different: 0

## Only in TEST
- GET /api/UserService/PingHealth
- POST /api/UserService/Authenticate
- POST /api/UserService/CheckUserExists

## Only in PROD
- None

## Different in TEST and PROD
- None
