# yourBook API Project Plan

## 1. Overview

A backend API for managing books, users, sharing, and pages. Built with Flask and MongoDB, with Cloudinary for storage.

## 2. Entities & Models

### User

- model_id
- name
- identities
- avatarUrl
- banner_id
- user_type
- updated_by

### Book

- model_id
- title
- description
- contains_id (pages)
- createdAt
- updatedAt
- share_id
- updated_by

### Page

- model_id
- book_id
- title
- description
- createdAt
- updatedAt
- contains (content)
- updated_by

### Share

- \_id (share_id)
- created_by (user_id)
- share_id (users)
- shared_to (users)
- permissions
- book_id
- permission_start_date
- permission_end_date

## 3. API Endpoints

- `/users` (CRUD, list, details)
- `/books` (CRUD, list, details)
- `/books/:book_id/pages` (CRUD pages for a book)
- `/books/:book_id/share` (share book with users, set permissions, expiry)
- `/shares` (list, details, revoke)
- `/pages/:page_id` (details, update, delete)
- `/user/config` (create user config)

## 4. Backend Structure

- Modules: users, books, pages, sharing, utils (cloudinary, etc.)
- Models: User, Book, Page, Share
- Controllers: REST endpoints for each module
- Services: Business logic for each module

## 5. Database

- MongoDB Atlas (collections: users, books, pages, shares)
- Relations: Book has many Pages, Share links Book/User/Permissions

## 6. Storage

- Cloudinary integration for book/page images/files

## 7. Auth & Permissions

- User authentication (JWT)
- Share permissions (read, write, expiry)

## 8. Other

- Timestamps: createdAt, updatedAt
- Audit: updatedBy, sharedTo

## 9. Tech Stack

- Flask (Python)
- MongoDB Atlas
- Cloudinary
- JWT for auth

## 10. Workflow

1. Scaffold Flask modules for users, books, pages, sharing.
2. Define MongoDB schemas for each entity.
3. Implement controllers/services for CRUD and sharing logic.
4. Integrate MongoDB Atlas (connection config).
5. Add Cloudinary service for file uploads.
6. Implement JWT auth for users.
7. Document API endpoints (Swagger/OpenAPI).
8. Write minimal tests for each module.

## 11. Example MongoDB Document (Book)

```json
{
  "_id": "...",
  "title": "Book Title",
  "description": "...",
  "pages": ["..."],
  "createdBy": "user_id",
  "createdAt": "2025-08-20T12:00:00Z",
  "updatedAt": "2025-08-20T12:00:00Z",
  "updatedBy": "user_id"
}
```

## 12. Example Share Document

```json
{
  "_id": "...",
  "book": "book_id",
  "sharedTo": ["user_id1", "user_id2"],
  "permissions": ["read", "write"],
  "permissionEndDate": "2025-09-01T00:00:00Z"
}
```

## 13. Example User Config Endpoint

- POST `/user/config` with `{ "name": "alice", "pass": "secret" }` creates a config document in MongoDB.

---

_For diagrams, see attached blueprint image. This PDF summarizes the project plan for development and onboarding._
