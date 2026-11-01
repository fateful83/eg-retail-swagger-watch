# TEST vs PROD drift detected: POS API

- Time: 2026-11-01T21:24:43Z
- Severity: non_breaking
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://posapi.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `eadc2897d909cac6f833092d238278ac5a51f64a3a39eb12aa9f61500211b8b7`
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
