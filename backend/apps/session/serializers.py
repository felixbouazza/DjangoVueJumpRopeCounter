from rest_framework import serializers

from .models import Session


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        read_only_fields = (
            'created_by',
            'created_at'
        ),
        fields = (
            "id",
            "jump_rope_number",
            "created_at",
            "ending_at"
        )
