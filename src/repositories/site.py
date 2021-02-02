from models import Site


class SiteRepository:
    @staticmethod
    def get(site_id):
        return Site.query.filter_by(site_id=site_id).one()

    def update(self, site_id, address, site_name, ems_id):
        site = self.get(site_id)
        site.address = address
        site.site_name = site_name
        site.ems_id = ems_id

        return site.save()

    @staticmethod
    def create(site_id, address, site_name, ems_id):
        site = Site(
            site_id=site_id, address=address, site_name=site_name, ems_id=ems_id
        )

        return site.save()
