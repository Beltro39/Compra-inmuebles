
from django.test.runner import DiscoverRunner

class NoDBInitializationTestRunner (DiscoverRunner):

    # NoDBInitializationTestRunner is a helper class used to run unit tests   #
    # without initializing or tearing down a test database instance in order  #
    # to ease the use of existing database instances as test databases        #

    def setup_databases(self, **kwargs):

        """ Override the database creation defined in parent class """
        pass

    def teardown_databases(self, old_config, **kwargs):

        """ Override the database teardown defined in parent class """
        pass
