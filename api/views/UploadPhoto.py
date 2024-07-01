from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os

class PhotoUploadView(APIView):
    def post(self, request, *args, **kwargs):
        if 'photo' not in request.FILES:
            return Response({'error': 'No photo provided'}, status=status.HTTP_400_BAD_REQUEST)

        photo = request.FILES['photo']
        # Save the photo to the default storage (e.g., local filesystem, S3, etc.)
        file_path = default_storage.save('photos/' + photo.name, ContentFile(photo.read()))

        return Response({'message': 'Photo uploaded successfully', 'file_path': file_path}, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        photos_dir = os.path.join(settings.MEDIA_ROOT, 'photos')
        user_id = request.query_params.get('user_id', None)
        photo_files = []

        if os.path.exists(photos_dir):
            photo_files = [
                f for f in os.listdir(photos_dir)
                if os.path.isfile(os.path.join(photos_dir, f)) and f.startswith(user_id+'_')
            ]

        # Correctly construct URLs using the relative path
        photo_urls = [
            request.build_absolute_uri(os.path.join(settings.MEDIA_URL, 'photos', file.replace('\\', '/')))
            for file in photo_files
        ]

        photo_list = []
        for idx, filename in enumerate(photo_files, start=1):
            # Construct the full image URL
            image_url = request.build_absolute_uri(f"{settings.MEDIA_URL}photos/{filename}")
            caption = f"Image {idx}"
            photo_list.append({
                'image_url': image_url,
                'caption': caption
            })

        #return Response(photo_list, status=status.HTTP_200_OK)

        return Response({'photos': photo_list}, status=status.HTTP_200_OK)