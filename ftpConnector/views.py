from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FTPRequestSerializer
from ftplib import FTP

class FetchFileView(APIView):
    def post(self, request, format=None):
        serializer = FTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            hostname = serializer.validated_data['hostname']
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            pathname = serializer.validated_data['pathname']

            try:
                # Connect to FTP server
                ftp = FTP(hostname)
                ftp.login(user=username, passwd=password)
                # Retrieve file data
                file_data = []
                ftp.retrbinary(f'RETR {pathname}', file_data.append)
                ftp.quit()
                
                # Join the file data and decode
                file_content = b''.join(file_data).decode('utf-8')
                
                return Response({"file_data": file_content}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
