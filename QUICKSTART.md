# Quick Start Guide for Mentora

## Prerequisites

- Python 3.8+
- MongoDB (local or cloud instance)
- Google API Key for AI features (optional but recommended)

## Installation Steps

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env` and update with your settings:

```bash
cp .env.example .env
```

Edit `.env`:
```
MONGO_URI=mongodb://localhost:27017/mentorship
SECRET_KEY=change-this-to-a-random-secret-key
GOOGLE_API_KEY=your-google-api-key-here
FLASK_ENV=development
DEBUG=True
```

### 3. Setup MongoDB

Make sure MongoDB is running:

**On Windows:**
```bash
mongod
```

**Using MongoDB Atlas (Cloud):**
Update `MONGO_URI` in `.env` with your MongoDB Atlas connection string.

### 4. Initialize Database

Run the setup script to create collections and sample data:

```bash
python setup_db.py
```

This will create:
- Database collections and indexes
- Sample faculty members
- Sample students
- Sample mentorship connections

### 5. Run the Application

```bash
python run.py
```

The application will start on `http://localhost:5000`

## Sample Login Credentials

**Faculty Account:**
- Email: dr.smith@university.edu
- Password: password123

**Student Account:**
- Email: john.doe@student.edu
- Password: password123

## Features Overview

### Student Features
- Browse faculty members by department and expertise
- Connect with faculty for mentorship
- Send messages to mentors
- Use AI Assistant for academic help
- View and edit profile

### Faculty Features
- View connected students
- Send and receive messages
- Manage mentorship relationships
- Update expertise and profile information
- Help students with academic questions

### AI Assistant
- Ask academic questions
- Get instant AI-powered responses
- Access learning resources

## API Usage Examples

### Create a Student Account
```bash
curl -X POST http://localhost:5000/auth/register \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "email=student@example.com&name=Student Name&password=password123&confirm_password=password123&role=student&department=Computer Science"
```

### Login
```bash
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "email=student@example.com&password=password123"
```

### Send a Message
```bash
curl -X POST http://localhost:5000/messages/send \
  -H "Content-Type: application/json" \
  -d '{"receiver_id":"faculty_user_id","content":"Hello, I need help with..."}'
```

## Project Structure

```
mentorship/
├── app/                      # Application package
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── routes/              # API routes
│   ├── static/              # Frontend assets (CSS, JS)
│   └── templates/           # HTML templates
├── config.py                # Configuration
├── run.py                   # Entry point
├── setup_db.py              # Database initialization
├── requirements.txt         # Python dependencies
├── .env.example            # Environment template
└── README.md               # Full documentation
```

## Troubleshooting

### MongoDB Connection Error
- Ensure MongoDB is running
- Check `MONGO_URI` in `.env` is correct
- For MongoDB Atlas, whitelist your IP address

### Google API Error (AI Assistant)
- Set `GOOGLE_API_KEY` in `.env` to use AI features
- Get API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Port 5000 Already in Use
```bash
# Change port in run.py or use:
python run.py --port 5001
```

### Module Import Errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

## Development Tips

### Enable Debug Mode
Set in `.env`:
```
DEBUG=True
FLASK_ENV=development
```

### Database Inspection
```bash
# Connect to MongoDB shell
mongosh

# Use mentorship database
use mentorship

# View collections
show collections

# Query users
db.users.find()
```

### Clear Sample Data
```bash
# Connect to MongoDB shell
mongosh
use mentorship

# Drop all collections
db.users.deleteMany({})
db.messages.deleteMany({})
db.connections.deleteMany({})
```

## Deployment

### Deploy to Heroku

1. Create `Procfile`:
```
web: gunicorn run:app
```

2. Add Gunicorn to requirements.txt:
```bash
pip install gunicorn
pip freeze > requirements.txt
```

3. Deploy:
```bash
heroku create mentora-app
git push heroku main
```

### Environment Variables on Heroku
```bash
heroku config:set MONGO_URI=your_mongodb_uri
heroku config:set SECRET_KEY=your_secret_key
heroku config:set GOOGLE_API_KEY=your_api_key
```

## Next Steps

1. Customize the application branding
2. Add more fields to user profiles
3. Implement video conferencing for meetings
4. Add document sharing features
5. Create a mobile app with React Native
6. Set up email notifications
7. Add two-factor authentication

## Support

For issues or questions:
1. Check the [README.md](README.md)
2. Review error messages in the console
3. Check MongoDB logs
4. Open an issue on GitHub

---

**Happy learning with Mentora!** 🚀
