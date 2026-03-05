# ruff: noqa: E402
import asyncio
import logging

from .config import Settings

_config = Settings.get_config()

from openg2p_fastapi_common.app import Initializer as BaseInitializer
from openg2p_registry_core.app import Initializer as CoreInitializer

from .register_domain.models import (
    G2PLocationRegion,
    G2PLocationZone,
    G2PLocationWoreda,
    G2PLocationEA,
    G2PRegisterHousehold,
    G2PRegisterHistoryHousehold,
    G2PRegisterIndividual,
    G2PRegisterHistoryIndividual,
    G2PRegisterIndividualProgram,
    G2PRegisterHistoryIndividualProgram,
    G2PRegisterIndividualGrievance,
    G2PRegisterHistoryIndividualGrievance,
    G2PRegisterHouseholdProgram,
    G2PRegisterHistoryHouseholdProgram,
    G2PRegisterHouseholdGrievance,
    G2PRegisterHistoryHouseholdGrievance,
)
from .register_domain.factory import G2PRegisterDomainFactory
from .register_domain.services import G2PRegisterDomainServiceHousehold, G2PRegisterDomainServiceIndividual

_logger = logging.getLogger(_config.logging_default_logger_name)


class Initializer(BaseInitializer):
    def initialize(self, **kwargs):
        super().initialize()
        CoreInitializer().initialize()

        G2PRegisterDomainServiceHousehold()
        G2PRegisterDomainServiceIndividual()
        G2PRegisterDomainFactory()

    def migrate_database(self, args):

        async def migrate():
            _logger.info("Migrating NSR extensions database")

            # Location tables
            await G2PLocationRegion.create_migrate()
            await G2PLocationZone.create_migrate()
            await G2PLocationWoreda.create_migrate()
            await G2PLocationEA.create_migrate()

            await G2PRegisterHousehold.create_migrate()
            await G2PRegisterHistoryHousehold.create_migrate()

            await G2PRegisterIndividual.create_migrate()
            await G2PRegisterHistoryIndividual.create_migrate()

            # Individual sub-tables
            await G2PRegisterIndividualProgram.create_migrate()
            await G2PRegisterHistoryIndividualProgram.create_migrate()
            await G2PRegisterIndividualGrievance.create_migrate()
            await G2PRegisterHistoryIndividualGrievance.create_migrate()

            # Household sub-tables
            await G2PRegisterHouseholdProgram.create_migrate()
            await G2PRegisterHistoryHouseholdProgram.create_migrate()
            await G2PRegisterHouseholdGrievance.create_migrate()
            await G2PRegisterHistoryHouseholdGrievance.create_migrate()

        asyncio.run(migrate())
