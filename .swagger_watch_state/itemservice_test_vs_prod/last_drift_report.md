# TEST vs PROD drift detected: ItemService

- Time: 2026-06-22T02:13:38Z
- Severity: breaking
- TEST Swagger URL: https://itemservice.egretail-test.cloud/swagger/v1/swagger.json
- PROD Swagger URL: https://itemservice.egretail.cloud/swagger/v1/swagger.json
- TEST hash: `a21d1a5e8ae40385c9a7def022a37c00eda3b239767cd2f31eb0204e216d1e0d`
- PROD hash: `98d3fefa6188b48439efd7663b4d4ca054241a13f56e3765ae56bd465d8dee47`

## Summary
- Only in TEST: 0
- Only in PROD: 10
- Present in both but different: 42

## Only in TEST
- None

## Only in PROD
- GET /api/CalculationRulesets
- GET /api/CalculationRulesets/DefaultRuleset
- GET /api/CalculationRulesets/{id}
- GET /api/Imports/{id}/calculationRuleset
- GET /api/PriceCalculations/StorePriceCalculations
- GET /api/RetailPriceCalculationRules
- POST /api/StorePrices/GetCorrelatedPrices
- POST /api/StorePrices/GetPriceCounts
- POST /api/StorePrices/PriceDateValidate
- POST /api/StorePrices/{id}/Copy

## Different in TEST and PROD
- GET /api/Brands
- GET /api/Brands/{id}
- GET /api/Collections
- GET /api/Collections/{id}
- GET /api/ItemCategories
- GET /api/ItemCategories/{id}
- GET /api/ItemLists
- GET /api/MarketingCodes
- GET /api/MarketingCodes/{id}
- GET /api/MarketingExclusivities
- GET /api/MarketingExclusivities/{id}
- GET /api/NonsaleType
- GET /api/Nutritions
- GET /api/ProcurementRules
- GET /api/ProcurementRules/{id}
- GET /api/ReplenishmentCodes
- GET /api/ReplenishmentCodes/{id}
- GET /api/Sizes
- GET /api/Sizes/{id}
- POST /api/Brands
- POST /api/Collections
- POST /api/Colors/upsertByName
- POST /api/ItemCategories
- POST /api/ItemLists
- POST /api/MarketingCodes
- POST /api/MarketingExclusivities
- POST /api/NonsaleType
- POST /api/ProcurementRules
- POST /api/ReplenishmentCodes
- POST /api/Sizes
- POST /api/TradingUnits
- PUT /api/Brands/{id}
- PUT /api/Collections/{id}
- PUT /api/ItemCategories/{id}
- PUT /api/ItemLists/{id}
- PUT /api/MarketingCodes/{id}
- PUT /api/MarketingExclusivities/{id}
- PUT /api/NonsaleType/{id}
- PUT /api/ProcurementRules/{id}
- PUT /api/ReplenishmentCodes/{id}
- PUT /api/Sizes/{id}
- PUT /api/TradingUnits/{id}
