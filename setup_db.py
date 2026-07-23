#!/usr/bin/env python
"""
Mentora - Setup Script
Initializes the MongoDB database and creates sample data
"""

import os
import sys
from pymongo import MongoClient
from datetime import datetime
from werkzeug.security import generate_password_hash

def setup_database():
    """Initialize MongoDB and create sample data"""
    
    # Connect to MongoDB
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/mentorship')
    
    try:
        client = MongoClient(mongo_uri)
        db = client.get_database()
        print(f"✓ Connected to MongoDB: {mongo_uri}")
    except Exception as e:
        print(f"✗ Failed to connect to MongoDB: {e}")
        return False
    
    # Create collections and indexes
    try:
        # Users collection
        db.users.create_index('email', unique=True)
        print("✓ Created users collection and indexes")
        
        # Messages collection
        db.messages.create_index([('sender_id', 1), ('receiver_id', 1)])
        db.messages.create_index('created_at')
        print("✓ Created messages collection and indexes")
        
        # Connections collection
        db.connections.create_index([('student_id', 1), ('faculty_id', 1)], unique=True)
        print("✓ Created connections collection and indexes")
        
    except Exception as e:
        print(f"✗ Error creating indexes: {e}")
        return False
    
    # Create sample data
    try:
        # Check if data already exists
        if db.users.count_documents({}) > 0:
            print("⚠ Database already contains users. Skipping sample data creation.")
            return True
        
        # Sample faculty members
        faculty_data = [
            {
                'email': 'dr.smith@university.edu',
                'name': 'Dr. James Smith',
                'password_hash': generate_password_hash('password123'),
                'role': 'faculty',
                'department': 'Computer Science',
                'expertise': ['Python', 'Machine Learning', 'Data Science', 'AI'],
                'bio': 'Expert in machine learning and AI with 10+ years of experience.',
                'profile_picture': '',
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow(),
                'is_active': True
            },
            {
                'email': 'prof.jones@university.edu',
                'name': 'Prof. Sarah Jones',
                'password_hash': generate_password_hash('password123'),
                'role': 'faculty',
                'department': 'Mathematics',
                'expertise': ['Calculus', 'Linear Algebra', 'Statistics', 'Number Theory'],
                'bio': 'Passionate about teaching mathematics and its applications.',
                'profile_picture': '',
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow(),
                'is_active': True
            },
            {
                'email': 'dr.wilson@university.edu',
                'name': 'Dr. Michael Wilson',
                'password_hash': generate_password_hash('password123'),
                'role': 'faculty',
                'department': 'Physics',
                'expertise': ['Quantum Mechanics', 'Thermodynamics', 'Classical Mechanics'],
                'bio': 'Leading researcher in theoretical physics.',
                'profile_picture': '',
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow(),
                'is_active': True
            }
        ]
        
        # Sample students
        student_data = [
            {
                'email': 'john.doe@student.edu',
                'name': 'John Doe',
                'password_hash': generate_password_hash('password123'),
                'role': 'student',
                'department': 'Computer Science',
                'expertise': [],
                'bio': 'Passionate about learning AI and machine learning.',
                'profile_picture': '',
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow(),
                'is_active': True
            },
            {
                'email': 'emily.wilson@student.edu',
                'name': 'Emily Wilson',
                'password_hash': generate_password_hash('password123'),
                'role': 'student',
                'department': 'Mathematics',
                'expertise': [],
                'bio': 'Focused on applied mathematics and statistics.',
                'profile_picture': '',
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow(),
                'is_active': True
            },
            {
                'email': 'alex.kumar@student.edu',
                'name': 'Alex Kumar',
                'password_hash': generate_password_hash('password123'),
                'role': 'student',
                'department': 'Physics',
                'expertise': [],
                'bio': 'Interested in quantum mechanics and theoretical physics.',
                'profile_picture': '',
                'created_at': datetime.utcnow(),
                'updated_at': datetime.utcnow(),
                'is_active': True
            }
        ]
        
        # Insert faculty
        faculty_result = db.users.insert_many(faculty_data)
        print(f"✓ Created {len(faculty_result.inserted_ids)} sample faculty members")
        
        # Insert students
        student_result = db.users.insert_many(student_data)
        print(f"✓ Created {len(student_result.inserted_ids)} sample students")
        
        # Create sample connections
        connections = [
            {
                'student_id': student_result.inserted_ids[0],
                'faculty_id': faculty_result.inserted_ids[0],
                'created_at': datetime.utcnow(),
                'status': 'active'
            },
            {
                'student_id': student_result.inserted_ids[1],
                'faculty_id': faculty_result.inserted_ids[1],
                'created_at': datetime.utcnow(),
                'status': 'active'
            }
        ]
        
        connection_result = db.connections.insert_many(connections)
        print(f"✓ Created {len(connection_result.inserted_ids)} sample connections")
        
    except Exception as e:
        print(f"✗ Error creating sample data: {e}")
        return False
    
    print("\n" + "="*50)
    print("✓ Database setup completed successfully!")
    print("="*50)
    print("\nSample Credentials:")
    print("Faculty:")
    print("  Email: dr.smith@university.edu")
    print("  Password: password123")
    print("\nStudent:")
    print("  Email: john.doe@student.edu")
    print("  Password: password123")
    print("\n" + "="*50)
    
    return True

if __name__ == '__main__':
    from dotenv import load_dotenv
    
    # Load environment variables
    load_dotenv()
    
    print("Mentora Database Setup")
    print("=" * 50)
    
    if setup_database():
        sys.exit(0)
    else:
        sys.exit(1)
