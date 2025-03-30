# Ryan Portfolio Backend API Documentation

This document provides comprehensive information on all available API endpoints, expected request fields, and returned data structures.

## Base URL

All endpoints are relative to: `http://localhost:3003`

## API Endpoints

### Main

| Method | Endpoint | Description                |
| ------ | -------- | -------------------------- |
| GET    | /        | Health check/root endpoint |

### Blog Posts

| Method | Endpoint    | Description             |
| ------ | ----------- | ----------------------- |
| GET    | /blog       | Retrieve all blog posts |
| GET    | /blog/:slug | Get blog post by slug   |
| POST   | /blog       | Create a new blog post  |
| PATCH  | /blog/:id   | Update an existing post |
| DELETE | /blog/:id   | Delete a blog post      |

**Blog Post Fields:**

```json
{
  "slug": "post-slug",
  "title": "Post Title",
  "date": "YYYY-MM-DD",
  "excerpt": "Brief summary of the post",
  "coverImage": "/image-path.jpg",
  "readingTime": "X min read",
  "tags": ["Tag1", "Tag2"],
  "content": "Full markdown content",
  "relatedPosts": [
    {
      "slug": "related-post-slug",
      "title": "Related Post Title",
      "coverImage": "/related-image.jpg"
    }
  ]
}
```

### Work Experience

| Method | Endpoint             | Description                   |
| ------ | -------------------- | ----------------------------- |
| GET    | /experience/work     | Retrieve all work experiences |
| GET    | /experience/work/:id | Get work experience by ID     |
| POST   | /experience/work     | Create a new work experience  |
| PATCH  | /experience/work/:id | Update an existing experience |
| DELETE | /experience/work/:id | Delete a work experience      |

**Work Experience Fields:**

```json
{
  "title": "Job Title",
  "company": "Company Name",
  "location": "City, State, Country",
  "startDate": "Month YYYY",
  "endDate": "Month YYYY or Present",
  "description": [
    "Responsibility/achievement 1",
    "Responsibility/achievement 2"
  ]
}
```

### Achievements

| Method | Endpoint                     | Description                    |
| ------ | ---------------------------- | ------------------------------ |
| GET    | /experience/achievements     | Retrieve all achievements      |
| GET    | /experience/achievements/:id | Get achievement by ID          |
| POST   | /experience/achievements     | Create a new achievement       |
| PATCH  | /experience/achievements/:id | Update an existing achievement |
| DELETE | /experience/achievements/:id | Delete an achievement          |

**Achievement Fields:**

```json
{
  "title": "Achievement Title",
  "organization": "Organization Name",
  "date": "Month YYYY",
  "description": "Detailed description of the achievement"
}
```

### Education

| Method | Endpoint                  | Description                  |
| ------ | ------------------------- | ---------------------------- |
| GET    | /experience/education     | Retrieve all education items |
| GET    | /experience/education/:id | Get education by ID          |
| POST   | /experience/education     | Create a new education item  |
| PATCH  | /experience/education/:id | Update an education item     |
| DELETE | /experience/education/:id | Delete an education item     |

**Education Fields:**

```json
{
  "degree": "Degree Name",
  "institution": "Institution Name",
  "startYear": "YYYY",
  "endYear": "YYYY"
}
```

### Skills

| Method | Endpoint    | Description                   |
| ------ | ----------- | ----------------------------- |
| GET    | /skills     | Retrieve all skill categories |
| GET    | /skills/:id | Get skill category by ID      |
| POST   | /skills     | Create a new skill category   |
| PATCH  | /skills/:id | Update a skill category       |
| DELETE | /skills/:id | Delete a skill category       |

**Skill Category Fields:**

```json
{
  "name": "Category Name",
  "skills": ["Skill 1", "Skill 2"]
}
```

### Projects

| Method | Endpoint           | Description                |
| ------ | ------------------ | -------------------------- |
| GET    | /projects          | Retrieve all projects      |
| GET    | /projects/featured | Get only featured projects |
| GET    | /projects/:slug    | Get project by slug        |
| POST   | /projects          | Create a new project       |
| PATCH  | /projects/:id      | Update an existing project |
| DELETE | /projects/:id      | Delete a project           |

**Project Fields:**

```json
{
  "title": "Project Title",
  "description": "Brief project description",
  "fullDescription": "Detailed project description",
  "image": "/project-image.jpg",
  "tags": ["Tag1", "Tag2"],
  "slug": "project-slug",
  "demoUrl": "https://demo-url.com",
  "githubUrl": "https://github.com/example/project",
  "features": [
    "Feature 1",
    "Feature 2"
  ],
  "featured": true|false
}
```

## Error Responses

All endpoints return standard HTTP status codes:

- `200 OK`: Request successful
- `201 Created`: Resource successfully created
- `400 Bad Request`: Invalid input/parameters
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

Error response format:

```json
{
  "statusCode": 400,
  "message": ["Error message details"],
  "error": "Error Type"
}
```

## Database Initialization

To populate the database with initial demo data:

```bash
python post_initial_data.py
```

This script will clear all existing data and insert predefined content for all collections.

## Authentication

This API currently does not implement authentication. All endpoints are publicly accessible.

## Rate Limiting

No rate limiting is currently implemented.
