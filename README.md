## Mentora - AI-Powered Student-Faculty Mentorship Platform

A full-stack web application that connects students with faculty mentors while providing AI-powered academic assistance.

### Features

✨ **Student-Faculty Mentorship**
- Browse and connect with faculty members
- View faculty profiles with expertise and departments
- Maintain mentorship relationships

💬 **Real-Time Messaging**
- Direct messaging between students and faculty
- Message history and conversation management
- Unread message tracking

🤖 **AI Academic Assistant**
- Powered by Google Gemini API
- Instant answers to academic questions
- Context-aware responses for better learning
- Learning resources repository

👥 **Role-Based Access Control**
- Secure user authentication
- Student and Faculty roles with distinct features
- Profile management and customization

🔐 **Security**
- Password hashing with Werkzeug
- Session management with Flask-Login
- MongoDB for secure data storage
- CSRF protection

### Technology Stack

**Backend:**
- Flask 3.0.0
- Flask-PyMongo 2.3.0
- Flask-Login 0.6.3
- Python 3.8+

**Frontend:**
- Bootstrap 5.3.0
- HTML5, CSS3, JavaScript
- Font Awesome Icons

**Database:**
- MongoDB
- PyMongo 4.6.0

**AI Integration:**
- Google Generative AI (Gemini)

### Project Structure

```
mentorship/
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── models.py             # Database models (User, Message, Connection)
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication routes
│   │   ├── dashboard.py     # Dashboard routes
│   │   ├── messaging.py     # Messaging routes
│   │   ├── ai_assistant.py  # AI assistant routes
│   │   └── profile.py       # User profile routes
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css    # Global styles
│   │   └── js/
│   │       └── main.js      # JavaScript functionality
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── auth/
│       │   ├── login.html
│       │   └── register.html
│       ├── dashboard/
│       │   ├── student_dashboard.html
│       │   ├── faculty_dashboard.html
│       │   ├── faculty_profile.html
│       │   └── students_list.html
│       ├── messaging/
│       │   ├── inbox.html
│       │   └── chat.html
│       ├── ai/
│       │   └── assistant.html
│       └── profile/
│           ├── profile.html
│           ├── edit_profile.html
│           └── other_profile.html
├── config.py                # Configuration management
├── run.py                   # Application entry point
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

### Installation & Setup

1. **Clone the repository:**
```bash
cd mentorship
```

2. **Create a virtual environment:**
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
```bash
# Copy .env.example to .env
cp .env.example .env

# Edit .env with your settings:
MONGO_URI=mongodb://localhost:27017/mentorship
SECRET_KEY=your-secret-key-here
GOOGLE_API_KEY=your-google-api-key-here
FLASK_ENV=development
```

5. **Set up MongoDB:**
```bash
# Make sure MongoDB is running locally or update MONGO_URI to your MongoDB server
mongod
```

6. **Run the application:**
```bash
python run.py
```

7. **Access the application:**
Open your browser and go to `http://localhost:5000`

### Usage

**For Students:**
1. Register as a Student
2. Browse available Faculty members
3. Connect with faculty mentors
4. Message your mentors
5. Use AI Assistant for academic help

**For Faculty:**
1. Register as Faculty with your expertise
2. View connected students
3. Respond to student messages
4. Help guide student learning

### API Endpoints

**Authentication:**
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `GET /auth/logout` - Logout user

**Dashboard:**
- `GET /dashboard/` - View dashboard
- `GET /dashboard/faculty/<faculty_id>` - View faculty profile
- `POST /dashboard/connect/<user_id>` - Connect with faculty
- `GET /dashboard/students` - View all students (faculty)

**Messaging:**
- `GET /messages/` - View inbox
- `GET /messages/chat/<user_id>` - View chat with user
- `POST /messages/send` - Send message
- `GET /messages/get_unread_count` - Get unread count

**AI Assistant:**
- `GET /ai/assistant` - AI assistant page
- `POST /ai/ask` - Ask AI question
- `GET /ai/resources` - View learning resources

**Profile:**
- `GET /profile/` - View own profile
- `GET /profile/edit` - Edit profile page
- `POST /profile/edit` - Update profile
- `GET /profile/<user_id>` - View user profile

### Database Schema

**Users Collection:**
```json
{
  "_id": ObjectId,
  "email": "user@example.com",
  "name": "User Name",
  "password_hash": "hashed_password",
  "role": "student|faculty",
  "department": "Computer Science",
  "expertise": ["Python", "AI"],
  "bio": "User biography",
  "profile_picture": "url",
  "created_at": ISODate,
  "updated_at": ISODate,
  "is_active": true
}
```

**Messages Collection:**
```json
{
  "_id": ObjectId,
  "sender_id": ObjectId,
  "receiver_id": ObjectId,
  "content": "message content",
  "created_at": ISODate,
  "read": false
}
```

**Connections Collection:**
```json
{
  "_id": ObjectId,
  "student_id": ObjectId,
  "faculty_id": ObjectId,
  "created_at": ISODate,
  "status": "active"
}
```

### Future Enhancements

- [ ] Real-time notifications with WebSockets
- [ ] Video calling integration
- [ ] Session scheduling and calendar
- [ ] Performance analytics and reports
- [ ] Mobile app (React Native)
- [ ] Advanced search and filtering
- [ ] Ratings and reviews system
- [ ] Document sharing and collaboration
- [ ] Email notifications
- [ ] Two-factor authentication

### Security Best Practices

- Password hashing using Werkzeug
- Session management with Flask-Login
- CSRF protection (Flask-WTF)
- Secure MongoDB indexes
- Environment variables for sensitive data
- Role-based access control

### Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### License

This project is licensed under the MIT License.

### Support

For support, email support@mentora.com or open an issue on GitHub.

---

**Made with ❤️ by the Mentora Team**
