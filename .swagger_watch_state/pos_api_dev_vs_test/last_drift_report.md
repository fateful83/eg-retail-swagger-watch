# DEV vs TEST drift detected: POS API

- Time: 2026-10-22T16:08:17Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `7055f5dd3af6663b9c64e252500b3ece116e50693f64aa13194c5cb5744951f4`
- TEST hash: `5082da7402781211984e89240a695a4af4af5281a603852e594c95c1639cc387`

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
