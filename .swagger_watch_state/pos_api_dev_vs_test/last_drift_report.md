# DEV vs TEST drift detected: POS API

- Time: 2026-10-16T20:09:32Z
- Severity: non_breaking
- DEV Swagger URL: https://posapi.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://posapi.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `045f464ad4bdcbf21ff71cda996fd1084cb51feba0b0ee76ba0410feb9e47689`
- TEST hash: `b74937d0b5995794a970d1c1f0f233801a2694bc581106091d61c5bf54726c99`

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
