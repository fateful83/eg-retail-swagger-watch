# DEV vs TEST drift detected: POS API

- Time: 2026-10-26T11:36:55Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `84a43dd961c7a8a39d4e1b371584084ecc91cae79ae66fe1e1a18107159e84a4`
- TEST hash: `0e5fdb0c898e28d307d04e04a2e853b837f793a28744ff8065da40c38bbda146`

## Summary
- Only in DEV: 3
- Only in TEST: 0
- Present in both but different: 0

## Only in DEV
- GET /api/UserService/PingHealth
- POST /api/UserService/Authenticate
- POST /api/UserService/CheckUserExists

## Only in TEST
- None

## Different in DEV and TEST
- None
