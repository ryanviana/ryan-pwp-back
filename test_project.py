#!/usr/bin/env python3
import requests
import json
import time

# Base URL for the API
BASE_URL = "http://localhost:3000"  # Assuming default NestJS port

# Test with a minimal project
test_project = {
    "title": "Test Project",
    "description": "A minimal test project",
    "image": "/test-image.jpg",
    "slug": "test-project",
    "tags": ["Test"],
    "featured": False,
}

try:
    print("Attempting to post a minimal project...")
    response = requests.post(f"{BASE_URL}/projects", json=test_project)

    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")

    if response.status_code in [200, 201]:
        print("Success!")
    else:
        print("Failed to post project")

except Exception as e:
    print(f"Error: {str(e)}")
