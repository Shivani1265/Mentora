# Mentora - Development Guide

## Local Development Setup

### 1. Environment Setup

```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure `.env` File

```bash
cp .env.example .env
```

Edit `.env`:
```
MONGO_URI=mongodb://localhost:27017/mentorship
SECRET_KEY=dev-secret-key-change-in-production
GOOGLE_API_KEY=your-google-api-key-here
FLASK_ENV=development
DEBUG=True
```

### 3. MongoDB Setup

**Option A: Local MongoDB**
```bash
# Windows
mongod

# macOS (with Homebrew)
brew services start mongodb-community

# Linux
sudo systemctl start mongod
```

**Option B: MongoDB Atlas (Cloud)**
1. Create account at mongodb.com
2. Create cluster
3. Get connection string
4. Update MONGO_URI in .env

### 4. Initialize Database

```bash
python setup_db.py
```

This creates:
- Database collections
- Indexes
- Sample data

### 5. Run Application

```bash
python run.py
```

Access at: http://localhost:5000

---

## Development Workflow

### File Organization

```
app/
├── models.py          # Database models
├── routes/            # API endpoints
│   ├── auth.py
│   ├── dashboard.py
│   ├── messaging.py
│   ├── ai_assistant.py
│   └── profile.py
├── templates/         # HTML templates
└── static/            # CSS, JS, images
```

### Adding New Features

#### 1. Create a New Route

Create `app/routes/feature.py`:
```python
from flask import Blueprint
from flask_login import login_required

bp = Blueprint('feature', __name__, url_prefix='/feature')

@bp.route('/')
@login_required
def index():
    return render_template('feature/index.html')
```

#### 2. Register Blueprint

In `app/__init__.py`:
```python
from app.routes import feature
app.register_blueprint(feature.bp)
```

#### 3. Create Template

Create `app/templates/feature/index.html`:
```html
{% extends "base.html" %}
{% block content %}
<!-- Your content here -->
{% endblock %}
```

### Adding New Database Models

In `app/models.py`:
```python
class Feature:
    @staticmethod
    def create(data):
        result = mongo.db.features.insert_one(data)
        return str(result.inserted_id)
    
    @staticmethod
    def get_by_id(feature_id):
        return mongo.db.features.find_one({'_id': ObjectId(feature_id)})
```

---

## Testing

### Manual Testing

1. **Authentication**
   - Register new user
   - Login/logout
   - Session management

2. **Dashboard**
   - Browse faculty/students
   - View profiles
   - Connect with mentors

3. **Messaging**
   - Send messages
   - View conversations
   - Check unread count

4. **AI Assistant**
   - Ask questions
   - Get responses
   - View resources

5. **Profile**
   - Edit profile
   - Upload picture
   - Update expertise

### Automated Testing

Create `tests/test_auth.py`:
```python
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        yield client

def test_register(client):
    response = client.post('/auth/register', data={
        'email': 'test@example.com',
        'name': 'Test User',
        'password': 'password123',
        'confirm_password': 'password123',
        'role': 'student',
        'department': 'CS'
    })
    assert response.status_code == 302
```

Run tests:
```bash
pytest
```

---

## Debugging

### Enable Debug Mode

In `.env`:
```
DEBUG=True
FLASK_ENV=development
```

### Use Flask Shell

```bash
flask shell
```

```python
>>> from app.models import User
>>> user = User.get_by_email('test@example.com')
>>> print(user.name)
```

### Database Inspection

```bash
# Connect to MongoDB
mongosh

# Use database
use mentorship

# View collections
show collections

# Query data
db.users.find()
db.messages.find()
db.connections.find()
```

### Application Logs

```bash
# View logs
tail -f app.log

# Or in Python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## Performance Optimization

### Database Optimization

1. **Create Indexes**
   ```python
   db.users.create_index('email', unique=True)
   db.messages.create_index([('sender_id', 1), ('receiver_id', 1)])
   db.connections.create_index([('student_id', 1), ('faculty_id', 1)], unique=True)
   ```

2. **Use Projections**
   ```python
   db.users.find({}, {'password_hash': 0})  # Exclude password
   ```

3. **Pagination**
   ```python
   db.users.find().limit(10).skip(0)
   ```

### Frontend Optimization

1. **Minify CSS/JS** (production)
2. **Lazy load images**
3. **Use CDN** for libraries
4. **Compress assets**

### Caching

```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/faculty')
@cache.cached(timeout=300)
def get_faculty():
    return render_template('faculty.html')
```

---

## Code Style & Standards

### Python Style (PEP 8)

```bash
# Install linter
pip install flake8

# Check code
flake8 app/

# Format code
pip install black
black app/
```

### Naming Conventions

- **Variables:** `snake_case`
- **Classes:** `PascalCase`
- **Constants:** `CONSTANT_CASE`
- **Functions:** `snake_case`

### Documentation

```python
def send_message(sender_id, receiver_id, content):
    """
    Send a message between two users.
    
    Args:
        sender_id (str): ObjectId of sender
        receiver_id (str): ObjectId of receiver
        content (str): Message content
    
    Returns:
        str: Message ID
    
    Raises:
        ValueError: If sender or receiver not found
    """
```

---

## Version Control

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes
git add .
git commit -m "Add new feature"

# Push to remote
git push origin feature/new-feature

# Create pull request
```

### Commit Messages

```
[type] Short description

Longer description of changes if needed.

Related issues: #123
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

---

## Deployment

### Heroku Deployment

1. **Create Heroku App**
   ```bash
   heroku create mentora-app
   ```

2. **Set Environment Variables**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set MONGO_URI=your-mongodb-uri
   ```

3. **Deploy**
   ```bash
   git push heroku main
   ```

### Docker Deployment

```bash
# Build image
docker build -t mentora:latest .

# Run container
docker run -p 5000:5000 mentora:latest

# Or use docker-compose
docker-compose up
```

### Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Use strong `SECRET_KEY`
- [ ] Enable HTTPS
- [ ] Set up logging
- [ ] Configure backups
- [ ] Set up monitoring
- [ ] Enable rate limiting
- [ ] Test error pages

---

## Troubleshooting

### Issue: Module not found

```bash
# Solution: Reinstall dependencies
pip install -r requirements.txt
```

### Issue: MongoDB connection error

```bash
# Solution: Check MongoDB is running
# Windows: mongod
# macOS: brew services start mongodb-community

# Or check connection string in .env
```

### Issue: Port 5000 already in use

```bash
# Solution: Use different port
python run.py --port 5001

# Or kill process
# Windows: netstat -ano | findstr :5000
# macOS/Linux: lsof -i :5000 | kill -9 <PID>
```

### Issue: Import errors

```bash
# Solution: Check file paths and __init__.py exists
# Ensure app/ is a package with __init__.py
```

---

## Best Practices

### Code Quality
- ✅ Use type hints
- ✅ Write docstrings
- ✅ Follow PEP 8
- ✅ Use linting tools
- ✅ Write tests
- ✅ Keep functions small
- ✅ Use meaningful names

### Security
- ✅ Never commit .env
- ✅ Hash passwords
- ✅ Validate input
- ✅ Use HTTPS in production
- ✅ Keep dependencies updated
- ✅ Use environment variables for secrets
- ✅ Implement rate limiting

### Performance
- ✅ Use indexes
- ✅ Implement pagination
- ✅ Cache results
- ✅ Optimize queries
- ✅ Lazy load resources
- ✅ Monitor performance
- ✅ Use CDN for static files

### Maintenance
- ✅ Document code
- ✅ Use version control
- ✅ Keep dependencies updated
- ✅ Monitor logs
- ✅ Backup data regularly
- ✅ Test changes
- ✅ Review code

---

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [MongoDB Documentation](https://docs.mongodb.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/)

---

## Contributing

1. Fork the repository
2. Create feature branch
3. Make changes
4. Test thoroughly
5. Commit with clear messages
6. Push to branch
7. Create pull request

---

## Contact & Support

For questions or issues:
- Check documentation first
- Review code comments
- Check error logs
- Open an issue on GitHub

Happy coding! 🚀
