from django.urls import path
from api.views import StartupsAPIView , StartupCommentAPIView , StartupCommentList, StartupReplyAPIView , StartupReplyList

urlpatterns = [
	path('api/startups',StartupsAPIView.as_view(), name='api-startups'),
	path('api/comment', StartupCommentAPIView.as_view(), name='api-comment'),
	path('api/com/list', StartupCommentList.as_view(), name = 'api-comment-list'),
	path('api/reply',StartupReplyAPIView.as_view(), name='api-reply-list'),
	path('api/rep/list', StartupReplyList.as_view(), name='api-comment-list'),
]