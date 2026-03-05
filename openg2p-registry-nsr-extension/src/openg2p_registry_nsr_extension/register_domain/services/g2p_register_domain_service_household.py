import logging

from openg2p_registry_core.services import G2PRegisterDomainService
from openg2p_registry_core.schemas import ChangeRequestRequestPayload

_logger = logging.getLogger('g2p-register-household-service')

class G2PRegisterDomainServiceHousehold(G2PRegisterDomainService):

    async def validate_domain_attributes(self, change_request_request_payload: ChangeRequestRequestPayload):
        _logger.info("Validating household domain attributes")
        return
