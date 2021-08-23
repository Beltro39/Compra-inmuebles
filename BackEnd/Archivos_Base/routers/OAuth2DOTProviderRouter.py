
class OAuth2DOTProviderRouter:

    # A router to control all database operations on models in the            #
    # oauth2_provider application                                             #

    # Attempts to read oauth2_provider models go to users_db_read             #

    def db_for_read (self, model, **hints):

        if model._meta.app_label == 'oauth2_provider':

            return 'users_db_read'

        return None

    # Attempts to write oauth2_provider models go to users_db_write           #

    def db_for_write (self, model, **hints):

        if model._meta.app_label == 'oauth2_provider':

            return 'users_db_write'

        return None

    # Allow relations if a model in the oauth2_provider app is involved       #
    # Allow relations if a model in the dot_restrict_scopes app is involved   #

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label == 'oauth2_provider' or \
           obj2._meta.app_label == 'oauth2_provider':

            return True

        if obj1._meta.app_label == 'dot_restrict_scopes' or \
           obj2._meta.app_label == 'dot_restrict_scopes':

            return True

        return None

    # Make sure the oauth2_provider app only appears in the users_db_write    #
    # database                                                                #

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'oauth2_provider':

            return db == 'users_db_write'

        return None
