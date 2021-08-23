
class AdminProviderRouter:

    # A router to control all database operations on models in the admin       #
    # application                                                              #

    # Attempts to read admin models go to users_db_read                        #

    def db_for_read (self, model, **hints):

        if model._meta.app_label == 'admin':

            return 'users_db_read'

        return None

    # Attempts to write admin models go to users_db_write                      #

    def db_for_write (self, model, **hints):

        if model._meta.app_label == 'admin':

            return 'users_db_write'

        return None

    # Allow relations if a model in the admin app is involved                  #

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label == 'admin' or \
           obj2._meta.app_label == 'admin':

            return True

        return None

    # Make sure the admin app only appears in the users_db_write database      #

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'admin':

            return db == 'users_db_write'

        return None
