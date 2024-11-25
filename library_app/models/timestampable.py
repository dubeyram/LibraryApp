# python imports


from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampable(models.Model):
    """Timestampable behaviour for models. Record timestamps of a Content.
    * Model instance is never deleted, its marked as deleted with is_deleted.
    """

    created_at = models.DateTimeField(
        verbose_name=_("Created At"),
        auto_now_add=True,
    )
    modified_at = models.DateTimeField(
        verbose_name=_("Modified At"),
        auto_now=True,
    )
    is_deleted = models.BooleanField(
        verbose_name=_("Is deleted instance"),
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name=_("Is active instance"),
        default=True,
    )
    extra_data = models.JSONField(
        verbose_name=_("Extra Data"),
        default=dict,
        blank=True,
        null=True,
    )


    class Meta:
        abstract = True

    # noinspection PyMethodOverriding
    def delete(self, force: bool = False):
        """Soft delete object"""
        self.is_deleted = True
        if force:
            super().delete()
        self.save()

    def save(
        self,
        force_insert=False,
        force_update=False,
        using=None,
        update_fields=None,
    ):
        """Overriding save to support cacheing"""
        super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )

    @classmethod
    def sortable_field_names(cls):
        """Sortable field names

        Return a list of all field names for the model, including reverse sort options,
        and include names of fields present in related models if a field is a foreign key.

        Args:
        ----
            cls: class object

        """
        sortable_fields = ["-pk", "pk"]
        if hasattr(cls, "_meta"):
            for field in cls._meta.get_fields():
                if field.is_relation and field.related_model:
                    sortable_fields.extend(
                        [
                            f"{field.name}__{fk_field.name}"
                            for fk_field in field.related_model._meta.get_fields()
                        ],
                    )
                    sortable_fields.append(f"{field.name}_id")
                else:
                    sortable_fields.append(field.name)
        return sortable_fields + [f"-{field}" for field in sortable_fields]
