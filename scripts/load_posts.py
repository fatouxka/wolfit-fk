#!/usr/bin/env python
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import User, Post, Category
from datetime import datetime, timedelta
import random

def load_sample_posts():
    app = create_app()
    
    with app.app_context():
        user = User.query.first()
        if not user:
            user = User(username='demo_user', email='demo@example.com')
            user.set_password('demo123')
            db.session.add(user)
            db.session.commit()
            print(f"✓ Created user: {user.username}")
        else:
            print(f"✓ Using existing user: {user.username}")
        
        categories = ['Technology', 'Programming', 'Data Science', 'Web Development', 'Python']
        category_objects = []
        
        for cat_title in categories:
            category = Category.query.filter_by(title=cat_title).first()
            if not category:
                category = Category(title=cat_title)
                db.session.add(category)
                print(f"✓ Created category: {cat_title}")
            category_objects.append(category)
        db.session.commit()
        
        sample_posts = [
            ("Getting Started with Wolfit", "Wolfit is a powerful microblogging platform that helps you share content easily. Here's how to get started...", 0),
            ("Python Best Practices for 2024", "Learn the latest Python programming patterns including type hints, async/await, and context managers...", 4),
            ("Understanding Flask Application Structure", "A deep dive into Flask blueprints, application factories, and organization patterns...", 3),
            ("Database Optimization Techniques", "Tips for improving SQL query performance including indexing, eager loading, and query optimization...", 0),
            ("User Authentication Best Practices", "Secure your web application with proper password hashing, session management, and CSRF protection...", 3),
            ("Testing Flask Applications with Pytest", "Comprehensive testing strategies including unit tests, integration tests, and test coverage...", 4),
            ("Deploying Wolfit to Production", "Step-by-step deployment guide using Gunicorn, Nginx, and Docker...", 3),
            ("REST API Design Patterns", "Building robust APIs with Flask including versioning, error handling, and documentation...", 0),
            ("Frontend Integration with Wolfit", "Using JavaScript with Flask templates and building interactive features...", 3),
            ("Code Coverage Strategies", "Achieving 100% test coverage with pytest-cov and understanding what to test...", 4),
            ("Debugging Flask Applications", "Tools and techniques for debugging including Flask debug toolbar, logging, and breakpoints...", 4),
            ("Security Headers and Best Practices", "Protecting against common web vulnerabilities like XSS, CSRF, and SQL injection...", 0),
            ("Caching Strategies for Performance", "Improving response times with Redis caching and template caching...", 0),
            ("Background Tasks with Celery", "Handling async operations for email sending, image processing, and data analysis...", 4),
            ("Microservices Architecture", "Breaking down monolithic applications into smaller, manageable services...", 0)
        ]
        
        posts_created = 0
        posts_skipped = 0
        
        for title, body, category_index in sample_posts:
            existing = Post.query.filter_by(title=title).first()
            if existing:
                posts_skipped += 1
                continue
            
            random_days = random.randint(0, 30)
            random_hours = random.randint(0, 23)
            created_at = datetime.utcnow() - timedelta(days=random_days, hours=random_hours)
            
            post = Post(
                title=title,
                body=body,
                author_id=user.id,
                category_id=category_objects[category_index].id,
                created_at=created_at
            )
            db.session.add(post)
            posts_created += 1
        
        db.session.commit()
        
        print(f"\n📊 Summary:")
        print(f"  ✓ Created: {posts_created} new posts")
        print(f"  ✓ Skipped: {posts_skipped} existing posts")
        
        total_posts = Post.query.count()
        print(f"  ✓ Total posts in database: {total_posts}")
        
        print(f"\n📝 Recent posts:")
        recent_posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
        for post in recent_posts:
            print(f"  • {post.title[:50]}... ({post.created_at.strftime('%Y-%m-%d')})")
        
        return total_posts

if __name__ == '__main__':
    print("🔄 Loading sample posts into Wolfit...\n")
    load_sample_posts()
