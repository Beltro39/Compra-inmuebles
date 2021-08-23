
class FrancaPaisaBackendZonasRouter:

    def db_for_read (self, model, **hints):

        if model._meta.app_label == 'francapaisa_zonas':

            return 'francapaisa_zonas_db_read'

        return None

    def db_for_write (self, model, **hints):

        if model._meta.app_label == 'francapaisa_zonas':

            return 'francapaisa_zonas_db_write'

        return None

    def allow_relation(self, obj1, obj2, **hints):

        if obj1._meta.app_label == 'francapaisa_zonas' or \
           obj2._meta.app_label == 'francapaisa_zonas':

            return True

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if app_label == 'francapaisa_zonas':

            return db == 'francapaisa_zonas_db_write'

        return None
