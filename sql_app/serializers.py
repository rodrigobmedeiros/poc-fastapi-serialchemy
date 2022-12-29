from serialchemy import ModelSerializer
from serialchemy import NestedModelField
from serialchemy import NestedModelListField

from models import User
from models import Item

class ItemSerializer(ModelSerializer):

    owner = NestedModelField(User)

class UserSerializer(ModelSerializer):

    items = NestedModelListField(Item)

item_serializer = ItemSerializer(Item)
user_serializer = UserSerializer(User)