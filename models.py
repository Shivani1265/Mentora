from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from datetime import datetime
from app import mongo, login_manager

class User(UserMixin):
    """User model for authentication"""
    
    def __init__(self, data):
        self._data = data
    
    @property
    def id(self):
        return str(self._data.get('_id', ''))
    
    @property
    def email(self):
        return self._data.get('email', '')
    
    @property
    def name(self):
        return self._data.get('name', '')
    
    @property
    def role(self):
        return self._data.get('role', '')  # 'student' or 'faculty'
    
    @property
    def bio(self):
        return self._data.get('bio', '')
    
    @property
    def expertise(self):
        return self._data.get('expertise', [])
    
    @property
    def department(self):
        return self._data.get('department', '')
    
    @property
    def profile_picture(self):
        return self._data.get('profile_picture', '')
    
    @staticmethod
    def create_user(email, name, password, role, department='', expertise=None):
        """Create a new user"""
        user_data = {
            'email': email,
            'name': name,
            'password_hash': generate_password_hash(password),
            'role': role,  # 'student' or 'faculty'
            'department': department,
            'expertise': expertise or [],
            'bio': '',
            'profile_picture': '',
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow(),
            'is_active': True
        }
        result = mongo.db.users.insert_one(user_data)
        return User(mongo.db.users.find_one({'_id': result.inserted_id}))
    
    @staticmethod
    def get_by_email(email):
        """Get user by email"""
        user_data = mongo.db.users.find_one({'email': email})
        if user_data:
            return User(user_data)
        return None
    
    @staticmethod
    def get_by_id(user_id):
        """Get user by ID"""
        try:
            user_data = mongo.db.users.find_one({'_id': ObjectId(user_id)})
            if user_data:
                return User(user_data)
        except:
            pass
        return None
    
    def verify_password(self, password):
        """Verify password"""
        return check_password_hash(self._data.get('password_hash', ''), password)
    
    def update_profile(self, name, bio, expertise=None, profile_picture=''):
        """Update user profile"""
        update_data = {
            'name': name,
            'bio': bio,
            'profile_picture': profile_picture,
            'updated_at': datetime.utcnow()
        }
        if expertise:
            update_data['expertise'] = expertise
        
        mongo.db.users.update_one(
            {'_id': ObjectId(self.id)},
            {'$set': update_data}
        )
        # Refresh user data
        self._data = mongo.db.users.find_one({'_id': ObjectId(self.id)})
    
    def to_dict(self):
        """Convert user to dictionary (without password)"""
        data = self._data.copy()
        data.pop('password_hash', None)
        data['_id'] = str(data['_id'])
        return data

@login_manager.user_loader
def load_user(user_id):
    """Load user for Flask-Login"""
    return User.get_by_id(user_id)

class Message:
    """Message model for communications"""
    
    @staticmethod
    def send_message(sender_id, receiver_id, content):
        """Send a message"""
        message_data = {
            'sender_id': ObjectId(sender_id),
            'receiver_id': ObjectId(receiver_id),
            'content': content,
            'created_at': datetime.utcnow(),
            'read': False
        }
        result = mongo.db.messages.insert_one(message_data)
        return str(result.inserted_id)
    
    @staticmethod
    def get_conversation(user_id1, user_id2, limit=50):
        """Get messages between two users"""
        messages = list(mongo.db.messages.find({
            '$or': [
                {'sender_id': ObjectId(user_id1), 'receiver_id': ObjectId(user_id2)},
                {'sender_id': ObjectId(user_id2), 'receiver_id': ObjectId(user_id1)}
            ]
        }).sort('created_at', -1).limit(limit))
        
        return [Message.format_message(msg) for msg in reversed(messages)]
    
    @staticmethod
    def mark_as_read(message_id):
        """Mark message as read"""
        mongo.db.messages.update_one(
            {'_id': ObjectId(message_id)},
            {'$set': {'read': True}}
        )
    
    @staticmethod
    def get_unread_count(user_id):
        """Get unread message count"""
        return mongo.db.messages.count_documents({
            'receiver_id': ObjectId(user_id),
            'read': False
        })
        """Format message for display"""
        return {
            '_id': str(msg['_id']),
            'sender_id': str(msg['sender_id']),
            'receiver_id': str(msg['receiver_id']),
            'content': msg['content'],
            'created_at': msg['created_at'],
            'read': msg['read']
        }

class Connection:
    """Mentorship connection model"""
    
    @staticmethod
    def create_connection(student_id, faculty_id):
        """Create a mentorship connection"""
        connection_data = {
            'student_id': ObjectId(student_id),
            'faculty_id': ObjectId(faculty_id),
            'created_at': datetime.utcnow(),
            'status': 'active'
        }
        result = mongo.db.connections.insert_one(connection_data)
        return str(result.inserted_id)
    
    @staticmethod
    def get_connections(user_id, role):
        """Get connections for a user"""
        if role == 'student':
            query = {'student_id': ObjectId(user_id)}
        else:
            query = {'faculty_id': ObjectId(user_id)}
        
        connections = list(mongo.db.connections.find(query))
        return [Connection.format_connection(conn) for conn in connections]
    
    @staticmethod
    def format_connection(conn):
        """Format connection for display"""
        return {
            '_id': str(conn['_id']),
            'student_id': str(conn['student_id']),
            'faculty_id': str(conn['faculty_id']),
            'created_at': conn['created_at'],
            'status': conn['status']
        }
    
    @staticmethod
    def is_connected(student_id, faculty_id):
        """Check if student and faculty are connected"""
        return mongo.db.connections.find_one({
            'student_id': ObjectId(student_id),
            'faculty_id': ObjectId(faculty_id)
        }) is not None
