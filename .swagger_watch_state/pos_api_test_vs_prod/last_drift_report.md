# TEST vs PROD drift detected: POS API

- Time: 2026-11-02T02:51:10Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `dfd6916b4f50b40aefee79cfe60aed1e203a5145100464ec8844e9cea9c6af4c`
- PROD hash: `6a9655ebb70af26168a1f83ebc0c9ccce4316a80766f85bb425eef8edf403058`

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
