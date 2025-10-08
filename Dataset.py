#!/usr/bin/env python
# coding: utf-8

# Step 1: Try importing instaloader, install if not found
try:
    import instaloader
except ImportError:
    import subprocess
    import sys
    print("Instaloader not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "instaloader"])
    import instaloader  # Try again after installation

# Step 2: Create an instance of Instaloader
L = instaloader.Instaloader()

# Optional: Log in to Instagram (for private profiles)
# Uncomment and replace with your Instagram credentials if needed
# L.login('your_username', 'your_password')

# Step 3: List of Instagram profiles to download
profiles = ['womensordination', 'citizenGO']

# Step 4: Download each profile
for profile in profiles:
    print(f"Downloading profile: {profile}")
    L.download_profile(profile, profile_pic_only=False)







