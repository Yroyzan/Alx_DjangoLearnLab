1. Likes System
Endpoints
Like a post
POST /api/posts/{post_id}/like/
Action: Authenticated users can like a post.
Response: Returns confirmation of the like.
Unlike a post
POST /api/posts/{post_id}/unlike/
Action: Authenticated users can remove their like.
Response: Returns confirmation of the unlike.
User Experience
Users can express appreciation for content by liking posts.
A user can only like a post once (duplicate likes are prevented).
Post owners get notified when their content is liked, fostering recognition and engagement.


# Notifications System
Endpoints
Get notifications
GET /api/notifications/
Action: Fetches all notifications for the logged-in user.
Response: Returns both read and unread notifications, with unread shown first.



# Notification Types
New Follower → When someone follows a user.
New Like → When someone likes the user’s post.
New Comment → When someone comments on the user’s post.
User Experience
Notifications help users stay updated on interactions that matter.
Unread notifications are prioritized, so users don’t miss important updates.
Creates a real-time social feedback loop, making the platform more interactive and engaging.


# Benefits to User Engagement
Increased Interaction → Likes provide instant feedback and encourage more participation.
Community Building → Notifications foster connections by highlighting interactions.
Retention Boost → Users return more often when they’re notified of new activity.
Personalization → Each user sees updates relevant to them, making the platform feel tailored.