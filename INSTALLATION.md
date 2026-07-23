# 🚀 MENTORA - COMPLETE INSTALLATION & USAGE GUIDE

## ✅ WHAT HAS BEEN BUILT

Your **Mentora** application is a production-ready, full-stack AI-powered mentorship platform featuring:

✨ **Core Features:**
- Student & Faculty authentication with secure login
- Real-time messaging between students and faculty
- Mentorship connection management
- AI-powered academic assistant (Google Gemini)
- Profile management with picture uploads
- Dashboard with user directory
- Responsive Bootstrap UI
- MongoDB database integration

---

## 🎯 QUICK START (5 MINUTES)

### Step 1: Navigate to Project
```bash
cd c:\Users\DELL\Desktop\mentorship
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Setup Environment File
```bash
# Copy the example file
copy .env.example .env

# Edit .env (use any text editor):
# MONGO_URI=mongodb://localhost:27017/mentorship
# SECRET_KEY=your-secret-key-here
# GOOGLE_API_KEY=your-google-api-key-here
# FLASK_ENV=development
# DEBUG=True
```

### Step 5: Start MongoDB
```bash
# Windows - start MongoDB service or run:
mongod

# If using MongoDB Atlas (cloud), update MONGO_URI in .env
```

### Step 6: Initialize Database
```bash
python setup_db.py
```

Output should show:
```
✓ Connected to MongoDB
✓ Created users collection and indexes
✓ Created messages collection and indexes
✓ Created connections collection and indexes
✓ Created sample faculty members
✓ Created sample students
✓ Created sample connections
✓ Database setup completed successfully!
```

### Step 7: Run Application
```bash
python run.py
```

Visit: **http://localhost:5000**

---

## 🔐 TEST CREDENTIALS

### Faculty Account
```
Email:    dr.smith@university.edu
Password: password123
```

### Student Account
```
Email:    john.doe@student.edu
Password: password123
```

---

## 📋 PROJECT FILES STRUCTURE

```
c:\Users\DELL\Desktop\mentorship\
│
├── 📄 DOCUMENTATION (Start Here!)
│   ├── INDEX.md                    ← Documentation index
│   ├── README.md                   ← Full documentation
│   ├── QUICKSTART.md              ← 5-min setup
│   ├── PROJECT_SUMMARY.md         ← Overview
│   ├── API_DOCUMENTATION.md       ← API endpoints
│   ├── DATABASE_SCHEMA.md         ← Database info
│   ├── DEVELOPMENT.md             ← Dev guidelines
│   └── DOCKER.md                  ← Docker setup
│
├── 🚀 APPLICATION
│   ├── run.py                     ← Start here (python run.py)
│   ├── config.py                  ← Configuration
│   ├── setup_db.py                ← Database setup
│   ├── requirements.txt            ← Python packages
│   ├── .env.example               ← Environment template
│   ├── .gitignore                 ← Git ignore
│   │
│   └── app/                        ← Main application
│       ├── __init__.py
│       ├── models.py               ← Database models
│       │
│       ├── routes/                 ← API routes
│       │   ├── auth.py             ← Login/Register
│       │   ├── dashboard.py        ← Dashboard
│       │   ├── messaging.py        ← Messages
│       │   ├── ai_assistant.py     ← AI features
│       │   └── profile.py          ← User profiles
│       │
│       ├── static/                 ← Frontend assets
│       │   ├── css/
│       │   │   └── style.css
│       │   ├── js/
│       │   │   └── main.js
│       │   └── uploads/            ← User uploads
│       │
│       └── templates/              ← HTML pages
│           ├── base.html
│           ├── index.html
│           ├── auth/
│           │   ├── login.html
│           │   └── register.html
│           ├── dashboard/
│           │   ├── student_dashboard.html
│           │   ├── faculty_dashboard.html
│           │   ├── faculty_profile.html
│           │   └── students_list.html
│           ├── messaging/
│           │   ├── inbox.html
│           │   └── chat.html
│           ├── ai/
│           │   └── assistant.html
│           └── profile/
│               ├── profile.html
│               ├── edit_profile.html
│               └── other_profile.html
│
├── 🐳 DEPLOYMENT
│   ├── Dockerfile                 ← Container definition
│   └── docker-compose.yml         ← Docker orchestration
│
└── 📚 THIS FILE
    └── INSTALLATION.md            ← Complete guide
```

---

## 🎮 FEATURES TOUR

### 1. **Authentication**
- Sign up as Student or Faculty
- Secure password hashing
- Remember me option
- Session management

### 2. **Student Dashboard**
- Browse all faculty members
- View expertise and departments
- Connect with mentors
- See connection count

### 3. **Faculty Dashboard**
- View connected students
- Manage mentorship relationships
- Message students
- Track connections

### 4. **Messaging System**
- Real-time student-faculty communication
- Inbox with conversation history
- Unread message tracking
- Auto-marking as read

### 5. **AI Assistant**
- Ask academic questions
- Get AI-powered answers (Google Gemini)
- Learning resources
- Context-aware responses

### 6. **User Profiles**
- Create detailed profile
- Add bio and expertise (faculty)
- Upload profile picture
- View public profiles

---

## 🔧 CONFIGURATION

### Environment Variables (.env)

```
# MongoDB Connection
MONGO_URI=mongodb://localhost:27017/mentorship

# Flask Security
SECRET_KEY=change-this-to-random-string

# Google AI
GOOGLE_API_KEY=get-from-google-cloud

# Flask Settings
FLASK_ENV=development
DEBUG=True
```

### Getting Google API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Create API key
3. Add to .env: `GOOGLE_API_KEY=your_key_here`

---

## 🗄️ DATABASE

### MongoDB Collections

**Users** - Student & Faculty accounts
```json
{
  "email": "user@example.com",
  "name": "User Name",
  "role": "student|faculty",
  "department": "Computer Science",
  "expertise": ["Python", "AI"],
  "bio": "Bio text",
  "profile_picture": "url"
}
```

**Messages** - Communications
```json
{
  "sender_id": "user_id",
  "receiver_id": "user_id",
  "content": "Message text",
  "read": false,
  "created_at": "timestamp"
}
```

**Connections** - Mentorship links
```json
{
  "student_id": "user_id",
  "faculty_id": "user_id",
  "status": "active",
  "created_at": "timestamp"
}
```

---

## 🌐 USING THE APPLICATION

### For Students

1. **Register**
   - Go to http://localhost:5000/auth/register
   - Choose "Student" role
   - Fill in details

2. **Find Mentors**
   - Go to Dashboard
   - Browse Faculty directory
   - Click "View Profile"

3. **Connect**
   - Click "Request Connection"
   - Mentor will see your connection

4. **Message Mentor**
   - Go to Messages
   - Find mentor in conversations
   - Send message

5. **Get Help**
   - Go to AI Assistant
   - Ask academic question
   - Get instant answer

### For Faculty

1. **Register**
   - Go to http://localhost:5000/auth/register
   - Choose "Faculty" role
   - Add expertise areas

2. **View Students**
   - Go to Dashboard
   - See connected students
   - Browse all students

3. **Communicate**
   - Go to Messages
   - Chat with students
   - Provide guidance

4. **Help with AI**
   - Students use AI Assistant
   - You can also use it
   - Assist in learning

---

## 🚨 TROUBLESHOOTING

### Issue: "Could not connect to MongoDB"

**Solution:**
```bash
# Make sure MongoDB is running
mongod

# Or check your connection string in .env
MONGO_URI=mongodb://localhost:27017/mentorship
```

### Issue: "ModuleNotFoundError"

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "Port 5000 already in use"

**Solution:**
```bash
# Edit run.py and change port, or kill process:
# Windows:
netstat -ano | findstr :5000
taskkill /PID <process_id> /F

# macOS/Linux:
lsof -i :5000 | kill -9 <pid>
```

### Issue: "Google API not working"

**Solution:**
```bash
# Get API key from https://makersuite.google.com/app/apikey
# Add to .env:
GOOGLE_API_KEY=your_key_here

# Application will work without it (fallback messages)
```

---

## 📱 RESPONSIVE DESIGN

The application works on:
- Desktop browsers (Chrome, Firefox, Safari, Edge)
- Tablets (iPad, Android tablets)
- Mobile phones (iPhone, Android)
- Responsive Bootstrap layout

---

## 🐳 DOCKER DEPLOYMENT

### Option 1: Run with Docker Compose
```bash
docker-compose up --build
```

### Option 2: Build Docker Image
```bash
docker build -t mentora:latest .
docker run -p 5000:5000 mentora:latest
```

---

## 📊 API ENDPOINTS

### Authentication
- `POST /auth/register` - Create account
- `POST /auth/login` - Login
- `GET /auth/logout` - Logout

### Dashboard
- `GET /dashboard/` - View dashboard
- `GET /dashboard/faculty/<id>` - View faculty profile
- `POST /dashboard/connect/<id>` - Connect

### Messages
- `GET /messages/` - View inbox
- `GET /messages/chat/<id>` - View conversation
- `POST /messages/send` - Send message

### AI
- `GET /ai/assistant` - AI page
- `POST /ai/ask` - Ask question

### Profile
- `GET /profile/` - View profile
- `POST /profile/edit` - Update profile

---

## ✨ NEXT STEPS

### Customize the Application

1. **Change Branding**
   - Edit `app/templates/base.html` (change logo, colors)
   - Update CSS in `app/static/css/style.css`

2. **Add Features**
   - Create new routes in `app/routes/`
   - Add templates in `app/templates/`
   - Update models in `app/models.py`

3. **Modify Database**
   - Edit collection structure
   - Add new indexes
   - Update validation rules

4. **Deploy to Production**
   - Use Docker
   - Set up MongoDB Atlas
   - Deploy to Heroku or AWS

---

## 📚 DOCUMENTATION FILES

Read in this order:

1. **INDEX.md** - Documentation roadmap
2. **README.md** - Full project info
3. **QUICKSTART.md** - Setup guide
4. **PROJECT_SUMMARY.md** - Feature overview
5. **API_DOCUMENTATION.md** - API reference
6. **DATABASE_SCHEMA.md** - Database design
7. **DEVELOPMENT.md** - Developer guide
8. **DOCKER.md** - Container setup

---

## 🎓 LEARNING RESOURCES

### Technologies Used
- [Flask Documentation](https://flask.palletsprojects.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/)
- [Python Guide](https://docs.python.org/3/)

### AI Integration
- [Google Generative AI](https://ai.google.dev/)
- [Gemini API Docs](https://ai.google.dev/docs)

---

## 🤝 GETTING HELP

1. **Check Documentation**
   - All answers in docs provided

2. **Check Error Messages**
   - Application shows helpful errors

3. **Check Logs**
   - Console shows debug info when `DEBUG=True`

4. **MongoDB Inspection**
   ```bash
   mongosh
   use mentorship
   db.users.find()
   ```

---

## 📈 FUTURE ENHANCEMENTS

Possible additions:
- Video conferencing
- Session scheduling
- Performance analytics
- Mobile app
- Email notifications
- Rating system
- Document sharing
- Payment integration

---

## 🎉 YOU'RE READY!

Your complete Mentora application is now ready to use!

### Quick Checklist:
- ✅ All files created
- ✅ Dependencies listed
- ✅ Database models implemented
- ✅ All routes configured
- ✅ Templates ready
- ✅ Styles applied
- ✅ AI integration setup
- ✅ Documentation complete

### To Start:
```bash
cd c:\Users\DELL\Desktop\mentorship
venv\Scripts\activate
python setup_db.py
python run.py
```

Visit: http://localhost:5000

**Enjoy your Mentora platform! 🚀**

---

## 📞 SUPPORT

- **Documentation:** See INDEX.md
- **Issues:** Check QUICKSTART.md Troubleshooting
- **Development:** See DEVELOPMENT.md
- **Deployment:** See DOCKER.md

---

**Version:** 1.0  
**Status:** Production Ready  
**Last Updated:** January 2024  
**License:** MIT

