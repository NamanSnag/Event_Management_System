from django.contrib.auth import get_user_model
from django.db.models import SET_NULL, DateTimeField, ForeignKey, Model

Users = get_user_model()


class Timestamp(Model):
    created_ts = DateTimeField(auto_now_add=True)
    modified_ts = DateTimeField(auto_now=True)
    created_by = ForeignKey(
        Users,
        related_name="%(class)s_created_by",
        on_delete=SET_NULL,
        null=True,
        blank=True,
    )
    modified_by = ForeignKey(
        Users,
        related_name="%(class)s_modified_by",
        on_delete=SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
