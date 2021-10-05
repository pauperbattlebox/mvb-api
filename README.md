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
  <summary>GET /sets/{cardsphere_id}</summary>
    
  Returns the specified Cardsphere set and a list of the cards in the set.
  
  ```
  {
    "cs_id": 755,
    "cs_name": "10th Edition",
    "mtgjson_code": "10E",
    "cards": [{
      "cs_id": 1,
      "url": "",
      "name": "Abundance",
      "edition": "10th Edition",
      "is_foil": true,
      "mtgjson_id": "",
      "scryfall_id": "",
      "collector_number": ""
    },
    ...
    ]
  }
  ```
</details>