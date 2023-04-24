from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from .serializers import UserCreateSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
import jwt
import datetime
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Account
# User = get_user_model()


class RegisterView(APIView):
    print("ethi")
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data

        serializer = UserCreateSerializer(data=data)
        print(serializer)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.create(serializer.validated_data)
        user = UserSerializer(user)

        return Response(user.data, status=status.HTTP_201_CREATED)
User
    
@api_view(['POST'])
def LoginView(request):
    print("hai Login View")
    try:
        email = request.data['email']
        password = request.data['password']
    except:
        return Response({'status':'Please provide the mentioned details'})
    
    try:
        user = Account.objects.get(email=email)
        print(user)
        if user is not None:
            # print('kkkkkkkkkkkk')

            payload = {
                    'email':user.email,
                    'password':user.password,

                }
            jwt_token = jwt.encode(payload, 'secret', algorithm='HS256')
            print(jwt_token,"toooooooooooken")
            return Response({'status' : "Success",'payload' : payload ,'user_jwt': jwt_token,'id':user.id})
    except:
        if User.DoesNotExist:
            return Response("Email or Password is Wrong")



class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user = UserSerializer(user)

        return Response(user.data, status=status.HTTP_200_OK)



@api_view(['POST'])   
def verify_token(request):
    token  = request.data['token']
    print("###################################",token,'############################################')
    decoded = jwt.decode(token, 'secret', algorithms='HS256')
    print(decoded.get('email'),'Yes iam back////.......')
    user = Account.objects.get(email=decoded.get('email'))
    serializer = UserSerializer(user,many=False)

    if user:
        return Response(serializer.data)
    else:
        return Response({'status' : 'Token Invalid'})


@api_view(['GET'])
def profile_view(request,id):
    user = Account.objects.get(id=id)
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)


@api_view(["POST"])
def addImage(request,id):
    user = Account.objects.get(id=id)
    user.image = request.data['image']
    user.save()
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)
    







@api_view(['GET'])
def user_list(request):
    user = Account.objects.all()
    serializer = UserSerializer(user,many=True)
    # print(serializer.data)
    return Response(serializer.data)



@api_view(['POST'])
def admin_login(request):
    print("i am in the admin login")
    try:
        email = request.data['email']
        password =str(request.data['password']) 
        
    except:
        return Response({'status': "Please provide the details"})
    try:
        print('try block.....')
        user = Account.objects.get(email=email)
        # user=admin_user.objects.all()
        # print(user,'userrrrrrrrrrrr')
        if user is not None:
            print('kkkkkkkkkkkk')
            if user.is_superuser is True:
                payload = {
                    'email':user.email,
                    'password':user.password,
                }
                jwt_token = jwt.encode(payload, 'secret', algorithm='HS256')
                # print(jwt_token,"toooooooooooken")
                return Response({'status' : "Success",'payload' : payload ,'admin_jwt': jwt_token})
            else:
                return Response({'status' : 'Not a superuser'})
    except:
        if User.DoesNotExist:
            return Response("Email or Password is Wrong")
        

@api_view(['GET'])
def edit_user(request,id):
    user = Account.objects.get(id=id)
    serializer = UserSerializer(user,many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update_user(request,id):
    user = Account.objects.get(id=id)
    user.full_name = request.data["username"]
    user.email = request.data["email"]
    user.save()
    return Response("User Updated")


@api_view(['GET'])
def delete_user(request,id):
    user = Account.objects.get(id=id)
    user.delete()
    return Response("User deleted")