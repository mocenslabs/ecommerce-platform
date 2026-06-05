from django.db import models


class ActiveQuerySet(
    models.QuerySet,
):
    """
    QuerySet with soft delete support.
    """

    def active(self):
        """
        Return only active records.
        """

        return self.filter(
            is_deleted=False,
        )

    def deleted(self):
        """
        Return deleted records.
        """

        return self.filter(
            is_deleted=True,
        )


class ActiveManager(
    models.Manager,
):
    """
    Default active records manager.
    """

    def get_queryset(self):
        """
        Filter deleted records.
        """

        return ActiveQuerySet(
            self.model,
            using=self._db,
        ).filter(
            is_deleted=False,
        )
