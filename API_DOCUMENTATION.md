# Mentora API Documentation

## Base URL

```
http://localhost:5000
```

## Authentication

All protected routes require the user to be logged in via Flask sessions.

---

## Endpoints

### Authentication Routes

#### Register New User

**POST** `/auth/register`

Create a new user account.

**Request Form Data:**
```
- email (string, required): User email
- name (string, required): Full name
- password (string, required): Password (min 6 characters)
- confirm_password (string, required): Password confirmation
- role (string, required): "student" or "faculty"
- department (string, optional): Academic department
- expertise (string, optional): Comma-separated expertise (for faculty)
```

**Response:**
- Redirect to login page on success
- Flash message with status

**Example:**
```bash
curl -X POST http://localhost:5000/auth/register \
  -d "email=student@example.com&name=John Doe&password=password123&confirm_password=password123&role=student&department=CS"
```

---

#### Login

**POST** `/auth/login`

Authenticate user and create session.

**Request Form Data:**
```
- email (string, required): User email
- password (string, required): User password
- remember (checkbox, optional): Remember me option
```

**Response:**
- Redirect to dashboard on success
- Flash message with status

**Example:**
```bash
curl -X POST http://localhost:5000/auth/login \
  -d "email=student@example.com&password=password123"
```

---

#### Logout

**GET** `/auth/logout`

End user session and logout.

**Authentication:** Required

**Response:**
- Redirect to login page
- Flash message confirming logout

---

### Dashboard Routes

#### Get Dashboard

**GET** `/dashboard/`

Get user's dashboard based on role.

**Authentication:** Required

**Response:**
- For students: Faculty list and connection count
- For faculty: Student list and connection count

---

#### View Faculty Profile

**GET** `/dashboard/faculty/<faculty_id>`

View faculty member's profile.

**Authentication:** Required

**Parameters:**
- `faculty_id` (string): Faculty member's ObjectId

**Response:**
- Faculty profile page with connection status

---

#### Connect with Faculty

**POST** `/dashboard/connect/<user_id>`

Create mentorship connection as a student.

**Authentication:** Required (Student only)

**Parameters:**
- `user_id` (string): Faculty member's ObjectId

**Response:**
- Flash message with connection status
- Redirect to faculty profile

---

#### View All Students

**GET** `/dashboard/students`

List all students (Faculty only).

**Authentication:** Required (Faculty only)

**Response:**
- List of all students with contact information

---

### Messaging Routes

#### Get Inbox

**GET** `/messages/`

Get all conversations for the logged-in user.

**Authentication:** Required

**Response:**
- List of conversations with last message and unread count

---

#### View Chat

**GET** `/messages/chat/<user_id>`

View conversation history with a specific user.

**Authentication:** Required

**Parameters:**
- `user_id` (string): Other user's ObjectId

**Response:**
- Chat interface with message history
- Automatically marks messages as read

---

#### Send Message

**POST** `/messages/send`

Send a message to another user.

**Authentication:** Required

**Request JSON:**
```json
{
  "receiver_id": "user_object_id",
  "content": "Message content"
}
```

**Response:**
```json
{
  "success": true,
  "message_id": "message_object_id",
  "timestamp": "2024-01-15T10:30:00.000000"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/messages/send \
  -H "Content-Type: application/json" \
  -d '{"receiver_id":"507f1f77bcf86cd799439011","content":"Hello!"}'
```

---

#### Get Unread Count

**GET** `/messages/get_unread_count`

Get number of unread messages for the current user.

**Authentication:** Required

**Response:**
```json
{
  "unread_count": 5
}
```

---

### AI Assistant Routes

#### Open AI Assistant

**GET** `/ai/assistant`

Open AI assistant interface.

**Authentication:** Required

**Response:**
- AI assistant page

---

#### Ask Question

**POST** `/ai/ask`

Submit a question to the AI assistant.

**Authentication:** Required

**Request JSON:**
```json
{
  "question": "What is machine learning?"
}
```

**Response:**
```json
{
  "success": true,
  "answer": "AI-generated answer to the question",
  "sources": []
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/ai/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"How do I solve this math problem?"}'
```

---

#### View Learning Resources

**GET** `/ai/resources`

View curated learning resources by subject.

**Authentication:** Required

**Response:**
- Learning resources page organized by subject

---

### Profile Routes

#### View Own Profile

**GET** `/profile/`

View current user's profile.

**Authentication:** Required

**Response:**
- User profile page

---

#### Edit Profile

**GET** `/profile/edit`

Get profile edit page.

**Authentication:** Required

**Response:**
- Profile edit form

---

#### Update Profile

**POST** `/profile/edit`

Update user profile information.

**Authentication:** Required

**Request Form Data:**
```
- name (string, required): Full name
- bio (string, optional): User biography
- expertise (string, optional): Comma-separated expertise (faculty only)
- profile_picture (file, optional): Profile image
```

**Response:**
- Flash message with status
- Redirect to profile page

---

#### View Other User Profile

**GET** `/profile/<user_id>`

View another user's public profile.

**Authentication:** Required

**Parameters:**
- `user_id` (string): User's ObjectId

**Response:**
- User profile page (read-only)

---

## Error Responses

### 400 Bad Request
```json
{
  "success": false,
  "error": "Description of what went wrong"
}
```

### 403 Forbidden
User lacks permission for the requested resource.

### 404 Not Found
Resource not found.

### 500 Internal Server Error
```json
{
  "success": false,
  "error": "Error message"
}
```

---

## Rate Limiting

Currently no rate limiting implemented. Recommended for production:
- 100 requests per minute per IP
- 1000 requests per hour per user

---

## Pagination

Implemented in future versions. Current response patterns:
- Messages: Limited to 50 per query
- Users: Limited to 10 per query

---

## Data Types

- **ObjectId**: MongoDB object ID (24-character hex string or ObjectId)
- **ISODate**: ISO 8601 date format (YYYY-MM-DDTHH:mm:ss.sssZ)
- **Boolean**: true or false
- **Array**: JSON array of items

---

## Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Server Error |

---

## Example Usage Workflow

```bash
# 1. Register as student
curl -X POST http://localhost:5000/auth/register \
  -d "email=john@example.com&name=John&password=pass123&confirm_password=pass123&role=student&department=CS"

# 2. Login
curl -X POST http://localhost:5000/auth/login \
  -d "email=john@example.com&password=pass123" \
  -c cookies.txt

# 3. Get dashboard (redirected from / )
curl http://localhost:5000/dashboard/ -b cookies.txt

# 4. Send message to faculty
curl -X POST http://localhost:5000/messages/send \
  -H "Content-Type: application/json" \
  -d '{"receiver_id":"faculty_id","content":"Hello professor"}' \
  -b cookies.txt

# 5. Ask AI question
curl -X POST http://localhost:5000/ai/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"What is recursion?"}' \
  -b cookies.txt

# 6. Logout
curl http://localhost:5000/auth/logout -b cookies.txt
```

---

## CORS

CORS not currently enabled. For cross-origin requests in production, add:

```python
from flask_cors import CORS
CORS(app)
```

---

## Versioning

Current API Version: 1.0

Future versions will include:
- API v2 with RESTful improvements
- Webhook support
- Advanced filtering and search
- WebSocket for real-time updates

