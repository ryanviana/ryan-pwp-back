#!/usr/bin/env python3
import requests
import json
import time

# Base URL for the API
BASE_URL = "http://localhost:3003"  # Assuming default NestJS port

# Test with a minimal blog post
test_blog = {
    "slug": "test-blog",
    "title": "Test Blog Post",
    "date": "2024-03-30",
    "excerpt": "This is a test blog post",
    "coverImage": "/test-cover.jpg",
    "readingTime": "1 min read",
    "tags": ["Test"],
    "content": "This is test content.",
}

try:
    print("Attempting to post a minimal blog post...")
    response = requests.post(f"{BASE_URL}/blog", json=test_blog)

    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")

    if response.status_code in [200, 201]:
        print("Success!")
    else:
        print("Failed to post blog post")

except Exception as e:
    print(f"Error: {str(e)}")
