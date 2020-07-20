# coursebook-api

Unofficial API for UT Dallas Coursebook

This was a fun sophomore summer project. I will maintain this API till 2022/2023. Just open an issue if you have any suggestions or something is breaking the API. UTD coursebook sometimes makes some subtle changes that break the API, I have tried my best to account for those in my API but it might not be perfect.

[Prettier API Docs](https://documentup.com/aemmadi/coursebook-api/__recompile)

## v1 Routes

### Specific Class Details

`GET /v1/:term/:course/:section` : Returns a single object for requested class.

<details>

<summary> Click to expand </summary>

**Parameters:**

- `term` :
  - Semester term
  - Formatting: `<two-digit year><single letter semester>`
  - Examples: `20f`, `18s`
- `course` :
  - Course number with subject code
  - Formatting: `<subject code><number>`
  - Examples: `cs4337`, `math2414`, `hist1301`
- `section` :
  - Section number
  - Formatting: `<three-digit section number>`
  - Examples: `001`, `0w1`, `HON`

**Response**:

```json
{
  "data": {
    "class_attributes": string[],
    "class_info": {
      "add_consent": string,
      "class_level": string,
      "class_section": string,
      "course_number": string,
      "date/time": string,
      "grading": string,
      "mode": string,
      "semester_credit_hours": string,
      "type": string
  },
  "college": string,
  "course_title": string,
  "description": string,
  "enrollment_reqs": string,
  "evaluation": string,
  "instructor": string[],
  "schedule": {
      "ends": string,
      "misc": string[],
      "starts": string,
      "term": string,
      "type": string
  },
  "status": {
      "available_seats": string,
      "enrolled_total": string,
      "enrollment_status": string,
      "waitlist": string
  },
  "syllabus": string,
  "ta/ra": string
  }
}
```

</details>


### Class Details For All Sections (Broken for now)

`GET /v1/<course>` : Returns an array of objects with class details for every section in **current semester**

<details>

<summary> Click to expand </summary>

**Parameters:**

- `course` :
  - Course number with subject code
  - Formatting: `<subject code><number>`
  - Examples: `cs4337`, `math2414`, `hist1301`

</details>

### Grades Data

> Source: [UTDGrades](https://utdgrades.com/)

`GET /v1/grades/:term/:course` : Returns an array of objects for all sections in the course with appropriate grades

<details>

<summary> Click to expand </summary>

**Parameters:**

- `term`:
  - Semester term
  - Formatting: `<two-digit year><single letter semester>`
  - Examples: `20f`, `18s`
- `course` :
  - Course number with subject code
  - Formatting: `<subject code><number>`
  - Examples: `cs4337`, `math2414`, `hist1301`

**Response:**

```json
{
  "data": [
    {
      "grades": {
          "A": int,
          "A+": int,
          "A-": int,
          "B": int,
          "B+": int,
          "B-": int,
          "C": int,
          "C+": int,
          "C-": int,
          "D": int,
          "F": int,
          "W": int
      },
      "num": string,
      "prof": string,
      "sect": string,
      "subj": string,
      "term": string
    },
    { ... },
    { ... }
  ]
}
```

</details>

`GET /v1/grades/:term/:course/:section`: Returns a single object with grade data for the given course and section

<details>

<summary> Click to expand </summary>

**Parameters:**

- `term`:
  - Semester term
  - Formatting: `<two-digit year><single letter semester>`
  - Examples: `20f`, `18s`
- `course` :
  - Course number with subject code
  - Formatting: `<subject code><number>`
  - Examples: `cs4337`, `math2414`, `hist1301`
- `section` :
  - Section number
  - Formatting: `<three-digit section number>`
  - Examples: `001`, `0w1`, `HON`

**Response:**

```json
{
  "data": {
    "grades": {
        "A": int,
        "A+": int,
        "A-": int,
        "B": int,
        "B+": int,
        "B-": int,
        "C": int,
        "C+": int,
        "C-": int,
        "D": int,
        "F": int,
        "W": int
    },
    "num": string,
    "prof": string,
    "sect": string,
    "subj": string,
    "term": string
  }
}
```

</details>

### Professor Data

> Source: [UTD Directory](https://www.utdallas.edu/directory/)

`GET /v1/prof/:name`: Returns an array of objects for all professors matched with the given `:name`

<details>

<summary> Click to expand </summary>

**Parameters**:

- `name`:
  - String to search directory with
  - When providing full name encode spaces with `%20`
  - Examples: `John`, `Mazidi`, `john%20cole`

**Response**:

```json
{
  "data": [
    {
        "department": string,
        "email": string,
        "mailstop": string,
        "name": string,
        "office": string,
        "phone": string,
        "title": string
    },
    { ... }
  ]
}
```

</details>

## Contributing

Feel free to fork the repository and pull request it.

Branch naming convention:

- `feature/<name-of-feat>`: Feature branch, new features, usually labelled as **Enhancements** in issues. _Example: `feature/professor-data`_
- `bug/<name-of-bug>`: Bug branch, bug fixes, usually labelled as **Bug** in issues. _Example: `bug/heading-format`_
- `internal/<name>`: Internal branch, internal improvements, misc. items go under this branch, labelled accordingly as **Internal** in issues. _Example: `internal/refactor`_
- `update/<name-of-feat>`: Update branch, update existing features, not neccessarily a bug fix. _Example: `update/data-storage`_

Make sure to `comment your code` so that it would be easy to review it. Work on any issue you are interested in fixing, or just want to tidy up my inefficient code :)
