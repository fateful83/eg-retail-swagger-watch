# DEV vs TEST drift detected: ItemService

- Time: 2026-11-10T13:50:06Z
- Severity: breaking
- DEV Swagger URL: https://itemservice.egretail-dev.cloud/swagger/v1/swagger.json
- TEST Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- DEV hash: `a1877a1f177c17284a9c75c1ccae4ab05cfe981b83665ad6530ce83b9e50315f`
- TEST hash: `3659a666b6eafd51649e4863093687e661c92c1e30286074603f47a310c9fed8`

## Summary
- Only in DEV: 0
- Only in TEST: 0
- Present in both but different: 30

## Only in DEV
- None

## Only in TEST
- None

## Different in DEV and TEST
- GET /api/Brands
- GET /api/Brands/{id}
- GET /api/ItemCategories
- GET /api/ItemCategories/{id}
- GET /api/ItemLists
- GET /api/NonsaleType
- GET /api/Nutritions
- GET /api/ProcurementRules
- GET /api/ProcurementRules/{id}
- GET /api/ReplenishmentCodes
- GET /api/ReplenishmentCodes/{id}
- GET /api/Sizes
- GET /api/Sizes/{id}
- POST /api/Brands
- POST /api/Colors/upsertByName
- POST /api/ItemCategories
- POST /api/ItemLists
- POST /api/NonsaleType
- POST /api/ProcurementRules
- POST /api/ReplenishmentCodes
- POST /api/Sizes
- POST /api/TradingUnits
- PUT /api/Brands/{id}
- PUT /api/ItemCategories/{id}
- PUT /api/ItemLists/{id}
- PUT /api/NonsaleType/{id}
- PUT /api/ProcurementRules/{id}
- PUT /api/ReplenishmentCodes/{id}
- PUT /api/Sizes/{id}
- PUT /api/TradingUnits/{id}
