# Multiverse Bridge API
The Multiverse Bridge is a Cardsphere community-built project aimed to help translate Cardsphere card and set data to other platforms.

The project leverages existing tools MTGJSON and Scryfall to provide the data to enable consumers to translate their Cardsphere collection data to another platform that supports MTGJSON or Scryfall identifiers.

## APIs

<details>
  <summary>GET /sets</summary>
  
  Returns a list of all Cardsphere sets including that set's MTGJSON equivalent code value.
  
  ```
  [{
      "cs_id": 755,
      "cs_name": "10th Edition",
      "mtgjson_code": "10E"
    },
    {
      "cs_id": 756,
      "cs_name": "4th Edition",
      "mtgjson_code": "4ED"
    },
    ...
  ]
  ```
</details>

<details>
  <summary>GET /sets/{cs_id}</summary>
    
  Returns the Cardsphere set specified by the cs_id and a list of the cards in the set.
  
  ```
  {
    "cs_id": 755,
    "cs_name": "10th Edition",
    "mtgjson_code": "10E",
    "cards": [{
      "cs_id": 1,
      "url": "/cards/1",
      "name": "Abundance",
      "edition": "10th Edition",
      "is_foil": true,
      "mtgjson_id": "1669af17-d287-5094-b005-4b143441442f",
      "scryfall_id": "46184f97-d5c9-4a98-9fd9-e19057ce9b7e",
      "collector_number": "249",
      "mtgjson_code": "10E"
    },
    ...
    ]
  }
  ```
</details>

<details>
  <summary>GET /sets/mtgjson/{mtgjson_code}</summary>
  
  Returns the Cardsphere set specified by the MTGJSON set code and a list of the cards in the set.
  ```
  {
    "cs_id": 755,
    "cs_name": "10th Edition",
    "mtgjson_code": "10E",
    "cards": [{
      "edition": "10th Edition",
          "name": "Abundance",
          "collector_number": "249",
          "cs_id": 1,
          "is_foil": true,
          "mtgjson_id": "1669af17-d287-5094-b005-4b143441442f",
          "url": "/cards/1",
          "mtgjson_code": "10E",
          "scryfall_id": "46184f97-d5c9-4a98-9fd9-e19057ce9b7e"
    },
    ...
    ]
  }
  ```
</details>

<details>
  <summary>GET /cards/{cs_id}</summary>
  
  Returns the Cardsphere card details specified by the cs_id.
  
  `includeRelatedPrintings` (bool, optional) - Query parameter to include the other printings of the specified card. 
  
  ```
  {
    "cs_id": 1,
    "url": "/cards/1",
    "name": "Abundance",
    "edition": "10th Edition",
    "is_foil": true,
    "mtgjson_id": "1669af17-d287-5094-b005-4b143441442f",
    "scryfall_id": "46184f97-d5c9-4a98-9fd9-e19057ce9b7e",
    "collector_number": "249",
    "related_printings": [{
      "edition": "10th Edition",
        "name": "Abundance",
        "collector_number": "249",
        "cs_id": 2,
        "is_foil": false,
        "mtgjson_id": "1669af17-d287-5094-b005-4b143441442f",
        "url": "/cards/2",
        "mtgjson_code": "10E",
        "scryfall_id": "46184f97-d5c9-4a98-9fd9-e19057ce9b7e"
    },
    {
        "edition": "Commander 2017",
        "name": "Abundance",
        "collector_number": "145",
        "cs_id": 50776,
        "is_foil": false,
        "mtgjson_id": "7e89befa-00f2-5326-a98d-70c5a54f0bea",
        "url": "/cards/50776",
        "mtgjson_code": "10E",
        "scryfall_id": "7f3fff7e-f34d-4a99-a805-bd66c4e9f0cb"
    },
    ...
    ]
  }
  ```
</details>

<details>
  <summary>GET /cards/mtgjson/{mtgjson_id}</summary>
  
  Returns the Cardsphere card details specified by the MTGJSON Id.
  ```
  {
    "name": "Abundance",
    "mtgjson_id": "1669af17-d287-5094-b005-4b143441442f",
    "url": "/cards/1",
    "collector_number": "249",
    "cs_id": 1,
    "mtgjson_code": "10E",
    "is_foil": true,
    "scryfall_id": "46184f97-d5c9-4a98-9fd9-e19057ce9b7e",
    "edition": "10th Edition"
  }
  ```
</details>

<details>
  <summary>GET /cards/scryfall/{scryfall_id}</summary>
  
  Returns the Cardsphere card details specified by the Scryfall Id.
  ```
  {
    "name": "Abundance",
    "mtgjson_id": "1669af17-d287-5094-b005-4b143441442f",
    "url": "/cards/1",
    "collector_number": "249",
    "cs_id": 1,
    "mtgjson_code": null,
    "is_foil": true,
    "scryfall_id": "46184f97-d5c9-4a98-9fd9-e19057ce9b7e",
    "mtgjson_code": "10E",
    "edition": "10th Edition"
  }
  ```
</details>

<details>
  <summary>GET /cards/search/{string}</summary>
  
  Returns the Cardsphere card details of the card whose name best matches the search string provided.
  ```
 [
    {
        "name": "Abundance",
        "mtgjson_id": "7e89befa-00f2-5326-a98d-70c5a54f0bea",
        "url": "/cards/50776",
        "collector_number": "145",
        "cs_id": 50776,
        "mtgjson_code": "C17",
        "is_foil": false,
        "scryfall_id": "7f3fff7e-f34d-4a99-a805-bd66c4e9f0cb",
        "edition": "Commander 2017"
    },
    {
        "name": "Abundance",
        "mtgjson_id": "d122a279-8bd3-5eb2-8ab9-38974c8fa7f0",
        "url": "/cards/15267",
        "collector_number": "2",
        "cs_id": 15267,
        "mtgjson_code": "DDR",
        "is_foil": false,
        "scryfall_id": "9ab8ad39-840e-474b-beb8-96a7c2a8d0fa",
        "edition": "Duel Decks: Nissa vs. Ob Nixilis"
    },
    ...
  ]
  ```
</details>
