from rest_framework import viewsets

from registration.serializers import CustomUserSerializer
from .models import Statusapp
from .serializers import StatusappSerializer
#
# class StatusappViewSet(viewsets.ModelViewSet):
#     queryset = Statusapp.objects.all()
#     serializer_class = StatusappSerializer
#
#     def get_queryset(self):
#         # Get the user ID from the URL parameter (e.g., /api/Statusapps/?user_id=123)
#         user_id = self.request.query_params.get('user_id')
#         hello = Statusapp.objects.all()
#         hello = hello.order_by('-uploaded_at')
#         # Filter Statusapps by the user ID if it's provided in the query parameter
#         if user_id is not None:
#             queryset = Statusapp.objects.filter(user_id=user_id)
#
#             # Sort the queryset by the last uploaded date in descending order (newest first)
#             queryset = queryset.order_by('-uploaded_at')
#
#             return queryset
#         else:
#             # If user_id is not provided, return all Statusapps
#             return hello
#
# # Create your views here.

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Statusapp
from .serializers import StatusappSerializer
from django.shortcuts import get_object_or_404
from registration.models import CustomUser

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def upload_status(request):
#     if request.method == 'POST':
#         serializer = StatusappSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save(user_id=request.user)
#             return Response({'message': 'Status uploaded successfully'}, status=201)
#         return Response(serializer.errors, status=400)
def upload_status(request):

    # Get user_id from the request data
    user_id = request.data.get('user_id', None)

    # Check if user_id is provided in the request data
    if user_id is None:
        return Response({'message': 'user_id is required'})

    # Retrieve the user with the provided user_id
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return Response({'message': 'User not found'})

    # Add the user instance to the request data
    request.data['user_id'] = user.id
    request.data['status'] = True
    # Create the serializer with the user instance as user_id
    serializer = StatusappSerializer(data=request.data)
    if serializer.is_valid():
        # Assign the user instance as user_id and save the status
        serializer.save()

        return Response({'message': 'Status uploaded successfully'})

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def upload_status(request):
#     if request.method == 'POST':
#         # Get user_id from the request data
#         user_id = request.data.get('user_id', None)
#
#         # Check if user_id is provided in the request data
#         if user_id is None:
#             return Response({'message': 'user_id is required'}, status=400)
#
#         # Retrieve the user with the provided user_id
#         try:
#             user = CustomUser.objects.get(id=user_id)
#         except CustomUser.DoesNotExist:
#             return Response({'message': 'User not found'}, status=404)
#         request.data['status'] = True
#         # Create the serializer with the user instance as user_id
#         serializer = StatusappSerializer(data=request.data)
#         if serializer.is_valid():
#
#             # Assign the user instance as user_id and save the status
#             serializer.save(user_id=user)
#
#             return Response({'message': 'Status uploaded successfully'}, status=201)
#         return Response(serializer.errors, status=400)
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
@api_view(['DELETE'])
def delete_status(request):
    user_id = request.GET.get('user_id')
    status_id = request.GET.get('status_id')

    if user_id is None or status_id is None:
        return Response({'error': 'Missing user_id or status_id query parameters'}, status=400)

    try:
        # Get the status based on the provided status_id
        status = Statusapp.objects.get(id=status_id, user_id=user_id)
        
        # Check if the user making the request is the owner of the status
        if user_id != status.user_id.id:
            return Response({'error': 'You are not authorized to delete this status'}, status=403)

        # Delete the status
        status.delete()

        return Response({'message': 'Status deleted successfully'})
    except Statusapp.DoesNotExist:
        return Response({'error': 'Status not found'}, status=404)



from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from relationship.models import  Follow
from .serializers import StatusappSerializer

@api_view(['GET'])
def list_statuses(request):
    # Get the user_id from the query parameters
    user_id = request.query_params.get('user_id')

    # Initialize a dictionary to store the results
    statuses_data = {}

    if user_id is not None:
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=404)

        # Include statuses of the specified user (user_id)
        user_statuses_query = Statusapp.objects.filter(user_id=user).order_by('-uploaded_at')
        user_statuses_serializer = StatusappSerializer(user_statuses_query, many=True)
        statuses_data['user_statuses'] = user_statuses_serializer.data

        # Include statuses of users you are following, excluding blocked users
        following_users = Follow.objects.filter(follower=user, approved=True).values_list('followed', flat=True)

        for following_user_id in following_users:
            following_user = CustomUser.objects.get(id=following_user_id)

            # Exclude blocked users
            if user not in following_user.blocked_users.all() and following_user not in user.blocked_users.all():
                following_statuses_query = Statusapp.objects.filter(user_id=following_user).order_by('-uploaded_at')
                following_statuses_serializer = StatusappSerializer(following_statuses_query, many=True)
                statuses_data[following_user.name] = following_statuses_serializer.data

    return Response(statuses_data)
@api_view(['GET'])
def list_all_statuses(request):
    # Query all Statusapp objects and order them by the 'uploaded_at' field in descending order
    all_statuses_query = Statusapp.objects.all().order_by('-uploaded_at')
    all_statuses_serializer = StatusappSerializer(all_statuses_query, many=True)

    # Serialize the data and return it as a JSON response
    return Response(all_statuses_serializer.data)
from rest_framework.views import APIView
class UserStatusAPIView(APIView):
    def get(self, request):
        user_id = self.request.query_params.get('user_id')
        try:
            # Check if the user with the provided user_id has a status
            status_exists = Statusapp.objects.filter(user_id=user_id, status=True).exists()

            if not status_exists:
                return Response({'message': 'User has no status'})

            # Retrieve the user with the provided user_id
            user = CustomUser.objects.get(id=user_id)

            # Serialize the user data
            user_serializer = CustomUserSerializer(user)

            return Response(user_serializer.data)

        except CustomUser.DoesNotExist:
            return Response({'message': 'User not found'})