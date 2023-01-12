"""
Serializers for recipe APIs
"""
from rest_framework import serializers

from core.models import (
    Recipe,
    # Tag,
    # Ingredient,
)


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""
    # tags = TagSerializer(many=True, required=False)
    # ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'time_minutes', 'price', 'link'
        ]
        read_only_fields = ['id']

    # def _get_or_create_tags(self, tags, recipe):
    #     """Handle getting or creating tags as needed."""
    #     auth_user = self.context['request'].user
    #     for tag in tags:
    #         tag_obj, created = Tag.objects.get_or_create(
    #             user=auth_user,
    #             **tag,
    #         )
    #         recipe.tags.add(tag_obj)


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
