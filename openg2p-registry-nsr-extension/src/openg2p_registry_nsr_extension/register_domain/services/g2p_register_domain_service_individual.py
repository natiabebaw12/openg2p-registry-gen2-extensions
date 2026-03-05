import logging
from datetime import date, datetime

from openg2p_registry_core.services import G2PRegisterDomainService
from openg2p_registry_core.schemas import ChangeRequestRequestPayload
from openg2p_registry_core.models import G2PRegisterChangeRequest, G2PRegisterChangeRequestPayload
from ..models import G2PRegisterHousehold, G2PRegisterIndividual
from sqlalchemy.ext.asyncio import AsyncSession

_logger = logging.getLogger('g2p-register-individual-service')

class G2PRegisterDomainServiceIndividual(G2PRegisterDomainService):

    async def validate_domain_attributes(self, change_request_request_payload: ChangeRequestRequestPayload):
        _logger.info("Validating individual domain attributes")
        return

    async def post_approve(self, change_request: G2PRegisterChangeRequest, session: AsyncSession):

        payload_obj = await session.get(G2PRegisterChangeRequestPayload, change_request.change_request_id)

        if not payload_obj or not payload_obj.change_payload:
            return

        for record in payload_obj.change_payload:

            edit_action = record.get("edit_action")
            link_internal_record_id = record.get("link_internal_record_id")

            if not link_internal_record_id:
                continue

            g2p_register_household = await session.get(G2PRegisterHousehold, link_internal_record_id)

            if not g2p_register_household:
                continue

            # ---------------- ADD ----------------
            if edit_action == "ADD":
                g2p_register_household.household_size_total = (
                    (g2p_register_household.household_size_total or 0) + 1
                )

            # ---------------- DELETE ----------------
            elif edit_action == "DELETE":
                g2p_register_household.household_size_total = max(
                    0,
                    (g2p_register_household.household_size_total or 0) - 1
                )

            # ---------------- NO CHANGE ----------------
            elif edit_action == "NO_CHANGE":
                continue
        return
