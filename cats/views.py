from rest_framework import viewsets

from .models import Achievement, Cat, User

from .serializers import AchievementSerializer, CatSerializer, UserSerializer

from .permissions import OwnerOrReadOnly, ReadOnly

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    # Устанавливаем разрешение
    permission_classes = (OwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer