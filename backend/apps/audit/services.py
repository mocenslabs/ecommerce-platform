from apps.audit.models import (
    AuditLog,
)


def create_audit_log(
    *,
    action,
    entity_type,
    entity_id,
    user=None,
    metadata=None,
    ip_address=None,
    user_agent="",
):
    """
    Create audit log entry.
    """

    return AuditLog.objects.create(
        user=user,
        action=action,
        entity_type=entity_type,
        entity_id=str(entity_id),
        metadata=metadata or {},
        ip_address=ip_address,
        user_agent=user_agent,
    )
