# coursebook-api

Unofficial API for UT Dallas Coursebook

| Version | Status                   |
| ------- | ------------------------ |
| v1\*    | _under development_      |
| v2      | _planned, check roadmap_ |
| v3      | _planned, check roadmap_ |

> \* => current API version

## API v1 Documentation

The API dynamically scrapes content from coursebook, allowing for it to account towards additional data fields/ommitted data fields returned by coursebook. However, this also means that the schema may not always be the same. I have provided the general schema, but depending on the class the schema might have extra or lesser key value pairs.

**General Schema:**

```json
  {
    "data": {
        "class_attributes": string/string[],
        "class_info": string[],
        "class_notes": string,
        "college": string,
        "core": string,
        "course_title": string,
        "cross_listed_with": string[],
        "description": string,
        "enrollment_reqs": string,
        "evaluation": string,
        "instructor": string[],
        "schedule": string[],
        "status": string[],
        "syllabus": string,
        "ta/ra": string
    }
}
```

## Routes

### Specific Class Details

`GET /v1/<term>/<course>/<section>` : Returns a single object for requested class.

**Formatting:**

- `<term>` :
  - Semester term
  - Formatting: `<two-digit year><single letter semester>`
  - Examples: `20f`, `18s`
- `<course>` :
  - Course number
  - Formatting: `<subject code><number>`
  - Examples: `cs4337`, `math2414`, `hist1301`
- `<section>` :
  - Section number
  - Formatting: `<three-digit section number>`
  - Examples: `001`, `0w1`, `HON`

## Contributing

Feel free to fork the repository and pull request it.

All I ask of you is to `comment your code` so that it would be easy to review it. Work on any issue you are interested in fixing, or just want to tidy up my inefficient code :)
