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

### Class Details For All Sections

`GET /v1/<course>` : Returns an array of objects with class details for every section in **current semester**

**Formatting:**

- `<course>` :
  - Course number
  - Formatting: `<subject code><number>`
  - Examples: `cs4337`, `math2414`, `hist1301`

## Contributing

Feel free to fork the repository and pull request it.

Branch naming convention:
- `feature/<name-of-feat>`: Feature branch, new features, usually labelled as **Enhancements** in issues. _Example: `feature/professor-data`_
- `bug/<name-of-bug>`: Bug branch, bug fixes, usually labelled as **Bug** in issues. _Example: `bug/heading-format`_
- `internal/<name>`: Internal branch, internal improvements, misc. items go under this branch, labelled accordingly as **Internal** in issues. _Example: `internal/refactor`_
- `update/<name-of-feat>`: Update branch, update existing features, not neccessarily a bug fix. _Example: `update/data-storage`_ 

Make sure to `comment your code` so that it would be easy to review it. Work on any issue you are interested in fixing, or just want to tidy up my inefficient code :)
