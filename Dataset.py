#!/usr/bin/env python
# coding: utf-8

import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Optional: Log in to Instagram
# Uncomment and replace with your actual credentials if needed
# L.login('your_username', 'your_password')

# List of Instagram profiles to download
profiles = ['womensordination', 'citizenGO']

# Download profile data
for profile in profiles:
    print(f"Downloading profile: {profile}")
    L.download_profile(profile, profile_pic_only=False)





