from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):

        
        this_user = Advertisement.objects.filter(creator__username = self.context["request"].user, status='OPEN')


        """Метод для валидации. Вызывается при создании и обновлении."""
     
        this_user_open_ads = len(this_user)

        
        print(self.context['request'].method)
    

        if self.context['request'].method == 'POST':
            if this_user_open_ads < 10:
                if data['title'] != '':
                    return data
            else:
                raise serializers.ValidationError(
                    'number of open ads exceeded')
        else:
            return data

        
        


    
