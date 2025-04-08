from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Clear existing data
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activity.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # Insert test data
        users = [
            {"_id": "1", "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
            {"_id": "2", "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
            {"_id": "3", "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
            {"_id": "4", "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
            {"_id": "5", "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
        ]
        db.users.insert_many(users)

        teams = [
            {"_id": "1", "name": "Blue Team"},
            {"_id": "2", "name": "Gold Team"},
        ]
        db.teams.insert_many(teams)

        activities = [
            {"_id": "1", "user": "1", "activity_type": "Cycling", "duration": "1:00:00"},
            {"_id": "2", "user": "2", "activity_type": "Crossfit", "duration": "2:00:00"},
            {"_id": "3", "user": "3", "activity_type": "Running", "duration": "1:30:00"},
            {"_id": "4", "user": "4", "activity_type": "Strength", "duration": "0:30:00"},
            {"_id": "5", "user": "5", "activity_type": "Swimming", "duration": "1:15:00"},
        ]
        db.activity.insert_many(activities)

        leaderboard = [
            {"_id": "1", "user": "1", "score": 100},
            {"_id": "2", "user": "2", "score": 90},
            {"_id": "3", "user": "3", "score": 95},
            {"_id": "4", "user": "4", "score": 85},
            {"_id": "5", "user": "5", "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        workouts = [
            {"_id": "1", "name": "Cycling Training", "description": "Training for a road cycling event"},
            {"_id": "2", "name": "Crossfit", "description": "Training for a crossfit competition"},
            {"_id": "3", "name": "Running Training", "description": "Training for a marathon"},
            {"_id": "4", "name": "Strength Training", "description": "Training for strength"},
            {"_id": "5", "name": "Swimming Training", "description": "Training for a swimming competition"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data using pymongo.'))
