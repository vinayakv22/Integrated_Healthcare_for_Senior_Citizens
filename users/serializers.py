from users.models import User, Patient, Doctor
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'type', 'phone', 'address')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.type = validated_data['type']
        user.phone = validated_data['phone']
        user.address = validated_data['address']
        user.save()
        if user.type == 'P':
            patient = Patient(user=user)
            patient.save()
        elif user.type == 'D':
            doctor = Doctor(user=user)
            doctor.save()
            
        return user

class PatientSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source='user.phone')
    address = serializers.CharField(source='user.address')
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source='user.phone')
    address = serializers.CharField(source='user.address')
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Doctor
        fields = '__all__'
