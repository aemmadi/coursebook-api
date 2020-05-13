# coursebook-api

Unofficial API for UT Dallas Coursebook

| Version | Status                   |
| ------- | ------------------------ |
| v1\*    | _under development_      |
| v2      | _planned, check roadmap_ |
| v3      | _planned, check roadmap_ |

> \* => current API version

## API v1 Documentation

**Schema:**

```json
{
  "class_attr": string,
  "class_college": string,
  "class_crosslist": string[],
  "class_desc": string,
  "class_eval": string,
  "class_info": string[],
  "class_instructor": string[],
  "class_reqs": string,
  "class_schedule": string[],
  "class_status": string[],
  "class_syllabus": string,
  "class_ta": string,
  "class_title": string
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
